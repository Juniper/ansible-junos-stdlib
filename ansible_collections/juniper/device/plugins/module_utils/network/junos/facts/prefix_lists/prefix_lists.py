#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos prefix_lists fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.prefix_lists.prefix_lists import (
    Prefix_listsArgs,
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


class Prefix_listsFacts(object):
    """The junos prefix_lists fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Prefix_listsArgs.argument_spec
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
        """Populate the facts for bgp_address_family
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")
        if not HAS_XMLTODICT:
            self._module.fail_json(msg="xmltodict is not installed.")
        if not data:
            config_filter = """
                        <configuration>
                           <policy-options>
                             <prefix-list>
                             </prefix-list>
                           </policy-options>
                        </configuration>
                        """
            data = self.get_device_data(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/policy-options")

        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"prefix_lists": []}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            for cfg in params["config"]:
                facts["prefix_lists"].append(utils.remove_empties(cfg))
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
        prefix_lists_config = []
        pl_dict = {}
        pl_cfg = []
        # Parse facts for routing instances node
        prefix_lists = conf["policy-options"].get("prefix-list")
        if isinstance(prefix_lists, dict):
            pl_cfg.append(prefix_lists)
        else:
            pl_cfg = prefix_lists
        for cfg in pl_cfg:
            # Parse attribute name
            if cfg.get("name"):
                pl_dict["name"] = cfg.get("name")

            # Parse attribute dynamic-db
            if "dynamic-db" in cfg.keys():
                pl_dict["dynamic_db"] = True

            # Parse attribute address-prefix
            if cfg.get("prefix-list-item"):
                addr_prefix = cfg.get("prefix-list-item")
                addr_pre_list = []
                if isinstance(addr_prefix, dict):
                    addr_pre_list.append(addr_prefix["name"])
                else:
                    for prefix in addr_prefix:
                        addr_pre_list.append(prefix["name"])
                pl_dict["address_prefixes"] = addr_pre_list

            if pl_dict:
                prefix_lists_config.append(pl_dict)
                pl_dict = {}

        return prefix_lists_config
