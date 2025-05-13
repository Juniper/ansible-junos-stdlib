#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_acls class
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
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list

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


class Acls(ConfigBase):
    """
    The junos_acls class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["acls"]

    def __init__(self, module):
        super(Acls, self).__init__(module)

    def get_acls_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        acls_facts = facts["ansible_network_resources"].get("acls")
        if not acls_facts:
            return []
        return acls_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_acls_facts = self.get_acls_facts()
        else:
            existing_acls_facts = {}
        if state == "gathered":
            existing_acls_facts = self.get_acls_facts()
            result["gathered"] = existing_acls_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_acls_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_acls_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            diff = None
            config_xmls = self.set_config(existing_acls_facts)
            with locked_config(self._module):
                for config_xml in config_xmls:
                    diff = load_config(self._module, config_xml, [])

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

            changed_acls_facts = self.get_acls_facts()

            result["before"] = existing_acls_facts
            if result["changed"]:
                result["after"] = changed_acls_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_acls_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_acls_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        root = build_root_xml_node("firewall")
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
            root.append(xml)

        return tostring(root)

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        acls_xml = []
        acls_xml.extend(self._state_deleted(want, have))
        acls_xml.extend(self._state_merged(want, have))
        return acls_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        acls_xml = []
        acls_xml.extend(self._state_deleted(have, have))
        acls_xml.extend(self._state_merged(want, have))
        return acls_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        acls_xml = []
        family_node = build_root_xml_node("family")
        delete = dict(delete="delete")

        if not want:
            want = have

        for config in want:
            try:
                family = "inet6" if config.get("afi") == "ipv6" else "inet"
            except KeyError:
                family = "inet"
            inet_node = build_child_xml_node(family_node, family)

            # Look deeply into have to match replace correctly
            existing_acls = []
            for conf in have:
                if conf.get("afi") == config.get("afi"):
                    existing_acls.extend(conf["acls"] or [])
            acl_names = [acl["name"] for acl in existing_acls]

            if not config["acls"]:
                inet_node.attrib.update(delete)
                continue

            for acl in config["acls"]:
                if acl["name"] not in acl_names:
                    continue

                filter_node = build_child_xml_node(inet_node, "filter")
                build_child_xml_node(filter_node, "name", acl["name"])
                if not acl.get("aces"):
                    filter_node.attrib.update(delete)
                    continue

                for ace in acl["aces"]:
                    # if ace["name"] not in ace_names:
                    term_node = build_child_xml_node(filter_node, "term")
                    build_child_xml_node(term_node, "name", ace["name"])
                    term_node.attrib.update(delete)

        acls_xml.append(family_node)
        return acls_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        acls_xml = []
        family_node = build_root_xml_node("family")
        for config in want:
            try:
                family = "inet6" if config.pop("afi") == "ipv6" else "inet"
            except KeyError:
                family = "inet"
            inet_node = build_child_xml_node(family_node, family)

            for acl in config.get("acls") or []:
                filter_node = build_child_xml_node(inet_node, "filter")
                build_child_xml_node(filter_node, "name", acl["name"])
                for ace in acl.get("aces") or []:
                    term_node = build_child_xml_node(filter_node, "term")
                    build_child_xml_node(term_node, "name", ace["name"])

                    if ace.get("source") or ace.get("destination") or ace.get("protocol"):
                        from_node = build_child_xml_node(term_node, "from")
                        for direction in ("source", "destination"):
                            if ace.get(direction):
                                if ace[direction].get("address"):
                                    addresses = ace[direction]["address"]
                                    if not isinstance(addresses, list):
                                        addresses = [addresses]
                                    for address in addresses:
                                        build_child_xml_node(
                                            from_node,
                                            "{0}-address".format(direction),
                                            address,
                                        )
                                if ace[direction].get("prefix_list"):
                                    for prefix in ace[direction].get(
                                        "prefix_list",
                                    ):
                                        build_child_xml_node(
                                            from_node,
                                            "{0}-prefix-list".format(
                                                direction,
                                            ),
                                            prefix["name"],
                                        )
                                if ace[direction].get("port_protocol"):
                                    if "eq" in ace[direction]["port_protocol"]:
                                        build_child_xml_node(
                                            from_node,
                                            "{0}-port".format(direction),
                                            ace[direction]["port_protocol"]["eq"],
                                        )
                                    elif "range" in ace[direction]["port_protocol"]:
                                        ports = "{0}-{1}".format(
                                            ace[direction]["port_protocol"]["start"],
                                            ace[direction]["port_protocol"]["end"],
                                        )
                                        build_child_xml_node(
                                            from_node,
                                            "{0}-port".format(direction),
                                            ports,
                                        )
                        if ace.get("protocol"):
                            build_child_xml_node(
                                from_node,
                                "protocol",
                                ace["protocol"],
                            )
                        if ace.get("protocol_options"):
                            if ace["protocol_options"].get("icmp"):
                                icmp_code = build_child_xml_node(
                                    from_node,
                                    "icmp-code",
                                )
                                icmp_type = build_child_xml_node(
                                    from_node,
                                    "icmp-type",
                                )
                                icmp = ace["protocol_options"]["icmp"]
                                if "dod_host_prohibited" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "destination-host-prohibited",
                                    )
                                if "dod_net_prohibited" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "destination-network-prohibited",
                                    )
                                if "echo" in icmp:
                                    build_child_xml_node(
                                        icmp_type,
                                        "echo-request",
                                    )
                                if "echo_reply" in icmp:
                                    build_child_xml_node(
                                        icmp_type,
                                        "echo-reply",
                                    )
                                if "host_tos_unreachable" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "host-unreachable-for-tos",
                                    )
                                if "host_redirect" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "redirect-for-host",
                                    )
                                if "host_tos_redirect" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "redirect-for-host-and-tos",
                                    )
                                if "host_unknown" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "destination-host-unknown",
                                    )
                                if "host_unreachable" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "host-unreachable",
                                    )
                                if "net_redirect" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "redirect-for-network",
                                    )
                                if "net_tos_redirect" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "redirect-for-tos-and-net",
                                    )
                                if "network_unknown" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "destination-network-unknown",
                                    )
                                if "port_unreachable" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "port-unreachable",
                                    )
                                if "protocol_unreachable" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "protocol-unreachable",
                                    )
                                if "reassembly_timeout" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "ttl-eq-zero-during-reassembly",
                                    )
                                if "redirect" in icmp:
                                    build_child_xml_node(icmp_type, "redirect")
                                if "router_advertisement" in icmp:
                                    build_child_xml_node(
                                        icmp_type,
                                        "router-advertisement",
                                    )
                                if "router_solicitation" in icmp:
                                    build_child_xml_node(
                                        icmp_type,
                                        "router-solicit",
                                    )
                                if "source_route_failed" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "source-route-failed",
                                    )
                                if "time_exceeded" in icmp:
                                    build_child_xml_node(
                                        icmp_type,
                                        "time-exceeded",
                                    )
                                if "ttl_exceeded" in icmp:
                                    build_child_xml_node(
                                        icmp_code,
                                        "ttl-eq-zero-during-transit",
                                    )
                    if ace.get("grant"):
                        then_node = build_child_xml_node(term_node, "then")
                        if ace["grant"] == "permit":
                            build_child_xml_node(then_node, "accept")
                        if ace["grant"] == "deny":
                            build_child_xml_node(then_node, "discard")

        acls_xml.append(family_node)
        return acls_xml
