#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos acl_interfaces fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.acl_interfaces.acl_interfaces import (
    Acl_interfacesArgs,
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


class Acl_interfacesFacts(object):
    """The junos acl_interfaces fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Acl_interfacesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for acl_interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg=missing_required_lib("lxml"))

        if not data:
            config_filter = """
                <configuration>
                    <interfaces/>
                </configuration>
                """
            data = connection.get_configuration(filter=config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )

        resources = data.xpath("configuration/interfaces/interface")

        objs = []
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                obj = self.render_config(self.generated_spec, xml)
                if obj:
                    objs.append(obj)

        facts = {}
        if objs:
            facts["acl_interfaces"] = []
            # Included for compatibility, remove after 2025-07-01
            facts["junos_acl_interfaces"] = []
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )
            for cfg in params["config"]:
                facts["acl_interfaces"].append(utils.remove_empties(cfg))
                # Included for compatibility, remove after 2025-07-01
                facts["junos_acl_interfaces"].append(utils.remove_empties(cfg))

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
        config = deepcopy(spec)
        config["access_groups"] = []

        if "unit" in conf["interface"] and "family" in conf["interface"]["unit"]:
            for family in conf["interface"]["unit"]["family"].keys():
                access_groups = {
                    "afi": "ipv6" if family == "inet6" else "ipv4",
                    "acls": [],
                }
                if conf["interface"]["unit"]["family"][family] is not None and conf["interface"][
                    "unit"
                ]["family"][family].get(
                    "filter",
                ):
                    for direction in ["input-list", "output-list"]:
                        rendered_direction = "in" if direction == "input-list" else "out"
                        if conf["interface"]["unit"]["family"][family]["filter"].get(direction):
                            acl_name = conf["interface"]["unit"]["family"][family]["filter"][
                                direction
                            ]
                            if not isinstance(acl_name, list):
                                acl_name = [acl_name]
                            for filter_name in acl_name:
                                access_groups["acls"].append(
                                    {
                                        "name": filter_name,
                                        "direction": rendered_direction,
                                    },
                                )
                if access_groups["acls"]:
                    config["name"] = conf["interface"]["name"]
                    config["access_groups"].append(access_groups)

        return utils.remove_empties(config)
