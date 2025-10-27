#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos ntp_global fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.ntp_global.ntp_global import (
    Ntp_globalArgs,
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


class Ntp_globalFacts(object):
    """The junos ntp_global fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Ntp_globalArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_device_data(self, connection, config_filter):
        """
        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for ntp_gloabl
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
                            <system>
                                <ntp>
                                </ntp>
                            </system>
                        </configuration>
                        """
            data = self.get_device_data(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/system/ntp")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"ntp_global": {}}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["ntp_global"] = utils.remove_empties(params["config"])
        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root),
            dict_constructor=dict,
        )
        return xml_dict

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        ntp_global_config = {}

        # Parse facts for BGP address-family global node
        conf = conf.get("ntp")

        # Read allow-duplicates node
        if "authentication-key" in conf.keys():
            auth_key_lst = []
            auth_keys = conf.get("authentication-key")
            auth_key_dict = {}
            if isinstance(auth_keys, dict):
                auth_key_dict["id"] = auth_keys["name"]
                auth_key_dict["algorithm"] = auth_keys["type"]
                auth_key_dict["key"] = auth_keys["value"]
                auth_key_lst.append(auth_key_dict)

            else:
                for auth_key in auth_keys:
                    auth_key_dict["id"] = auth_key["name"]
                    auth_key_dict["algorithm"] = auth_key["type"]
                    auth_key_dict["key"] = auth_key["value"]
                    auth_key_lst.append(auth_key_dict)
                    auth_key_dict = {}
            if auth_key_lst:
                ntp_global_config["authentication_keys"] = auth_key_lst

        # Read boot-server node
        if "boot-server" in conf.keys():
            ntp_global_config["boot_server"] = conf.get("boot-server")

        # Read broadcast node
        if "broadcast" in conf.keys():
            broadcast_lst = []
            broadcasts = conf.get("broadcast")
            broadcast_dict = {}
            if isinstance(broadcasts, dict):
                broadcast_dict["address"] = broadcasts["name"]
                if "key" in broadcasts.keys():
                    broadcast_dict["key"] = broadcasts["key"]
                if "ttl" in broadcasts.keys():
                    broadcast_dict["ttl"] = broadcasts["ttl"]
                if "version" in broadcasts.keys():
                    broadcast_dict["version"] = broadcasts["version"]
                if "routing-instance-name" in broadcasts.keys():
                    broadcast_dict["routing_instance_name"] = broadcasts["routing-instance-name"]
                broadcast_lst.append(broadcast_dict)

            else:
                for broadcast in broadcasts:
                    broadcast_dict["address"] = broadcast["name"]
                    if "key" in broadcast.keys():
                        broadcast_dict["key"] = broadcast["key"]
                    if "ttl" in broadcast.keys():
                        broadcast_dict["ttl"] = broadcast["ttl"]
                    if "version" in broadcast.keys():
                        broadcast_dict["version"] = broadcast["version"]
                    if "routing-instance-name" in broadcast.keys():
                        broadcast_dict["routing_instance_name"] = broadcast["routing-instance-name"]
                    broadcast_lst.append(broadcast_dict)
                    broadcast_dict = {}
            if broadcast_lst:
                ntp_global_config["broadcasts"] = broadcast_lst

        # Read broadcast-client node
        if "broadcast-client" in conf.keys():
            ntp_global_config["broadcast_client"] = True

        # Read interval-range node
        if "interval-range" in conf.keys():
            ntp_global_config["interval_range"] = conf["interval-range"].get(
                "value",
            )

        # Read multicast-client node
        if "multicast-client" in conf.keys():
            ntp_global_config["multicast_client"] = conf["multicast-client"].get("address")

        # Read peer node
        if "peer" in conf.keys():
            peer_lst = []
            peers = conf.get("peer")
            peer_dict = {}
            if isinstance(peers, dict):
                peer_dict["peer"] = peers["name"]
                if "key" in peers.keys():
                    peer_dict["key_id"] = peers["key"]
                if "prefer" in peers.keys():
                    peer_dict["prefer"] = True
                if "version" in peers.keys():
                    peer_dict["version"] = peers["version"]
                peer_lst.append(peer_dict)

            else:
                for peer in peers:
                    peer_dict["peer"] = peer["name"]
                    if "key" in peer.keys():
                        peer_dict["key_id"] = peer["key"]
                    if "prefer" in peer.keys():
                        peer_dict["prefer"] = True
                    if "version" in peer.keys():
                        peer_dict["version"] = peer["version"]
                    peer_lst.append(peer_dict)
                    peer_dict = {}
            if peer_lst:
                ntp_global_config["peers"] = peer_lst

        # Read server node
        if "server" in conf.keys():
            server_lst = []
            servers = conf.get("server")
            server_dict = {}
            if isinstance(servers, dict):
                server_dict["server"] = servers["name"]
                if "key" in servers.keys():
                    server_dict["key_id"] = servers["key"]
                if "prefer" in servers.keys():
                    server_dict["prefer"] = True
                if "version" in servers.keys():
                    server_dict["version"] = servers["version"]
                if "routing-instance" in servers.keys():
                    server_dict["routing-instance"] = servers["routing-instance"]
                server_lst.append(server_dict)

            else:
                for server in servers:
                    server_dict["server"] = server["name"]
                    if "key" in server.keys():
                        server_dict["key_id"] = server["key"]
                    if "prefer" in server.keys():
                        server_dict["prefer"] = True
                    if "version" in server.keys():
                        server_dict["version"] = server["version"]
                    if "routing-instance" in server.keys():
                        server_dict["routing_instance"] = server["routing-instance"]
                    server_lst.append(server_dict)
                    server_dict = {}
            if server_lst:
                ntp_global_config["servers"] = server_lst

        # Read source-address node
        if "source-address" in conf.keys():
            source_address_lst = []
            source_addresses = conf.get("source-address")
            source_address_dict = {}
            if isinstance(source_addresses, dict):
                source_address_dict["source_address"] = source_addresses["name"]
                if "routing-instance" in source_addresses.keys():
                    source_address_dict["routing_instance"] = source_addresses["routing-instance"]
                source_address_lst.append(source_address_dict)

            else:
                for source_address in source_addresses:
                    source_address_dict["source_address"] = source_address["name"]
                    if "routing-instance" in source_address.keys():
                        source_address_dict["routing_instance"] = source_address["routing-instance"]
                    source_address_lst.append(source_address_dict)
                    source_address_dict = {}
            if source_address_lst:
                ntp_global_config["source_addresses"] = source_address_lst

        # Read threshold node
        if "threshold" in conf.keys():
            threshold = conf.get("threshold")
            threshold_dict = {}
            if "value" in threshold.keys():
                threshold_dict["value"] = threshold.get("value")
            if "action" in threshold.keys():
                threshold_dict["action"] = threshold.get("action")
            if threshold_dict:
                ntp_global_config["threshold"] = threshold_dict

        # read trusted-keys node
        if "trusted-key" in conf.keys():
            trusted_keys = conf.get("trusted-key")
            trusted_keys_lst = []
            trusted_keys_dict = {}
            if isinstance(trusted_keys, list):
                trusted_keys.sort(key=int)
                for key in trusted_keys:
                    trusted_keys_dict["key_id"] = key
                    trusted_keys_lst.append(trusted_keys_dict)
                    trusted_keys_dict = {}
                ntp_global_config["trusted_keys"] = trusted_keys_lst
            else:
                trusted_keys_dict["key_id"] = trusted_keys
                trusted_keys_lst.append(trusted_keys_dict)
                ntp_global_config["trusted_keys"] = trusted_keys_lst
        return utils.remove_empties(ntp_global_config)
