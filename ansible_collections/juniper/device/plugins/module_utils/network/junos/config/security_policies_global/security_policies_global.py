#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_security_policies_global class
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


class Security_policies_global(ConfigBase):
    """
    The junos_security_policies_global class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["security_policies_global"]

    def __init__(self, module):
        super(Security_policies_global, self).__init__(module)

    def get_security_policies_global_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        security_policies_global_facts = facts["ansible_network_resources"].get(
            "security_policies_global",
        )
        if not security_policies_global_facts:
            return {}
        return security_policies_global_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_security_policies_global_facts = self.get_security_policies_global_facts()
        else:
            existing_security_policies_global_facts = {}
        if self.state == "gathered":
            existing_security_policies_global_facts = self.get_security_policies_global_facts()
            result["gathered"] = existing_security_policies_global_facts

        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_security_policies_global_facts(
                data=running_config,
            )

        elif self.state == "rendered":
            config_xmls = self.set_config(
                existing_security_policies_global_facts,
            )
            if config_xmls:
                result["rendered"] = config_xmls

        else:
            diff = None
            config_xmls = self.set_config(
                existing_security_policies_global_facts,
            )
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

            changed_security_policies_global_facts = self.get_security_policies_global_facts()

            result["before"] = existing_security_policies_global_facts
            if result["changed"]:
                result["after"] = changed_security_policies_global_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_security_policies_global_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_security_policies_global_facts
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
        security_policies_global_xml = []
        security_policies_global_xml.extend(self._state_deleted(want, have))
        security_policies_global_xml.extend(self._state_merged(want, have))
        return security_policies_global_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        security_policies_global_xml = []
        security_policies_global_xml.extend(self._state_deleted(want, have))
        security_policies_global_xml.extend(self._state_merged(want, have))
        return security_policies_global_xml

    def _state_merged(self, want, _have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        security_policies_global_xml = []
        want = remove_empties(want)
        security_policies_global_node = build_root_xml_node("policies")
        if "default_policy" in want.keys():
            default_policy_node = build_child_xml_node(
                security_policies_global_node,
                "default-policy",
            )
            default_policy = want.get("default_policy")
            if default_policy == "deny-all":
                build_child_xml_node(default_policy_node, "deny-all")
            if default_policy == "permit-all":
                build_child_xml_node(default_policy_node, "permit-all")

        if "policy_rematch" in want.keys():
            policy_rematch_node = build_child_xml_node(
                security_policies_global_node,
                "policy-rematch",
                " ",
            )
            policy_rematch = want.get("policy_rematch") or {}
            if "extensive" in policy_rematch and policy_rematch["extensive"] is True:
                build_child_xml_node(policy_rematch_node, "extensive")

        if "policy_stats" in want.keys():
            policy_stats_node = build_child_xml_node(
                security_policies_global_node,
                "policy-stats",
                " ",
            )
            policy_stats = want.get("policy_stats") or {}
            if "system_wide" in policy_stats:
                if policy_stats["system_wide"] is True:
                    build_child_xml_node(
                        policy_stats_node,
                        "system-wide",
                        "enable",
                    )
                else:
                    build_child_xml_node(
                        policy_stats_node,
                        "system-wide",
                        "disable",
                    )

        if "pre_id_default_policy_action" in want.keys():
            pre_id_node = build_child_xml_node(
                security_policies_global_node,
                "pre-id-default-policy",
            )
            pre_id_node = build_child_xml_node(pre_id_node, "then")
            pre_id = want.get("pre_id_default_policy_action")

            if "log" in pre_id:
                log_node = build_child_xml_node(pre_id_node, "log")
                if "session_close" in pre_id["log"]:
                    build_child_xml_node(log_node, "session-close")
                if "session_init" in pre_id["log"]:
                    build_child_xml_node(log_node, "session-init")

            if "session_timeout" in pre_id:
                session_timeout_node = build_child_xml_node(
                    pre_id_node,
                    "session-timeout",
                )
                if "icmp" in pre_id["session_timeout"]:
                    build_child_xml_node(
                        session_timeout_node,
                        "icmp",
                        pre_id["session_timeout"]["icmp"],
                    )
                if "icmp6" in pre_id["session_timeout"]:
                    build_child_xml_node(
                        session_timeout_node,
                        "icmp6",
                        pre_id["session_timeout"]["icmp6"],
                    )
                if "ospf" in pre_id["session_timeout"]:
                    build_child_xml_node(
                        session_timeout_node,
                        "ospf",
                        pre_id["session_timeout"]["ospf"],
                    )
                if "others" in pre_id["session_timeout"]:
                    build_child_xml_node(
                        session_timeout_node,
                        "others",
                        pre_id["session_timeout"]["others"],
                    )
                if "tcp" in pre_id["session_timeout"]:
                    build_child_xml_node(
                        session_timeout_node,
                        "tcp",
                        pre_id["session_timeout"]["tcp"],
                    )
                if "udp" in pre_id["session_timeout"]:
                    build_child_xml_node(
                        session_timeout_node,
                        "udp",
                        pre_id["session_timeout"]["udp"],
                    )

        if "traceoptions" in want.keys():
            traceoptions_node = build_child_xml_node(
                security_policies_global_node,
                "traceoptions",
            )
            traceoptions = want.get("traceoptions")

            if "file" in traceoptions:
                file_node = build_child_xml_node(traceoptions_node, "file")
                if "files" in traceoptions["file"]:
                    build_child_xml_node(
                        file_node,
                        "files",
                        traceoptions["file"]["files"],
                    )
                if "match" in traceoptions["file"]:
                    build_child_xml_node(
                        file_node,
                        "match",
                        traceoptions["file"]["match"],
                    )
                if "size" in traceoptions["file"]:
                    build_child_xml_node(
                        file_node,
                        "size",
                        traceoptions["file"]["size"],
                    )
                if "world_readable" in traceoptions["file"]:
                    build_child_xml_node(file_node, "world-readable")
                if "no_world_readable" in traceoptions["file"]:
                    build_child_xml_node(file_node, "no-world-readable")

            if "flag" in traceoptions:
                if traceoptions["flag"] == "all":
                    flag_node = build_child_xml_node(traceoptions_node, "flag")
                    build_child_xml_node(flag_node, "name", "all")
                elif traceoptions["flag"] == "configuration":
                    flag_node = build_child_xml_node(traceoptions_node, "flag")
                    build_child_xml_node(flag_node, "name", "configuration")
                elif traceoptions["flag"] == "compilation":
                    flag_node = build_child_xml_node(traceoptions_node, "flag")
                    build_child_xml_node(flag_node, "name", "compilation")
                elif traceoptions["flag"] == "ipc":
                    flag_node = build_child_xml_node(traceoptions_node, "flag")
                    build_child_xml_node(flag_node, "name", "ipc")
                elif traceoptions["flag"] == "lookup":
                    flag_node = build_child_xml_node(traceoptions_node, "flag")
                    build_child_xml_node(flag_node, "name", "lookup")
                elif traceoptions["flag"] == "routing-socket":
                    flag_node = build_child_xml_node(traceoptions_node, "flag")
                    build_child_xml_node(flag_node, "name", "routing-socket")
                elif traceoptions["flag"] == "rules":
                    flag_node = build_child_xml_node(traceoptions_node, "flag")
                    build_child_xml_node(flag_node, "name", "rules")

            if "no_remote_trace" in traceoptions:
                build_child_xml_node(traceoptions_node, "no-remote-trace")

        if security_policies_global_node is not None:
            security_policies_global_xml.append(security_policies_global_node)
        return security_policies_global_xml

    def _state_deleted(self, _want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        security_policies_global_xml = []
        security_policies_global_root = None
        delete = {"delete": "delete"}
        if have is not None:
            security_policies_global_root = build_child_xml_node(
                self.root,
                "policies",
                None,
                delete,
            )

        if security_policies_global_root is not None:
            security_policies_global_xml.append(security_policies_global_root)
        return security_policies_global_xml
