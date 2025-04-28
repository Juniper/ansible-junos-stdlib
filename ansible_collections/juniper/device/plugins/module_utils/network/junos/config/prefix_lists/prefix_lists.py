#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_prefix_lists class
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


class Prefix_lists(ConfigBase):
    """
    The junos_prefix_lists class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["prefix_lists"]

    def __init__(self, module):
        super(Prefix_lists, self).__init__(module)

    def get_prefix_lists_facts(self, data=None):
        """Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        prefix_lists_facts = facts["ansible_network_resources"].get(
            "prefix_lists",
        )
        if not prefix_lists_facts:
            return []
        return prefix_lists_facts

    def execute_module(self):
        """Execute the module
        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_prefix_lists_facts = self.get_prefix_lists_facts()
        else:
            existing_prefix_lists_facts = {}
        if state == "gathered":
            existing_prefix_lists_facts = self.get_prefix_lists_facts()
            result["gathered"] = existing_prefix_lists_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_prefix_lists_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_prefix_lists_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            diff = None
            config_xmls = self.set_config(existing_prefix_lists_facts)
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

            changed_prefix_lists_facts = self.get_prefix_lists_facts()

            result["before"] = existing_prefix_lists_facts
            if result["changed"]:
                result["after"] = changed_prefix_lists_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_prefix_lists_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_prefix_lists_facts
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
        self.root = build_root_xml_node("policy-options")
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
            config_xmls = self._state_overridden(want, have)

        for xml in config_xmls:
            self.root.append(xml)
        return tostring(self.root)

    def _state_replaced(self, want, have):
        """The command generator when state is replaced
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        rinst_xml = []
        rinst_xml.extend(self._state_deleted(want, have))
        rinst_xml.extend(self._state_merged(want, have))

        return rinst_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        plist_xml = []
        delete = {"delete": "delete"}
        if have is not None:
            have_plist = [entry["name"] for entry in have]
            want_plist = [entry["name"] for entry in want]

            for instance in have_plist:
                if instance not in want_plist:
                    plist_node = build_root_xml_node("prefix-list")
                    build_child_xml_node(plist_node, "name", instance)
                    plist_node.attrib.update(delete)
                    plist_xml.append(plist_node)
        plist_xml.extend(self._state_deleted(want, have))
        plist_xml.extend(self._state_merged(want, have))

        return plist_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        prefix_list_xml = []
        for instance in want:
            instance = remove_empties(instance)

            # generate node: prefix-list
            prefix_root = build_root_xml_node("prefix-list")

            # generate node: name
            if "name" in instance.keys():
                build_child_xml_node(prefix_root, "name", instance.get("name"))

            # generate node: prefix-list-item
            if "address_prefixes" in instance.keys():
                address_prefixes = instance.get("address_prefixes")

                for entry in address_prefixes:
                    add_prefix_node = build_child_xml_node(
                        prefix_root,
                        "prefix-list-item",
                    )
                    # generate name node
                    build_child_xml_node(add_prefix_node, "name", entry)

            # generate node: dynamic_db
            if "dynamic_db" in instance.keys() and instance.get("dynamic_db"):
                build_child_xml_node(prefix_root, "dynamic-db")

            prefix_list_xml.append(prefix_root)

        return prefix_list_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        plist_xml = []
        existing_plist = []
        plist_node = None
        delete = {"delete": "delete"}
        if have is not None:
            # get the instances in running config
            # form existing instance list
            for h_rinst in have:
                existing_plist.append(h_rinst["name"])

            # Delete target routing-instance
            if want:
                for entry in want:
                    if entry["name"] not in existing_plist:
                        continue
                    plist_node = build_root_xml_node("prefix-list")
                    build_child_xml_node(plist_node, "name", entry["name"])
                    plist_node.attrib.update(delete)
                    plist_xml.append(plist_node)

            else:
                # Delete all the routing-instance
                plist_node = build_root_xml_node("prefix-list")
                plist_node.attrib.update(delete)
                plist_xml.append(plist_node)

            if plist_node is not None:
                plist_xml.append(plist_node)
        return plist_xml
