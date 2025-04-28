#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos ospf_interfaces fact class
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
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    generate_dict,
    remove_empties,
)

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.ospf_interfaces.ospf_interfaces import (
    Ospf_interfacesArgs,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.utils.utils import (
    _validate_config,
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


class Ospf_interfacesFacts(object):
    """The junos ospf_interfaces fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Ospf_interfacesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = generate_dict(facts_argument_spec)
        self.router_id = ""

    def get_connection(self, connection, config_filter):
        """

        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for ospf_interfaces
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
                  <protocols>
                    <ospf/>
                  </protocols>
                  <routing-options>
                    <router-id/>
                  </routing-options>
                </configuration>
                """
            data = self.get_connection(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )

        resources = data.xpath("configuration/protocols/ospf")
        router_id_path = data.xpath("configuration/routing-options/router-id")

        if router_id_path:
            self.router_id = self._get_xml_dict(router_id_path.pop())
        else:
            self.router_id = ""

        objs = []
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"ospf_interfaces": []}
        if objs:
            params = _validate_config(
                self._module,
                self.argument_spec,
                {"config": objs},
                redact=True,
            )

            for cfg in params["config"]:
                facts["ospf_interfaces"].append(remove_empties(cfg))

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
        ospf_interfaces_config = []
        ospf = conf.get("ospf")

        if ospf.get("area"):
            areas = ospf.get("area")

            if not isinstance(areas, list):
                areas = [areas]

            for area in areas:
                rendered_area = {}
                rendered_area["area_id"] = area.get("name")
                rendered_area["interfaces"] = []

                interfaces = area["interface"]
                if not isinstance(interfaces, list):
                    interfaces = [interfaces]
                for interface in interfaces:
                    interface_dict = {}
                    interface_dict["priority"] = interface.get("priority")
                    interface_dict["metric"] = interface.get("metric")
                    interface_dict["mtu"] = interface.get("mtu")
                    interface_dict["te_metric"] = interface.get("te-metric")
                    interface_dict["ipsec_sa"] = interface.get("ipsec-sa")
                    interface_dict["hello_interval"] = interface.get(
                        "hello-interval",
                    )
                    interface_dict["dead_interval"] = interface.get(
                        "dead-interval",
                    )
                    interface_dict["retransmit_interval"] = interface.get(
                        "retransmit-interval",
                    )
                    interface_dict["transit_delay"] = interface.get(
                        "transit-delay",
                    )
                    interface_dict["poll_interval"] = interface.get(
                        "poll-interval",
                    )
                    if "passive" in interface.keys():
                        interface_dict["passive"] = True
                    if "flood-reduction" in interface.keys():
                        interface_dict["flood_reduction"] = True
                    if "demand-circuit" in interface.keys():
                        interface_dict["demand_circuit"] = True
                    if "no-advertise-adjacency-segment" in interface.keys():
                        interface_dict["no_advertise_adjacency_segment"] = True
                    if "no-eligible-backup" in interface.keys():
                        interface_dict["no_eligible_backup"] = True
                    if "no-eligible-remote-backup" in interface.keys():
                        interface_dict["no_eligible_remote_backup"] = True
                    if "no-interface-state-traps" in interface.keys():
                        interface_dict["no_interface_state_traps"] = True
                    if "no-neighbor-down-notification" in interface.keys():
                        interface_dict["no_neighbor_down_notification"] = True
                    if "node-link-protection" in interface.keys():
                        interface_dict["node_link_protection"] = True
                    if "bandwidth-based-metrics" in interface.keys():
                        bandwidth_metrics = interface["bandwidth-based-metrics"].get("bandwidth")
                        if not isinstance(bandwidth_metrics, list):
                            bandwidth_metrics = [bandwidth_metrics]
                        interface_dict["bandwidth_based_metrics"] = []

                        for metric in bandwidth_metrics:
                            interface_dict["bandwidth_based_metrics"].append(
                                {
                                    "metric": metric.get("metric"),
                                    "bandwidth": metric.get("name"),
                                },
                            )

                    if "authentication" in interface.keys():
                        auth = interface["authentication"]
                        auth_dict = {}
                        if auth.get("simple-password"):
                            auth_dict["simple_password"] = auth.get(
                                "simple-password",
                            )
                        if "md5" in auth.keys():
                            md5_cfg = auth.get("md5")
                            md5_lst = []
                            if isinstance(md5_cfg, dict):
                                md5_dict = {}
                                md5_dict["key_id"] = md5_cfg.get("name")
                                md5_dict["key_value"] = md5_cfg.get("key")
                                md5_dict["start_time"] = md5_cfg.get("start-time")
                                md5_lst.append(md5_dict)
                            else:
                                for md5 in md5_cfg:
                                    md5_dict = {}
                                    md5_dict["key_id"] = md5.get("name")
                                    md5_dict["key_value"] = md5.get("key")
                                    md5_dict["start_time"] = md5.get("start-time")
                                    md5_lst.append(md5_dict)
                            auth_dict["md5"] = md5_lst
                        interface_dict["authentication"] = auth_dict

                    rendered_area["interfaces"].append(interface_dict)

                    af = {}
                    conf = {}
                    areas = {}
                    address_family = []
                    af["afi"] = "ipv4"
                    areas["area_id"] = rendered_area["area_id"]
                    interface_dict["area"] = areas
                    af["processes"] = interface_dict
                    address_family.append(af)
                    conf["address_family"] = address_family
                    conf["name"] = interface.get("name")
                    if self.router_id:
                        conf["router_id"] = self.router_id["router-id"]
                    remove_empties(conf)
                    ospf_interfaces_config.append(conf)

        return ospf_interfaces_config
