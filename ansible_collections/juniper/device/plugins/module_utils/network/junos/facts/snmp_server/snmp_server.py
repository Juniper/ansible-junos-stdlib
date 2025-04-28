#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos snmp_server fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.snmp_server.snmp_server import (
    Snmp_serverArgs,
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


class Snmp_serverFacts(object):
    """The junos snmp_server fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Snmp_serverArgs.argument_spec
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
        """Populate the facts for ntp_gloabl
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
                                <snmp>
                                </snmp>
                        </configuration>
                        """
            data = self.get_device_data(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/snmp")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"snmp_server": {}}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["snmp_server"] = utils.remove_empties(params["config"])
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
        snmp_server_config = {}

        # Parse facts for BGP address-family global node
        conf = conf.get("snmp")

        # Read arp node
        if "arp" in conf.keys():
            arp = conf.get("arp")
            arp_dict = {}
            if arp is None:
                arp_dict["set"] = True
            elif "host-name-resolution" in arp.keys():
                arp_dict["host_name_resolution"] = True
            snmp_server_config["arp"] = arp_dict

        # Read client_lists node
        if "client-list" in conf.keys():
            snmp_server_config["client_lists"] = self.get_client_list(
                conf.get("client-list"),
            )

        # Read communities node
        if "community" in conf.keys():
            comm_lst = []
            comm_lists = conf.get("community")

            if isinstance(comm_lists, dict):
                comm_lst.append(self.get_community(comm_lists))
            else:
                for item in comm_lists:
                    comm_lst.append(self.get_community(item))
            if comm_lst:
                snmp_server_config["communities"] = comm_lst

        # Read routing-instance-access
        if "routing-instance-access" in conf.keys():
            rinst_access = conf.get("routing-instance-access")
            rints_dict = {}
            access_lst = []
            if rinst_access is None:
                rints_dict["set"] = True
            else:
                access_lists = rinst_access.get("access-list")
                if isinstance(access_lists, dict):
                    access_lst.append(access_lists["name"])
                else:
                    for item in access_lists:
                        access_lst.append(item["name"])
                rints_dict["access_lists"] = access_lst
            snmp_server_config["routing_instance_access"] = rints_dict

        # Read contact
        if "contact" in conf.keys():
            snmp_server_config["contact"] = conf.get("contact")

        # Read description
        if "description" in conf.keys():
            snmp_server_config["description"] = conf.get("description")

        # Read customization
        if "customization" in conf.keys():
            custom_dict = {}
            if "ether-stats-ifd-only" in conf["customization"].keys():
                custom_dict["ether_stats_ifd_only"] = True
            snmp_server_config["customization"] = custom_dict

        # Read engine-id
        if "engine-id" in conf.keys():
            engine_id = conf.get("engine-id")
            engine_id_dict = {}
            if "local" in engine_id.keys():
                engine_id_dict["local"] = engine_id["local"]
            elif "use-default-ip-address" in engine_id.keys():
                engine_id_dict["use_default_ip_address"] = True
            else:
                engine_id_dict["use_mac_address"] = True

            snmp_server_config["engine_id"] = engine_id_dict

        # Read filter-duplicates
        if "filter-duplicates" in conf.keys():
            snmp_server_config["filter_duplicates"] = True

        # Read filter-interfaces
        if "filter-interfaces" in conf.keys():
            filter_dict = {}
            filter_interfaces = conf.get("filter-interfaces")

            if filter_interfaces is None:
                filter_dict["set"] = True
            else:
                if "all-internal-interfaces" in filter_interfaces.keys():
                    filter_dict["all_internal_interfaces"] = True
                if "interfaces" in filter_interfaces.keys():
                    int_lst = []
                    interfaces = filter_interfaces.get("interfaces")
                    if isinstance(interfaces, dict):
                        int_lst.append(interfaces["name"])
                    else:
                        for item in interfaces:
                            int_lst.append(item["name"])
                    filter_dict["interfaces"] = int_lst

            snmp_server_config["filter_interfaces"] = filter_dict

        # Read health_monitor
        if "health-monitor" in conf.keys():
            health_dict = {}
            health_monitor = conf.get("health-monitor")

            if health_monitor is None:
                health_dict["set"] = True
            else:
                if "idp" in health_monitor.keys():
                    health_dict["idp"] = True
                if "falling-threshold" in health_monitor.keys():
                    health_dict["falling_threshold"] = health_monitor["falling-threshold"]
                if "rising-threshold" in health_monitor.keys():
                    health_dict["rising_threshold"] = health_monitor["rising-threshold"]
                if "interval" in health_monitor.keys():
                    health_dict["interval"] = health_monitor["interval"]
            snmp_server_config["health_monitor"] = health_dict

        # Read if-count-with-filter-interfaces
        if "if-count-with-filter-interfaces" in conf.keys():
            snmp_server_config["if_count_with_filter_interfaces"] = True

        # Read interfaces
        if "interfaces" in conf.keys():
            int_lst = []
            interfaces = conf.get("interfaces")
            if isinstance(interfaces, dict):
                int_lst.append(interfaces["name"])
            else:
                for item in interfaces:
                    int_lst.append(item["name"])

            snmp_server_config["interfaces"] = int_lst

        # Read location
        if "location" in conf.keys():
            snmp_server_config["location"] = conf.get("location")

        # Read logical-system-trap-filter
        if "logical-system-trap-filter" in conf.keys():
            snmp_server_config["logical_system_trap_filter"] = True

        # Read name
        if "system-name" in conf.keys():
            snmp_server_config["name"] = conf.get("system-name")

        # Read nonvolatile
        if "nonvolatile" in conf.keys():
            cfg_dict = {}
            cfg_dict["commit_delay"] = conf["nonvolatile"].get("commit-delay")
            snmp_server_config["nonvolatile"] = cfg_dict

        # Read rmon
        if "rmon" in conf.keys():
            cfg_dict = {}
            events = []
            alarms = []
            rmon = conf.get("rmon")

            if rmon is None:
                cfg_dict["set"] = True
            else:
                if "event" in rmon.keys():
                    event = rmon.get("event")
                    if isinstance(event, dict):
                        events.append(self.get_events(event))
                    else:
                        for item in event:
                            events.append(self.get_events(item))
                    cfg_dict["events"] = events
                if "alarm" in rmon.keys():
                    alarm = rmon.get("alarm")
                    if isinstance(alarm, dict):
                        alarms.append(self.get_alarms(alarm))
                    else:
                        for item in alarm:
                            alarms.append(self.get_alarms(item))
                    cfg_dict["alarms"] = alarms

            snmp_server_config["rmon"] = cfg_dict

        # Read subagent node
        if "subagent" in conf.keys():
            cfg_dict = {}
            subagent = conf.get("subagent")

            if "tcp" in subagent.keys():
                tcp = subagent.get("tcp")
                tcp_dict = {}
                if tcp is None:
                    tcp_dict["set"] = True
                else:
                    tcp_dict["routing_instances_default"] = True
            cfg_dict["tcp"] = tcp_dict
            snmp_server_config["subagent"] = cfg_dict

        # Read traceoptions node
        if "traceoptions" in conf.keys():
            cfg_dict = {}
            trace_options = conf.get("traceoptions")

            if "file" in trace_options.keys():
                cfg_dict["file"] = self.get_trace_file(
                    trace_options.get("file"),
                )
            if "flag" in trace_options.keys():
                cfg_dict["flag"] = self.get_trace_flag(
                    trace_options.get("flag"),
                )
            if "memory-trace" in trace_options.keys():
                mtrace = trace_options.get("memory-trace")
                trace_dict = {}
                if mtrace is None:
                    trace_dict["set"] = True
                else:
                    trace_dict["size"] = mtrace.get("size")
                cfg_dict["memory_trace"] = trace_dict
            if "no-remote-trace" in conf.keys():
                cfg_dict["no_remote_trace"] = True

            snmp_server_config["traceoptions"] = cfg_dict

        # Read trap-group node
        if "trap-group" in conf.keys():
            cfg_lst = []
            trap_groups = conf.get("trap-group")

            if isinstance(trap_groups, dict):
                cfg_lst.append(self.get_trap_group(trap_groups))
            else:
                for item in trap_groups:
                    cfg_lst.append(self.get_trap_group(item))

            snmp_server_config["trap_groups"] = cfg_lst

        # Read trap-options node
        if "trap-options" in conf.keys():
            cfg_dict = {}
            trap_options = conf.get("trap-options")
            if trap_options is None:
                cfg_dict["set"] = True
            else:
                if "agent-address" in trap_options.keys():
                    agent_dict = {}
                    agent_dict["outgoing_interface"] = True
                    cfg_dict["agent_address"] = agent_dict
                if "context-oid" in trap_options.keys():
                    cfg_dict["context_oid"] = True
                if "enterprise-oid" in trap_options.keys():
                    cfg_dict["enterprise_oid"] = True
                if "source-address" in trap_options.keys():
                    source_address = trap_options.get("source-address")
                    source_dict = {}
                    if "address" in source_address.keys():
                        source_dict["address"] = source_address["address"]
                    if "lowest-loopback" in source_address.keys():
                        source_dict["lowest_loopback"] = True
                    cfg_dict["source_address"] = source_dict
                if "routing-instance" in trap_options.keys():
                    cfg_dict["routing_instance"] = trap_options.get(
                        "routing-instance",
                    )

            snmp_server_config["trap_options"] = cfg_dict

        # Read snmp-v3
        if "v3" in conf.keys():
            cfg_dict = {}
            snmp_v3 = conf.get("v3")

            if "notify" in snmp_v3.keys():
                notify_lst = []
                notify = snmp_v3.get("notify")
                if isinstance(notify, dict):
                    notify_lst.append(self.get_notify(notify))
                else:
                    for item in notify:
                        notify_lst.append(self.get_notify(item))
                cfg_dict["notify"] = notify_lst
            if "notify-filter" in snmp_v3.keys():
                notify_filter = snmp_v3.get("notify-filter")
                notify_lst = []
                if isinstance(notify_filter, dict):
                    notify_lst.append(self.get_notify_filter(notify_filter))
                else:
                    for item in notify_filter:
                        notify_lst.append(self.get_notify_filter(item))
                cfg_dict["notify_filter"] = notify_lst

            if "snmp-community" in snmp_v3.keys():
                comm_lst = []
                communities = snmp_v3.get("snmp-community")
                if isinstance(communities, dict):
                    comm_lst.append(self.get_snmpv3_comm(communities))
                else:
                    for item in communities:
                        comm_lst.append(self.get_snmpv3_comm(item))
                cfg_dict["snmp_community"] = comm_lst

            if "target-address" in snmp_v3.keys():
                tar_addr_lst = []
                tar_addr = snmp_v3.get("target-address")
                if isinstance(tar_addr, dict):
                    tar_addr_lst.append(self.get_snmpv3_target(tar_addr))
                else:
                    for item in tar_addr:
                        tar_addr_lst.append(self.get_snmpv3_target(item))
                cfg_dict["target_addresses"] = tar_addr_lst

            if "target-parameters" in snmp_v3.keys():
                tar_param_lst = []
                tar_params = snmp_v3.get("target-parameters")
                if isinstance(tar_params, dict):
                    tar_param_lst.append(self.get_snmpv3_param(tar_params))
                else:
                    for item in tar_params:
                        tar_param_lst.append(self.get_snmpv3_param(item))
                cfg_dict["target_parameters"] = tar_param_lst

            if "usm" in snmp_v3.keys():
                usm_dict = {}
                usm = snmp_v3.get("usm")
                if "local-engine" in usm.keys():
                    local_dict = {}
                    local_engine = usm.get("local-engine")
                    if "user" in local_engine.keys():
                        user_lst = []
                        users = local_engine.get("user")
                        if isinstance(users, dict):
                            user_lst.append(self.get_user(users))
                        else:
                            for item in users:
                                user_lst.append(self.get_user(item))
                        local_dict["users"] = user_lst

                    usm_dict["local_engine"] = local_dict

                if "remote-engine" in usm.keys():
                    remote_lst = []
                    remote_dict = {}
                    remote_engine = usm.get("remote-engine")
                    if isinstance(remote_engine, dict):
                        remote_dict["id"] = remote_engine["name"]
                        if "user" in remote_engine.keys():
                            user_lst = []
                            users = remote_engine.get("user")
                            if isinstance(users, dict):
                                user_lst.append(self.get_user(users))
                            else:
                                for item in users:
                                    user_lst.append(self.get_user(item))
                            remote_dict["users"] = user_lst
                        remote_lst.append(remote_dict)
                    else:
                        for remote_eng in remote_engine:
                            remote_dict["id"] = remote_eng["name"]
                            if "user" in remote_eng.keys():
                                user_lst = []
                                users = remote_eng.get("user")
                                if isinstance(users, dict):
                                    user_lst.append(self.get_user(users))
                                else:
                                    for item in users:
                                        user_lst.append(self.get_user(item))
                                remote_dict["users"] = user_lst
                            remote_lst.append(remote_dict)
                            remote_dict = {}
                    usm_dict["remote_engine"] = remote_lst
                cfg_dict["usm"] = usm_dict

            snmp_server_config["snmp_v3"] = cfg_dict

        # Read view
        if "view" in conf.keys():
            cfg_lst = []
            views = conf.get("view")
            if isinstance(views, dict):
                cfg_lst.append(self.get_view(views))
            else:
                for item in views:
                    cfg_lst.append(self.get_view(item))

            snmp_server_config["views"] = cfg_lst
        return utils.remove_empties(snmp_server_config)

    def get_view(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg["name"]
        if "oid" in cfg.keys():
            oid_lst = []
            oid_dict = {}
            oids = cfg.get("oid")
            if isinstance(oids, list):
                for item in oids:
                    oid_dict["oid"] = item["name"]
                    if "exclude" in item.keys():
                        oid_dict["exclude"] = True
                    if "include" in item.keys():
                        oid_dict["include"] = True
                    oid_lst.append(oid_dict)
                    oid_dict = {}
            else:
                oid_dict["oid"] = oids["name"]
                if "exclude" in oids.keys():
                    oid_dict["exclude"] = True
                if "include" in oids.keys():
                    oid_dict["include"] = True
                oid_lst.append(oid_dict)
            cfg_dict["oids"] = oid_lst

        return cfg_dict

    def get_user(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg.get("name")
        if "authentication-md5" in cfg.keys():
            auth_dict = {}
            auth_md5 = cfg.get("authentication-md5")
            auth_dict["key"] = auth_md5["authentication-key"]
            if "authentication-password" in auth_md5.keys():
                auth_dict["password"] = auth_md5["authentication-password"]
            cfg_dict["authentication_md5"] = auth_dict
        if "authentication-none" in cfg.keys():
            cfg_dict["authentication_none"] = True
        if "authentication-sha" in cfg.keys():
            auth_dict = {}
            auth_sha = cfg.get("authentication-sha")
            auth_dict["key"] = auth_sha["authentication-key"]
            if "authentication-password" in auth_sha.keys():
                auth_dict["password"] = auth_sha["authentication-password"]
            cfg_dict["authentication_sha"] = auth_dict
        if "privacy-3des" in cfg.keys():
            pri_dict = {}
            pri_3des = cfg.get("privacy-3des")
            pri_dict["key"] = pri_3des["privacy-key"]
            if "privacy-password" in pri_3des.keys():
                pri_dict["password"] = pri_3des["privacy-password"]
            cfg_dict["privacy_3des"] = pri_dict
        if "privacy-aes128" in cfg.keys():
            pri_dict = {}
            pri_aes = cfg.get("privacy-aes128")
            pri_dict["key"] = pri_aes["privacy-key"]
            if "privacy-password" in pri_aes.keys():
                pri_dict["password"] = pri_aes["privacy-password"]
            cfg_dict["privacy_aes128"] = pri_dict
        if "privacy-none" in cfg.keys():
            cfg_dict["privacy_none"] = True
        return cfg_dict

    def get_snmpv3_param(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg.get("name")
        if "notify-filter" in cfg.keys():
            cfg_dict["notify_filter"] = cfg.get("notify-filter")
        if "parameters" in cfg.keys():
            param_dict = {}
            parameters = cfg.get("parameters")
            for key in parameters.keys():
                param_dict[key.replace("-", "_")] = parameters.get(key)
            cfg_dict["parameters"] = param_dict
        return cfg_dict

    def get_snmpv3_target(self, cfg):
        cfg_dict = {}
        for key in cfg.keys():
            cfg_dict[key.replace("-", "_")] = cfg.get(key)
        return cfg_dict

    def get_snmpv3_comm(self, cfg):
        cfg_dict = {}
        cfg_dict["community_index"] = cfg["name"]
        if "context" in cfg.keys():
            cfg_dict["context"] = cfg.get("context")
        if "tag" in cfg.keys():
            cfg_dict["tag"] = cfg.get("tag")
        if "security-name" in cfg.keys():
            cfg_dict["security_name"] = cfg.get("security-name")
        if "community-name" in cfg.keys():
            cfg_dict["community_name"] = cfg.get("community-name")
        return cfg_dict

    def get_notify_filter(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg["name"]
        if "oid" in cfg.keys():
            oid_lst = []
            oid_dict = {}
            oids = cfg.get("oid")
            if isinstance(oids, list):
                for item in oids:
                    oid_dict["oid"] = item["name"]
                    if "exclude" in item.keys():
                        oid_dict["exclude"] = True
                    if "include" in item.keys():
                        oid_dict["include"] = True
                    oid_lst.append(oid_dict)
                    oid_dict = {}
            else:
                oid_dict["oid"] = oids["name"]
                if "exclude" in oids.keys():
                    oid_dict["exclude"] = True
                if "include" in oids.keys():
                    oid_dict["include"] = True
                oid_lst.append(oid_dict)
            cfg_dict["oids"] = oid_lst
        return cfg_dict

    def get_notify(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg["name"]
        if "type" in cfg.keys():
            cfg_dict["type"] = cfg.get("type")
        if "tag" in cfg.keys():
            cfg_dict["tag"] = cfg.get("tag")

        return cfg_dict

    def get_trap_group(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg.get("name")
        if "categories" in cfg.keys():
            categories_dict = {}
            categories = cfg.get("categories")
            for item in categories.keys():
                if item == "otn-alarms":
                    otn_dict = {}
                    otn_alarms = categories.get("otn-alarms")
                    for key in otn_alarms.keys():
                        otn_dict[key.replace("-", "_")] = True
                    categories_dict["otn_alarms"] = otn_dict
                else:
                    categories_dict[item.replace("-", "_")] = True
            cfg_dict["categories"] = categories_dict
        if "destination-port" in cfg.keys():
            cfg_dict["destination_port"] = cfg.get("destination-port")
        if "routing-instance" in cfg.keys():
            cfg_dict["routing_instance"] = cfg.get("routing-instance")
        if "version" in cfg.keys():
            cfg_dict["version"] = cfg.get("version")
        if "targets" in cfg.keys():
            targets_lst = []
            targets = cfg.get("targets")
            if isinstance(targets, dict):
                targets_lst.append(targets["name"])
            else:
                for item in targets:
                    targets_lst.append(item["name"])
            cfg_dict["targets"] = targets_lst

        return cfg_dict

    def get_trace_flag(self, cfg):
        cfg_dict = {}
        if isinstance(cfg, dict):
            cfg_dict[cfg["name"].replace("-", "_")] = True
        else:
            for item in cfg:
                cfg_dict[item["name"].replace("-", "_")] = True

        return cfg_dict

    def get_trace_file(self, cfg):
        cfg_dict = {}
        if "match" in cfg.keys():
            cfg_dict["match"] = cfg.get("match")
        if "files" in cfg.keys():
            cfg_dict["files"] = cfg.get("files")
        if "no-world-readable" in cfg.keys():
            cfg_dict["no_world_readable"] = True
        if "world-readable" in cfg.keys():
            cfg_dict["world_readable"] = True
        if "size" in cfg.keys():
            cfg_dict["size"] = cfg.get("size")

        return cfg_dict

    def get_events(self, cfg):
        cfg_dict = {}
        cfg_dict["id"] = cfg["name"]
        if "community" in cfg.keys():
            cfg_dict["community"] = cfg.get("community")
        if "description" in cfg.keys():
            cfg_dict["description"] = cfg.get("description")
        if "type" in cfg.keys():
            cfg_dict["type"] = cfg.get("type")
        return cfg_dict

    def get_alarms(self, cfg):
        cfg_dict = {}
        cfg_dict["id"] = cfg["name"]
        if "description" in cfg.keys():
            cfg_dict["description"] = cfg.get("description")
        if "falling-event-index" in cfg.keys():
            cfg_dict["falling_event_index"] = cfg.get("falling-event-index")
        if "falling-threshold" in cfg.keys():
            cfg_dict["falling_threshold"] = cfg.get("falling-threshold")
        if "falling-threshold-interval" in cfg.keys():
            cfg_dict["falling_threshold_interval"] = cfg.get(
                "falling-threshold-interval",
            )
        if "interval" in cfg.keys():
            cfg_dict["interval"] = cfg.get("interval")
        if "request-type" in cfg.keys():
            cfg_dict["request_type"] = cfg.get("request-type")
        if "rising-event-index" in cfg.keys():
            cfg_dict["rising_event_index"] = cfg.get("rising-event-index")
        if "rising-threshold" in cfg.keys():
            cfg_dict["rising_threshold"] = cfg.get("rising-threshold")
        if "sample-type" in cfg.keys():
            cfg_dict["sample_type"] = cfg.get("sample-type")
        if "startup-alarm" in cfg.keys():
            cfg_dict["startup_alarm"] = cfg.get("startup-alarm")
        if "syslog-subtag" in cfg.keys():
            cfg_dict["syslog_subtag"] = cfg.get("syslog-subtag")
        if "variable" in cfg.keys():
            cfg_dict["variable"] = cfg.get("variable")

        return cfg_dict

    def get_routing_instance(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg["name"]
        if "client-list-name" in cfg.keys():
            cfg_dict["client_list_name"] = cfg.get("client-list-name")
        if "clients" in cfg.keys():
            client_lst = []
            if isinstance(cfg.get("clients"), dict):
                client_lst.append(self.get_client_address(cfg.get("clients")))
            else:
                clients = cfg.get("clients")
                for item in clients:
                    client_lst.append(self.get_client_address(item))
            cfg_dict["clients"] = client_lst
        return cfg_dict

    def get_community(self, cfg):
        cfg_dict = {}
        cfg_dict["name"] = cfg["name"]
        if "authorization" in cfg.keys():
            cfg_dict["authorization"] = cfg.get("authorization")
        if "client-list-name" in cfg.keys():
            cfg_dict["client_list_name"] = cfg.get("client-list-name")
        if "clients" in cfg.keys():
            client_lst = []
            if isinstance(cfg.get("clients"), dict):
                client_lst.append(self.get_client_address(cfg.get("clients")))
            else:
                clients = cfg.get("clients")
                for item in clients:
                    client_lst.append(self.get_client_address(item))
            cfg_dict["clients"] = client_lst
        if "routing-instance" in cfg.keys():
            rinst_lst = []
            rinst_lists = cfg.get("routing-instance")

            if isinstance(rinst_lists, dict):
                rinst_lst.append(self.get_routing_instance(rinst_lists))
            else:
                for item in rinst_lists:
                    rinst_lst.append(self.get_routing_instance(item))
            if rinst_lst:
                cfg_dict["routing_instances"] = rinst_lst
        if "view" in cfg.keys():
            cfg_dict["view"] = cfg.get("view")

        return cfg_dict

    def get_client_address(self, cfg):
        cfg_dict = {}
        cfg_dict["address"] = cfg["name"]
        if "restrict" in cfg.keys():
            cfg_dict["restrict"] = True
        return cfg_dict

    def get_client_list(self, cfg):
        client_lst = []
        client_lists = cfg
        client_dict = {}
        if isinstance(client_lists, dict):
            client_dict["name"] = client_lists["name"]
            if "client-address-list" in client_lists.keys():
                client_addresses = client_lists["client-address-list"]
                client_address_lst = []
                if isinstance(client_addresses, dict):
                    client_address_lst.append(
                        self.get_client_address(client_addresses),
                    )
                else:
                    for address in client_addresses:
                        client_address_lst.append(
                            self.get_client_address(address),
                        )
                if client_address_lst:
                    client_dict["addresses"] = client_address_lst
            client_lst.append(client_dict)

        else:
            for client in client_lists:
                client_dict["name"] = client["name"]
                if "client-address-list" in client.keys():
                    client_addresses = client["client-address-list"]
                    client_address_lst = []
                    if isinstance(client_addresses, dict):
                        client_address_lst.append(
                            self.get_client_address(client_addresses),
                        )
                    else:
                        for address in client_addresses:
                            client_address_lst.append(
                                self.get_client_address(address),
                            )
                    if client_address_lst:
                        client_dict["addresses"] = client_address_lst
                client_lst.append(client_dict)
                client_dict = {}
        return client_lst
