#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos lag_interfaces fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from copy import deepcopy

from ansible.module_utils._text import to_bytes
from ansible.module_utils.six import string_types
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.lag_interfaces.lag_interfaces import (
    Lag_interfacesArgs,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.utils.utils import (
    get_resource_config,
)


try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False


class Lag_interfacesFacts(object):
    """The junos lag_interfaces fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Lag_interfacesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for interfaces
        :param connection: the device connection
        :param data: previously collected configuration as lxml ElementTree root instance
                     or valid xml sting
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
            data = get_resource_config(connection, config_filter=config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        self._resources = data.xpath("configuration/interfaces/interface")

        objs = []
        for resource in self._resources:
            if resource is not None:
                obj = self.render_config(self.generated_spec, resource)
                if obj:
                    objs.append(obj)
        facts = {}
        if objs:
            facts["lag_interfaces"] = []
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )
            for cfg in params["config"]:
                facts["lag_interfaces"].append(utils.remove_empties(cfg))
        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def get_member_config(self, interface_obj, intf_name):
        """
        Extract member configuration for a given interface object and interface name.

        This function checks both `ether-options` and `gigether-options` for 802.3ad bundle configurations
        and determines the link type (primary or backup) if applicable.

        :param interface_obj: The ElementTree instance of an interface configuration object.
        :param intf_name: The name of the aggregated Ethernet interface (e.g., "ae0").
        :rtype: dictionary
        :returns: A dictionary containing the member configuration with the following structure:
                {
                    "member": <interface_name>,
                    "link_type": "primary" or "backup" (optional)
                }
                If no member configuration is found, an empty dictionary is returned.
        """

        member_config = {}
        lag_interface_member = utils.get_xml_conf_arg(
            interface_obj,
            "ether-options/ieee-802.3ad[bundle='%s']/../../name" % intf_name,
        ) or utils.get_xml_conf_arg(
            interface_obj,
            "gigether-options/ieee-802.3ad[bundle='%s']/../../name" % intf_name,
        )
        if lag_interface_member:
            member_config["member"] = lag_interface_member
            if utils.get_xml_conf_arg(
                interface_obj,
                "ether-options/ieee-802.3ad/primary",
                data="tag",
            ):
                member_config["link_type"] = "primary"
                member_config["ether_option_type"] = "ether"
            elif utils.get_xml_conf_arg(
                interface_obj,
                "gigether-options/ieee-802.3ad/primary",
                data="tag",
            ):
                member_config["link_type"] = "primary"
                member_config["ether_option_type"] = "gigether"
            elif utils.get_xml_conf_arg(
                interface_obj,
                "ether-options/ieee-802.3ad/backup",
                data="tag",
            ):
                member_config["link_type"] = "backup"
                member_config["ether_option_type"] = "ether"
            elif utils.get_xml_conf_arg(
                interface_obj,
                "gigether-options/ieee-802.3ad/backup",
                data="tag",
            ):
                member_config["link_type"] = "backup"
                member_config["ether_option_type"] = "gigether"
        return member_config

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values
        :param spec: The facts tree, generated from the argspec
        :param conf: The ElementTree instance of configuration object
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        intf_name = utils.get_xml_conf_arg(conf, "name")
        if intf_name.startswith("ae"):
            config["name"] = intf_name
            config["members"] = []
            for interface_obj in self._resources:
                member_config = self.get_member_config(interface_obj, intf_name)
                if member_config:
                    config["members"].append(member_config)

            for mode in ["active", "passive"]:
                if utils.get_xml_conf_arg(
                    conf,
                    "aggregated-ether-options/lacp/%s" % mode,
                    data="tag",
                ):
                    config["mode"] = mode
                    break

            if utils.get_xml_conf_arg(conf, "aggregated-ether-options/link-protection", data="tag"):
                config["link_protection"] = True

        lag_intf_cfg = utils.remove_empties(config)
        # if lag interfaces config is not present return empty dict
        if len(lag_intf_cfg) == 1:
            return {}
        else:
            return lag_intf_cfg
