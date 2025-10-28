#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_snmp_server class
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


class Snmp_server(ConfigBase):
    """
    The junos_snmp_server class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["snmp_server"]

    def __init__(self, module):
        super(Snmp_server, self).__init__(module)

    def get_snmp_server_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        snmp_server_facts = facts["ansible_network_resources"].get(
            "snmp_server",
        )
        if not snmp_server_facts:
            return {}
        return snmp_server_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_snmp_server_facts = self.get_snmp_server_facts()
        else:
            existing_snmp_server_facts = {}
        if state == "gathered":
            existing_snmp_server_facts = self.get_snmp_server_facts()
            result["gathered"] = existing_snmp_server_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_snmp_server_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_snmp_server_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]

        else:
            diff = None
            config_xmls = self.set_config(existing_snmp_server_facts)
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

            changed_snmp_server_facts = self.get_snmp_server_facts()

            result["before"] = existing_snmp_server_facts
            if result["changed"]:
                result["after"] = changed_snmp_server_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_snmp_server_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_snmp_server_facts
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
        self.root = build_root_xml_node("configuration")
        self.snmp = build_child_xml_node(self.root, "snmp")
        cmd_lst = []
        state = self._module.params["state"]
        if state in ("merged", "replaced", "rendered", "overridden") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state,
                ),
            )
        if state == "deleted":
            self._state_deleted(want, have)
        elif state in ("merged", "rendered"):
            self._state_merged(want, have)
        elif state == "replaced":
            self._state_replaced(want, have)
        elif state == "overridden":
            self._state_replaced(want, have)

        if self.root is not None:
            for xml in self.root.getchildren():
                xml = tostring(xml)
                cmd_lst.append(xml)
        return cmd_lst

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self._state_deleted(want, have)
        self.snmp = build_child_xml_node(self.root, "snmp")
        self._state_merged(want, have)

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        want = remove_empties(want)
        snmp_node = self.snmp
        # add arp node
        if "arp" in want.keys():
            arp = want.get("arp")
            if arp.get("host_name_resolution"):
                arp_node = build_child_xml_node(snmp_node, "arp")
                build_child_xml_node(arp_node, "host-name-resolution")
            elif arp.get("set"):
                build_child_xml_node(snmp_node, "arp")

        # add node client list
        if "client_lists" in want.keys():
            client_lists = want.get("client_lists")
            for client in client_lists:
                client_node = build_child_xml_node(snmp_node, "client-list")
                # add name node
                build_child_xml_node(client_node, "name", client.get("name"))
                if "addresses" in client.keys():
                    addresses = client.get("addresses")
                    for address in addresses:
                        add_lst_node = build_child_xml_node(
                            client_node,
                            "client-address-list",
                        )
                        build_child_xml_node(
                            add_lst_node,
                            "name",
                            address["address"],
                        )
                        if address.get("restrict"):
                            build_child_xml_node(add_lst_node, "restrict")

        # add routing_instance_access
        if "routing_instance_access" in want.keys():
            ria = want.get("routing_instance_access")

            if "access_lists" not in ria.keys() and ria.get("set"):
                build_child_xml_node(snmp_node, "routing-instance-access")
            elif "access_lists" in ria.keys():
                ria_node = build_child_xml_node(
                    snmp_node,
                    "routing-instance-access",
                )
                access_lists = ria.get("access_lists")
                for item in access_lists:
                    al_node = build_child_xml_node(ria_node, "access-list")
                    build_child_xml_node(al_node, "name", item)
        # add communities node
        if "communities" in want.keys():
            communities = want.get("communities")
            for community in communities:
                comm_node = build_child_xml_node(snmp_node, "community")
                build_child_xml_node(comm_node, "name", community["name"])
                if "authorization" in community.keys():
                    build_child_xml_node(
                        comm_node,
                        "authorization",
                        community["authorization"],
                    )
                if "clients" in community.keys():
                    clients = community.get("clients")
                    for client in clients:
                        client_node = build_child_xml_node(
                            comm_node,
                            "clients",
                        )
                        build_child_xml_node(
                            client_node,
                            "name",
                            client["address"],
                        )
                        if client.get("restrict"):
                            build_child_xml_node(client_node, "restrict")
                if "client_list_name" in community.keys():
                    build_child_xml_node(
                        comm_node,
                        "client-list-name",
                        community.get("client_list_name"),
                    )
                if "routing_instances" in community.keys():
                    routing_instances = community.get("routing_instances")
                    for inst in routing_instances:
                        inst_node = build_child_xml_node(
                            comm_node,
                            "routing-instance",
                        )
                        build_child_xml_node(inst_node, "name", inst["name"])
                        if "clients" in inst.keys():
                            clients = inst.get("clients")
                            for client in clients:
                                client_node = build_child_xml_node(
                                    inst_node,
                                    "clients",
                                )
                                build_child_xml_node(
                                    client_node,
                                    "name",
                                    client["address"],
                                )
                                if client.get("restrict"):
                                    build_child_xml_node(
                                        client_node,
                                        "restrict",
                                    )
                        if "client_list_name" in inst.keys():
                            build_child_xml_node(
                                inst_node,
                                "client-list-name",
                                inst.get("client_list_name"),
                            )
                if "view" in community.keys():
                    build_child_xml_node(
                        comm_node,
                        "view",
                        community.get("view"),
                    )

        # add contact node
        if "contact" in want.keys():
            build_child_xml_node(snmp_node, "contact", want.get("contact"))

        # add customization node
        if "customization" in want.keys():
            custom = want.get("customization")
            if custom.get("ether_stats_ifd_only"):
                custom_node = build_child_xml_node(snmp_node, "customization")
                build_child_xml_node(custom_node, "ether-stats-ifd-only")

        # add description node
        if "description" in want.keys():
            build_child_xml_node(
                snmp_node,
                "description",
                want.get("description"),
            )

        # add engine_id
        if "engine_id" in want.keys():
            engine = want.get("engine_id")
            engine_node = build_child_xml_node(snmp_node, "engine-id")
            if "local" in engine.keys():
                build_child_xml_node(engine_node, "local", engine["local"])
            if engine.get("use_default_ip_address"):
                build_child_xml_node(engine_node, "use-default-ip-address")
            if engine.get("use_mac_address"):
                build_child_xml_node(engine_node, "use-mac-address")

        # add filter_duplicates node
        if want.get("filter_duplicates"):
            build_child_xml_node(snmp_node, "filter-duplicates")

        # add filter_interfaces node
        if "filter_interfaces" in want.keys():
            fints = want.get("filter_interfaces")

            if "all_internal_interfaces" not in fints.keys() and "interfaces" not in fints.keys():
                build_child_xml_node(snmp_node, "filter-interfaces")
            else:
                fints_node = build_child_xml_node(
                    snmp_node,
                    "filter-interfaces",
                )
                if "all_internal_interfaces" in fints.keys():
                    build_child_xml_node(fints_node, "all-internal-interfaces")
                if "interfaces" in fints.keys():
                    interfaces = fints.get("interfaces")
                    for item in interfaces:
                        int_node = build_child_xml_node(
                            fints_node,
                            "interfaces",
                        )
                        build_child_xml_node(int_node, "name", item)

        # add health_monitor node
        if "health_monitor" in want.keys():
            health = want.get("health_monitor")

            if "falling_threshold" not in health.keys() and "rising_threshold" not in health.keys():
                if "idp" not in health.keys() and "interval" not in health.keys():
                    build_child_xml_node(snmp_node, "health-monitor")
            else:
                health_node = build_child_xml_node(snmp_node, "health-monitor")
                if "falling_threshold" in health.keys():
                    build_child_xml_node(
                        health_node,
                        "falling-threshold",
                        health.get("falling_threshold"),
                    )
                if "rising_threshold" in health.keys():
                    build_child_xml_node(
                        health_node,
                        "rising-threshold",
                        health.get("rising_threshold"),
                    )
                if "interval" in health.keys():
                    build_child_xml_node(
                        health_node,
                        "interval",
                        health.get("interval"),
                    )
                if health.get("idp"):
                    build_child_xml_node(health_node, "idp")

        # add if_count_with_filter_interfaces
        if want.get("if_count_with_filter_interfaces"):
            build_child_xml_node(snmp_node, "if-count-with-filter-interfaces")

        # add interfaces node
        if "interfaces" in want.keys():
            interfaces = want.get("interfaces")
            for item in interfaces:
                build_child_xml_node(snmp_node, "interface", item)

        # add location
        if "location" in want.keys():
            build_child_xml_node(snmp_node, "location", want.get("location"))

        # add logical_system_trap_filter
        if want.get("logical_system_trap_filter"):
            build_child_xml_node(snmp_node, "logical-system-trap-filter")

        # add name
        if "name" in want.keys():
            build_child_xml_node(snmp_node, "system-name", want.get("name"))

        # add nonvolatile
        if "nonvolatile" in want.keys():
            nonvolatile = want.get("nonvolatile")
            non_node = build_child_xml_node(snmp_node, "nonvolatile")
            if "commit_delay" in nonvolatile.keys():
                build_child_xml_node(
                    non_node,
                    "commit-delay",
                    nonvolatile.get("commit_delay"),
                )

        # add rmon
        if "rmon" in want.keys():
            rmon = want.get("rmon")

            if "alarms" not in rmon.keys() and "events" not in rmon.keys() and want.get("set"):
                build_child_xml_node(snmp_node, "rmon")
            else:
                rmon_node = build_child_xml_node(snmp_node, "rmon")
                if "alarms" in rmon.keys():
                    alarms = rmon.get("alarms")
                    for alarm in alarms:
                        alarm_node = build_child_xml_node(rmon_node, "alarm")
                        for key in alarm.keys():
                            if key == "id":
                                build_child_xml_node(
                                    alarm_node,
                                    "name",
                                    alarm.get("id"),
                                )
                            else:
                                build_child_xml_node(
                                    alarm_node,
                                    key.replace("_", "-"),
                                    alarm.get(key),
                                )
                if "events" in rmon.keys():
                    events = rmon.get("events")
                    for event in events:
                        event_node = build_child_xml_node(rmon_node, "event")
                        for key in event.keys():
                            if key == "id":
                                build_child_xml_node(
                                    event_node,
                                    "name",
                                    event.get("id"),
                                )
                            else:
                                build_child_xml_node(
                                    event_node,
                                    key.replace("_", "-"),
                                    event.get(key),
                                )
        # subagent
        if "subagent" in want.keys():
            subagent = want.get("subagent")
            sub_node = build_child_xml_node(snmp_node, "subagent")
            if "tcp" in subagent.keys():
                tcp = subagent.get("tcp")
                if tcp.get("set") and "routing_instances_default" not in tcp.keys():
                    build_child_xml_node(sub_node, "tcp")
                elif tcp.get("routing_instances_default"):
                    tcp_node = build_child_xml_node(sub_node, "tcp")
                    routing_node = build_child_xml_node(
                        tcp_node,
                        "routing-instance",
                    )
                    build_child_xml_node(routing_node, "default")

        # traceoptions
        if "traceoptions" in want.keys():
            options = want.get("traceoptions")
            trace_node = build_child_xml_node(snmp_node, "traceoptions")

            if "file" in options.keys():
                file = options.get("file")
                file_node = build_child_xml_node(trace_node, "file")
                if "match" in file.keys():
                    build_child_xml_node(file_node, "match", file.get("match"))
                if "files" in file.keys():
                    build_child_xml_node(file_node, "files", file.get("files"))
                if "no_world_readable" in file.keys():
                    build_child_xml_node(file_node, "no-world-readable")
                if "world_readable" in file.keys():
                    build_child_xml_node(file_node, "world-readable")
                if "size" in file.keys():
                    build_child_xml_node(file_node, "size", file.get("size"))

            if "flag" in options.keys():
                flags = options.get("flag")
                for key in flags.keys():
                    flag_node = build_child_xml_node(trace_node, "flag")
                    build_child_xml_node(
                        flag_node,
                        "name",
                        key.replace("_", "-"),
                    )

            if "memory_trace" in options.keys():
                mem = options.get("memory_trace")

                if mem.get("set") and "size" not in mem.keys():
                    build_child_xml_node(trace_node, "memory-trace")
                elif "size" in mem.keys():
                    mem_node = build_child_xml_node(trace_node, "memory-trace")
                    build_child_xml_node(mem_node, "size", mem.get("size"))

        if "trap_groups" in want.keys():
            groups = want.get("trap_groups")

            for trap in groups:
                trap_node = build_child_xml_node(snmp_node, "trap-group")
                for key in trap.keys():
                    if key == "name":
                        build_child_xml_node(
                            trap_node,
                            "name",
                            trap["name"],
                        )
                    if key == "destination_port":
                        build_child_xml_node(
                            trap_node,
                            "destination-port",
                            trap["destination_port"],
                        )
                    if key == "categories":
                        cat_node = build_child_xml_node(
                            trap_node,
                            "categories",
                        )
                        categories = trap.get("categories")
                        for key in categories:
                            if key == "otn_alarms":
                                alarms = categories.get("otn_alarms")
                                alarm_node = build_child_xml_node(
                                    cat_node,
                                    "otn-alarms",
                                )
                                for key in alarms:
                                    build_child_xml_node(
                                        alarm_node,
                                        key.replace("_", "-"),
                                    )
                            else:
                                build_child_xml_node(
                                    cat_node,
                                    key.replace("_", "-"),
                                )
                    if key == "routing_instance":
                        build_child_xml_node(
                            trap_node,
                            "routing-instance",
                            trap.get(key),
                        )
                    if key == "version":
                        build_child_xml_node(
                            trap_node,
                            "version",
                            trap.get(key),
                        )
                    if key == "targets":
                        targets = trap.get("targets")
                        for target in targets:
                            tar_node = build_child_xml_node(
                                trap_node,
                                "targets",
                            )
                            build_child_xml_node(tar_node, "name", target)
        # trap_options
        if "trap_options" in want.keys():
            options = want.get("trap_options")
            if options.keys() == {"set"}:
                build_child_xml_node(snmp_node, "trap-options")
            else:
                trap_node = build_child_xml_node(snmp_node, "trap-options")
                if "agent_address" in options.keys():
                    agent = options.get("agent_address")
                    if agent.get("outgoing_interface"):
                        agent_node = build_child_xml_node(
                            trap_node,
                            "agent-address",
                            "outgoing-interface",
                        )

                if options.get("context_oid"):
                    build_child_xml_node(trap_node, "context-oid")
                if "routing_instance" in options.keys():
                    inst = options.get("routing_instances")
                    build_child_xml_node(
                        trap_node,
                        "routing-instance",
                        inst,
                    )
                if "source_address" in options.keys():
                    address = options.get("source_address")
                    source_node = build_child_xml_node(
                        trap_node,
                        "source-address",
                    )
                    if "address" in address.keys():
                        build_child_xml_node(
                            source_node,
                            "address",
                            address.get("address"),
                        )
                    if "lowest_loopback" in address.keys():
                        build_child_xml_node(
                            source_node,
                            "lowest-loopback",
                        )
        if "views" in want.keys():
            views = want.get("views")
            for view in views:
                view_node = build_child_xml_node(snmp_node, "view")

                if "name" in view.keys():
                    build_child_xml_node(
                        view_node,
                        "name",
                        view.get("name"),
                    )
                if "oids" in view.keys():
                    oids = view.get("oids")
                    for oid in oids:
                        oids_node = build_child_xml_node(view_node, "oid")
                        if "oid" in oid.keys():
                            build_child_xml_node(
                                oids_node,
                                "name",
                                oid["oid"],
                            )
                        if "exclude" in oid.keys():
                            build_child_xml_node(oids_node, "exclude")
                        if "include" in oid.keys():
                            build_child_xml_node(oids_node, "include")
        # snmp_v3
        if "snmp_v3" in want.keys():
            snmpv3 = want.get("snmp_v3")
            v3_node = build_child_xml_node(snmp_node, "v3")

            if "notify" in snmpv3.keys():
                notify = snmpv3.get("notify")
                for item in notify:
                    not_node = build_child_xml_node(v3_node, "notify")
                    for key in item.keys():
                        build_child_xml_node(not_node, key, item.get(key))
            if "notify_filter" in snmpv3.keys():
                filters = snmpv3.get("notify_filter")
                for filter in filters:
                    fil_node = build_child_xml_node(v3_node, "notify-filter")
                    if "name" in filter.keys():
                        build_child_xml_node(
                            fil_node,
                            "name",
                            filter.get("name"),
                        )
                    if "oids" in filter.keys():
                        oids = filter.get("oids")
                        for oid in oids:
                            oids_node = build_child_xml_node(fil_node, "oid")
                            if "oid" in oid.keys():
                                build_child_xml_node(
                                    oids_node,
                                    "name",
                                    oid["oid"],
                                )
                            if "exclude" in oid.keys():
                                build_child_xml_node(oids_node, "exclude")
                            if "include" in oid.keys():
                                build_child_xml_node(oids_node, "include")
            if "snmp_community" in snmpv3.keys():
                snmp_community = snmpv3.get("snmp_community")
                for snmp in snmp_community:
                    snmp_node = build_child_xml_node(v3_node, "snmp-community")
                    for key in snmp.keys():
                        if key == "community_index":
                            build_child_xml_node(
                                snmp_node,
                                "name",
                                snmp.get(key),
                            )
                        else:
                            build_child_xml_node(
                                snmp_node,
                                key.replace("_", "-"),
                                snmp.get(key),
                            )

            if "target_addresses" in snmpv3.keys():
                addresses = snmpv3.get("target_addresses")
                for address in addresses:
                    tar_node = build_child_xml_node(v3_node, "target-address")
                    for key in address:
                        build_child_xml_node(
                            tar_node,
                            key.replace("_", "-"),
                            address.get(key),
                        )

            # target_parameters
            if "target_parameters" in snmpv3.keys():
                parameters = snmpv3.get("target_parameters")

                for param in parameters:
                    param_node = build_child_xml_node(
                        v3_node,
                        "target-parameters",
                    )

                    if "name" in param:
                        build_child_xml_node(
                            param_node,
                            "name",
                            param.get("name"),
                        )
                    if "notify_filter" in param:
                        build_child_xml_node(
                            param_node,
                            "notify-filter",
                            param.get("notify_filter"),
                        )
                    if "parameters" in param:
                        subnode = build_child_xml_node(
                            param_node,
                            "parameters",
                        )
                        parameter = param.get("parameters")
                        for key in parameter.keys():
                            build_child_xml_node(
                                subnode,
                                key.replace("_", "-"),
                                parameter.get(key),
                            )
            # usm
            if "usm" in snmpv3.keys():
                usm = snmpv3.get("usm")

                usm_node = build_child_xml_node(v3_node, "usm")
                if "local_engine" in usm.keys():
                    local = usm.get("local_engine")

                    local_node = build_child_xml_node(usm_node, "local-engine")
                    if "users" in local.keys():
                        users = local.get("users")
                        for user in users:
                            user_node = build_child_xml_node(
                                local_node,
                                "user",
                            )
                            for key in user.keys():
                                if key == "name":
                                    build_child_xml_node(
                                        user_node,
                                        "name",
                                        user["name"],
                                    )
                                elif key == "authentication_none":
                                    build_child_xml_node(
                                        user_node,
                                        "authentication-none",
                                    )
                                elif key == "privacy_none":
                                    build_child_xml_node(
                                        user_node,
                                        "privacy-none",
                                    )
                                else:
                                    sub_dict = user.get(key)
                                    sub_node = build_child_xml_node(
                                        user_node,
                                        key.replace("_", "-"),
                                    )

                                    if "authentication" in key:
                                        build_child_xml_node(
                                            sub_node,
                                            "authentication-key",
                                            sub_dict["key"],
                                        )
                                        build_child_xml_node(
                                            sub_node,
                                            "authentication-password",
                                            sub_dict["password"],
                                        )
                                    else:
                                        build_child_xml_node(
                                            sub_node,
                                            "privacy-key",
                                            sub_dict["key"],
                                        )
                                        build_child_xml_node(
                                            sub_node,
                                            "privacy-password",
                                            sub_dict["password"],
                                        )
                if "remote_engine" in usm.keys():
                    remotes = usm.get("remote_engine")

                    for remote in remotes:
                        remote_node = build_child_xml_node(
                            usm_node,
                            "remote-engine",
                        )
                        if "id" in remote:
                            build_child_xml_node(
                                remote_node,
                                "name",
                                remote.get("id"),
                            )
                        if "users" in remote.keys():
                            users = remote.get("users")
                            for user in users:
                                user_node = build_child_xml_node(
                                    remote_node,
                                    "user",
                                )
                                for key in user.keys():
                                    if key == "name":
                                        build_child_xml_node(
                                            user_node,
                                            "name",
                                            user["name"],
                                        )
                                    elif key == "authentication_none":
                                        build_child_xml_node(
                                            user_node,
                                            "authentication-none",
                                        )
                                    elif key == "privacy_none":
                                        build_child_xml_node(
                                            user_node,
                                            "privacy-none",
                                        )
                                    else:
                                        sub_dict = user.get(key)
                                        sub_node = build_child_xml_node(
                                            user_node,
                                            key.replace("_", "-"),
                                        )

                                        if "authentication" in key:
                                            build_child_xml_node(
                                                sub_node,
                                                "authentication-key",
                                                sub_dict["key"],
                                            )
                                            build_child_xml_node(
                                                sub_node,
                                                "authentication-password",
                                                sub_dict["password"],
                                            )
                                        else:
                                            build_child_xml_node(
                                                sub_node,
                                                "privacy-key",
                                                sub_dict["key"],
                                            )
                                            build_child_xml_node(
                                                sub_node,
                                                "privacy-password",
                                                sub_dict["password"],
                                            )

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        delete = {"delete": "delete"}
        if have is not None:
            build_child_xml_node(self.root, "snmp", None, delete)
