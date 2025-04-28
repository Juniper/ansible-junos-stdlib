#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos routing_instances fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.routing_instances.routing_instances import (
    Routing_instancesArgs,
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


class Routing_instancesFacts(object):
    """The junos routing_instances fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Routing_instancesArgs.argument_spec
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
                           <routing-instances/>
                        </configuration>
                        """
            data = self.get_device_data(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/routing-instances")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"routing_instances": []}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            for cfg in params["config"]:
                facts["routing_instances"].append(utils.remove_empties(cfg))
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
        routing_instances_config = []

        # Parse facts for routing instances node
        conf = conf.get("routing-instances")

        # Parse routing instances
        routing_instances = conf.get("instance")
        if isinstance(routing_instances, list):
            for instance in routing_instances:
                instance_dict = self.parse_instance(instance)
                routing_instances_config.append(instance_dict)
        else:
            instance_dict = self.parse_instance(routing_instances)
            routing_instances_config.append(instance_dict)

        return routing_instances_config

    def parse_instance(self, instance):
        """

        :param instance:
        :return:
        """
        instance_dict = {}
        # read instance name
        instance_dict["name"] = instance["name"]

        # read connection-id-advertise
        if "connector-id-advertise" in instance.keys():
            instance_dict["connector_id_advertise"] = True

        # read description
        if instance.get("description"):
            instance_dict["description"] = instance["description"]

        # read instance role
        if instance.get("instance-role"):
            instance_dict["instance_role"] = instance["instance-role"]

        # read instance type
        if instance.get("instance-type"):
            instance_dict["type"] = instance["instance-type"]

        # read interfaces
        if instance.get("interface"):
            interfaces = instance.get("interface")
            interfaces_list = []
            if isinstance(interfaces, list):
                for interface in interfaces:
                    interfaces_list.append(self.parse_interface(interface))
            else:
                interfaces_list.append(self.parse_interface(interfaces))
            instance_dict["interfaces"] = interfaces_list

        # read l2vpn-id
        if instance.get("l2vpn-id"):
            instance_dict["l2vpn_id"] = instance["l2vpn-id"].get("community")

        # read no-irb-layer2-copy
        if "no-irb-layer2-copy" in instance.keys():
            instance_dict["no_irb_layer_2_copy"] = True

        # read no_local_switching
        if "no-local-switching" in instance.keys():
            instance_dict["no_local_switching"] = True

        # read no-vrf-advertise
        if "no-vrf-advertise" in instance.keys():
            instance_dict["no_vrf_advertise"] = True

        # read no_vrf_propagate_ttl
        if "no-vrf-propagate-ttl" in instance.keys():
            instance_dict["no_vrf_propagate_ttl"] = True

        # read qualified_bum_pruning_mode
        if instance.get("qualified-bum-pruning-mode"):
            instance_dict["qualified_bum_pruning_mode"] = True

        # read route-distinguisher
        if instance.get("route-distinguisher"):
            instance_dict["route_distinguisher"] = instance["route-distinguisher"].get("rd-type")

        # read vrf imports
        if instance.get("vrf-import"):
            vrf_imp_lst = []
            vrf_imp = instance.get("vrf-import")

            if isinstance(vrf_imp, list):
                vrf_imp_lst = vrf_imp
            else:
                vrf_imp_lst.append(vrf_imp)
            instance_dict["vrf_imports"] = vrf_imp_lst

        # read vrf exports
        if instance.get("vrf-export"):
            vrf_exp_lst = []
            vrf_exp = instance.get("vrf-export")
            if isinstance(vrf_exp, list):
                vrf_exp_lst = vrf_exp
            else:
                vrf_exp_lst.append(vrf_exp)
            instance_dict["vrf_exports"] = vrf_exp_lst

        # read bridge domains
        if instance.get("bridge-domains"):
            br_domain_lst = []
            br_domains = instance.get("bridge-domains").get("domain")
            if isinstance(br_domains, list):
                for domain in br_domains:
                    br_item = {
                        k.replace("-", "_"): (v if v is not None else True)
                        for k, v in domain.items()
                    }
                    br_domain_lst.append(br_item)
            else:
                br_item = {
                    k.replace("-", "_"): (v if v is not None else True)
                    for k, v in br_domains.items()
                }
                br_domain_lst.append(br_item)
            instance_dict["bridge_domains"] = br_domain_lst

        return utils.remove_empties(instance_dict)

    def parse_interface(self, interface):
        """

        :param instance:
        :return:
        """
        cfg_dict = {}
        cfg_dict["name"] = interface["name"]
        if interface.get("protect-interface"):
            cfg_dict["protect_interface"] = interface.get("protect-interface")

        return cfg_dict
