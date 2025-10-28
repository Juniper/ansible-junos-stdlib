#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: tbrdevice_facts
author: Nathaniel Case (@Qalthos)
short_description: Collect facts from remote devices running Juniper Junos
description:
- Collects fact information from a remote device running the Junos operating system.  By
  default, the module will collect basic fact information from the device to be included
  with the hostvars. Additional fact information can be collected based on the configured
  set of arguments.
version_added: 1.0.0
extends_documentation_fragment:
- juniper.device.junos
options:
  gather_subset:
    description:
    - When supplied, this argument will restrict the facts collected to a given subset.  Possible
      values for this argument include C(all), C(hardware), C(config), C(interfaces) and C(min). Can
      specify a list of values to include a larger subset.  Values can also be used
      with an initial C(!) to specify that a specific subset should not be collected.
      To maintain backward compatibility old style facts can be retrieved by explicitly
      adding C(ofacts)  to value, this requires junos-eznc to be installed as a prerequisite.
      Valid value of gather_subset are default, hardware, config, interfaces, ofacts.
      If C(ofacts) is present in the list it fetches the old style facts (fact keys
      without 'ansible_' prefix) and it requires junos-eznc library to be installed.
    required: false
    default:
    - 'min'
    type: list
    elements: str
  config_format:
    description:
    - The I(config_format) argument specifies the format of the configuration when
      serializing output from the device. This argument is applicable only when C(config)
      value is present in I(gather_subset). The I(config_format) should be supported
      by the junos version running on device. This value is not applicable while fetching
      old style facts that is when C(ofacts) value is present in value if I(gather_subset)
      value. This option is valid only for C(gather_subset) values.
    type: str
    required: false
    default: text
    choices:
    - xml
    - text
    - set
    - json
  gather_network_resources:
    description:
    - When supplied, this argument will restrict the facts collected to a given subset.
      Possible values for this argument include all and the resources like interfaces,
      vlans etc. Can specify a list of values to include a larger subset. Values can
      also be used with an initial C(!) to specify that a specific subset should
      not be collected. Valid subsets are 'all', 'interfaces', 'lacp', 'lacp_interfaces',
      'lag_interfaces', 'l2_interfaces', 'l3_interfaces', 'lldp_global', 'lldp_interfaces',
      'vlans'.
    required: false
    type: list
    elements: str
  available_network_resources:
    description: When 'True' a list of network resources for which resource modules are available will be provided.
    type: bool
    default: false
requirements:
- ncclient (>=v0.5.2)
notes:
- Ensure I(config_format) used to retrieve configuration from device is supported
  by junos version running on device.
- With I(config_format = json), configuration in the results will be a dictionary(and
  not a JSON string)
- This module requires the netconf system service be enabled on the remote device
  being managed.
- Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
- Recommended connection is C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- This module also works with C(local) connections for legacy playbooks.
"""

EXAMPLES = """
- name: collect default set of facts
  juniper.device.junos_facts:

- name: collect default set of facts and configuration
  juniper.device.junos_facts:
    gather_subset: config

- name: Gather legacy and resource facts
  juniper.device.junos_facts:
    gather_subset: all
    gather_network_resources: all
"""

RETURN = """
ansible_facts:
  description: Returns the facts collect from the device
  returned: always
  type: dict
"""
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.facts.facts import (
    FactsArgs,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.facts import (
    FACT_RESOURCE_SUBSETS,
    Facts,
)


def main():
    """
    Main entry point for module execution

    :returns: ansible_facts
    """
    argument_spec = FactsArgs.argument_spec

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    warnings = []
    ansible_facts = {}
    if module.params.get("available_network_resources"):
        ansible_facts["available_network_resources"] = sorted(
            FACT_RESOURCE_SUBSETS.keys(),
        )
    result = Facts(module).get_facts()
    additional_facts, additional_warnings = result
    ansible_facts.update(additional_facts)
    warnings.extend(additional_warnings)
    module.exit_json(ansible_facts=ansible_facts, warnings=warnings)


if __name__ == "__main__":
    main()
