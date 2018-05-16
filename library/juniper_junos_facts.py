#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2014, Jeremy Schulman
#
# All rights reserved.
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
extends_documentation_fragment: 
  - juniper_junos_common.connection_documentation
  - juniper_junos_common.logging_documentation
module: juniper_junos_facts
version_added: "2.0.0" # of Juniper.junos role
author: "Juniper Networks - Stacy Smith (@stacywsmith)"
short_description: Retrieve facts from a Junos device
description:
  - Retrieve facts from a Junos device using the
    U(PyEZ fact gathering system|http://junos-pyez.readthedocs.io/en/stable/jnpr.junos.facts.html).
  - Also returns the committed configuration of the Junos device if the
    I(config_format) option has a value other than C(none).
options:
  config_format:
    description:
      - The format of the configuration returned. The specified format must be
        supported by the target Junos device.
    required: false
    default: none
    choices:
      - none
      - xml
      - set
      - text
      - json
  savedir:
    description:
      - A path to a directory, on the Ansible control machine, where facts
        will be stored in a JSON file.
      - The resulting JSON file is saved in
        I(savedir)C(/)I(hostname)C(-facts.json).
      - The I(savedir) directory is the value of the I(savedir) option.
      - The I(hostname)C(-facts.json) filename begins with the value of the 
        C(hostname) fact returned from the Junos device, which might be
        different than the value of the I(host) option passed to the module.
      - If the value of the I(savedir) option is C(none), the default, then
        facts are NOT saved to a file.
    required: false
    default: none
    type: path
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

# Print a fact

# Using config_format option

# Print the config

# Using savedir option

# Print the saved JSON file
'''

RETURN = '''
ansible_facts.junos:
  description:
    - Facts collected from the Junos device. This dictionary contains the
      keys listed in the I(contains) section of this documentation PLUS all
      of the keys returned from PyEZ's fact gathering system. See
      U(PyEZ facts|http://junos-pyez.readthedocs.io/en/stable/jnpr.junos.facts.html)
      for a complete list of these keys and their meaning.
  returned: success
  type: complex
  contains:
    config:
      description:
        - The device's committed configuration, in the format specified by
          I(config_format), as a single multi-line string.
      returned: when I(config_format) is not C(none).
      type: str
    has_2RE:
      description:
        - Indicates if the device has more than one Routing Engine installed.
          Because Ansible does not allow keys to begin with a number, this fact
          is returned in place of PyEZ's C(2RE) fact.
      returned: success
      type: bool
    re_name:
      description:
        - The name of the current Routing Engine to which Ansible is connected.
      returned: success
      type: str
    master_state:
      description:
        - The mastership state of the Routing Engine to which Ansible is
          connected. C(true) if the RE is the master Routing Engine. C(false)
          if the RE is not the master Routing Engine.
      returned: success
      type: bool
changed:
  description:
    - Indicates if the device's state has changed. Since this module does not
      change the operational or configuration state of the device, the value is
      always set to C(false).
  returned: success
  type: bool
  sample: false
facts:
  description:
    - Returned for backwards compatibility. Returns the same keys and values
      which are returned under I(ansible_facts.junos).
  returned: success
  type: dict
failed:
  description:
    - Indicates if the task failed.
  returned: always
  type: bool
  sample: false
'''

# Standard library imports
import json
import os.path



"""From Ansible 2.1, Ansible uses Ansiballz framework for assembling modules
But custom module_utils directory is supported from Ansible 2.3
Reference for the issue: https://groups.google.com/forum/#!topic/ansible-project/J8FL7Z1J1Mw """

# Ansiballz packages module_utils into ansible.module_utils
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import juniper_junos_common


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
    if 'version_info' in facts and facts['version_info'] is not None:
        facts['version_info'] = dict(facts['version_info'])
    # The values of the ['junos_info'][re_name]['object'] keys are
    # custom junos.version_info objects. Convert all of these to dicts.
    if 'junos_info' in facts and facts['junos_info'] is not None:
        for key in facts['junos_info']:
            facts['junos_info'][key]['object'] = dict(
                facts['junos_info'][key]['object'])
    return facts


def save_facts(junos_module, facts):
    """If the savedir option was specified, save the facts into a JSON file.

    If the savedir option was specified, save the facts into a JSON file named
    savedir/hostname-facts.json. The filename begins with the value of the
    hostname fact returned from the Junos device, which might be different than
    the value of the host option passed to the module.

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
        junos_module.logger.debug("Saving facts to: %s.", file_path)
        try:
            with open(file_path, 'w') as fact_file:
                json.dump(facts, fact_file)
            junos_module.logger.debug("Facts saved to: %s.", file_path)
        except IOError:
            junos_module.fail_json(msg="Unable to save facts. Failed to open "
                                       "the %s file." % (file_path))


def save_inventory(junos_module, inventory):
    """If the savedir option was specified, save the XML inventory.

    If the savedir option was specified, save the inventory XML output into
    an XML file named savedir/hostname-inventory.xml. The filename begins with
    the value of the hostname fact returned from the Junos device, which might
    be different than the value of the host option passed to the module.

    Args:
        junos_module: An instance of a JuniperJunosModule.
        inventory: The XML string of inventory to save.

    Raises:
        IOError: Calls junos_module.fail_json if unable to open the inventory
                 file for writing.
    """
    if junos_module.params.get('savedir') is not None:
        save_dir = junos_module.params.get('savedir')
        file_name = '%s-inventory.xml' % (junos_module.dev.facts['hostname'])
        file_path = os.path.normpath(os.path.join(save_dir, file_name))
        junos_module.logger.debug("Saving inventory to: %s.", file_path)
        try:
            with open(file_path, 'wb') as fact_file:
                fact_file.write(inventory.encode(encoding='utf-8'))
            junos_module.logger.debug("Inventory saved to: %s.", file_path)
        except IOError:
            junos_module.fail_json(msg="Unable to save inventory. Failed to "
                                       "open the %s file." % (file_path))


def main():
    config_format_choices = [None]
    config_format_choices += juniper_junos_common.CONFIG_FORMAT_CHOICES

    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            config_format=dict(choices=config_format_choices,
                               required=False,
                               default=None),
            savedir=dict(type='path', required=False, default=None),
        ),
        # Since this module doesn't change the device's configuration, there is
        # no additional work required to support check mode. It's inherently
        # supported.
        supports_check_mode=True,
        min_jxmlease_version=juniper_junos_common.MIN_JXMLEASE_VERSION,
    )

    junos_module.logger.debug("Gathering facts.")
    # Get the facts dictionary from the device.
    facts = get_facts_dict(junos_module)
    junos_module.logger.debug("Facts gathered.")

    if junos_module.params.get('savedir') is not None:
        # Save the facts.
        save_facts(junos_module, facts)

        # Get and save the inventory
        try:
            junos_module.logger.debug("Gathering inventory.")
            inventory = junos_module.dev.rpc.get_chassis_inventory()
            junos_module.logger.debug("Inventory gathered.")
            save_inventory(junos_module,
                           junos_module.etree.tostring(inventory,
                                                       pretty_print=True))
        except junos_module.pyez_exception.RpcError as ex:
            junos_module.fail_json(msg='Unable to retrieve hardware '
                                       'inventory: %s' % (str(ex)))

    config_format = junos_module.params.get('config_format')
    if config_format is not None:
        (config, config_parsed) = junos_module.get_configuration(
                                      format=config_format)
        if config is not None:
            facts.update({'config': config})
        # Need to wait until the ordering issues are figured out before
        # using config_parsed.
        # if config_parsed is not None:
        #    facts.update({'config_parsed': config_parsed})

    # Return response.
    junos_module.exit_json(
        changed=False,
        failed=False,
        ansible_facts={'junos': facts},
        facts=facts)


if __name__ == '__main__':
    main()
