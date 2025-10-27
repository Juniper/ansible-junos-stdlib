#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos security_policies_global fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.security_policies_global.security_policies_global import (
    Security_policies_globalArgs,
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


class Security_policies_globalFacts(object):
    """The junos security_policies_global fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Security_policies_globalArgs.argument_spec
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
                            <policies>
                            </policies>
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
        resources = data.xpath("configuration/security/policies")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"security_policies_global": {}}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["security_policies_global"] = utils.remove_empties(
                params["config"],
            )

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
        security_policies_global_config = {}

        # Parse facts for security policies global settings
        global_policies = conf.get("policies") or {}

        if "default-policy" in global_policies:
            if "deny-all" in global_policies["default-policy"]:
                security_policies_global_config["default_policy"] = "deny-all"
            elif "permit-all" in global_policies["default-policy"]:
                security_policies_global_config["default_policy"] = "permit-all"

        if "policy-rematch" in global_policies:
            security_policies_global_config["policy_rematch"] = {}
            security_policies_global_config["policy_rematch"]["enable"] = True

            global_policies["policy-rematch"] = global_policies["policy-rematch"] or {}
            if "extensive" in global_policies["policy-rematch"]:
                security_policies_global_config["policy_rematch"]["extensive"] = True

        if "policy-stats" in global_policies:
            security_policies_global_config["policy_stats"] = {}
            security_policies_global_config["policy_stats"]["enable"] = True

            global_policies["policy-stats"] = global_policies["policy-stats"] or {}
            if "system-wide" in global_policies["policy-stats"]:
                if global_policies["policy-stats"]["system-wide"] == "enable":
                    security_policies_global_config["policy_stats"]["system_wide"] = True
                elif global_policies["policy-stats"]["system-wide"] == "disable":
                    security_policies_global_config["policy_stats"]["system_wide"] = False

        if "pre-id-default-policy" in global_policies:
            security_policies_global_config["pre_id_default_policy_action"] = {}
            pre_id_action = security_policies_global_config["pre_id_default_policy_action"]
            policy_pre_id_action = global_policies["pre-id-default-policy"]["then"]

            if "log" in policy_pre_id_action:
                pre_id_action["log"] = {}
                if "session-close" in policy_pre_id_action["log"]:
                    pre_id_action["log"]["session_close"] = True
                if "session-init" in policy_pre_id_action["log"]:
                    pre_id_action["log"]["session_init"] = True

            if "session-timeout" in policy_pre_id_action:
                pre_id_action["session_timeout"] = {}
                if "icmp" in policy_pre_id_action["session-timeout"]:
                    pre_id_action["session_timeout"]["icmp"] = policy_pre_id_action[
                        "session-timeout"
                    ]["icmp"]
                if "icmp6" in policy_pre_id_action["session-timeout"]:
                    pre_id_action["session_timeout"]["icmp6"] = policy_pre_id_action[
                        "session-timeout"
                    ]["icmp6"]
                if "ospf" in policy_pre_id_action["session-timeout"]:
                    pre_id_action["session_timeout"]["ospf"] = policy_pre_id_action[
                        "session-timeout"
                    ]["ospf"]
                if "others" in policy_pre_id_action["session-timeout"]:
                    pre_id_action["session_timeout"]["others"] = policy_pre_id_action[
                        "session-timeout"
                    ]["others"]
                if "tcp" in policy_pre_id_action["session-timeout"]:
                    pre_id_action["session_timeout"]["tcp"] = policy_pre_id_action[
                        "session-timeout"
                    ]["tcp"]
                if "udp" in policy_pre_id_action["session-timeout"]:
                    pre_id_action["session_timeout"]["udp"] = policy_pre_id_action[
                        "session-timeout"
                    ]["udp"]

        if "traceoptions" in global_policies:
            security_policies_global_config["traceoptions"] = {}
            traceoptions = security_policies_global_config["traceoptions"]
            policy_traceoptions = global_policies["traceoptions"]

            if "file" in policy_traceoptions:
                traceoptions["file"] = {}
                if "files" in policy_traceoptions["file"]:
                    traceoptions["file"]["files"] = policy_traceoptions["file"]["files"]
                if "match" in policy_traceoptions["file"]:
                    traceoptions["file"]["match"] = policy_traceoptions["file"]["match"]
                if "size" in policy_traceoptions["file"]:
                    traceoptions["file"]["size"] = policy_traceoptions["file"]["size"]
                if "world-readable" in policy_traceoptions["file"]:
                    traceoptions["file"]["world_readable"] = True
                if "no-world-readable" in policy_traceoptions["file"]:
                    traceoptions["file"]["no_world_readable"] = True

            if "flag" in policy_traceoptions:
                traceoptions["flag"] = {}

                if policy_traceoptions["flag"]["name"] == "all":
                    traceoptions["flag"] = "all"
                elif policy_traceoptions["flag"]["name"] == "configuration":
                    traceoptions["flag"] = "configuration"
                elif policy_traceoptions["flag"]["name"] == "compilation":
                    traceoptions["flag"] = "compilation"
                elif policy_traceoptions["flag"]["name"] == "ipc":
                    traceoptions["flag"] = "ipc"
                elif policy_traceoptions["flag"]["name"] == "lookup":
                    traceoptions["flag"] = "lookup"
                elif policy_traceoptions["flag"]["name"] == "routing-socket":
                    traceoptions["flag"] = "routing-socket"
                elif policy_traceoptions["flag"]["name"] == "rules":
                    traceoptions["flag"] = "rules"

            if "no-remote-trace" in policy_traceoptions:
                traceoptions["no_remote_trace"] = True

        return security_policies_global_config
