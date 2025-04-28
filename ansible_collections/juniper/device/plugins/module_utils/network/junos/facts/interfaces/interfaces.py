#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos interfaces fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.interfaces.interfaces import (
    InterfacesArgs,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.utils.utils import (
    get_resource_config,
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


class InterfacesFacts(object):
    """The junos interfaces fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = InterfacesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_config(self, connection, config_filter):
        """

        :param connection:
        :param config_filter:
        :return:
        """
        return get_resource_config(connection, config_filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for interfaces

        :param connection: the device connection
        :param data: previously collected configuration as lxml ElementTree root instance
                     or valid xml sting
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            config_filter = """
                <configuration>
                    <interfaces/>
                </configuration>
            """
            data = self.get_config(connection, config_filter=config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )

        resources = data.xpath("configuration/interfaces/interface")

        objs = []
        for resource in resources:
            if resource is not None:
                obj = self.render_config(self.generated_spec, resource)
                if obj:
                    objs.append(obj)
        facts = {}
        if objs:
            facts["interfaces"] = []
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )
            for cfg in params["config"]:
                facts["interfaces"].append(utils.remove_empties(cfg))
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
        :param conf: The ElementTree instance of configuration object
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        config["name"] = utils.get_xml_conf_arg(conf, "name")
        config["description"] = utils.get_xml_conf_arg(conf, "description")
        mtu = utils.get_xml_conf_arg(conf, "mtu")
        config["mtu"] = int(mtu) if mtu else None
        config["speed"] = utils.get_xml_conf_arg(conf, "speed")
        config["duplex"] = utils.get_xml_conf_arg(conf, "link-mode")
        config["hold_time"]["down"] = utils.get_xml_conf_arg(
            conf,
            "hold-time/down",
        )
        config["hold_time"]["up"] = utils.get_xml_conf_arg(
            conf,
            "hold-time/up",
        )
        disable = utils.get_xml_conf_arg(conf, "disable", data="tag")
        if disable:
            config["enabled"] = False
        else:
            config["enabled"] = True
        cfg = self._get_xml_dict(conf)
        unit_cfg = cfg.get("interface")
        if "unit" in unit_cfg.keys():
            units = unit_cfg.get("unit")
            unit_lst = []
            unit_dict = {}
            if isinstance(units, dict):
                if "description" in units.keys():
                    unit_dict["name"] = units["name"]
                    unit_dict["description"] = units["description"]
                    unit_lst.append(unit_dict)
            else:
                for unit in units:
                    if "description" in unit.keys():
                        unit_dict["name"] = unit["name"]
                        unit_dict["description"] = unit["description"]
                        unit_lst.append(unit_dict)
                        unit_dict = {}
            config["units"] = unit_lst

        return utils.remove_empties(config)
