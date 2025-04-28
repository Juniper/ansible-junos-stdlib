#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_logging_global class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible.module_utils.six import iteritems
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


class Logging_global(ConfigBase):
    """
    The junos_logging_global class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["logging_global"]

    def __init__(self, module):
        super(Logging_global, self).__init__(module)

    def get_logging_global_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        logging_global_facts = facts["ansible_network_resources"].get(
            "logging_global",
        )
        if not logging_global_facts:
            return {}
        return logging_global_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_logging_global_facts = self.get_logging_global_facts()
        else:
            existing_logging_global_facts = {}
        if state == "gathered":
            existing_logging_global_facts = self.get_logging_global_facts()
            result["gathered"] = existing_logging_global_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_logging_global_facts(
                data=running_config,
            )
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_logging_global_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]

        else:
            diff = None
            config_xmls = self.set_config(existing_logging_global_facts)
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

            changed_logging_global_facts = self.get_logging_global_facts()

            result["before"] = existing_logging_global_facts
            if result["changed"]:
                result["after"] = changed_logging_global_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_logging_global_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_logging_global_facts
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
        self.root = build_root_xml_node("system")
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
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)
        elif state == "overridden":
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
        logging_xml = []
        logging_xml.extend(self._state_deleted(want, have))
        logging_xml.extend(self._state_merged(want, have))
        return logging_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        logging_xml = []
        want = remove_empties(want)
        level_parser = [
            "any",
            "authorization",
            "change_log",
            "conflict_log",
            "daemon",
            "dfc",
            "external",
            "firewall",
            "ftp",
            "interactive_commands",
            "kernel",
            "ntp",
            "pfe",
            "security",
            "user",
        ]
        want = remove_empties(want)
        logging_node = build_root_xml_node("syslog")

        # add allow-duplicates node
        if "allow_duplicates" in want.keys() and want.get("allow_duplicates"):
            build_child_xml_node(logging_node, "allow-duplicates")

        # add archive node
        if "archive" in want.keys():
            self.render_archive(logging_node, want)

        # add console node
        if "console" in want.keys():
            console = want.get("console")
            # add any level node
            for k, v in iteritems(console):
                if v is not None:
                    console_node = build_child_xml_node(
                        logging_node,
                        "console",
                    )
                    build_child_xml_node(
                        console_node,
                        "name",
                        k.replace("_", "-"),
                    )
                    build_child_xml_node(console_node, v.get("level"))

        # add file node
        if "files" in want.keys():
            files = want.get("files")
            for file in files:
                file_node = build_child_xml_node(logging_node, "file")
                # add name node
                build_child_xml_node(file_node, "name", file.get("name"))
                # add allow-duplicates node
                if "allow_duplicates" in file.keys() and file.get(
                    "allow_duplicates",
                ):
                    build_child_xml_node(file_node, "allow-duplicates")
                # add contents
                for k, v in iteritems(file):
                    if k in level_parser and v is not None:
                        content_node = build_child_xml_node(
                            file_node,
                            "contents",
                        )
                        build_child_xml_node(
                            content_node,
                            "name",
                            k.replace("_", "-"),
                        )
                        build_child_xml_node(content_node, v.get("level"))
                # add archive node
                if "archive" in file.keys():
                    self.render_archive(file_node, file)
                # add explicit-priority
                if "explicit_priority" in file.keys() and file.get(
                    "explicit_priority",
                ):
                    build_child_xml_node(file_node, "explicit-priority")
                # add match node
                if "match" in file.keys():
                    build_child_xml_node(file_node, "match", file.get("match"))
                # add match-strings node
                if "match_strings" in file.keys():
                    match_strings = file.get("match_strings")
                    for match in match_strings:
                        build_child_xml_node(file_node, "match-strings", match)
                # add structured-data
                if "structured_data" in file.keys():
                    structured_data = file.get("structured_data")
                    s_data_node = build_child_xml_node(
                        file_node,
                        "structured-data",
                    )
                    if "brief" in structured_data.keys() and structured_data.get("brief"):
                        build_child_xml_node(s_data_node, "brief")

        # add host node
        if "hosts" in want.keys():
            hosts = want.get("hosts")
            for host in hosts:
                host_node = build_child_xml_node(logging_node, "host")
                # add name node
                build_child_xml_node(host_node, "name", host.get("name"))
                # add allow-duplicates node
                if "allow_duplicates" in host.keys() and host.get(
                    "allow_duplicates",
                ):
                    build_child_xml_node(host_node, "allow-duplicates")
                # add contents
                for k, v in iteritems(host):
                    if k in level_parser and v is not None:
                        content_node = build_child_xml_node(
                            host_node,
                            "contents",
                        )
                        build_child_xml_node(
                            content_node,
                            "name",
                            k.replace("_", "-"),
                        )
                        build_child_xml_node(content_node, v.get("level"))
                # add exclude-hostname node
                if "exclude_hostname" in host.keys() and host.get(
                    "exclude_hostname",
                ):
                    build_child_xml_node(host_node, "exclude-hostname")
                # add facility_override node
                if "facility_override" in host.keys():
                    build_child_xml_node(
                        host_node,
                        "facility-override",
                        host.get("facility_override"),
                    )
                # add log_prefix node
                if "log_prefix" in host.keys():
                    build_child_xml_node(
                        host_node,
                        "log-prefix",
                        host.get("log_prefix"),
                    )
                # add match node
                if "match" in host.keys():
                    build_child_xml_node(host_node, "match", host.get("match"))
                # add match-strings node
                if "match_strings" in host.keys():
                    match_strings = host.get("match_strings")
                    for match in match_strings:
                        build_child_xml_node(host_node, "match-strings", match)
                # add port node
                if "port" in host.keys():
                    build_child_xml_node(host_node, "port", host.get("port"))
                # add routing_instance node
                if "routing_instance" in host.keys():
                    build_child_xml_node(
                        host_node,
                        "routing-instance",
                        host.get("routing_instance"),
                    )
                # add source_address node
                if "source_address" in host.keys():
                    build_child_xml_node(
                        host_node,
                        "source-address",
                        host.get("source_address"),
                    )
                # add structured-data
                if "structured_data" in host.keys():
                    structured_data = host.get("structured_data")
                    if "set" not in structured_data.keys() or structured_data.get("set"):
                        s_data_node = build_child_xml_node(
                            host_node,
                            "structured-data",
                        )
                    if "brief" in structured_data.keys() and structured_data.get("brief"):
                        build_child_xml_node(s_data_node, "brief")

        # add log_rotate_frequency node
        if "log_rotate_frequency" in want.keys():
            build_child_xml_node(
                logging_node,
                "log-rotate-frequency",
                want.get("log_rotate_frequency"),
            )

        # add routing_instance node
        if "routing_instance" in want.keys():
            build_child_xml_node(
                logging_node,
                "routing-instance",
                want.get("routing_instance"),
            )

        # add server node
        if "server" in want.keys():
            server = want.get("server")
            if "set" not in server.keys() or server.get("set"):
                server_node = build_child_xml_node(logging_node, "server")
            if "routing_instance" in server.keys():
                routing_instance = server.get("routing_instance")
                if "all" in routing_instance.keys() and routing_instance.get(
                    "all",
                ):
                    build_child_xml_node(server_node, "all")
                if "default" in routing_instance.keys() and routing_instance.get("default"):
                    build_child_xml_node(server_node, "default")
                if "routing_instances" in routing_instance.keys():
                    r_instances = routing_instance.get("routing_instances")
                    for instance in r_instances:
                        instance_node = build_child_xml_node(
                            server_node,
                            "name",
                            instance.get("name"),
                        )
                        if "disable" in instance.keys() and instance.get(
                            "disable",
                        ):
                            build_child_xml_node(instance_node, "disable")

        # add source_address node
        if "source_address" in want.keys():
            build_child_xml_node(
                logging_node,
                "source-address",
                want.get("source_address"),
            )

        # add time_format
        if "time_format" in want.keys():
            time_format = want.get("time_format")

            time_node = build_child_xml_node(logging_node, "time-format")
            if "millisecond" in time_format.keys() and time_format.get(
                "millisecond",
            ):
                build_child_xml_node(time_node, "millisecond")
            if "year" in time_format.keys() and time_format.get("year"):
                build_child_xml_node(time_node, "year")

        # add user node
        if "users" in want.keys():
            users = want.get("users")
            for user in users:
                user_node = build_child_xml_node(logging_node, "user")
                # add name node
                build_child_xml_node(user_node, "name", user.get("name"))
                # add allow-duplicates node
                if "allow_duplicates" in user.keys() and user.get(
                    "allow_duplicates",
                ):
                    build_child_xml_node(user_node, "allow-duplicates")
                # add contents
                for k, v in iteritems(user):
                    if k in level_parser and v is not None:
                        content_node = build_child_xml_node(
                            user_node,
                            "contents",
                        )
                        build_child_xml_node(
                            content_node,
                            "name",
                            k.replace("_", "-"),
                        )
                        build_child_xml_node(content_node, v.get("level"))
                # add match node
                if "match" in user.keys():
                    build_child_xml_node(user_node, "match", user.get("match"))
                # add match-strings node
                if "match_strings" in user.keys():
                    match_strings = user.get("match_strings")
                    for match in match_strings:
                        build_child_xml_node(user_node, "match-strings", match)

        if logging_node is not None:
            logging_xml.append(logging_node)
        return logging_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        logging_xml = []
        logging_root = None
        delete = {"delete": "delete"}
        if have is not None:
            logging_root = build_child_xml_node(
                self.root,
                "syslog",
                None,
                delete,
            )

        if logging_root is not None:
            logging_xml.append(logging_root)
        return logging_xml

    def render_archive(self, root, want):
        archive = want.get("archive")
        archive_node = build_child_xml_node(root, "archive")

        # add binary-data node
        if "binary_data" in archive.keys() and archive.get("binary_data"):
            build_child_xml_node(archive_node, "binary-data")
        # add files node
        if "files" in archive.keys():
            build_child_xml_node(archive_node, "files", archive.get("files"))
        # add no-binary-data node
        if "no_binary_data" in archive.keys() and archive.get(
            "no_binary_data",
        ):
            build_child_xml_node(archive_node, "no-binary-data")
        # add size node
        if "file_size" in archive.keys():
            build_child_xml_node(
                archive_node,
                "size",
                archive.get("file_size"),
            )
        # add world-readable node
        if "world_readable" in archive.keys() and archive.get(
            "world_readable",
        ):
            build_child_xml_node(archive_node, "world-readable")
        # add no-world-readable node
        if "no_world_readable" in archive.keys() and archive.get(
            "no_world_readable",
        ):
            build_child_xml_node(archive_node, "no-world-readable")
