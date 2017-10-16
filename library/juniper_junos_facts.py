#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2017, Juniper Networks Inc. All rights reserved.
#
# License: Apache 2.0
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# * Neither the name of the Juniper Networks nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Juniper Networks, Inc. ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Juniper Networks, Inc. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from __future__ import absolute_import, division, print_function

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'supported_by': 'community',
                    'status': ['stableinterface']}

DOCUMENTATION = '''
---
module: juniper_junos_facts
version_added: "2.0.0" # of Juniper.junos role
author: "Juniper Networks - Stacy Smith (@stacywsmith)"
short_description: Retrieve facts from a Junos device
description:
  - Retrieve facts from a Junos device using the PyEZ fact gathering system.
    The specific facts returned are documented at:
    U(http://junos-pyez.readthedocs.io/en/latest/jnpr.junos.facts.html)
    Also returns the committed configuration of the Junos device if the
    I(config_format) option has a value other than C(none).
extends_documentation_fragment: juniper_junos_common
options:
  config_format:
    description:
      - The format of the configuration returned. The specified format must be
        supported by the target Junos device.
    required: false
    default: none
    choices: [none, 'xml', 'set', 'text', 'json']
  savedir:
    description:
      - A path to a directory, on the Ansible control machine, where facts
        will be stored in a JSON file. The resulting JSON file is saved in:
        C(savedir/hostname-facts.json). The directory is the value of
        I(savedir). The filename begins with the value of the hostname fact
        returned from the Junos device, which might be different than the
        value of the I(host) option passed to the module. If the value of the
        I(savedir) option is C(none), the default, then facts are NOT saved to
        a file.
    required: false
    default: none
    type: path
requirements:
  - junos-eznc >= 2.1.7
notes:
  - The NETCONF system service must be enabled on the target Junos device.
'''

EXAMPLES = '''
---
- name: Gather facts from Junos devices
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos
  tasks:
    - name: Gather Junos facts with no configuration
      juniper_junos_facts:
'''

RETURN = '''
ansible_facts.junos:
  description: The facts collected from the Junos device.
  returned: success
  type: dict
  sample:
'''

import os.path
import json


def import_juniper_junos_common():
    """Imports the juniper_junos_common module from module_utils_path.

    Ansible versions < 2.4 do not provide a way to package common code in a
    role. This function solves that problem for juniper_junos_* modules by
    reading the module arguments passed on stdin and interpreting the special
    argument module_utils_path as a path to the the directory where the
    juniper_junos_common module resides. It temporarily inserts this path at
    the head of sys.path, imports the juniper_junos_common module, and removes
    the path from sys.path. It then returns the imported juniper_junos_common
    module object. All juniper_junos_* modules must include this boilerplate
    function in order to import the shared juniper_junos_common module.

    Args:
        None.

    Returns:
        The juniper_junos_common module object.

    Raises:
        ImportError: If the juniper_junos_common object can not be imported
                     from the path specified by the module_utils_path argument.
    """
    from ansible.module_utils.basic import AnsibleModule
    import sys

    juniper_junos_common = None
    module = AnsibleModule(
        argument_spec={
            'module_utils_path': dict(type='path', default=None),
            'passwd': dict(no_log=True)
        },
        check_invalid_arguments=False,
        bypass_checks=True
    )
    import_path = module.params.get('module_utils_path')
    if import_path is not None:
        sys.path.insert(0, import_path)
        import juniper_junos_common
        del sys.path[0]
    return juniper_junos_common


def get_facts_dict(junos_module):
    """Retreive PyEZ facts and convert to a standard dict w/o custom types.

    Ansible >= 2.0 doesn't like custom objects in a modules return value.
    Because PyEZ facts are a custom object rather than a true dict they must be
    converted to a standard dict. Since facts are read-only, we must begin by
    copying facts into a dict. Since PyEZ facts are "on-demand", the
    junos_module.dev instance must be an open PyEZ Device instance ojbect
    before this function is called.

    Args:
        junos_module: An instance of a JuniperJunosModule.

    Returns:
        A dict containing the device facts.
    """
    # Retrieve all PyEZ-supported facts and copy to a standard dict.
    facts = dict(junos_module.dev.facts)
    # Add two useful facts that are implement as PyEZ Device attributes.
    facts['re_name'] = junos_module.dev.re_name
    facts['master_state'] = junos_module.dev.master
    # Ansible doesn't allow keys starting with numbers.
    # Replace the '2RE' key with the 'has_2RE' key.
    if '2RE' in facts:
        facts['has_2RE'] = facts['2RE']
        del facts['2RE']
    # The value of the 'version_info' key is a custom junos.version_info
    # object. Convert this value to a dict.
    if 'version_info' in facts:
        facts['version_info'] = dict(facts['version_info'])
    # The values of the ['junos_info'][re_name]['object'] keys are
    # custom junos.version_info objects. Convert all of these to dicts.
    if 'junos_info' in facts:
        for key in facts['junos_info']:
            facts['junos_info'][key]['object'] = dict(
                facts['junos_info'][key]['object'])
    return facts


def save_facts(junos_module, facts):
    """If the savedir argument was specified, save the facts into a JSON file.

    Ansible >= 2.0 doesn't like custom objects in a modules return value.
    Because PyEZ facts are a custom object rather than a true dict they must be
    converted to a standard dict. Since facts are read-only, we must begin by
    copying facts into a dict. Since PyEZ facts are "on-demand", the
    junos_module.dev instance must be an open PyEZ Device instance ojbect
    before this function is called..

    Args:
        junos_module: An instance of a JuniperJunosModule.
        facts: The facts dict returned by get_facts_dict().

    Raises:
        IOError: Calls junos_module.fail_json if unable to open the facts
                 file for writing.
    """
    if junos_module.params.get('savedir') is not None:
        save_dir = junos_module.params.get('savedir')
        file_name = '%s-facts.json' % (facts['hostname'])
        file_path = os.path.normpath(os.path.join(save_dir, file_name))
        try:
            with open(file_path, 'w') as fact_file:
                json.dump(facts, fact_file)
        except IOError:
            junos_module.fail_json(msg="Unable to save facts. Faile to open "
                                       "the %s file." % (file_path))


def main():
    # Import juniper_junos_common
    juniper_junos_common = import_juniper_junos_common()

    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            config_format=dict(choices=[None, 'xml', 'set', 'text', 'json'],
                               required=False,
                               default=None),
            savedir=dict(type='path', required=False, default=None),
        ),
        supports_check_mode=True
    )

    junos_module.log("Device opened. Gathering facts.")

    # Get the facts dictionary from the device.
    facts = get_facts_dict(junos_module)

    # Add code to implement config_format option

    junos_module.log("Facts gathered.")

    # Save the facts.
    save_facts(junos_module, facts)

    junos_module.log("Facts saved.")

    # Return response.
    junos_module.exit_json(
        changed=False,
        failed=False,
        ansible_facts={'junos': facts},
        logobject=str(junos_module.log),
        facts=facts)


if __name__ == '__main__':
    main()
