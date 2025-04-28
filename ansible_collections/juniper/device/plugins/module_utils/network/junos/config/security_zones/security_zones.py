#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_security_zones class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    build_child_xml_node,
    build_root_xml_node,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_empties,
)

from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.facts import (
    Facts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    commit_configuration,
    discard_changes,
    load_config,
    locked_config,
    tostring,
)


class Security_zones(ConfigBase):
    """
    The junos_security_zones class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["security_zones"]

    def __init__(self, module):
        super(Security_zones, self).__init__(module)

    def get_security_zones_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        security_zones_facts = facts["ansible_network_resources"].get(
            "security_zones",
        )
        if not security_zones_facts:
            return {}
        return security_zones_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_security_zones_facts = self.get_security_zones_facts()
        else:
            existing_security_zones_facts = {}
        if self.state == "gathered":
            existing_security_zones_facts = self.get_security_zones_facts()
            result["gathered"] = existing_security_zones_facts

        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_security_zones_facts(
                data=running_config,
            )

        elif self.state == "rendered":
            config_xmls = self.set_config(existing_security_zones_facts)
            if config_xmls:
                result["rendered"] = config_xmls

        else:
            diff = None
            config_xmls = self.set_config(existing_security_zones_facts)
            with locked_config(self._module):
                diff = load_config(self._module, config_xmls, [])

                commit = not self._module.check_mode
                if diff:
                    if commit:
                        commit_configuration(self._module)
                    else:
                        discard_changes(self._module)
                    result["changed"] = True

                    if self._module._diff:
                        result["diff"] = {"prepared": diff}

            result["commands"] = config_xmls

            changed_security_zones_facts = self.get_security_zones_facts()

            result["before"] = existing_security_zones_facts
            if result["changed"]:
                result["after"] = changed_security_zones_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_security_zones_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_security_zones_facts
        resp = self.set_state(want, have)
        return resp

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self.root = build_root_xml_node("security")
        state = self._module.params["state"]
        if state in ("merged", "replaced", "rendered", "overridden") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state,
                ),
            )
        config_xmls = []
        if state == "overridden":
            config_xmls = self._state_overridden(want, have)
        elif state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)
        for xml in config_xmls:
            self.root.append(xml)
        return tostring(self.root)

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        security_zones_xml = []
        security_zones_xml.extend(self._state_deleted(want, have))
        security_zones_xml.extend(self._state_merged(want, have))
        return security_zones_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        security_zones_xml = []
        security_zones_xml.extend(self._state_deleted(want, have))
        security_zones_xml.extend(self._state_merged(want, have))
        return security_zones_xml

    def _state_merged(self, want, _have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        zones_xml = []
        want = remove_empties(want)
        zones_node = build_root_xml_node("zones")

        def build_host_inbound_traffic(node, host_inbound_traffic):
            host_inbound_traffic_node = build_child_xml_node(
                node,
                "host-inbound-traffic",
            )

            if "protocols" in host_inbound_traffic:
                for protocol in host_inbound_traffic["protocols"]:
                    protocol_node = build_child_xml_node(
                        host_inbound_traffic_node,
                        "protocols",
                    )
                    build_child_xml_node(
                        protocol_node,
                        "name",
                        protocol["name"],
                    )
                    if "except" in protocol:
                        build_child_xml_node(protocol_node, "except")
            if "system_services" in host_inbound_traffic:
                for system_service in host_inbound_traffic["system_services"]:
                    system_service_node = build_child_xml_node(
                        host_inbound_traffic_node,
                        "system-services",
                    )
                    build_child_xml_node(
                        system_service_node,
                        "name",
                        system_service["name"],
                    )
                    if "except" in system_service:
                        build_child_xml_node(system_service_node, "except")

        # add zone-pair policies
        if "functional_zone_management" in want.keys():
            functional_zone_management = want.get("functional_zone_management")
            functional_zone_node = build_child_xml_node(
                zones_node,
                "functional-zone",
            )
            functional_zone_management_node = build_child_xml_node(
                functional_zone_node,
                "management",
            )

            if "description" in functional_zone_management:
                build_child_xml_node(
                    functional_zone_management_node,
                    "description",
                    functional_zone_management["description"],
                )
            if "host_inbound_traffic" in functional_zone_management:
                build_host_inbound_traffic(
                    functional_zone_management_node,
                    functional_zone_management["host_inbound_traffic"],
                )
            if "interfaces" in functional_zone_management:
                for interface in functional_zone_management["interfaces"]:
                    interface_node = build_child_xml_node(
                        functional_zone_management_node,
                        "interfaces",
                    )
                    build_child_xml_node(interface_node, "name", interface)
            if "screen" in functional_zone_management:
                build_child_xml_node(
                    functional_zone_management_node,
                    "screen",
                    functional_zone_management["screen"],
                )

        # add global policies
        if "zones" in want.keys():
            security_zones = want.get("zones")

            for security_zone in security_zones:
                security_zone_node = build_child_xml_node(
                    zones_node,
                    "security-zone",
                )
                if "name" in security_zone:
                    build_child_xml_node(
                        security_zone_node,
                        "name",
                        security_zone["name"],
                    )
                if "address_book" in security_zone:
                    address_book_node = build_child_xml_node(
                        security_zone_node,
                        "address-book",
                    )

                    if "addresses" in security_zone["address_book"]:
                        for address in security_zone["address_book"]["addresses"]:
                            address_node = build_child_xml_node(
                                address_book_node,
                                "address",
                            )

                            build_child_xml_node(
                                address_node,
                                "name",
                                address["name"],
                            )
                            if "ip_prefix" in address:
                                build_child_xml_node(
                                    address_node,
                                    "ip-prefix",
                                    address["ip_prefix"],
                                )
                            elif "dns_name" in address:
                                dns_node = build_child_xml_node(
                                    address_node,
                                    "dns-name",
                                )
                                build_child_xml_node(
                                    dns_node,
                                    "name",
                                    address["dns_name"]["name"],
                                )
                                if "ipv4_only" in address["dns_name"]:
                                    build_child_xml_node(dns_node, "ipv4-only")
                                if "ipv6_only" in address["dns_name"]:
                                    build_child_xml_node(dns_node, "ipv6-only")
                            elif "range_address" in address:
                                range_address_node = build_child_xml_node(
                                    address_node,
                                    "range-address",
                                )
                                build_child_xml_node(
                                    range_address_node,
                                    "name",
                                    address["range_address"]["from"],
                                )
                                to_node = build_child_xml_node(
                                    range_address_node,
                                    "to",
                                )
                                build_child_xml_node(
                                    to_node,
                                    "range-high",
                                    address["range_address"]["to"],
                                )
                            elif "wildcard_address" in address:
                                wildcard_node = build_child_xml_node(
                                    address_node,
                                    "wildcard-address",
                                )
                                build_child_xml_node(
                                    wildcard_node,
                                    "name",
                                    address["wildcard_address"],
                                )
                            if "description" in address:
                                build_child_xml_node(
                                    address_node,
                                    "description",
                                    address["description"],
                                )
                    if "address_sets" in security_zone["address_book"]:
                        for address_set in security_zone["address_book"]["address_sets"]:
                            address_set_node = build_child_xml_node(
                                address_book_node,
                                "address-set",
                            )

                            build_child_xml_node(
                                address_set_node,
                                "name",
                                address_set["name"],
                            )
                            if "addresses" in address_set:
                                for address in address_set["addresses"]:
                                    addr_node = build_child_xml_node(
                                        address_set_node,
                                        "address",
                                    )
                                    build_child_xml_node(
                                        addr_node,
                                        "name",
                                        address,
                                    )
                            if "address_sets" in address_set:
                                for address in address_set["address_sets"]:
                                    addr_node = build_child_xml_node(
                                        address_set_node,
                                        "address-set",
                                    )
                                    build_child_xml_node(
                                        addr_node,
                                        "name",
                                        address,
                                    )
                            if "description" in address_set:
                                build_child_xml_node(
                                    address_set_node,
                                    "description",
                                    address_set["description"],
                                )

                if "advance_policy_based_routing_profile" in security_zone:
                    routing_profile_node = build_child_xml_node(
                        security_zone_node,
                        "advance-policy-based-routing-profile",
                    )
                    build_child_xml_node(
                        routing_profile_node,
                        "profile",
                        security_zone["advance_policy_based_routing_profile"],
                    )
                if "advanced_connection_tracking" in security_zone:
                    act_node = build_child_xml_node(
                        security_zone_node,
                        "advanced-connection-tracking",
                    )
                    if "mode" in security_zone["advanced_connection_tracking"]:
                        build_child_xml_node(
                            act_node,
                            "mode",
                            security_zone["advanced_connection_tracking"]["mode"],
                        )
                    if "timeout" in security_zone["advanced_connection_tracking"]:
                        build_child_xml_node(
                            act_node,
                            "timeout",
                            security_zone["advanced_connection_tracking"]["timeout"],
                        )
                    if (
                        "track_all_policies_to_this_zone"
                        in security_zone["advanced_connection_tracking"]
                    ):
                        build_child_xml_node(
                            act_node,
                            "track-all-policies-to-this-zone",
                        )
                if "application_tracking" in security_zone:
                    build_child_xml_node(
                        security_zone_node,
                        "application-tracking",
                    )
                if "description" in security_zone:
                    build_child_xml_node(
                        security_zone_node,
                        "description",
                        security_zone["description"],
                    )
                if "enable_reverse_reroute" in security_zone:
                    build_child_xml_node(
                        security_zone_node,
                        "enable-reverse-reroute",
                    )
                if "host_inbound_traffic" in security_zone:
                    build_host_inbound_traffic(
                        security_zone_node,
                        security_zone["host_inbound_traffic"],
                    )
                if "interfaces" in security_zone:
                    for interface in security_zone["interfaces"]:
                        interface_node = build_child_xml_node(
                            security_zone_node,
                            "interfaces",
                        )
                        build_child_xml_node(interface_node, "name", interface)
                if "screen" in security_zone:
                    build_child_xml_node(
                        security_zone_node,
                        "screen",
                        security_zone["screen"],
                    )
                if "source_identity_log" in security_zone:
                    build_child_xml_node(
                        security_zone_node,
                        "source-identity-log",
                    )
                if "tcp_rst" in security_zone:
                    build_child_xml_node(security_zone_node, "tcp-rst")
                if "unidirectional_session_refreshing" in security_zone:
                    build_child_xml_node(
                        security_zone_node,
                        "unidirectional-session-refreshing",
                    )

        if zones_node is not None:
            zones_xml.append(zones_node)
        return zones_xml

    def _state_deleted(self, _want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        security_zones_xml = []
        security_zones_root = None
        delete = {"delete": "delete"}
        if have is not None:
            security_zones_root = build_child_xml_node(
                self.root,
                "zones",
                None,
                delete,
            )

        if security_zones_root is not None:
            security_zones_xml.append(security_zones_root)
        return security_zones_xml
