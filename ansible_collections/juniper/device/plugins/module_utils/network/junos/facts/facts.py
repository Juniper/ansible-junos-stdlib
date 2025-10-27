#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The facts class for junos
this file validates each subset of facts and selectively
calls the appropriate facts gathering function
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import (
    FactsBase,
)

from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.acl_interfaces.acl_interfaces import (
    Acl_interfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.acls.acls import (
    AclsFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.bgp_address_family.bgp_address_family import (
    Bgp_address_familyFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.bgp_global.bgp_global import (
    Bgp_globalFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.hostname.hostname import (
    HostnameFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.interfaces.interfaces import (
    InterfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.l2_interfaces.l2_interfaces import (
    L2_interfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.l3_interfaces.l3_interfaces import (
    L3_interfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.lacp.lacp import (
    LacpFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.lacp_interfaces.lacp_interfaces import (
    Lacp_interfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.lag_interfaces.lag_interfaces import (
    Lag_interfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.legacy.base import (
    Config,
    Default,
    Hardware,
    Interfaces,
    OFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.lldp_global.lldp_global import (
    Lldp_globalFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.lldp_interfaces.lldp_interfaces import (
    Lldp_interfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.logging_global.logging_global import (
    Logging_globalFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.ntp_global.ntp_global import (
    Ntp_globalFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.ospf_interfaces.ospf_interfaces import (
    Ospf_interfacesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.ospfv2.ospfv2 import (
    Ospfv2Facts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.ospfv3.ospfv3 import (
    Ospfv3Facts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.prefix_lists.prefix_lists import (
    Prefix_listsFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.routing_instances.routing_instances import (
    Routing_instancesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.routing_options.routing_options import (
    Routing_optionsFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.security_policies.security_policies import (
    Security_policiesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.security_policies_global.security_policies_global import (
    Security_policies_globalFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.security_zones.security_zones import (
    Security_zonesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.snmp_server.snmp_server import (
    Snmp_serverFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.static_routes.static_routes import (
    Static_routesFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.vlans.vlans import (
    VlansFacts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    HAS_PYEZ,
)


FACT_LEGACY_SUBSETS = dict(
    default=Default,
    hardware=Hardware,
    config=Config,
    interfaces=Interfaces,
)
FACT_RESOURCE_SUBSETS = dict(
    acls=AclsFacts,
    acl_interfaces=Acl_interfacesFacts,
    interfaces=InterfacesFacts,
    lacp=LacpFacts,
    lacp_interfaces=Lacp_interfacesFacts,
    lag_interfaces=Lag_interfacesFacts,
    l2_interfaces=L2_interfacesFacts,
    l3_interfaces=L3_interfacesFacts,
    lldp_global=Lldp_globalFacts,
    lldp_interfaces=Lldp_interfacesFacts,
    ospfv2=Ospfv2Facts,
    ospfv3=Ospfv3Facts,
    ospf_interfaces=Ospf_interfacesFacts,
    vlans=VlansFacts,
    static_routes=Static_routesFacts,
    bgp_global=Bgp_globalFacts,
    bgp_address_family=Bgp_address_familyFacts,
    routing_instances=Routing_instancesFacts,
    prefix_lists=Prefix_listsFacts,
    logging_global=Logging_globalFacts,
    ntp_global=Ntp_globalFacts,
    security_policies=Security_policiesFacts,
    security_policies_global=Security_policies_globalFacts,
    security_zones=Security_zonesFacts,
    snmp_server=Snmp_serverFacts,
    routing_options=Routing_optionsFacts,
    hostname=HostnameFacts,
)


class Facts(FactsBase):
    """The fact class for junos"""

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(
        self,
        legacy_facts_type=None,
        resource_facts_type=None,
        data=None,
    ):
        """Collect the facts for junos
        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(
                FACT_RESOURCE_SUBSETS,
                resource_facts_type,
                data,
            )

        if not legacy_facts_type:
            legacy_facts_type = self._gather_subset
            # fetch old style facts only when explicitly mentioned in gather_subset option
            if "ofacts" in legacy_facts_type:
                if HAS_PYEZ:
                    self.ansible_facts.update(OFacts(self._module).populate())
                else:
                    self._warnings.extend(
                        [
                            "junos-eznc is required to gather old style facts but does not appear to be installed. "
                            "It can be installed using `pip install junos-eznc`",
                        ],
                    )
                self.ansible_facts["ansible_net_gather_subset"].append(
                    "ofacts",
                )
                legacy_facts_type.remove("ofacts")

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(
                FACT_LEGACY_SUBSETS,
                legacy_facts_type,
            )

        return self.ansible_facts, self._warnings
