#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos security_zones fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from copy import deepcopy

from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils.six import string_types
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.security_zones.security_zones import (
    Security_zonesArgs,
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


class Security_zonesFacts(object):
    """The junos security_zones fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Security_zonesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root),
            dict_constructor=dict,
        )
        return xml_dict

    def _get_device_data(self, connection, config_filters):
        """
        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filters)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for security_polices
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
                        <security>
                            <zones>
                            </zones>
                        </security>
                    </configuration>
                    """
            data = self._get_device_data(connection, config_filter)

        # split the config into instances of the resource
        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/security/zones")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"security_zones": {}}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["security_zones"] = utils.remove_empties(params["config"])

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        security_zones_config = {}

        # Parse facts for security zones
        conf = conf.get("zones")

        if "functional-zone" in conf:
            security_zones_config["functional_zone_management"] = {}
            functional_zone_management = conf.get("functional-zone").get("management") or {}

            if "description" in functional_zone_management:
                security_zones_config["functional_zone_management"]["description"] = (
                    functional_zone_management["description"]
                )

            if "host-inbound-traffic" in functional_zone_management:
                security_zones_config["functional_zone_management"]["host_inbound_traffic"] = (
                    self.parse_host_inbound_traffic(
                        functional_zone_management["host-inbound-traffic"],
                    )
                )

            if "interfaces" in functional_zone_management:
                if isinstance(functional_zone_management["interfaces"], dict):
                    functional_zone_management["interfaces"] = [
                        functional_zone_management["interfaces"],
                    ]
                security_zones_config["functional_zone_management"]["interfaces"] = [
                    interface["name"] for interface in functional_zone_management["interfaces"]
                ]

            if "screen" in functional_zone_management:
                security_zones_config["functional_zone_management"]["screen"] = (
                    functional_zone_management["screen"]
                )

        if "security-zone" in conf:
            security_zones_list = conf.get("security-zone")
            if isinstance(security_zones_list, dict):
                security_zones_list = [security_zones_list]
            security_zones_config["zones"] = []

            for security_zone in security_zones_list:
                temp_sec_zone = {}
                temp_sec_zone["name"] = security_zone["name"]

                if "address-book" in security_zone:
                    temp_sec_zone["address_book"] = {}

                    if "address" in security_zone["address-book"]:
                        temp_sec_zone["address_book"]["addresses"] = []
                        if isinstance(
                            security_zone["address-book"]["address"],
                            dict,
                        ):
                            security_zone["address-book"]["address"] = [
                                security_zone["address-book"]["address"],
                            ]

                        for address in security_zone["address-book"]["address"]:
                            temp_address = {}

                            temp_address["name"] = address["name"]
                            if "ip-prefix" in address:
                                temp_address["ip_prefix"] = address["ip-prefix"]
                            elif "dns-name" in address:
                                temp_address["dns_name"] = {}
                                temp_address["dns_name"]["name"] = address["dns-name"]["name"]
                                if "ipv4-only" in address["dns-name"]:
                                    temp_address["dns_name"]["ipv4_only"] = True
                                if "ipv6-only" in address["dns-name"]:
                                    temp_address["dns_name"]["ipv6_only"] = True
                            elif "range-address" in address:
                                temp_address["range_address"] = {}
                                temp_address["range_address"]["from"] = address["range-address"][
                                    "name"
                                ]
                                temp_address["range_address"]["to"] = address["range-address"][
                                    "to"
                                ]["range-high"]
                            elif "wildcard-address" in address:
                                temp_address["wildcard_address"] = address["wildcard-address"][
                                    "name"
                                ]
                            if "description" in address:
                                temp_address["description"] = address["description"]

                            temp_sec_zone["address_book"]["addresses"].append(
                                temp_address,
                            )

                    if "address-set" in security_zone["address-book"]:
                        temp_sec_zone["address_book"]["address_sets"] = []

                        for address_set in security_zone["address-book"]["address-set"]:
                            temp_address_set = {}

                            temp_address_set["name"] = address_set["name"]
                            if "address" in address_set:
                                if isinstance(address_set["address"], dict):
                                    address_set["address"] = [
                                        address_set["address"],
                                    ]
                                temp_address_set["addresses"] = [
                                    address["name"] for address in address_set["address"]
                                ]
                            if "address-set" in address_set:
                                if isinstance(
                                    address_set["address-set"],
                                    dict,
                                ):
                                    address_set["address-set"] = [
                                        address_set["address-set"],
                                    ]
                                temp_address_set["address_sets"] = [
                                    addr_set["name"] for addr_set in address_set["address-set"]
                                ]
                            if "description" in address_set:
                                temp_address_set["description"] = address_set["description"]

                            temp_sec_zone["address_book"]["address_sets"].append(temp_address_set)

                if "advance-policy-based-routing-profile" in security_zone:
                    temp_sec_zone["advance_policy_based_routing_profile"] = security_zone[
                        "advance-policy-based-routing-profile"
                    ]["profile"]
                if "advanced-connection-tracking" in security_zone:
                    temp_sec_zone["advanced_connection_tracking"] = {}
                    temp_act = temp_sec_zone["advanced_connection_tracking"]
                    if "mode" in security_zone["advanced-connection-tracking"]:
                        temp_act["mode"] = security_zone["advanced-connection-tracking"]["mode"]
                    if "timeout" in security_zone["advanced-connection-tracking"]:
                        temp_act["timeout"] = security_zone["advanced-connection-tracking"][
                            "timeout"
                        ]
                    if (
                        "track-all-policies-to-this-zone"
                        in security_zone["advanced-connection-tracking"]
                    ):
                        temp_act["track_all_policies_to_this_zone"] = True
                if "application-tracking" in security_zone:
                    temp_sec_zone["application_tracking"] = True
                if "description" in security_zone:
                    temp_sec_zone["description"] = security_zone["description"]
                if "enable-reverse-reroute" in security_zone:
                    temp_sec_zone["enable_reverse_reroute"] = True
                if "host-inbound-traffic" in security_zone:
                    temp_sec_zone["host_inbound_traffic"] = self.parse_host_inbound_traffic(
                        security_zone["host-inbound-traffic"],
                    )
                if "interfaces" in security_zone:
                    if isinstance(security_zone["interfaces"], dict):
                        security_zone["interfaces"] = [
                            security_zone["interfaces"],
                        ]
                    else:
                        temp_sec_zone["interfaces"] = [
                            interface["name"] for interface in security_zone["interfaces"]
                        ]
                if "screen" in security_zone:
                    temp_sec_zone["screen"] = security_zone["screen"]
                if "source-identity-log" in security_zone:
                    temp_sec_zone["source_identity_log"] = True
                if "tcp-rst" in security_zone:
                    temp_sec_zone["tcp_rst"] = True
                if "unidirectional-session-refreshing" in security_zone:
                    temp_sec_zone["unidirectional_session_refreshing"] = True

                security_zones_config["zones"].append(temp_sec_zone)

        return security_zones_config

    def parse_host_inbound_traffic(self, host_inbound_traffic):
        temp_hit = {}

        if "protocols" in host_inbound_traffic:
            temp_hit["protocols"] = []
            if isinstance(host_inbound_traffic["protocols"], dict):
                host_inbound_traffic["protocols"] = [
                    host_inbound_traffic["protocols"],
                ]
            for protocol in host_inbound_traffic["protocols"]:
                temp_protocol = {}
                temp_protocol["name"] = protocol["name"]
                if "except" in protocol:
                    temp_protocol["except"] = True

                temp_hit["protocols"].append(temp_protocol)

        if "system-services" in host_inbound_traffic:
            temp_hit["system_services"] = []
            if isinstance(host_inbound_traffic["system-services"], dict):
                host_inbound_traffic["system-services"] = [
                    host_inbound_traffic["system-services"],
                ]
            for system_services in host_inbound_traffic["system-services"]:
                temp_system_services = {}
                temp_system_services["name"] = system_services["name"]
                if "except" in system_services:
                    temp_system_services["except"] = True

                temp_hit["system_services"].append(temp_system_services)

        return temp_hit
