# Copyright (C) 2019  Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
The junos_vlans class
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


class Vlans(ConfigBase):
    """
    The junos_vlans class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["vlans"]

    def __init__(self, module):
        super(Vlans, self).__init__(module)

    def get_vlans_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        vlans_facts = facts["ansible_network_resources"].get("vlans")
        if not vlans_facts:
            return []
        return vlans_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_vlans_facts = self.get_vlans_facts()
        else:
            existing_vlans_facts = []
        if state == "gathered":
            existing_vlans_facts = self.get_vlans_facts()
            result["gathered"] = existing_vlans_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_vlans_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_vlans_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_vlans_facts)
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

            changed_vlans_facts = self.get_vlans_facts()

            result["before"] = existing_vlans_facts
            if result["changed"]:
                result["after"] = changed_vlans_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_vlans_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_vlans_facts
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
        root = build_root_xml_node("vlans")
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

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        intf_xml.extend(self._state_deleted(want, have))
        intf_xml.extend(self._state_merged(want, have))
        return intf_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        intf_xml.extend(self._state_deleted(have, have))
        intf_xml.extend(self._state_merged(want, have))
        return intf_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to merge the provided into
                  the current configuration
        """
        intf_xml = []

        for config in want:
            vlan_name = str(config["name"])
            vlan_id = str(config["vlan_id"])
            vlan_description = config.get("description")
            vlan_root = build_root_xml_node("vlan")
            build_child_xml_node(vlan_root, "name", vlan_name)
            build_child_xml_node(vlan_root, "vlan-id", vlan_id)
            if vlan_description:
                build_child_xml_node(
                    vlan_root,
                    "description",
                    vlan_description,
                )
            if config.get("l3_interface"):
                build_child_xml_node(
                    vlan_root,
                    "l3-interface",
                    config.get("l3_interface"),
                )

            intf_xml.append(vlan_root)
        return intf_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to remove the current configuration
                  of the provided objects
        """
        intf_xml = []

        if not want:
            want = have

        for config in want:
            vlan_name = config["name"]
            vlan_root = build_root_xml_node("vlan")
            vlan_root.attrib.update({"delete": "delete"})
            build_child_xml_node(vlan_root, "name", vlan_name)
            intf_xml.append(vlan_root)
        return intf_xml
