#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_static_routes class
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


class Static_routes(ConfigBase):
    """
    The junos_static_routes class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["static_routes"]

    def __init__(self, module):
        super(Static_routes, self).__init__(module)

    def get_static_routes_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        static_routes_facts = facts["ansible_network_resources"].get(
            "static_routes",
        )
        if not static_routes_facts:
            return []
        return static_routes_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_static_routes_facts = self.get_static_routes_facts()
        else:
            existing_static_routes_facts = []
        if state == "gathered":
            existing_static_routes_facts = self.get_static_routes_facts()
            result["gathered"] = existing_static_routes_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_static_routes_facts(
                data=running_config,
            )
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_static_routes_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_static_routes_facts)
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

            changed_static_routes_facts = self.get_static_routes_facts()

            result["before"] = existing_static_routes_facts
            if result["changed"]:
                result["after"] = changed_static_routes_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_static_routes_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_static_routes_facts
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
        state = self._module.params["state"]
        if state in ("merged", "replaced", "overridden", "rendered") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state,
                ),
            )
        root = build_root_xml_node("configuration")
        routing_options = build_child_xml_node(root, "routing-options")
        routing_instances = build_child_xml_node(root, "routing-instances")
        if state == "overridden":
            config_xmls = self._state_overridden(want, have)
        elif state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)

        for xml in config_xmls:
            if xml["root_type"] == "routing-options":
                routing_options.append(xml["static_route_xml"])
            elif xml["root_type"] == "routing-instances":
                routing_instances.append(xml["static_route_xml"])

        return [tostring(xml) for xml in root.getchildren()]

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        static_route_xml = []
        static_route_xml.extend(self._state_deleted(want, have))
        static_route_xml.extend(self._state_merged(want, have))
        return static_route_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        static_route_xml = []
        static_route_xml.extend(self._state_deleted(have, have))
        static_route_xml.extend(self._state_merged(want, have))
        return static_route_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        if not want:
            want = have
        static_route_xml = self._state_merged(
            want,
            have,
            delete={"delete": "delete"},
        )
        return static_route_xml

    def _state_merged(self, want, have, delete=None):
        """The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        static_route_xml = []
        root_type = ""
        vrf_name = None
        for config in want:
            if config.get("vrf"):
                vrf_name = config["vrf"]
            if vrf_name:
                root_type = "routing-instances"
                instance = build_root_xml_node("instance")
                build_child_xml_node(instance, "name", vrf_name)
                routing_options = build_child_xml_node(
                    instance,
                    "routing-options",
                )
            else:
                root_type = "routing-options"

            for afi in config["address_families"]:
                protocol = afi["afi"]
                if protocol == "ipv6":
                    if vrf_name:
                        rib_route_root = build_child_xml_node(
                            routing_options,
                            "rib",
                        )
                        build_child_xml_node(
                            rib_route_root,
                            "name",
                            vrf_name + ".inet6.0",
                        )
                    else:
                        rib_route_root = build_root_xml_node("rib")
                        build_child_xml_node(rib_route_root, "name", "inet6.0")
                    static_route_root = build_child_xml_node(
                        rib_route_root,
                        "static",
                    )
                elif protocol == "ipv4":
                    if vrf_name:
                        static_route_root = build_child_xml_node(
                            routing_options,
                            "static",
                        )
                    else:
                        static_route_root = build_root_xml_node("static")

                if afi.get("routes"):
                    for route in afi["routes"]:
                        route_node = build_child_xml_node(
                            static_route_root,
                            "route",
                        )
                        if delete:
                            route_node.attrib.update(delete)
                        if route.get("dest"):
                            build_child_xml_node(
                                route_node,
                                "name",
                                route["dest"],
                            )
                        if not delete:
                            if route.get("metric"):
                                build_child_xml_node(
                                    route_node,
                                    "metric",
                                    route["metric"],
                                )
                            if route.get("next_hop"):
                                for hop in route["next_hop"]:
                                    build_child_xml_node(
                                        route_node,
                                        "next-hop",
                                        hop["forward_router_address"],
                                    )
                elif delete:
                    if vrf_name:
                        instance.attrib.update(delete)
                    static_route_root.attrib.update(delete)

                if vrf_name:
                    static_route_xml.append(
                        {"root_type": root_type, "static_route_xml": instance},
                    )
                else:
                    if protocol == "ipv6":
                        static_route_xml.append(
                            {
                                "root_type": root_type,
                                "static_route_xml": rib_route_root,
                            },
                        )
                    else:
                        static_route_xml.append(
                            {
                                "root_type": root_type,
                                "static_route_xml": static_route_root,
                            },
                        )
        return static_route_xml
