#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos routing_options fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.routing_options.routing_options import (
    Routing_optionsArgs,
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


class Routing_optionsFacts(object):
    """The junos routing_options fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Routing_optionsArgs.argument_spec
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
        """Populate the facts for routing_options
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
                            <routing-options>
                            </routing-options>
                        </configuration>
                        """
            data = self.get_device_data(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/routing-options")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"routing_options": []}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["routing_options"] = utils.remove_empties(params["config"])
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
        routing_config = {}
        conf = conf.get("routing-options")

        # Read autonomous-system
        if "autonomous-system" in conf.keys():
            as_num = conf.get("autonomous-system")
            as_dict = {}
            if "as-number" in as_num.keys():
                as_dict["as_number"] = as_num.get("as-number")
            if as_num.get("loops"):
                as_dict["loops"] = as_num.get("loops")
            if "asdot-notation" in as_num.keys():
                as_dict["asdot_notation"] = True
            routing_config["autonomous_system"] = as_dict

        # Read router-id
        if "router-id" in conf.keys():
            routing_config["router_id"] = conf.get("router-id")

        return utils.remove_empties(routing_config)
