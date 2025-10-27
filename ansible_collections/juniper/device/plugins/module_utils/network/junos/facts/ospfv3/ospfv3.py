# Copyright (C) 2020  Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


"""
The junos_ospfv3 fact class
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

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.ospfv3.ospfv3 import (
    Ospfv3Args,
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


class Ospfv3Facts(object):
    """The junos ospfv3 fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Ospfv3Args.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)
        self.router_id = ""

    def get_connection(self, connection, config_filter):
        """

        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for ospfv3
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
                    <ospf3/>
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

        resources = data.xpath("configuration/protocols/ospf3")
        router_id_path = data.xpath("configuration/routing-options/router-id")
        if router_id_path:
            self.router_id = self._get_xml_dict(router_id_path.pop())
        else:
            self.router_id = ""

        objs = []
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                obj = self.render_config(self.generated_spec, xml)
                if obj:
                    objs.append(obj)

        facts = {"ospfv3": []}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            for cfg in params["config"]:
                facts["ospfv3"].append(utils.remove_empties(cfg))

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
        ospfv3 = conf.get("ospf3")

        if ospfv3.get("area"):
            rendered_areas = []
            areas = ospfv3.get("area")

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
                    interface_dict["name"] = interface.get("name")
                    interface_dict["priority"] = interface.get("priority")
                    interface_dict["metric"] = interface.get("metric")
                    interface_dict["timers"] = {}
                    interface_dict["timers"]["hello_interval"] = interface.get(
                        "hello-interval",
                    )
                    interface_dict["timers"]["dead_interval"] = interface.get(
                        "dead-interval",
                    )
                    interface_dict["timers"]["retransmit_interval"] = interface.get(
                        "retransmit-interval",
                    )
                    interface_dict["timers"]["transit_delay"] = interface.get(
                        "transit-delay",
                    )
                    interface_dict["timers"]["poll_interval"] = interface.get(
                        "poll-interval",
                    )
                    if "passive" in interface.keys():
                        interface_dict["passive"] = True
                    if "flood-reduction" in interface.keys():
                        interface_dict["flood_reduction"] = True
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
                            auth_dict["type"] = "simple_password"
                            auth_dict["password"] = auth.get("simple-password")
                        elif auth.get("md5"):
                            auth_dict["type"] = {"md5": []}
                            md5_list = auth.get("md5")

                            if not isinstance(md5_list, list):
                                md5_list = [md5_list]

                            for md5_auth in md5_list:
                                auth_dict["type"]["md5"].append(
                                    {
                                        "key_id": md5_auth.get("name"),
                                        "key": md5_auth.get("key"),
                                    },
                                )
                        interface_dict["authentication"] = auth_dict

                    rendered_area["interfaces"].append(interface_dict)

                if area.get("area-range"):
                    area_range = area["area-range"]
                    if not isinstance(area_range, list):
                        area_range = [area_range]
                    rendered_area["area_range"] = []
                    for a_range in area_range:
                        rendered_area["area_range"].append(a_range["name"])

                if area.get("stub"):
                    rendered_area["stub"] = {"set": True}
                    if "no-summaries" in area.get("stub").keys():
                        rendered_area["stub"]["no_summary"] = True
                    if "default-metric" in area.get("stub").keys():
                        rendered_area["stub"]["default_metric"] = area["stub"].get("default-metric")
                if area.get("nssa"):
                    rendered_area["nssa"] = {"set": True}
                    if "no-summaries" in area.get("nssa").keys():
                        rendered_area["nssa"]["no_summary"] = True
                    elif "summaries" in area.get("nssa").keys():
                        rendered_area["nssa"]["no_summary"] = False
                    if "default-lsa" in area.get("nssa").keys():
                        rendered_area["nssa"]["default-lsa"] = True
                rendered_areas.append(rendered_area)

            if "no-rfc-1583" in ospfv3.keys():
                config["rfc1583compatibility"] = False
            if ospfv3.get("spf-options"):
                config["spf_options"] = {}
                config["spf_options"]["delay"] = ospfv3["spf-options"].get(
                    "delay",
                )
                config["spf_options"]["holddown"] = ospfv3["spf-options"].get(
                    "holddown",
                )
                config["spf_options"]["rapid_runs"] = ospfv3["spf-options"].get("rapid-runs")
            config["overload"] = ospfv3.get("overload")
            config["preference"] = ospfv3.get("preference")
            config["external_preference"] = ospfv3.get("external-preference")
            config["prefix_export_limit"] = ospfv3.get("prefix-export-limit")
            config["reference_bandwidth"] = ospfv3.get("reference-bandwidth")
            config["areas"] = rendered_areas
            if self.router_id:
                config["router_id"] = self.router_id["router-id"]
        return utils.remove_empties(config)
