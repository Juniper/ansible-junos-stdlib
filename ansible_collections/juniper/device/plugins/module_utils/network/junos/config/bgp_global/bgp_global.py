#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_bgp_global class
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
    to_list,
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


class Bgp_global(ConfigBase):
    """
    The junos_bgp_global class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["bgp_global"]

    def __init__(self, module):
        super(Bgp_global, self).__init__(module)

    def get_bgp_global_facts(self, data=None):
        """Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        bgp_facts = facts["ansible_network_resources"].get("bgp_global")
        if not bgp_facts:
            return {}
        return bgp_facts

    def execute_module(self):
        """Execute the module
        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_bgp_global_facts = self.get_bgp_global_facts()
        else:
            existing_bgp_global_facts = {}
        if state == "gathered":
            existing_bgp_global_facts = self.get_bgp_global_facts()
            result["gathered"] = existing_bgp_global_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_bgp_global_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_bgp_global_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_bgp_global_facts)
            with locked_config(self._module):
                for config_xml in to_list(config_xmls):
                    diff = load_config(self._module, config_xml, [])

                commit = not self._module.check_mode
                if config_xmls and diff:
                    if commit:
                        commit_configuration(self._module)
                    else:
                        discard_changes(self._module)
                    result["changed"] = True

                    if self._module._diff:
                        result["diff"] = {"prepared": diff}

            result["commands"] = config_xmls

            changed_bgp_global_facts = self.get_bgp_global_facts()

            result["before"] = existing_bgp_global_facts
            if result["changed"]:
                result["after"] = changed_bgp_global_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_bgp_global_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_bgp_global_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the list xml configuration necessary to migrate the current configuration
                  to the desired configuration
        """
        self.autonomous_system = None
        self.root = build_root_xml_node("configuration")
        self.protocols = build_child_xml_node(self.root, "protocols")
        self.routing_options = build_child_xml_node(
            self.root,
            "routing-options",
        )
        state = self._module.params["state"]
        if state in ("merged", "replaced", "rendered") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state,
                ),
            )
        config_xmls = []
        temp_lst = []
        if state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state == "purged":
            config_xmls = self._state_purged(want, have)
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state in ("replaced", "overridden"):
            config_xmls = self._state_replaced(want, have)

        if config_xmls:
            for xml in config_xmls:
                self.protocols.append(xml)
            for xml in self.root.getchildren():
                xml = tostring(xml)
                temp_lst.append(xml)
        if state == "purged":
            for xml in self.root.getchildren():
                xml = tostring(xml)
                temp_lst.append(xml)
        return temp_lst

    def _state_replaced(self, want, have):
        """The xml configuration generator when state is merged
        :rtype: A list
        :returns: the xml configuration necessary to merge the provided into
                  the current configuration
        """
        bgp_xml = []
        bgp_xml.extend(self._state_deleted(want, have))
        bgp_xml.extend(self._state_merged(want, have))

        return bgp_xml

    def _state_merged(self, want, have):
        """Select the appropriate function based on the state provided
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the list xml configuration necessary to migrate the current configuration
                  to the desired configuration
        """
        bgp_xml = []

        want = remove_empties(want)
        if want:
            bgp_root = build_root_xml_node("bgp")
            bool_parser = [
                "accept-remote-nexthop",
                "add-path-display-ipv4-address",
                "advertise-from-main-vpn-tables",
                "advertise-inactive",
                "advertise-peer-as",
                "damping",
                "disable",
                "egress-te-sid-stats",
                "enforce-first-as",
                "holddown-all-stale-labels",
                "include-mp-next-hop",
                "log-updown",
                "mtu-discovery",
                "no-advertise-peer-as",
                "no-aggregator-id",
                "no-client-reflect",
                "no-precision-timers",
                "passive",
                "precision-timers",
                "rfc6514-compliant-safi129",
                "route-server-client",
                "send-addpath-optimization",
                "itcp-aggressive-transmission",
                "unconfigured-peer-graceful-restart",
                "vpn-apply-export",
                "as-override",
                "unconfigured-peer-graceful-restart",
                "vpn-apply-export",
            ]
            cfg_parser = [
                "authentication-algorithm",
                "authentication-key",
                "authentication-key-chain",
                "description",
                "export",
                "forwarding-context",
                "hold-time",
                "import",
                "ipsec-sa",
                "keep",
                "local-address",
                "local-interface",
                "local-preference",
                "peer-as",
                "preference",
                "out-delay",
                "sr-preference-override",
                "stale-labels-holddown-period",
                "tcp-mss",
                "ttl",
                "type",
            ]
            for item in bool_parser:
                bgp_root = self._add_node(
                    want,
                    item,
                    item.replace("-", "_"),
                    bgp_root,
                )

            for item in cfg_parser:
                bgp_root = self._add_node(
                    want,
                    item,
                    item.replace("-", "_"),
                    bgp_root,
                    True,
                )

            # Generate xml node for autonomous-system
            if want.get("as_number"):
                as_node = build_child_xml_node(
                    self.routing_options,
                    "autonomous-system",
                    want.get("as_number"),
                )
                # Add node for loops
                if want.get("loops"):
                    build_child_xml_node(as_node, "loops", want.get("loops"))
                # Add node for asdot_notation
                if want.get("asdot_notation"):
                    if "asdot_notation" in want.keys():
                        build_child_xml_node(as_node, "asdot-notation")

            # Generate commands for bgp node
            self.parse_attrib(bgp_root, want)

            # Generate commands for groups
            if want.get("groups"):
                groups = want.get("groups")

                # Generate commands for each group in group list
                for group in groups:
                    groups_node = build_child_xml_node(bgp_root, "group")
                    build_child_xml_node(groups_node, "name", group["name"])
                    # Parse the boolean value attributes
                    for item in bool_parser:
                        groups_node = self._add_node(
                            group,
                            item,
                            item.replace("-", "_"),
                            groups_node,
                        )

                    # Parse the non-boolean leaf attributes
                    for item in cfg_parser:
                        groups_node = self._add_node(
                            group,
                            item,
                            item.replace("-", "_"),
                            groups_node,
                            True,
                        )

                    # Generate commands for nodes with child attributes
                    self.parse_attrib(groups_node, group)

                    # Generate commands for each neighbors
                    if group.get("neighbors"):
                        neighbors = group.get("neighbors")
                        # Generate commands for each neighbor in neighbors list
                        for neighbor in neighbors:
                            neighbors_node = build_child_xml_node(
                                groups_node,
                                "neighbor",
                            )
                            build_child_xml_node(
                                neighbors_node,
                                "name",
                                neighbor["neighbor_address"],
                            )
                            # Parse the boolean value attributes
                            for item in bool_parser:
                                neighbors_node = self._add_node(
                                    neighbor,
                                    item,
                                    item.replace("-", "_"),
                                    neighbors_node,
                                )

                            # Parse the non-boolean leaf attributes
                            for item in cfg_parser:
                                neighbors_node = self._add_node(
                                    neighbor,
                                    item,
                                    item.replace("-", "_"),
                                    neighbors_node,
                                    True,
                                )

                            # Generate commands for nodes with child attributes
                            self.parse_attrib(neighbors_node, neighbor)

            bgp_xml.append(bgp_root)

        return bgp_xml

    def parse_attrib(self, bgp_root, want):
        # Generate config commands for advertise-bgp-static
        if want.get("advertise_bgp_static"):
            ad_bgp_static_node = build_child_xml_node(
                bgp_root,
                "advertise-bgp-static",
            )
            ad_bgp_static = want.get("advertise_bgp_static")
            if "policy" in ad_bgp_static.keys():
                build_child_xml_node(
                    ad_bgp_static_node,
                    "policy",
                    ad_bgp_static["policy"],
                )

        # Generate config commands for advertise-external
        if want.get("advertise_external"):
            ad_ext_node = build_child_xml_node(bgp_root, "advertise-external")
            ad_ext = want.get("advertise_external")
            if "conditional" in ad_ext.keys():
                build_child_xml_node(ad_ext_node, "conditional")

        # Generate config commands for bfd-liveness-detection
        if want.get("bfd_liveness_detection"):
            bfd_live_node = build_child_xml_node(
                bgp_root,
                "bfd-liveness-detection",
            )
            bfd_live_detect = want.get("bfd_liveness_detection")

            # Add node for authentication

            if "authentication" in bfd_live_detect.keys():
                bld_auth = bfd_live_detect["authentication"]
                bld_auth_node = build_child_xml_node(
                    bfd_live_node,
                    "authentication",
                )
                # Add node for algorithm
                if "algorithm" in bld_auth.keys():
                    build_child_xml_node(
                        bld_auth_node,
                        "algorithm",
                        bld_auth["algorithm"],
                    )
                # Add node for key-chain
                if "key_chain" in bld_auth.keys():
                    build_child_xml_node(
                        bld_auth_node,
                        "key-chain",
                        bld_auth["key_chain"],
                    )
                # Add node for loose-check
                if "loose_check" in bld_auth.keys():
                    b_val = bld_auth.get("loose_check")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(bld_auth_node, "loose-check")
            # Add node for detection-time
            if "detection_time" in bfd_live_detect.keys():
                d_time = bfd_live_detect["detection_time"]
                bld_dtime_node = build_child_xml_node(
                    bfd_live_node,
                    "detection-time",
                )
                # Add node for threshold
                if "threshold" in d_time.keys():
                    build_child_xml_node(
                        bld_dtime_node,
                        "threshold",
                        d_time["threshold"],
                    )
            # Add node for transmit-interval
            if "transmit_interval" in bfd_live_detect.keys():
                t_int = bfd_live_detect["transmit_interval"]
                t_int_node = build_child_xml_node(
                    bfd_live_node,
                    "transmit-interval",
                )
                # Add node for minimum-interval
                if "minimum_interval" in t_int.keys():
                    build_child_xml_node(
                        t_int_node,
                        "minimum-interval",
                        t_int["minimum_interval"],
                    )
            # Add node for holddown-interval
            if "holddown_interval" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node,
                    "holddown-interval",
                    bfd_live_detect["holddown_interval"],
                )
            # Add node for minimum-receive-interval
            if "minimum_receive_interval" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node,
                    "minimum-receive-interval",
                    bfd_live_detect["minimum_receive_interval"],
                )
            # Add node for minimum-interval
            if "minimum_interval" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node,
                    "minimum-interval",
                    bfd_live_detect["minimum_interval"],
                )
            # Add node for multiplier
            if "multiplier" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node,
                    "multiplier",
                    bfd_live_detect["multiplier"],
                )
            # Add node for no-adaptation
            if "no_adaptation" in bfd_live_detect.keys():
                b_val = bfd_live_detect.get("no_adaptation")
                if b_val is not None:
                    if b_val is True:
                        build_child_xml_node(bfd_live_node, "no-adaptation")
            # Add node for session-mode
            if "session_mode" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node,
                    "session-mode",
                    bfd_live_detect["session_mode"],
                )
            # Add node for version
            if "version" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node,
                    "version",
                    bfd_live_detect["version"],
                )
        # Generate config commands for bgp-error-tolerance
        if want.get("bgp_error_tolerance"):
            bgp_err_tol_node = build_child_xml_node(
                bgp_root,
                "bgp-error-tolerance",
            )
            bgp_err_tol = want.get("bgp_error_tolerance")
            # Add node for malformed-route-limit"
            if "malformed_route_limit" in bgp_err_tol.keys():
                build_child_xml_node(
                    bgp_err_tol_node,
                    "malformed-route-limit",
                    bgp_err_tol["malformed_route_limit"],
                )
            # Add node for malformed-update-log-interval
            if "malformed_update_log_interval" in bgp_err_tol.keys():
                build_child_xml_node(
                    bgp_err_tol_node,
                    "malformed-update-log-interval",
                    bgp_err_tol["malformed_update_log_interval"],
                )
            # Generate config commands for no-malformed-route-limit
            if "no_malformed_route_limit" in bgp_err_tol.keys():
                b_val = bgp_err_tol.get("no_malformed_route_limit")
                if b_val is not None:
                    if b_val is True:
                        build_child_xml_node(
                            bgp_err_tol_node,
                            "no-malformed-route-limit",
                        )

        # Generate config commands for bmp
        if want.get("bmp"):
            bmp_node = build_child_xml_node(bgp_root, "bmp")
            bmp = want.get("bmp")
            # Add node for monitor
            if "monitor" in bmp.keys():
                b_val = bmp.get("monitor")
                if b_val is not None:
                    if b_val is True:
                        build_child_xml_node(bmp_node, "monitor", "enable")
                    else:
                        build_child_xml_node(bmp_node, "monitor", "disable")

            # Add node for route-monitoring
            if "route_monitoring" in bmp.keys():
                r_mon_node = build_child_xml_node(bmp_node, "route-monitoring")
                r_mon = bmp["route_monitoring"]
                # Add node for none
                if "none" in r_mon.keys():
                    b_val = r_mon.get("none")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(r_mon_node, "none")
                # Add node for post-policy
                if "post_policy_exclude_non_eligible" in r_mon.keys():
                    b_val = r_mon.get("post_policy_exclude_non_eligible")
                    if b_val is not None:
                        if b_val is True:
                            policy_node = build_child_xml_node(
                                r_mon_node,
                                "post-policy",
                            )
                            build_child_xml_node(
                                policy_node,
                                "exclude-non-eligible",
                            )
                elif "post_policy" in r_mon.keys():
                    b_val = r_mon.get("post_policy")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(r_mon_node, "post-policy")
                # Add node for post-policy
                if "pre_policy_exclude_non_feasible" in r_mon.keys():
                    b_val = r_mon.get("pre_policy_exclude_non_feasible")
                    if b_val is not None:
                        if b_val is True:
                            policy_node = build_child_xml_node(
                                r_mon_node,
                                "pre-policy",
                            )
                            build_child_xml_node(
                                policy_node,
                                "exclude-non-eligible",
                            )
                elif "pre-policy" in r_mon.keys():
                    b_val = r_mon.get("pre_policy")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(r_mon_node, "pre-policy")

        # Generate config commands for egress-te
        if want.get("egress_te"):
            et_node = build_child_xml_node(bgp_root, "egress-te")
            et = want.get("egress_te")
            if "backup_path" in et:
                build_child_xml_node(
                    et_node,
                    "backup-path",
                    et.get("backup_path"),
                )

        # Generate config commands for egress-te-backup-paths
        if want.get("egress_te_backup_paths"):
            etbp_node = build_child_xml_node(
                bgp_root,
                "egress-te-backup-paths",
            )
            etbp = want.get("egress_te_backup_paths")
            # generate commands for templates
            templates = etbp.get("templates")
            for template in templates:
                template_node = build_child_xml_node(etbp_node, "template")
                # add name node
                if "path_name" in template.keys():
                    build_child_xml_node(
                        template_node,
                        "name",
                        template.get("path_name"),
                    )
                # add peers
                if "peers" in template.keys():
                    peers = template.get("peers")
                    for peer in peers:
                        peer_node = build_child_xml_node(template_node, "peer")
                        build_child_xml_node(peer_node, "name", peer)
                # add remote-nexthop
                if "remote_nexthop" in template.keys():
                    build_child_xml_node(
                        template_node,
                        "remote-nexthop",
                        template.get("remote_nexthop"),
                    )
                # add ip-forward
                if "ip_forward" in template.keys():
                    ipf = template.get("ip_forward")
                    ipf_node = build_child_xml_node(
                        template_node,
                        "ip-forward",
                    )

                    if "rti_name" not in ipf.keys():
                        build_child_xml_node(
                            ipf_node,
                            "name",
                            ipf.get("rti_name"),
                        )

        # Generate config commands for allow
        if want.get("allow"):
            allow = want.get("allow")
            for network in allow:
                build_child_xml_node(bgp_root, "allow", network)

        # Generate config commands for optimal-route-reflection
        if want.get("optimal_route_reflection"):
            orr_node = build_child_xml_node(
                bgp_root,
                "optimal-route-reflection",
            )
            orr = want.get("optimal_route_reflection")
            if "igp_backup" in orr.keys():
                build_child_xml_node(
                    orr_node,
                    "igp-backup",
                    orr.get("igp_backup"),
                )
            if "igp_primary" in orr.keys():
                build_child_xml_node(
                    orr_node,
                    "igp-primary",
                    orr.get("igp_primary"),
                )

    def _state_deleted(self, want, have):
        """The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        bgp_xml = []
        parser = [
            "accept-remote-nexthop",
            "add-path-display-ipv4-address",
            "advertise-bgp-static",
            "advertise-external",
            "advertise-from-main-vpn-tables",
            "advertise-inactive",
            "advertise-peer-as",
            "authentication-algorithm",
            "authentication-key",
            "authentication-key-chain",
            "bfd-liveness-detection",
            "bgp-error-tolerance",
            "bmp",
            "group",
            "cluster",
            "damping",
            "description",
            "disable",
            "egress-te-sid-stats",
            "enforce-first-as",
            "export",
            "forwarding-context",
            "hold-time",
            "holddown-all-stale-labels",
            "import",
            "include-mp-next-hop",
            "ipsec-sa",
            "keep",
            "local-address",
            "local-interface",
            "local-preference",
            "log-updown",
            "mtu-discovery",
            "no-advertise-peer-as",
            "no-aggregator-id",
            "no-client-reflect",
            "no-precision-timers",
            "passive",
            "peer-as",
            "precision-timers",
            "preference",
            "out-delay",
            "rfc6514-compliant-safi129",
            "route-server-client",
            "send-addpath-optimization",
            "sr-preference-override",
            "stale-labels-holddown-period",
            "tcp-aggressive-transmission",
            "tcp-mss",
            "ttl",
            "unconfigured-peer-graceful-restart",
            "vpn-apply-export",
        ]
        if have is not None:
            bgp_root = build_root_xml_node("bgp")
            for attrib in parser:
                build_child_xml_node(
                    bgp_root,
                    attrib,
                    None,
                    {"delete": "delete"},
                )
            autonomous_system = have.get("as_number")
            if autonomous_system:
                build_child_xml_node(
                    self.routing_options,
                    "autonomous-system",
                    None,
                    {"delete": "delete"},
                )
            bgp_xml.append(bgp_root)
        return bgp_xml

    def _state_purged(self, want, have):
        """The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        bgp_xml = []
        delete = {"delete": "delete"}
        build_child_xml_node(self.protocols, "bgp", None, delete)
        autonomous_system = have.get("as_number")
        if autonomous_system:
            build_child_xml_node(
                self.routing_options,
                "autonomous-system",
                None,
                {"delete": "delete"},
            )
        return bgp_xml

    def _add_node(self, want, h_key, w_key, node, cfg=False):
        """Append the child node to the root node
        :param want: the desired configuration as a dictionary
        :param h_key: the current configuration key
        :param: node: root node
        """
        if cfg:
            if want.get(w_key):
                build_child_xml_node(node, h_key, want[w_key])
        else:
            if w_key in want.keys():
                b_val = want.get(w_key)
                if b_val is not None:
                    if b_val is True:
                        build_child_xml_node(node, h_key)
        return node
