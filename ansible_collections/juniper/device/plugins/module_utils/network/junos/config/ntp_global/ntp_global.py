#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_ntp_global class
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


class Ntp_global(ConfigBase):
    """
    The junos_ntp_global class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["ntp_global"]

    def __init__(self, module):
        super(Ntp_global, self).__init__(module)

    def get_ntp_global_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        ntp_global_facts = facts["ansible_network_resources"].get("ntp_global")
        if not ntp_global_facts:
            return {}
        return ntp_global_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_ntp_global_facts = self.get_ntp_global_facts()
        else:
            existing_ntp_global_facts = {}
        if state == "gathered":
            existing_ntp_global_facts = self.get_ntp_global_facts()
            result["gathered"] = existing_ntp_global_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_ntp_global_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_ntp_global_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]

        else:
            diff = None
            config_xmls = self.set_config(existing_ntp_global_facts)
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

            changed_ntp_global_facts = self.get_ntp_global_facts()

            result["before"] = existing_ntp_global_facts
            if result["changed"]:
                result["after"] = changed_ntp_global_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_ntp_global_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_ntp_global_facts
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
        self.root = build_root_xml_node("system")
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
        ntp_xml = []
        ntp_xml.extend(self._state_deleted(want, have))
        ntp_xml.extend(self._state_merged(want, have))
        return ntp_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        ntp_xml = []
        want = remove_empties(want)
        ntp_node = build_root_xml_node("ntp")

        # add authentication-keys node
        if "authentication_keys" in want.keys():
            auth_keys = want.get("authentication_keys")
            for key in auth_keys:
                key_node = build_child_xml_node(ntp_node, "authentication-key")
                # add name node
                build_child_xml_node(key_node, "name", key.get("id"))
                # add type node
                build_child_xml_node(key_node, "type", key.get("algorithm"))
                # add value node
                build_child_xml_node(key_node, "value", key.get("key"))

        # add boot_server node
        if "boot_server" in want.keys():
            build_child_xml_node(
                ntp_node,
                "boot-server",
                want.get("boot_server"),
            )

        # add broadcast node
        if "broadcasts" in want.keys():
            broadcasts = want.get("broadcasts")
            for item in broadcasts:
                broadcast_node = build_child_xml_node(ntp_node, "broadcast")
                # add name node
                build_child_xml_node(
                    broadcast_node,
                    "name",
                    item.get("address"),
                )
                # add key node
                if "key" in item.keys():
                    build_child_xml_node(
                        broadcast_node,
                        "key",
                        item.get("key"),
                    )
                # add routing-instance-name node
                if "routing_instance_name" in item.keys():
                    build_child_xml_node(
                        broadcast_node,
                        "routing-instance-name",
                        item.get("routing_instance_name"),
                    )
                # add ttl node
                if "ttl" in item.keys():
                    build_child_xml_node(
                        broadcast_node,
                        "ttl",
                        item.get("ttl"),
                    )
                # add version node
                if "version" in item.keys():
                    build_child_xml_node(
                        broadcast_node,
                        "version",
                        item.get("version"),
                    )

        # add broadcast_client node
        if "broadcast_client" in want.keys() and want.get("broadcast_client"):
            build_child_xml_node(ntp_node, "broadcast-client")

        # add interval_range node
        if "interval_range" in want.keys():
            build_child_xml_node(
                ntp_node,
                "interval-range",
                want.get("interval_range"),
            )

        # add multicast_client node
        if "multicast_client" in want.keys():
            build_child_xml_node(
                ntp_node,
                "multicast-client",
                want.get("multicast_client"),
            )

        # add peers node
        if "peers" in want.keys():
            peers = want.get("peers")
            for item in peers:
                peer_node = build_child_xml_node(ntp_node, "peer")
                # add name node
                build_child_xml_node(peer_node, "name", item.get("peer"))
                # add key node
                if "key_id" in item.keys():
                    build_child_xml_node(peer_node, "key", item.get("key_id"))
                # add prefer node
                if "prefer" in item.keys() and item.get("prefer"):
                    build_child_xml_node(peer_node, "prefer")
                # add version node
                if "version" in item.keys():
                    build_child_xml_node(
                        peer_node,
                        "version",
                        item.get("version"),
                    )

        # add server node
        if "servers" in want.keys():
            servers = want.get("servers")
            for item in servers:
                server_node = build_child_xml_node(ntp_node, "server")
                # add name node
                build_child_xml_node(server_node, "name", item.get("server"))
                # add key node
                if "key_id" in item.keys():
                    build_child_xml_node(
                        server_node,
                        "key",
                        item.get("key_id"),
                    )
                # add routing-instance node
                if "routing_instance" in item.keys():
                    build_child_xml_node(
                        server_node,
                        "routing-instance",
                        item.get("routing_instance"),
                    )
                # add prefer node
                if "prefer" in item.keys() and item.get("prefer"):
                    build_child_xml_node(server_node, "prefer")
                # add version node
                if "version" in item.keys():
                    build_child_xml_node(
                        server_node,
                        "version",
                        item.get("version"),
                    )
        # add source_address node
        if "source_addresses" in want.keys():
            source_addresses = want.get("source_addresses")
            for item in source_addresses:
                source_node = build_child_xml_node(ntp_node, "source-address")
                # add name node
                build_child_xml_node(
                    source_node,
                    "name",
                    item.get("source_address"),
                )
                # add routing-instance node
                if "routing_instance" in item.keys():
                    build_child_xml_node(
                        source_node,
                        "routing-instance",
                        item.get("routing_instance"),
                    )
        # add threshold node
        if "threshold" in want.keys():
            threshold = want.get("threshold")
            threshold_node = build_child_xml_node(ntp_node, "threshold")
            if "value" in threshold.keys():
                build_child_xml_node(
                    threshold_node,
                    "value",
                    threshold.get("value"),
                )
            if "action" in threshold.keys():
                build_child_xml_node(
                    threshold_node,
                    "action",
                    threshold.get("action"),
                )

        # add trusted key
        if "trusted_keys" in want.keys():
            trusted_keys = want.get("trusted_keys")
            for key in trusted_keys:
                build_child_xml_node(ntp_node, "trusted-key", key["key_id"])

        if ntp_node is not None:
            ntp_xml.append(ntp_node)
        return ntp_xml

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        ntp_xml = []
        ntp_root = None
        delete = {"delete": "delete"}
        if have is not None:
            ntp_root = build_child_xml_node(self.root, "ntp", None, delete)

        if ntp_root is not None:
            ntp_xml.append(ntp_root)
        return ntp_xml
