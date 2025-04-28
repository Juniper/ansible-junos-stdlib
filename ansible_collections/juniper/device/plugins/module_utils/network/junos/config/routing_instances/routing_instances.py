#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_routing_instances class
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


class Routing_instances(ConfigBase):
    """
    The junos_routing_instances class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["routing_instances"]

    def __init__(self, module):
        super(Routing_instances, self).__init__(module)

    def get_routing_instances_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        routing_instances_facts = facts["ansible_network_resources"].get(
            "routing_instances",
        )
        if not routing_instances_facts:
            return []
        return routing_instances_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_routing_instances_facts = self.get_routing_instances_facts()
        else:
            existing_routing_instances_facts = {}
        if state == "gathered":
            existing_routing_instances_facts = self.get_routing_instances_facts()
            result["gathered"] = existing_routing_instances_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_routing_instances_facts(
                data=running_config,
            )
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_routing_instances_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            diff = None
            config_xmls = self.set_config(existing_routing_instances_facts)
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

            changed_routing_instances_facts = self.get_routing_instances_facts()

            result["before"] = existing_routing_instances_facts
            if result["changed"]:
                result["after"] = changed_routing_instances_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_routing_instances_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_routing_instances_facts
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
        self.root = build_root_xml_node("routing-instances")
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
        rinst_xml = []
        delete = {"delete": "delete"}
        if have is not None:
            have_rinst = [instance["name"] for instance in have]
            want_rinst = [instance["name"] for instance in want]

            for instance in have_rinst:
                if instance not in want_rinst:
                    rinstance_node = build_root_xml_node("instance")
                    build_child_xml_node(rinstance_node, "name", instance)
                    rinstance_node.attrib.update(delete)
                    rinst_xml.append(rinstance_node)
        rinst_xml.extend(self._state_deleted(want, have))
        rinst_xml.extend(self._state_merged(want, have))

        return rinst_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        instance_xml = []
        rinst_node = None
        for instance in want:
            rinst_node = build_root_xml_node("instance")

            # add node routing table-name
            build_child_xml_node(rinst_node, "name", instance["name"])

            # add node connector-id-advertise
            if instance.get("connector_id_advertise"):
                build_child_xml_node(rinst_node, "connector-id-advertise")

            # add node description
            if instance.get("description"):
                build_child_xml_node(
                    rinst_node,
                    "description",
                    instance["description"],
                )

            # add node instance-role
            if instance.get("instance_role"):
                build_child_xml_node(
                    rinst_node,
                    "instance-role",
                    instance["insatnce_role"],
                )

            # add node instance-type
            if instance.get("type"):
                build_child_xml_node(
                    rinst_node,
                    "instance-type",
                    instance["type"],
                )

            # add child node interface
            if instance.get("interfaces"):
                interfaces = instance.get("interfaces")
                for interface in interfaces:
                    int_node = build_child_xml_node(rinst_node, "interface")
                    if interface.get("protect_interface"):
                        build_child_xml_node(
                            int_node,
                            "protect-interface",
                            interface["protect-interface"],
                        )
                    build_child_xml_node(int_node, "name", interface["name"])

            # add child node bridge-domains
            if instance.get("bridge_domains"):
                br_domains = instance["bridge_domains"]
                for domain in br_domains:
                    br_domain_node = build_child_xml_node(rinst_node, "bridge-domains")
                    domain_node = build_child_xml_node(br_domain_node, "domain")

                    attributes = ["name", "description", "domain_id", "service_id", "vlan_id"]
                    for attr in attributes:
                        if domain.get(attr):
                            build_child_xml_node(domain_node, attr.replace("_", "-"), domain[attr])

                    boolean_attributes = [
                        "enable_mac_move_action",
                        "mcae_mac_flush",
                        "no_irb_layer_2_copy",
                        "no_local_switching",
                    ]
                    for attr in boolean_attributes:
                        if domain.get(attr):
                            build_child_xml_node(domain_node, attr.replace("_", "-"))

            # add node l2vpn-id TODO
            if instance.get("l2vpn_id"):
                build_child_xml_node(
                    rinst_node,
                    "l2vpn-id",
                    instance["l2vpn_id"],
                )

            # add node no-irb-layer2-copy
            if instance.get("no_irb_layer2_copy"):
                build_child_xml_node(rinst_node, "no-irb-layer2-copy")

            # add node no-local-switching
            if instance.get("no_local_switching"):
                build_child_xml_node(rinst_node, "no-local-switching")

            # add node no-vrf-advertise
            if instance.get("no_vrf_advertise"):
                build_child_xml_node(rinst_node, "no-vrf-advertise")

            # add node no-vrf-propagate-ttl
            if instance.get("no_vrf_propagate_ttl"):
                build_child_xml_node(rinst_node, "no-vrf-propagate-ttl")

            # add node qualified-bum-pruning-mode
            if instance.get("qualified_bum_pruning_mode"):
                build_child_xml_node(rinst_node, "qualified-bum-pruning-mode")

            # add node route-distinguisher
            if instance.get("route_distinguisher"):
                rd_instance = build_child_xml_node(
                    rinst_node,
                    "route-distinguisher",
                )
                build_child_xml_node(
                    rd_instance,
                    "rd-type",
                    instance.get("route_distinguisher"),
                )

            # add node vrf-import
            if instance.get("vrf_imports"):
                vrf_imports = instance.get("vrf_imports")
                for vrf in vrf_imports:
                    build_child_xml_node(rinst_node, "vrf-import", vrf)

            # add node vrf-export
            if instance.get("vrf_exports"):
                vrf_exports = instance.get("vrf_exports")
                for vrf in vrf_exports:
                    build_child_xml_node(rinst_node, "vrf-export", vrf)

            if rinst_node is not None:
                instance_xml.append(rinst_node)

        return instance_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        rinst_xml = []
        existing_rinsts = []
        rinstance_node = None
        delete = {"delete": "delete"}
        if have is not None:
            # get the instances in running config
            # form existing instance list
            for h_rinst in have:
                existing_rinsts.append(h_rinst["name"])

            # Delete target routing-instance
            if want:
                for instance in want:
                    if instance["name"] not in existing_rinsts:
                        continue
                    rinstance_node = build_root_xml_node("instance")
                    build_child_xml_node(
                        rinstance_node,
                        "name",
                        instance["name"],
                    )
                    rinstance_node.attrib.update(delete)
                    rinst_xml.append(rinstance_node)

            else:
                # Delete all the routing-instance
                rinstance_node = build_root_xml_node("instance")
                rinstance_node.attrib.update(delete)
                rinst_xml.append(rinstance_node)

            if rinstance_node is not None:
                rinst_xml.append(rinstance_node)
        return rinst_xml
