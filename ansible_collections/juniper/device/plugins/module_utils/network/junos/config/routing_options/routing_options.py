#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_routing_options class
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


class Routing_options(ConfigBase):
    """
    The junos_routing_options class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["routing_options"]

    def __init__(self, module):
        super(Routing_options, self).__init__(module)

    def get_routing_options_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        routing_options_facts = facts["ansible_network_resources"].get(
            "routing_options",
        )
        if not routing_options_facts:
            return {}
        return routing_options_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_routing_options_facts = self.get_routing_options_facts()
        else:
            existing_routing_options_facts = {}
        if state == "gathered":
            existing_routing_options_facts = self.get_routing_options_facts()
            result["gathered"] = existing_routing_options_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_routing_options_facts(
                data=running_config,
            )
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_routing_options_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]

        else:
            diff = None
            config_xmls = self.set_config(existing_routing_options_facts)
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

            changed_routing_options_facts = self.get_routing_options_facts()

            result["before"] = existing_routing_options_facts
            if result["changed"]:
                result["after"] = changed_routing_options_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_routing_options_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_routing_options_facts
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
        temp_lst = []
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
                temp_lst.append(xml)
        return temp_lst

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self._state_deleted(want, have)
        self._state_merged(want, have)

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        routing_xml = []
        want = remove_empties(want)

        # add authentication-keys node
        if "autonomous_system" in want.keys():
            as_num = want.get("autonomous_system")
            # Generate xml node for autonomous-system
            if as_num.get("as_number"):
                as_node = build_child_xml_node(
                    self.routing_options,
                    "autonomous-system",
                    as_num.get("as_number"),
                )
                # Add node for loops
                if as_num.get("loops"):
                    build_child_xml_node(as_node, "loops", as_num.get("loops"))
                # Add node for asdot_notation
                if as_num.get("asdot_notation"):
                    if "asdot_notation" in as_num.keys():
                        build_child_xml_node(as_node, "asdot-notation")
        if "router_id" in want.keys():
            build_child_xml_node(
                self.routing_options,
                "router-id",
                want.get("router_id"),
            )
        return routing_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        delete = {"delete": "delete"}
        if have is not None:
            if "autonomous_system" in have.keys():
                build_child_xml_node(
                    self.routing_options,
                    "autonomous-system",
                    None,
                    delete,
                )
            if "router_id" in have.keys():
                build_child_xml_node(
                    self.routing_options,
                    "router-id",
                    None,
                    delete,
                )
