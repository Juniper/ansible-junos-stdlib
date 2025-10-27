#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_interfaces class
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


class Interfaces(ConfigBase):
    """
    The junos_interfaces class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["interfaces"]

    def __init__(self, module):
        super(Interfaces, self).__init__(module)

    def get_interfaces_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        interfaces_facts = facts["ansible_network_resources"].get("interfaces")
        if not interfaces_facts:
            return []
        return interfaces_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        if self.state in self.ACTION_STATES:
            existing_interfaces_facts = self.get_interfaces_facts()
        else:
            existing_interfaces_facts = []

        if state == "gathered":
            existing_interfaces_facts = self.get_interfaces_facts()
            result["gathered"] = existing_interfaces_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_interfaces_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_interfaces_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_interfaces_facts)
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

            changed_interfaces_facts = self.get_interfaces_facts()

            result["before"] = existing_interfaces_facts
            if result["changed"]:
                result["after"] = changed_interfaces_facts

        return result

    def set_config(self, existing_interfaces_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_interfaces_facts
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
        intf_xml = []
        intf_xml.extend(self._state_deleted(want, have))
        intf_xml.extend(self._state_merged(want, have))

        return intf_xml

    def _state_overridden(self, want, have):
        """The xml configuration generator when state is overridden

        :rtype: A list
        :returns: the xml configuration necessary to migrate the current configuration
                  to the desired configuration
        """
        interface_xmls_obj = []
        # replace interface config with data in want
        interface_xmls_obj.extend(self._state_replaced(want, have))

        # delete interface config if interface in have not present in want
        delete_obj = []
        for have_obj in have:
            for want_obj in want:
                if have_obj["name"] == want_obj["name"]:
                    break
            else:
                delete_obj.append(have_obj)

        if delete_obj:
            interface_xmls_obj.extend(self._state_deleted(delete_obj, have))
        return interface_xmls_obj

    def _state_merged(self, want, have):
        """The xml configuration generator when state is merged

        :rtype: A list
        :returns: the xml configuration necessary to merge the provided into
                  the current configuration
        """
        intf_xml = []
        for config in want:
            intf = build_root_xml_node("interface")
            build_child_xml_node(intf, "name", config["name"])

            intf_fields = ["description", "speed"]
            if not config["name"].startswith("fxp"):
                intf_fields.append("mtu")
            for field in intf_fields:
                if config.get(field):
                    build_child_xml_node(intf, field, config[field])

            if config.get("duplex"):
                build_child_xml_node(intf, "link-mode", config["duplex"])

            if config.get("enabled") is not None:
                build_child_xml_node(intf, "enable" if config.get("enabled") else "disable")

            if config.get("units"):
                units = config.get("units")
                for unit in units:
                    unit_node = build_child_xml_node(intf, "unit")
                    build_child_xml_node(unit_node, "name", str(unit["name"]))
                    build_child_xml_node(
                        unit_node,
                        "description",
                        unit["description"],
                    )

            holdtime = config.get("hold_time")
            if holdtime:
                holdtime_ele = build_child_xml_node(intf, "hold-time")

                for holdtime_field in ["up", "down"]:
                    build_child_xml_node(
                        holdtime_ele,
                        holdtime_field,
                        holdtime.get(holdtime_field, ""),
                    )
            intf_xml.append(intf)

        return intf_xml

    def _state_deleted(self, want, have):
        """The xml configuration generator when state is deleted

        :rtype: A list
        :returns: the xml configuration necessary to remove the current configuration
                  of the provided objects
        """
        intf_xml = []
        intf_obj = want

        if not intf_obj:
            # delete base interfaces attribute from all the existing interface
            intf_obj = have

        if have:
            for config in intf_obj:
                intf = build_root_xml_node("interface")
                build_child_xml_node(intf, "name", config["name"])

                intf_fields = ["description"]
                if not any(
                    [
                        config["name"].startswith("gr"),
                        config["name"].startswith("lo"),
                    ],
                ):
                    intf_fields.append("speed")

                if not any(
                    [
                        config["name"].startswith("gr"),
                        config["name"].startswith("fxp"),
                        config["name"].startswith("lo"),
                    ],
                ):
                    intf_fields.append("mtu")

                for field in intf_fields:
                    build_child_xml_node(
                        intf,
                        field,
                        None,
                        {"delete": "delete"},
                    )

                if not any(
                    [
                        config["name"].startswith("gr"),
                        config["name"].startswith("lo"),
                    ],
                ):
                    build_child_xml_node(
                        intf,
                        "link-mode",
                        None,
                        {"delete": "delete"},
                    )

                build_child_xml_node(
                    intf,
                    "disable",
                    None,
                    {"delete": "delete"},
                )

                holdtime_ele = build_child_xml_node(intf, "hold-time")
                have_cfg = self.in_have(config["name"], have)
                if have_cfg:
                    logical_cfg = have_cfg
                else:
                    logical_cfg = config
                if logical_cfg.get("units"):
                    units = logical_cfg.get("units")
                    for unit in units:
                        unit_node = build_child_xml_node(intf, "unit")
                        build_child_xml_node(
                            unit_node,
                            "name",
                            str(unit["name"]),
                        )
                        build_child_xml_node(
                            unit_node,
                            "description",
                            None,
                            {"delete": "delete"},
                        )

                for holdtime_field in ["up", "down"]:
                    build_child_xml_node(
                        holdtime_ele,
                        holdtime_field,
                        None,
                        {"delete": "delete"},
                    )
                intf_xml.append(intf)

        return intf_xml

    def in_have(self, name, have):
        for item in have:
            if name == item["name"]:
                return item
        return None
