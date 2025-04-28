#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_bgp_address_family class
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


class Bgp_address_family(ConfigBase):
    """
    The junos_bgp_address_family class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["bgp_address_family"]

    def __init__(self, module):
        super(Bgp_address_family, self).__init__(module)

    def get_bgp_address_family_facts(self, data=None):
        """Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        bgp_facts = facts["ansible_network_resources"].get(
            "bgp_address_family",
        )
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
            existing_bgp_address_family_facts = self.get_bgp_address_family_facts()
        else:
            existing_bgp_address_family_facts = {}
        if state == "gathered":
            existing_bgp_address_family_facts = self.get_bgp_address_family_facts()
            result["gathered"] = existing_bgp_address_family_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_bgp_address_family_facts(
                data=running_config,
            )
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_bgp_address_family_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            diff = None
            config_xmls = self.set_config(existing_bgp_address_family_facts)
            with locked_config(self._module):
                for config_xml in to_list(config_xmls):
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

            changed_bgp_address_family_facts = self.get_bgp_address_family_facts()

            result["before"] = existing_bgp_address_family_facts
            if result["changed"]:
                result["after"] = changed_bgp_address_family_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_bgp_address_family_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_bgp_address_family_facts
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
        self.bgp = build_child_xml_node(self.protocols, "bgp")
        self.routing_options = build_child_xml_node(
            self.root,
            "routing-options",
        )
        state = self._module.params["state"]
        if state in ("merged", "replaced", "rendered", "overridden") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state,
                ),
            )
        config_xmls = []
        if state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state == "purged":
            config_xmls = self._state_purged(want, have)
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)
        elif state == "overridden":
            config_xmls = self._state_overridden(want, have)

        for xml in config_xmls:
            self.bgp.append(xml)
        cfg_lst = []

        if config_xmls:
            for xml in self.root.getchildren():
                xml = tostring(xml)
                cfg_lst.append(xml)
        return cfg_lst

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
        family_xml = []

        family_root = build_root_xml_node("family")

        want = remove_empties(want)

        # Generate xml node for autonomous-system
        if want.get("as_number"):
            build_child_xml_node(
                self.routing_options,
                "autonomous-system",
                want.get("as_number"),
            )
        w_af_list = want.get("address_family")
        # render global address family attribute commands
        self.render_af(w_af_list, family_root)

        # render commands for group address family attribute commands
        if "groups" in want.keys():
            groups = want.get("groups")
            for group in groups:
                groups_node = build_root_xml_node("group")
                build_child_xml_node(groups_node, "name", group["name"])
                g_family_root = build_child_xml_node(groups_node, "family")
                w_gaf_list = group.get("address_family")
                self.render_af(w_gaf_list, g_family_root)

                # render neighbor address-family commands
                if "neighbors" in group.keys():
                    neighbors = group.get("neighbors")
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
                        n_family_root = build_child_xml_node(
                            neighbors_node,
                            "family",
                        )
                        w_naf_list = neighbor.get("address_family")
                        self.render_af(w_naf_list, n_family_root)

            family_xml.append(groups_node)

        family_xml.append(family_root)

        return family_xml

    def render_af(self, w_af_list, family_root):
        if w_af_list:
            for waf in w_af_list:
                # Add the nlri node
                nlri_node = build_child_xml_node(family_root, waf["afi"])
                # Read nlri_types list
                nlri_types = waf.get("af_type")
                for type in nlri_types:
                    # Add the node for nlri type
                    type_node = build_child_xml_node(nlri_node, type["type"])
                    #  Add node for accepted-prefix-limit
                    if "accepted_prefix_limit" in type.keys():
                        apl = type.get("accepted_prefix_limit")
                        # build node for accepted-prefix-limit
                        apl_node = build_child_xml_node(
                            type_node,
                            "accepted-prefix-limit",
                        )
                        # Add node for maximum
                        if "maximum" in apl.keys():
                            build_child_xml_node(
                                apl_node,
                                "maximum",
                                apl["maximum"],
                            )
                        # Add node for teardown
                        td_node = None
                        if "limit_threshold" in apl.keys():
                            td_node = build_child_xml_node(
                                apl_node,
                                "teardown",
                            )
                            # add node for limit-threshold
                            build_child_xml_node(
                                td_node,
                                "limit-threshold",
                                apl.get("limit_threshold"),
                            )
                        elif "teardown" in apl.keys():
                            td_node = build_child_xml_node(
                                apl_node,
                                "teardown",
                            )
                        it_node = None
                        # Add node for teardown idle_timeout
                        if "idle_timeout_value" in apl.keys():
                            it_node = build_child_xml_node(
                                td_node,
                                "idle-timeout",
                            )
                            # add node for timeout
                            build_child_xml_node(
                                it_node,
                                "timeout",
                                apl.get("idle_timeout_value"),
                            )

                        elif "forever" in apl.keys():
                            if it_node is None:
                                it_node = build_child_xml_node(
                                    td_node,
                                    "idle-timeout",
                                )
                            if it_node is not None:
                                it_node = build_child_xml_node(
                                    td_node,
                                    "idle-timeout",
                                )
                            # add forever node
                            build_child_xml_node(it_node, "forever")

                    #  Add node for add-path
                    if "add_path" in type.keys():
                        ap = type.get("add_path")
                        # build node for add_path
                        ap_node = build_child_xml_node(type_node, "add-path")
                        # add node for receive
                        if "receive" in ap.keys():
                            build_child_xml_node(ap_node, "receive")
                        if "send" in ap.keys():
                            # add node for send
                            send = ap.get("send")
                            send_node = build_child_xml_node(ap_node, "send")
                            # add node for path_count
                            if "path_count" in send.keys():
                                build_child_xml_node(
                                    send_node,
                                    "path-count",
                                    send.get("path_count"),
                                )
                            # add node for include_backup_path
                            if "include_backup_path" in send.keys():
                                build_child_xml_node(
                                    send_node,
                                    "include-backup-path",
                                    send.get("include_backup_path"),
                                )
                            # add node for path_selection_mode
                            if "path_selection_mode" in send.keys():
                                psm = send.get("path_selection_mode")
                                psm_node = build_child_xml_node(
                                    send_node,
                                    "path-selection-mode",
                                )
                                # add node for all_paths
                                if "all_paths" in psm.keys():
                                    build_child_xml_node(psm_node, "all-paths")
                                # add node for equal_cost_paths
                                if "equal_cost_paths" in psm.keys():
                                    build_child_xml_node(
                                        psm_node,
                                        "equal-cost-paths",
                                    )
                            # add node for prefix_policy
                            if "prefix_policy" in send.keys():
                                build_child_xml_node(
                                    send_node,
                                    "prefix-policy",
                                    send.get("prefix_policy"),
                                )
                    #  Add node for aggregate_label
                    if "aggregate_label" in type.keys():
                        al = type.get("aggregate_label")
                        # build node for aggregate_label
                        al_node = build_child_xml_node(
                            type_node,
                            "aggregate_label",
                        )
                        # add node community
                        if "community" in al.keys():
                            build_child_xml_node(
                                al_node,
                                "community",
                                al.get("community"),
                            )

                    #  Add node for aigp
                    if "aigp" in type.keys():
                        aigp = type.get("aigp")
                        # build node for aigp
                        if "disable" in aigp.keys():
                            aigp_node = build_child_xml_node(type_node, "aigp")
                            build_child_xml_node(aigp_node, "disable")
                        else:
                            build_child_xml_node(type_node, "aigp")

                    #  Add node for damping
                    if "damping" in type.keys():
                        build_child_xml_node(type_node, "damping")

                    #  Add node for defer_initial_multipath_build
                    if "defer_initial_multipath_build" in type.keys():
                        dimb = type.get("defer_initial_multipath_build")
                        # build node for defer_initial_multipath_build
                        dimb_node = build_child_xml_node(
                            type_node,
                            "defer-initial-multipath-build",
                        )
                        # add node maximum_delay
                        if dimb and "maximum_delay" in dimb.keys():
                            build_child_xml_node(
                                dimb_node,
                                "maximum-delay",
                                dimb.get("maximum_delay"),
                            )

                    #  add node delay-route-advertisements
                    if "delay_route_advertisements" in type.keys():
                        dra = type.get("delay_route_advertisements")
                        # build node for delay_route_advertisements
                        dra_node = build_child_xml_node(
                            type_node,
                            "delay-route-advertisements",
                        )
                        # add maximum delay node
                        if (
                            "max_delay_route_age" in dra.keys()
                            or "max_delay_routing_uptime" in dra.keys()
                        ):
                            maxd_node = build_child_xml_node(
                                dra_node,
                                "maximum-delay",
                            )
                            # add node route-age
                            if "max_delay_route_age" in dra.keys():
                                build_child_xml_node(
                                    maxd_node,
                                    "route-age",
                                    dra.get("max_delay_route_age"),
                                )

                            # add node routing-uptime
                            if "max_delay_routing_uptime" in dra.keys():
                                build_child_xml_node(
                                    maxd_node,
                                    "routing-uptime",
                                    dra.get("max_delay_routing_uptime"),
                                )
                        # add minimum delay node
                        if (
                            "min_delay_inbound_convergence" in dra.keys()
                            or "min_delay_routing_uptime" in dra.keys()
                        ):
                            mind_node = build_child_xml_node(
                                dra_node,
                                "minimum-delay",
                            )
                            # add node inbound-convergence
                            if "min_delay_inbound_convergence" in dra.keys():
                                build_child_xml_node(
                                    mind_node,
                                    "inbound-convergence",
                                    dra.get("min_delay_inbound_convergence"),
                                )

                            # add node routing-uptime
                            if "min_delay_routing_uptime" in dra.keys():
                                build_child_xml_node(
                                    mind_node,
                                    "routing-uptime",
                                    dra.get("min_delay_routing_uptime"),
                                )

                    #  add node entropy-label
                    if "entropy_label" in type.keys():
                        el = type.get("entropy_label")
                        # build node for entropy_label
                        el_node = build_child_xml_node(
                            type_node,
                            "entropy-label",
                        )
                        # add node import
                        if "import" in el.keys():
                            build_child_xml_node(
                                el_node,
                                "import",
                                el.get("import"),
                            )
                        # add node no_next_hop_validation
                        if "no_next_hop_validation" in el.keys():
                            build_child_xml_node(
                                el_node,
                                "no-next-hop-validation",
                            )

                    #  add node explicit-null
                    if "explicit_null" in type.keys():
                        en = type.get("explicit_null")
                        # add node connected-only
                        if "connected_only" in en.keys():
                            en_node = build_child_xml_node(
                                type_node,
                                "explicit-null",
                            )
                            build_child_xml_node(en_node, "connected-only")
                        else:
                            # build node for explicit_null
                            build_child_xml_node(type_node, "explicit-null")

                    #  add node extended-nexthop
                    if "extended_nexthop" in type.keys():
                        enh = type.get("extended_nexthop")
                        # add node extended-nexthop
                        if enh:
                            build_child_xml_node(type_node, "extended-nexthop")

                    #  add node extended-nexthop-color
                    if "extended_nexthop_color" in type.keys():
                        enhc = type.get("extended_nexthop_color")
                        # add node extended-nexthop-color
                        if enhc:
                            build_child_xml_node(
                                type_node,
                                "extended-nexthop-color",
                            )

                    #  add node forwarding-state-bit
                    if "graceful_restart_forwarding_state_bit" in type.keys():
                        grfs = type.get(
                            "graceful_restart_forwarding_state_bit",
                        )

                        # add node forwarding-state-bit
                        gr_node = build_child_xml_node(
                            type_node,
                            "graceful-restart",
                        )
                        build_child_xml_node(
                            gr_node,
                            "forwarding-state-bit",
                            grfs,
                        )

                    #  add node local-ipv4-address
                    if "local_ipv4_address" in type.keys():
                        # add node local-ipv4-address
                        build_child_xml_node(
                            type_node,
                            "local-ipv4-address",
                            type.get("local_ipv4_address"),
                        )

                    #  add node legacy-redirect-ip-action
                    if "legacy_redirect_ip_action" in type.keys():
                        lria = type.get("legacy_redirect_ip_action")
                        # add node legacy_redirect_ip_action
                        lria_node = build_child_xml_node(
                            type_node,
                            "legacy-redirect-ip-action",
                        )
                        if "send" in lria.keys():
                            build_child_xml_node(lria_node, "send")
                        if "receive" in lria.keys():
                            build_child_xml_node(lria_node, "receive")

                    # add node loops
                    if "loops" in type.keys():
                        build_child_xml_node(
                            type_node,
                            "loops",
                            type.get("loops"),
                        )

                    #  add no-install
                    if "no_install" in type.keys():
                        if type.get("no_install"):
                            build_child_xml_node(type_node, "no-install")

                    # add node no-validate
                    if "no_validate" in type.keys():
                        build_child_xml_node(
                            type_node,
                            "no-validate",
                            type.get("no_validate"),
                        )

                    # add node output-queue-priority
                    if (
                        "output_queue_priority_expedited" in type.keys()
                        or "output_queue_priority_priority" in type.keys()
                    ):
                        # node for output-queue-priority
                        oqp_node = build_child_xml_node(
                            type_node,
                            "output-queue-priority",
                        )
                        # add node expedited
                        if "output_queue_priority_expedited" in type.keys() and type.get(
                            "output_queue_priority_expedited",
                        ):
                            build_child_xml_node(oqp_node, "expedited")
                        # add node priority
                        if "output_queue_priority_priority" in type.keys():
                            build_child_xml_node(
                                oqp_node,
                                "priority",
                                type.get("output_queue_priority_priority"),
                            )

                    #  add per-prefix-label
                    if "per_prefix_label" in type.keys():
                        if type.get("per_prefix_label"):
                            build_child_xml_node(type_node, "per-prefix-label")

                    #  add per-group-label
                    if "per_group_label" in type.keys():
                        if type.get("per_group_label"):
                            build_child_xml_node(type_node, "per-group-label")

                    #  Add node for prefix-limit
                    if "prefix_limit" in type.keys():
                        pl = type.get("prefix_limit")
                        # build node for prefix-limit
                        pl_node = build_child_xml_node(
                            type_node,
                            "prefix-limit",
                        )
                        # Add node for maximum
                        if "maximum" in pl.keys():
                            build_child_xml_node(
                                pl_node,
                                "maximum",
                                pl["maximum"],
                            )
                        # Add node for teardown
                        td_node = None
                        if "limit_threshold" in pl.keys():
                            td_node = build_child_xml_node(
                                pl_node,
                                "teardown",
                                pl.get("limit_threshold"),
                            )
                        elif "teardown" in pl.keys():
                            td_node = build_child_xml_node(pl_node, "teardown")
                        it_node = None
                        # Add node for teardown idle_timeout
                        if "idle_timeout_value" in pl.keys():
                            it_node = build_child_xml_node(
                                td_node,
                                "idle-timeout",
                                pl.get("idle_timeout_value"),
                            )
                        elif "idle_timeout" in pl.keys():
                            it_node = build_child_xml_node(
                                td_node,
                                "idle-timeout",
                            )
                        if "forever" in pl.keys():
                            if it_node is None:
                                it_node = build_child_xml_node(
                                    td_node,
                                    "idle-timeout",
                                )
                            # add forever node
                            build_child_xml_node(it_node, "forever")

                    # add resolve-vpn
                    if "resolve_vpn" in type.keys():
                        if type.get("resolve_vpn"):
                            build_child_xml_node(type_node, "resolve-vpn")

                    #  add rib
                    if "rib" in type.keys():
                        rib_node = build_child_xml_node(type_node, "rib")
                        # add node inet.3
                        build_child_xml_node(rib_node, "inet.3")

                    # add rib-group
                    if "ribgroup_name" in type.keys():
                        build_child_xml_node(
                            type_node,
                            "rib-group",
                            type.get("ribgroup_name"),
                        )

                    # add node route-refresh-priority
                    if (
                        "route_refresh_priority_expedited" in type.keys()
                        or "route_refresh_priority_priority" in type.keys()
                    ):
                        # node for route-refresh-priority
                        rrp_node = build_child_xml_node(
                            type_node,
                            "route-refresh-priority",
                        )
                        # add node expedited
                        if "route_refresh_priority_expedited" in type.keys() and type.get(
                            "route_refresh_priority_expedited",
                        ):
                            build_child_xml_node(rrp_node, "expedited")
                        # add node priority
                        if "route_refresh_priority_priority" in type.keys():
                            build_child_xml_node(
                                rrp_node,
                                "priority",
                                type.get("route_refresh_priority_priority"),
                            )

                    # add secondary-independent-resolution
                    if "secondary_independent_resolution" in type.keys():
                        if type.get("secondary_independent_resolution"):
                            build_child_xml_node(
                                type_node,
                                "secondary-independent-resolution",
                            )

                    # add node withdraw-priority
                    if (
                        "withdraw_priority_expedited" in type.keys()
                        or "withdraw_priority_priority" in type.keys()
                    ):
                        # node for withdraw-priority
                        wp_node = build_child_xml_node(
                            type_node,
                            "withdraw-priority",
                        )
                        # add node expedited
                        if "withdraw_priority_expedited" in type.keys() and type.get(
                            "withdraw_priority_expedited",
                        ):
                            build_child_xml_node(wp_node, "expedited")
                        # add node priority
                        if "withdraw_priority_priority" in type.keys():
                            build_child_xml_node(
                                wp_node,
                                "priority",
                                type.get("withdraw_priority_priority"),
                            )

                    # add strip-nexthop
                    if "strip_nexthop" in type.keys():
                        if type.get("strip_nexthop"):
                            build_child_xml_node(type_node, "strip-nexthop")

                    # add topology
                    if "topology" in type.keys():
                        topologies = type.get("topology")
                        top_node = build_child_xml_node(type_node, "topology")
                        for topology in topologies:
                            if "name" in topology.keys():
                                build_child_xml_node(
                                    top_node,
                                    "name",
                                    topology.get("name"),
                                )
                            if "community" in topology.keys():
                                communities = topology.get("community")
                                for community in communities:
                                    build_child_xml_node(
                                        top_node,
                                        "community",
                                        community,
                                    )

                    # add traffic-statistics
                    if "traffic_statistics" in type.keys():
                        ts = type.get("traffic_statistics")
                        ts_node = build_child_xml_node(
                            type_node,
                            "traffic-statistics",
                        )
                        # add node interval
                        if "interval" in ts.keys():
                            build_child_xml_node(
                                ts_node,
                                "interval",
                                ts.get("interval"),
                            )
                        # add node labeled-path
                        if "labeled_path" in ts.keys and ts.get(
                            "labeled_path",
                        ):
                            build_child_xml_node(ts_node, "labeled-path")

    def _state_deleted(self, want, have):
        """The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        bgp_xml = []
        family_root = None
        groups_node = None
        existing_groups = []
        if have is not None and have.get("address_family"):
            h_af = have.get("address_family")
            existing_af = [af["afi"] for af in h_af]

            h_groups = have.get("groups")
            if h_groups:
                for group in h_groups:
                    existing_groups.append(group["name"])
            if not want or not want.get("address_family"):
                want = have

            # Delete root address family
            w_af = want["address_family"]
            for af in w_af:
                if af["afi"] not in existing_af:
                    continue
                if family_root is None:
                    family_root = build_child_xml_node(self.bgp, "family")
                build_child_xml_node(
                    family_root,
                    af["afi"],
                    None,
                    {"delete": "delete"},
                )

            # Delete group address-family
            w_groups = want.get("groups")
            if w_groups:
                for group in w_groups:
                    if group["name"] not in existing_groups:
                        continue

                    groups_node = build_child_xml_node(self.bgp, "group")
                    build_child_xml_node(groups_node, "name", group["name"])

                    for h_group in h_groups:
                        if h_group["name"] == group["name"]:
                            address_family = h_group.get("address_family")
                            if address_family:
                                for af in address_family:
                                    family_node = build_child_xml_node(
                                        groups_node,
                                        "family",
                                    )
                                    build_child_xml_node(
                                        family_node,
                                        af["afi"],
                                        None,
                                        {"delete": "delete"},
                                    )
                            if "neighbors" in h_group.keys():
                                h_neighbors = h_group.get("neighbors")
                                for neighbor in h_neighbors:
                                    if "address_family" in neighbor.keys():
                                        neighbors_node = build_child_xml_node(
                                            groups_node,
                                            "neighbor",
                                        )
                                        build_child_xml_node(
                                            neighbors_node,
                                            "name",
                                            neighbor["neighbor_address"],
                                        )
                                        address_family = neighbor.get(
                                            "address_family",
                                        )
                                        for af in address_family:
                                            family_node = build_child_xml_node(
                                                neighbors_node,
                                                "family",
                                            )
                                            build_child_xml_node(
                                                family_node,
                                                af["afi"],
                                                None,
                                                {"delete": "delete"},
                                            )

            if groups_node is not None:
                bgp_xml.append(groups_node)
            if family_root is not None:
                bgp_xml.append(family_root)
        return bgp_xml

    def _state_overridden(self, want, have):
        """The xml configuration generator when state is merged
        :rtype: A list
        :returns: the xml configuration necessary to merge the provided into
                  the current configuration
        """
        bgp_xml = []
        family_root = None
        if have is not None and have.get("address_family"):
            h_af = have.get("address_family")
            existing_af = [af["afi"] for af in h_af]
            for af in existing_af:
                if family_root is None:
                    family_root = build_child_xml_node(self.bgp, "family")
                build_child_xml_node(
                    family_root,
                    af,
                    None,
                    {"delete": "delete"},
                )
            if family_root is not None:
                bgp_xml.append(family_root)
        bgp_xml.extend(self._state_deleted(want, have))
        bgp_xml.extend(self._state_merged(want, have))
        return bgp_xml
