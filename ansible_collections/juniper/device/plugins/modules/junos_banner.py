#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_banner
author: Ganesh Nalawade (@ganeshrn)
short_description: Manage multiline banners on Juniper JUNOS devices
description:
- This will configure both login and motd banners on network devices. It allows playbooks
  to add or remote banner text from the active running configuration.
version_added: 1.0.0
extends_documentation_fragment:
- junipernetworks.junos.junos
options:
  banner:
    description:
    - Specifies which banner that should be configured on the remote device. Value
      C(login) indicates system login message prior to authenticating, C(motd) is
      login announcement after successful authentication.
    type: str
    required: true
    choices:
    - login
    - motd
  text:
    description:
    - The banner text that should be present in the remote device running configuration.  This
      argument accepts a multiline string, with no empty lines. Requires I(state=present).
    type: str
  state:
    description:
    - Specifies whether or not the configuration is present in the current devices
      active running configuration.
    type: str
    default: present
    choices:
    - present
    - absent
  active:
    description:
    - Specifies whether or not the configuration is active or deactivated
    type: bool
    default: true
requirements:
- ncclient (>=v0.5.2)
notes:
- This module requires the netconf system service be enabled on the remote device
  being managed.
- Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
- Recommended connection is C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- This module also works with C(local) connections for legacy playbooks.
"""

EXAMPLES = """
- name: configure the login banner
  junipernetworks.junos.junos_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present

- name: remove the motd banner
  junipernetworks.junos.junos_banner:
    banner: motd
    state: absent

- name: deactivate the motd banner
  junipernetworks.junos.junos_banner:
    banner: motd
    state: present
    active: false

- name: activate the motd banner
  junipernetworks.junos.junos_banner:
    banner: motd
    state: present
    active: true

- name: Configure banner from file
  junipernetworks.junos.junos_banner:
    banner: motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present
"""

RETURN = """
diff.prepared:
  description: Configuration difference before and after applying change.
  returned: when configuration is changed and diff option is enabled.
  type: str
  sample: >
          [edit system login]
          +   message \"this is my login banner\";
"""
import collections

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    commit_configuration,
    discard_changes,
    load_config,
    locked_config,
    map_obj_to_ele,
    map_params_to_obj,
    tostring,
)


USE_PERSISTENT_CONNECTION = True


def validate_param_values(module, obj):
    for key in obj:
        # validate the param value (if validator func exists)
        validator = globals().get("validate_%s" % key)
        if callable(validator):
            validator(module.params.get(key), module)


def main():
    """main entry point for module execution"""
    argument_spec = dict(
        banner=dict(required=True, choices=["login", "motd"]),
        text=dict(),
        state=dict(default="present", choices=["present", "absent"]),
        active=dict(default=True, type="bool"),
    )

    required_if = [("state", "present", ("text",))]

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    warnings = list()
    result = {"changed": False}

    if warnings:
        result["warnings"] = warnings

    top = "system/login"

    param_to_xpath_map = collections.OrderedDict()

    param_to_xpath_map.update(
        [
            (
                "text",
                {
                    "xpath": "message" if module.params["banner"] == "login" else "announcement",
                    "leaf_only": True,
                },
            ),
        ],
    )

    validate_param_values(module, param_to_xpath_map)

    want = map_params_to_obj(module, param_to_xpath_map)
    ele = map_obj_to_ele(module, want, top)

    with locked_config(module):
        diff = load_config(module, tostring(ele), warnings, action="merge")

        commit = not module.check_mode
        if diff:
            if commit:
                commit_configuration(module)
            else:
                discard_changes(module)
            result["changed"] = True

            if module._diff:
                result["diff"] = {"prepared": diff}

    module.exit_json(**result)


if __name__ == "__main__":
    main()
