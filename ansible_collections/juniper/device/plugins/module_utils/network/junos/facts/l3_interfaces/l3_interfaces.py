#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos l3_interfaces fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from copy import deepcopy

from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils.six import iteritems, string_types
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.l3_interfaces.l3_interfaces import (
    L3_interfacesArgs,
)


try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False

try:
    import xmltodict

    HAS_XMLTODICT = True
except ImportError:
    HAS_XMLTODICT = False


class L3_interfacesFacts(object):
    """The junos l3_interfaces fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = L3_interfacesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_config(self, connection, config_filter):
        """

        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root),
            dict_constructor=dict,
        )
        return xml_dict

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for l3_interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            config_filter = """
                <configuration>
                    <interfaces/>
                </configuration>
                """
            data = self.get_config(connection, config_filter)
        data_string = etree.tostring(data, pretty_print=True).decode()

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        resources = data.xpath("configuration/interfaces/interface")
        config = []

        if resources:
            config = self.parse_l3_if_resources(resources)
        facts = {}
        facts["l3_interfaces"] = config
        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def parse_l3_if_resources(self, l3_if_resources):
        l3_ifaces = []
        for iface in l3_if_resources:
            int_have = self._get_xml_dict(iface)
            int_dict = int_have["interface"]
            if "unit" in int_dict.keys() and int_dict.get("unit") is not None:
                unit_list = int_dict["unit"]
                if isinstance(unit_list, list):
                    for item in unit_list:
                        fact_dict = self._render_l3_intf(item, int_dict)
                        if fact_dict:
                            l3_ifaces.append(fact_dict)
                else:
                    fact_dict = self._render_l3_intf(unit_list, int_dict)
                    if fact_dict:
                        l3_ifaces.append(fact_dict)
        return l3_ifaces

    def _render_l3_intf(self, unit, int_dict):
        """

        :param item:
        :param int_dict:
        :return:
        """
        interface = {}
        ipv4 = []
        ipv6 = []
        if "family" in unit.keys():
            if "inet" in unit["family"].keys():
                interface["name"] = int_dict["name"]
                interface["unit"] = unit["name"]
                inet = unit["family"].get("inet")
                if inet is not None and "address" in inet.keys():
                    if isinstance(inet["address"], dict):
                        for key, value in iteritems(inet["address"]):
                            addr = {}
                            addr["address"] = value
                            ipv4.append(addr)
                    else:
                        for ip in inet["address"]:
                            addr = {}
                            addr["address"] = ip["name"]
                            ipv4.append(addr)
            if "inet" in unit["family"]:
                interface["name"] = int_dict["name"]
                interface["unit"] = unit["name"]
                inet = unit["family"].get("inet")
                if inet:
                    if inet.get("mtu"):
                        mtu = int(inet.get("mtu"))
                        interface["mtu"] = int(mtu)
                    if "dhcp" in inet:
                        ipv4.append({"address": "dhcp"})

            if "inet6" in unit["family"]:
                interface["name"] = int_dict["name"]
                interface["unit"] = unit["name"]

                inet6 = unit["family"].get("inet6")
                if inet6:
                    if inet6.get("mtu"):
                        mtu = int(inet6.get("mtu"))
                        interface["mtu"] = int(mtu)

                    addresses = inet6.get("address")
                    if addresses:
                        if isinstance(addresses, dict):
                            for value in addresses.values():
                                ipv6.append({"address": value})
                        else:
                            for ip in addresses:
                                ipv6.append({"address": ip["name"]})

            interface["ipv4"] = ipv4
            interface["ipv6"] = ipv6
        return utils.remove_empties(interface)
