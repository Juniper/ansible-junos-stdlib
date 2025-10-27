#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_l2_interfaces class
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
    build_subtree,
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
from ansible_collections.juniper.device.plugins.module_utils.network.junos.utils.utils import (
    get_resource_config,
)


class L2_interfaces(ConfigBase):
    """
    The junos_l2_interfaces class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["l2_interfaces"]

    def __init__(self, module):
        super(L2_interfaces, self).__init__(module)

    def get_l2_interfaces_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        l2_interfaces_facts = facts["ansible_network_resources"].get(
            "l2_interfaces",
        )
        if not l2_interfaces_facts:
            return []
        return l2_interfaces_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        if self.state in self.ACTION_STATES:
            existing_l2_interfaces_facts = self.get_l2_interfaces_facts()
        else:
            existing_l2_interfaces_facts = []
        if state == "gathered":
            existing_l2_interfaces_facts = self.get_l2_interfaces_facts()
            result["gathered"] = existing_l2_interfaces_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_l2_interfaces_facts(
                data=running_config,
            )
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_l2_interfaces_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_l2_interfaces_facts)
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

            changed_interfaces_facts = self.get_l2_interfaces_facts()

            result["before"] = existing_l2_interfaces_facts
            if result["changed"]:
                result["after"] = changed_interfaces_facts

        return result

    def set_config(self, existing_l2_interfaces_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_l2_interfaces_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the list xml configuration necessary to migrate the current configuration
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

    def _state_replaced(self, want, have):
        """The xml configuration generator when state is replaced

        :rtype: A list
        :returns: the xml configuration necessary to migrate the current configuration
                  to the desired configuration
        """
        l2_intf_xml = []
        l2_intf_xml.extend(self._state_deleted(want, have))
        l2_intf_xml.extend(self._state_merged(want, have))

        return l2_intf_xml

    def _state_overridden(self, want, have):
        """The xml configuration generator when state is overridden

        :rtype: A list
        :returns: the xml configuration necessary to migrate the current configuration
                  to the desired configuration
        """
        l2_interface_xmls_obj = []
        # replace interface config with data in want
        l2_interface_xmls_obj.extend(self._state_replaced(want, have))

        # delete interface config if interface in have not present in want
        delete_obj = []
        for have_obj in have:
            for want_obj in want:
                if have_obj["name"] == want_obj["name"]:
                    break
            else:
                delete_obj.append(have_obj)

        if delete_obj:
            l2_interface_xmls_obj.extend(self._state_deleted(delete_obj, have))
        return l2_interface_xmls_obj

    def _state_merged(self, want, have):
        """The xml configuration generator when state is merged

        :rtype: A list
        :returns: the xml configuration necessary to merge the provided into
                  the current configuration
        """
        intf_xml = []
        for config in want:
            enhanced_layer = True
            if config.get("enhanced_layer") is False:
                enhanced_layer = False

            mode = "interface-mode" if enhanced_layer else "port-mode"
            intf = build_root_xml_node("interface")
            build_child_xml_node(intf, "name", config["name"])
            unit_node = build_child_xml_node(intf, "unit")
            unit = config["unit"] if config["unit"] else "0"
            build_child_xml_node(unit_node, "name", unit)

            eth_node = build_subtree(unit_node, "family/ethernet-switching")
            if config.get("access"):
                vlan = config["access"].get("vlan")
                if vlan:
                    build_child_xml_node(eth_node, mode, "access")
                    vlan_node = build_child_xml_node(eth_node, "vlan")
                    build_child_xml_node(vlan_node, "members", vlan)
                    intf_xml.append(intf)
            elif config.get("trunk"):
                allowed_vlans = config["trunk"].get("allowed_vlans")
                native_vlan = config["trunk"].get("native_vlan")
                if allowed_vlans:
                    build_child_xml_node(eth_node, mode, "trunk")
                    vlan_node = build_child_xml_node(eth_node, "vlan")
                    for vlan in allowed_vlans:
                        build_child_xml_node(vlan_node, "members", vlan)
                if native_vlan:
                    build_child_xml_node(intf, "native-vlan-id", native_vlan)

                if allowed_vlans or native_vlan:
                    intf_xml.append(intf)

        return intf_xml

    def get_res_config(self, connection, config_filter):
        """

        :param connection:
        :param config_filter:
        :return:
        """
        return get_resource_config(connection, config_filter=config_filter)

    def _state_deleted(self, want, have):
        """The xml configuration generator when state is deleted

        :rtype: A list
        :returns: the xml configuration necessary to remove the current configuration
                  of the provided objects
        """
        l2_intf_xml = []
        l2_intf_obj = want

        config_filter = """
            <configuration>
                <interfaces/>
            </configuration>
            """
        data = self.get_res_config(
            self._connection,
            config_filter=config_filter,
        )

        if not l2_intf_obj:
            # delete l2 interfaces attribute from all the existing interface having l2 config
            l2_intf_obj = have

        for config in l2_intf_obj:
            name = config["name"]
            enhanced_layer = True
            l2_mode = data.xpath(
                "configuration/interfaces/interface[name='%s']/unit/family/ethernet-switching/interface-mode"
                % name,
            )

            if not len(l2_mode):
                l2_mode = data.xpath(
                    "configuration/interfaces/interface[name='%s']/unit/family/ethernet-switching/port-mode"
                    % name,
                )
                enhanced_layer = False

            if len(l2_mode):
                mode = "interface-mode" if enhanced_layer else "port-mode"

                intf = build_root_xml_node("interface")
                build_child_xml_node(intf, "name", name)

                unit_node = build_child_xml_node(intf, "unit")
                unit = config["unit"] if config["unit"] else "0"
                build_child_xml_node(unit_node, "name", unit)

                eth_node = build_subtree(
                    unit_node,
                    "family/ethernet-switching",
                )
                build_child_xml_node(
                    eth_node,
                    mode,
                    None,
                    {"delete": "delete"},
                )
                build_child_xml_node(
                    eth_node,
                    "vlan",
                    None,
                    {"delete": "delete"},
                )
                build_child_xml_node(
                    intf,
                    "native-vlan-id",
                    None,
                    {"delete": "delete"},
                )

                l2_intf_xml.append(intf)

        return l2_intf_xml
