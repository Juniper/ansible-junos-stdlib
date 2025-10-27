#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_acl_interfaces class
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


class Acl_interfaces(ConfigBase):
    """
    The junos_acl_interfaces class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["acl_interfaces"]

    def __init__(self, module):
        super(Acl_interfaces, self).__init__(module)

    def get_acl_interfaces_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        acl_interfaces_facts = facts["ansible_network_resources"].get(
            "acl_interfaces",
        )
        if not acl_interfaces_facts:
            return []
        return acl_interfaces_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_acl_interfaces_facts = self.get_acl_interfaces_facts()
        else:
            existing_acl_interfaces_facts = []
        if state == "gathered":
            existing_acl_interfaces_facts = self.get_acl_interfaces_facts()
            result["gathered"] = existing_acl_interfaces_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_acl_interfaces_facts(
                data=running_config,
            )
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_acl_interfaces_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_acl_interfaces_facts)
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

            changed_acl_interfaces_facts = self.get_acl_interfaces_facts()

            result["before"] = existing_acl_interfaces_facts
            if result["changed"]:
                result["after"] = changed_acl_interfaces_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_acl_interfaces_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_acl_interfaces_facts
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
        root = build_root_xml_node("interfaces")
        state = self._module.params["state"]
        if state in ("merged", "replaced", "overridden", "rendered") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state,
                ),
            )
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

    def _get_common_xml_node(self, name):
        root_node = build_root_xml_node("interface")
        build_child_xml_node(root_node, "name", name)
        intf_unit_node = build_child_xml_node(root_node, "unit")
        return root_node, intf_unit_node

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        acl_intf_xml = []
        acl_intf_xml.extend(self._state_deleted(want, have))
        acl_intf_xml.extend(self._state_merged(want, have))
        return acl_intf_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        acl_intf_xml = []
        acl_intf_xml.extend(self._state_deleted(have, have))
        acl_intf_xml.extend(self._state_merged(want, have))
        return acl_intf_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        acl_intf_xml = []
        delete = {"delete": "delete"}

        if not want:
            want = have

        acl_intf_xml = self._state_merged(want, have, delete=delete)
        return acl_intf_xml

    def _state_merged(self, want, have, delete=None):
        """The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """

        acl_intf_xml = []

        for config in want:
            root_node, unit_node = self._get_common_xml_node(config["name"])
            build_child_xml_node(unit_node, "name", "0")
            family_node = build_child_xml_node(unit_node, "family")
            for acl_filter in config["access_groups"]:
                inet_family = "inet"
                if acl_filter["afi"] == "ipv6":
                    inet_family = "inet6"
                inet_node = build_child_xml_node(family_node, inet_family)
                if acl_filter.get("acls"):
                    filter_node = build_child_xml_node(inet_node, "filter")
                    for acl in acl_filter["acls"]:
                        acl_node = None
                        if acl["direction"] == "in":
                            acl_node = build_child_xml_node(
                                filter_node,
                                "input-list",
                                acl["name"],
                            )
                        else:
                            acl_node = build_child_xml_node(
                                filter_node,
                                "output-list",
                                acl["name"],
                            )
                        if delete:
                            acl_node.attrib.update(delete)
                elif delete:
                    build_child_xml_node(inet_node, "filter", None, delete)
            acl_intf_xml.append(root_node)
        return acl_intf_xml
