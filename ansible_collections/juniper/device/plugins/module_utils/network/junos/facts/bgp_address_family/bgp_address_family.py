#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos bgp_address_family fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.bgp_address_family.bgp_address_family import (
    Bgp_address_familyArgs,
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


class Bgp_address_familyFacts(object):
    """The junos bgp_address_family fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Bgp_address_familyArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_device_data(self, connection, config_filter):
        """
        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for bgp_address_family
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
                            <protocols>
                                <bgp>
                                </bgp>
                            </protocols>
                            <routing-options>
                                <autonomous-system/>
                            </routing-options>
                        </configuration>
                        """
            data = self.get_device_data(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/protocols/bgp")
        autonomous_system_path = data.xpath(
            "configuration/routing-options/autonomous-system",
        )
        if autonomous_system_path:
            self.autonomous_system = self._get_xml_dict(
                autonomous_system_path.pop(),
            )
        else:
            self.autonomous_system = ""
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {}
        if objs:
            facts["bgp_address_family"] = {}
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["bgp_address_family"] = utils.remove_empties(
                params["config"],
            )
        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root),
            dict_constructor=dict,
        )
        return xml_dict

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        bgp_af_config = {}

        # Parse facts for BGP address-family global node
        conf = conf.get("bgp")
        bgp_af_config["address_family"] = self.parse_af_facts(conf)

        # Parse BGP group address-family config node
        if "group" in conf.keys():
            groups = conf.get("group")
            groups_af_lst = []
            group_af_dict = {}
            if isinstance(groups, list):
                for group in groups:
                    af_facts = self.parse_af_facts(group)
                    if af_facts is not None:
                        group_af_dict["address_family"] = af_facts
                    # Parse neighbors af node
                    if "neighbor" in group.keys():
                        neighbors_af_lst = []
                        nh_af_dict = {}
                        neighbors = group.get("neighbor")
                        if isinstance(neighbors, list):
                            for neighbor in neighbors:
                                # nh_af_dict["name"] = neighbor.get("neighbor_address")
                                naf_facts = self.parse_af_facts(neighbor)
                                if naf_facts is not None:
                                    nh_af_dict["address_family"] = naf_facts
                                    nh_af_dict["neighbor_address"] = neighbor.get("name")
                                if nh_af_dict:
                                    neighbors_af_lst.append(nh_af_dict)
                                    nh_af_dict = {}
                        else:
                            naf_facts = self.parse_af_facts(neighbors)
                            if naf_facts is not None:
                                nh_af_dict["address_family"] = naf_facts
                                nh_af_dict["neighbor_address"] = neighbors.get(
                                    "name",
                                )
                            if nh_af_dict:
                                neighbors_af_lst.append(nh_af_dict)
                        if neighbors_af_lst:
                            group_af_dict["neighbors"] = neighbors_af_lst
                    if group_af_dict:
                        group_af_dict["name"] = group.get("name")
                        groups_af_lst.append(group_af_dict)
                        group_af_dict = {}
            else:
                af_facts = self.parse_af_facts(groups)
                if af_facts is not None:
                    group_af_dict["address_family"] = af_facts
                # Parse neighbors af node
                if "neighbor" in groups.keys():
                    neighbors_af_lst = []
                    nh_af_dict = {}
                    neighbors = groups.get("neighbor")
                    if isinstance(neighbors, list):
                        for neighbor in neighbors:
                            # nh_af_dict["name"] = neighbor.get("name")
                            naf_facts = self.parse_af_facts(neighbor)
                            if naf_facts is not None:
                                nh_af_dict["address_family"] = naf_facts
                                nh_af_dict["neighbor_address"] = neighbor.get(
                                    "name",
                                )
                            if nh_af_dict:
                                neighbors_af_lst.append(nh_af_dict)
                                nh_af_dict = {}
                    else:
                        naf_facts = self.parse_af_facts(neighbors)
                        if naf_facts is not None:
                            nh_af_dict["address_family"] = naf_facts
                            nh_af_dict["neighbor_address"] = neighbors.get(
                                "name",
                            )
                        if nh_af_dict:
                            neighbors_af_lst.append(nh_af_dict)
                    if neighbors_af_lst:
                        group_af_dict["neighbors"] = neighbors_af_lst
                if group_af_dict:
                    group_af_dict["name"] = groups.get("name")
                    groups_af_lst.append(group_af_dict)
            if groups_af_lst is not None:
                bgp_af_config["groups"] = groups_af_lst

        return utils.remove_empties(bgp_af_config)

    def parse_af_facts(self, conf):
        """

        :return:
        """
        nlri_params = [
            "evpn",
            "inet",
            "inet-mdt",
            "inet-mvpn",
            "inet-vpn",
            "inet6",
            "inet6-mvpn",
            "inet6-vpn",
            "iso-vpn",
            "l2vpn",
            "traffic-engineering",
        ]
        # TBD wrap route-target'
        nlri_types = [
            "any",
            "flow",
            "multicast",
            "labeled-unicast",
            "segment-routing-te",
            "unicast",
            "signaling",
        ]
        bgp = conf.get("family")
        address_family = []
        # Parse NLRI Parameters
        for param in nlri_params:
            af_dict = {}
            if bgp and param in bgp.keys():
                af_type = []
                nlri_param = bgp.get(param)
                for nlri in nlri_types:
                    af_dict["afi"] = param
                    if nlri in nlri_param.keys():
                        nlri_dict = self.parse_nlri(nlri_param, nlri)
                        if nlri_dict:
                            af_type.append(nlri_dict)
                if af_type:
                    af_dict["af_type"] = af_type
            if af_dict:
                address_family.append(af_dict)

        return address_family

    def parse_nlri(self, cfg, nlri_t):
        """

        :param cfg:
        :return:
        """
        nlri_dict = {}
        if cfg and nlri_t in cfg.keys():
            nlri_dict["type"] = nlri_t
            nlri = cfg.get(nlri_t)

            if not nlri:
                nlri_dict["set"] = True
                return nlri_dict
            # Parse accepted-prefix-limit
            if "accepted-prefix-limit" in nlri.keys():
                apl_dict = self.parse_accepted_prefix_limit(nlri)
                # populate accepted_prefix_limit
                if apl_dict:
                    nlri_dict["accepted_prefix_limit"] = apl_dict

            # Parse add-path
            if "add-path" in nlri.keys():
                ap_dict = self.parse_add_path(nlri)
                # populate accepted_prefix_limit
                if ap_dict:
                    nlri_dict["add_path"] = ap_dict

            # Parse aggregate-label
            if "aggregate-label" in nlri.keys():
                al_dict = self.parse_aggregate_label(nlri)
                # populate aggregate-label
                if apl_dict:
                    nlri_dict["aggregate_label"] = al_dict

            # Parse aigp
            if "aigp" in nlri.keys():
                aigp_dict = self.parse_aigp(nlri)
                # populate aigp
                if aigp_dict:
                    nlri_dict["aigp"] = aigp_dict

            # Parse and populate damping
            if "damping" in nlri.keys():
                nlri_dict["damping"] = True

            # Parse defer-initial-multipath-build
            if "defer-initial-multipath-build" in nlri.keys():
                dimb_dict = self.parse_defer_initial_multipath_build(nlri)
                # populate defer_initial_multipath_build
                if dimb_dict:
                    nlri_dict["defer_initial_multipath_build"] = dimb_dict

            # Parse delay-route-advertisements
            if "delay-route-advertisements" in nlri.keys():
                dra_dict = self.parse_delay_route_advertisements(nlri)
                # populate delay_route_advertisements
                if dra_dict:
                    nlri_dict["delay_route_advertisements"] = dra_dict

            # Parse entropy-label
            if "entropy-label" in nlri.keys():
                el_dict = self.parse_entropy_label(nlri)
                # populate entropy-label
                if el_dict:
                    nlri_dict["entropy_label"] = el_dict

            # Parse explicit-null
            if "explicit-null" in nlri.keys():
                en_dict = self.parse_explicit_null(nlri)
                # populate explicit-null
                if en_dict:
                    nlri_dict["explicit_null"] = en_dict

            # Parse extended-nexthop
            if "extended-nexthop" in nlri.keys():
                nlri_dict["extended_nexthop"] = True

            # Parse extended-nexthop-color
            if "extended-nexthop-color" in nlri.keys():
                nlri_dict["extended_nexthop_color"] = True

            # Parse forwarding-state-bit
            if "graceful-restart" in nlri.keys():
                gr = nlri.get("graceful-restart")
                if "forwarding-state-bit" in gr.keys():
                    fsb = gr.get("forwarding-state-bit")
                    nlri_dict["graceful_restart_forwarding_state_bit"] = fsb

            # Parse legacy-redirect-ip-action
            if "legacy-redirect-ip-action" in nlri.keys():
                lria_dict = self.parse_legacy_redirect_ip_action(nlri)
                # populate legacy_redirect_ip_action
                if lria_dict:
                    nlri_dict["legacy_redirect_ip_action"] = lria_dict

            # Parse local-ipv4-address
            if "local-ipv4-address" in nlri.keys():
                nlri_dict["local_ipv4_address"] = nlri.get(
                    "local-ipv4-address",
                )

            # Parse loops
            if "loops" in nlri.keys():
                loops = nlri.get("loops")
                nlri_dict["loops"] = loops.get("loops")

            # Parse no-install
            if "no-install" in nlri.keys():
                nlri_dict["no_install"] = True

            # Parse no-validate
            if "no-validate" in nlri.keys():
                nlri_dict["no_validate"] = nlri.get("no-validate")

            # Parse output-queue-priority
            if "output-queue-priority" in nlri.keys():
                oqp = nlri.get("output-queue-priority")
                if "expedited" in oqp.keys():
                    nlri_dict["output_queue_priority_expedited"] = True
                if "priority" in oqp.keys():
                    nlri_dict["output_queue_priority_priority"] = oqp.get(
                        "priority",
                    )

            # Parse per-group-label
            if "per-group-label" in nlri.keys():
                nlri_dict["per_group_label"] = True

            # Parse per-prefix-label
            if "per-prefix-label" in nlri.keys():
                nlri_dict["per_prefix_label"] = True

            # Parse resolve-vpn
            if "resolve-vpn" in nlri.keys():
                nlri_dict["resolve_vpn"] = True

            # Parse prefix-limit
            if "prefix-limit" in nlri.keys():
                pl_dict = self.parse_accepted_prefix_limit(nlri)
                # populate delay_route_advertisements
                if pl_dict:
                    nlri_dict["prefix_limit"] = pl_dict

            # Parse resolve-vpn
            if "resolve-vpn" in nlri.keys():
                nlri_dict["resolve_vpn"] = True

            # Parse rib
            if "rib" in nlri.keys():
                nlri_dict["rib"] = "inet.3"

            # Parse rib-group
            if "rib-group" in nlri.keys():
                nlri_dict["rib_group"] = nlri.get("rib-group")

            # Parse route-refresh-priority
            if "route-refresh-priority" in nlri.keys():
                oqp = nlri.get("route-refresh-priority")
                if "expedited" in oqp.keys():
                    nlri_dict["route_refresh_priority_expedited"] = True
                if "priority" in oqp.keys():
                    nlri_dict["route_refresh_priority_priority"] = oqp.get(
                        "priority",
                    )

            # Parse secondary-independent-resolution
            if "secondary-independent-resolution" in nlri.keys():
                nlri_dict["secondary_independent_resolution"] = True

            # Parse strip-nexthop
            if "strip-nexthop" in nlri.keys():
                nlri_dict["strip_nexthop"] = True

            # Parse topology
            if "topology" in nlri.keys():
                t_list = self.parse_topology(nlri)
                # populate topology
                if t_list:
                    nlri_dict["topology"] = t_list

            # Parse traffic-statistics
            if "traffic-statistics" in nlri.keys():
                ts_dict = self.parse_traffic_statistics(nlri)
                # populate topology
                if ts_dict:
                    nlri_dict["traffic_statistics"] = ts_dict

            # Parse withdraw-priority
            if "withdraw-priority" in nlri.keys():
                oqp = nlri.get("withdraw-priority")
                if "expedited" in oqp.keys():
                    nlri_dict["withdraw_priority_expedited"] = True
                if "priority" in oqp.keys():
                    nlri_dict["withdraw_priority_priority"] = oqp.get(
                        "priority",
                    )
            return nlri_dict

    def parse_accepted_prefix_limit(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        apl_dict = {}
        if "accepted-prefix-limit" in cfg.keys():
            apl = cfg.get("accepted-prefix-limit")
        else:
            apl = cfg.get("prefix-limit")
        if "maximum" in apl.keys():
            apl_dict["maximum"] = apl.get("maximum")
        if "teardown" in apl.keys():
            if not apl.get("teardown"):
                apl_dict["teardown"] = True
            else:
                td = apl.get("teardown")
                if "idle-timeout" in td.keys():
                    if not td.get("idle-timeout"):
                        apl_dict["idle_timeout"] = True
                    elif "forever" in td["idle-timeout"].keys():
                        apl_dict["forever"] = True
                    elif "timeout" in td["idle-timeout"].keys():
                        apl_dict["idle_timeout_value"] = td["idle-timeout"].get("timeout")
                if "limit-threshold" in td.keys():
                    apl_dict["limit_threshold"] = td.get("limit-threshold")
        return apl_dict

    def parse_add_path(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        ap_dict = {}
        ap = cfg.get("add-path")
        if "receive" in ap.keys():
            ap_dict["receive"] = True
        if "send" in ap.keys():
            send = ap.get("send")
            s_dict = {}
            if "include-backup-path" in send.keys():
                s_dict["include_backup_path"] = send.get("include-backup-path")
            if "path-count" in send.keys():
                s_dict["path_count"] = send.get("path-count")
            if "multipath" in send.keys():
                s_dict["multipath"] = True
            if "path-selection-mode" in send.keys():
                psm = send.get("path-selection-mode")
                psm_dict = {}
                if "all-paths" in psm.keys():
                    psm_dict["all_paths"] = True
                if "equal-cost-paths" in psm.keys():
                    psm_dict["equal_cost_paths"] = True
                s_dict["path_selection_mode"] = psm_dict
            if "prefix-policy" in send.keys():
                s_dict["prefix_policy"] = send.get("prefix-policy")
            ap_dict["send"] = s_dict
        return ap_dict

    def parse_aggregate_label(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        al_dict = {}
        al = cfg.get("aggregate-label")
        if not al:
            al_dict["set"] = True
        else:
            al_dict["community"] = al.get("community")
        return al_dict

    def parse_aigp(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        aigp_dict = {}
        aigp = cfg.get("aigp")
        if aigp and "disable" in aigp.keys():
            aigp_dict["disable"] = True
        else:
            aigp_dict["set"] = True
        return aigp_dict

    def parse_defer_initial_multipath_build(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        dimb_dict = {}
        dimb = cfg.get("defer-initial-multipath-build")
        if not dimb:
            dimb_dict["set"] = True

        elif "maximum-delay" in dimb.keys():
            dimb_dict["maximum_delay"] = dimb.get("maximum-delay")
        return dimb_dict

    def parse_legacy_redirect_ip_action(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        lria_dict = {}
        lria = cfg.get("legacy-redirect-ip-action")
        if not lria:
            lria_dict["set"] = True
        else:
            if "send" in lria.keys():
                lria_dict["send"] = True
            if "receive" in lria.keys():
                lria_dict["receive"] = True
        return lria_dict

    def parse_delay_route_advertisements(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        dra_dict = {}
        dra = cfg.get("delay-route-advertisements")
        if not dra:
            dra_dict["set"] = True
        else:
            if "maximum-delay" in dra.keys():
                mxd = dra.get("maximum-delay")
                if "route-age" in mxd.keys():
                    dra_dict["max_delay_route_age"] = mxd.get("route-age")
                if "routing-uptime" in mxd.keys():
                    dra_dict["max_delay_routing_uptime"] = mxd.get(
                        "routing-uptime",
                    )
            if "minimum-delay" in dra.keys():
                mid = dra.get("minimum-delay")
                if "inbound-convergence" in mid.keys():
                    dra_dict["min_delay_inbound_convergence"] = mid.get(
                        "inbound-convergence",
                    )
                if "routing-uptime" in mid.keys():
                    dra_dict["min_delay_routing_uptime"] = mid.get(
                        "routing-uptime",
                    )
        return dra_dict

    def parse_entropy_label(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        el_dict = {}
        el = cfg.get("entropy-label")
        if not el:
            el_dict["set"] = True
        else:
            if "import" in el.keys():
                el_dict["import"] = el.get("import")
            if "no-next-hop-validation" in el.keys():
                el_dict["no_next_hop_validation"] = True
        return el_dict

    def parse_explicit_null(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        en_dict = {}
        en = cfg.get("explicit-null")
        if not en:
            en_dict["set"] = True
        elif "connected-only" in en.keys():
            en_dict["connected_only"] = True
        return en_dict

    def parse_topology(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        top_dict = {}
        topology_list = []
        topologies = cfg.get("topology")
        if isinstance(topologies, list):
            for topology in topologies:
                top_dict["name"] = topology["name"]
                communities = topology.get("community")
                community_lst = []
                if isinstance(communities, list):
                    for community in communities:
                        community_lst.append(community)
                else:
                    community_lst.append(communities)
                if community_lst is not None:
                    top_dict["community"] = community_lst
                if top_dict is not None:
                    topology_list.append(top_dict)
                    top_dict = {}
        else:
            top_dict["name"] = topologies["name"]
            communities = topologies.get("community")
            community_lst = []
            if isinstance(communities, list):
                for community in communities:
                    community_lst.append(community)
            else:
                community_lst.append(communities)
            if community_lst is not None:
                top_dict["community"] = community_lst
            if top_dict is not None:
                topology_list.append(top_dict)
        return topology_list

    def parse_traffic_statistics(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        ts_dict = {}
        ts = cfg.get("traffic-statistics")
        if not ts:
            ts_dict["set"] = True
        else:
            if "interval" in ts.keys():
                ts_dict["interval"] = ts.get("interval")
            if "labeled-path" in ts.keys():
                ts_dict["labeled_path"] = True
            if "file" in ts.keys():
                file = ts.get("file")
                file_dict = {}
                if "files" in file.keys():
                    file_dict["files"] = file.get("files")
                if "no-world-readable" in file.keys():
                    file_dict["no_world_readable"] = True
                if "size" in file.keys():
                    file_dict["size"] = file.get("size")
                if "world-readable" in file.keys():
                    file_dict["world_readable"] = True

        return ts_dict
