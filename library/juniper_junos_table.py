#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2016 Jason Edelman <jason@networktocode.com>
# Network to Code, LLC
#
# Copyright (c) 2017-2018, Juniper Networks Inc.
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
module: juniper_junos_table
version_added: "2.0.0" # of Juniper.junos role
author:
  - Jason Edelman (@jedelman8)
  - Updated by Juniper Networks - Stacy Smith (@stacywsmith)
short_description: Retrieve data from a Junos device using a PyEZ table/view
description:
  - Retrieve data from a Junos device using PyEZ's operational table/views.
    This module may be used with the tables/views which are included in the
    PyEZ distribution or it may be used with user-defined tables/views.
options:
  file:
    description:
      - Name of the YAML file, relative to the I(path) option, that contains
        the table/view definition. The file name must end with the C(.yml) or
        C(.yaml) extension.
    required: true
    default: none
    type: path
  kwargs:
    description:
      - Optional keyword arguments and values to the table's get() method. The
        value of this option is a dictionary of keywords and values which are
        used to refine the data return from performing a get() on the table.
        The exact keywords and values which are supported are specific to the
        table's definition and the underlying RPC which the table invokes.
    required: false
    default: none
    type: dict
    aliases:
      - kwarg
      - args
      - arg
  path:
    description:
      - The directory containing the YAML table/view definition file as
        specified by the I(file) option. The default value is the C(op)
        directory in C(jnpr.junos.op). This is the directory containing the
        table/view definitions which are included in the PyEZ distribution.
    required: false
    default: C(op) directory in C(jnpr.junos.op)
    type: path
    aliases:
      - directory
      - dir
  response_type:
    description:
      - Defines the format of data returned by the module. See RETURN.
        The value of the I(resource) key in the module's response is either
        a list of dictionaries C(list_of_dicts) or PyEZ's native return
        format C(juniper_items). Because Ansible module's may only return JSON
        data, PyEZ's native return format C(juniper_items) is translated into
        a list of lists.
    required: false
    default: list_of_dicts
    choices:
      - list_of_dicts
      - juniper_items
    type: str
  table:
    description:
      - Name of the PyEZ table used to retrieve data. If not specified,
        defaults to the name of the table defined in the I(file) option. Any
        table names in I(file) which begin with C(_) are ignored. If more than
        one table is defined in I(file), the module fails with an error
        message. In this case, you must manually specify the name of the table
        by setting this option.
    required: false
    default: The name of the table defined in the I(file) option.
    type: str
notes:
  - This module only works with operational tables/views; it does not work with
    configuration tables/views.
'''

EXAMPLES = '''
---
- name: Retrieve data from a Junos device using a PyEZ table/view.
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: Retrieve LLDP Neighbor Information Using PyEZ-included Table
      juniper_junos_table:
        file: "lldp.yml"
      register: response
    - name: Print response
      debug:
        var: response

    - name: Retrieve routes within 10.0.0/8
      juniper_junos_table:
        file: "routes.yml"
        table: "RouteTable"
        kwargs:
          destination: "10.0.0.0/8"
        response_type: "juniper_items"
      register: response
    - name: Print response
      debug:
        var: response

    - name: Retrieve from custom table in playbook directory
      juniper_junos_table:
        file: "fpc.yaml"
        path: "."
      register: response
    - name: Print response
      debug:
        var: response
'''

RETURN = '''
changed:
  description: 
    - Indicates if the device's configuration has changed. Since this
      module does not change the operational or configuration state of the
      device, the value is always set to C(false).
  returned: success
  type: bool
failed:
  description:
    - Indicates if the task failed.
  returned: always
  type: bool
msg:
  description:
    - A human-readable message indicating a summary of the result.
  returned: always
  type: str
resource:
  description:
    - The items retrieved by the table/view.
  returned: success
  type: list of dicts if I(response_type) is C(list_of_dicts) or list of
        lists if I(respsonse_type) is C(juniper_items).
  sample: |
    # when response_type == 'list_of_dicts'
    [
      {
         "local_int": "ge-0/0/3", 
         "local_parent": "-", 
         "remote_chassis_id": "00:05:86:08:d4:c0", 
         "remote_port_desc": null, 
         "remote_port_id": "ge-0/0/0", 
         "remote_sysname": "r5", 
         "remote_type": "Mac address"
      }, 
      {
         "local_int": "ge-0/0/0", 
         "local_parent": "-", 
         "remote_chassis_id": "00:05:86:18:f3:c0", 
         "remote_port_desc": null, 
         "remote_port_id": "ge-0/0/2", 
         "remote_sysname": "r4", 
         "remote_type": "Mac address"
      }
    ]
    # when response_type == 'juniper_items'
    [
      [
        "ge-0/0/3", 
        [
          [
            "local_parent", 
            "-"
          ], 
          [
            "remote_port_id", 
            "ge-0/0/0"
          ], 
          [
            "remote_chassis_id", 
            "00:05:86:08:d4:c0"
          ], 
          [
            "remote_port_desc", 
            null
          ], 
          [
            "remote_type", 
            "Mac address"
          ], 
          [
            "local_int", 
            "ge-0/0/3"
          ], 
          [
            "remote_sysname", 
            "r5"
          ]
        ]
      ], 
      [
        "ge-0/0/0", 
        [
          [
            "local_parent", 
            "-"
          ], 
          [
            "remote_port_id", 
            "ge-0/0/2"
          ], 
          [
            "remote_chassis_id", 
            "00:05:86:18:f3:c0"
          ], 
          [
            "remote_port_desc", 
            null
          ], 
          [
            "remote_type", 
            "Mac address"
          ], 
          [
            "local_int", 
            "ge-0/0/0"
          ], 
          [
            "remote_sysname", 
            "r4"
          ]
        ]
      ]
    ]
'''

# Standard library imports
import os.path

# Constants
RESPONSE_CHOICES = ['list_of_dicts', 'juniper_items']


"""From Ansible 2.1, Ansible uses Ansiballz framework for assembling modules
But custom module_utils directory is supported from Ansible 2.3
Reference for the issue: https://groups.google.com/forum/#!topic/ansible-project/J8FL7Z1J1Mw """

# Ansiballz packages module_utils into ansible.module_utils
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import juniper_junos_common


def expand_items(module, data):
    """Recursively expand any table items
    """
    resources = []
    # data.items() is a list of tuples
    for table_key, table_fields in data.items():
        # sample:
        # ('fxp0', [('neighbor_interface', '1'), ('local_interface', 'fxp0'),
        # ('neighbor', 'vmx2')]
        # table_key - element 0 is the key from the Table - not using at all
        # table_fields - element 1 is also a list of tuples
        temp = []
        for key, value in table_fields:
            # calling it normalized value because YOU/WE created the keys
            if value and isinstance(value, module.pyez_factory_table.Table):
                value = expand_items(module, value)
            temp.append((key, value))
        resources.append((table_key, temp))
    return resources


def juniper_items_to_list_of_dicts(module, data):
    """Recursively convert Juniper PyEZ Table/View items to list of dicts.
    """
    resources = []
    # data.items() is a list of tuples
    for table_key, table_fields in data.items():
        # sample:
        # ('fxp0', [('neighbor_interface', '1'), ('local_interface', 'fxp0'),
        # ('neighbor', 'vmx2')]
        # table_key - element 0 is the key from the Table - not using at all
        # table_fields - element 1 is also a list of tuples
        temp = {}
        for key, value in table_fields:
            if (value and isinstance(value, module.pyez_factory_table.Table)):
                value = juniper_items_to_list_of_dicts(module, value)
            temp[key] = value
        resources.append(temp)
    return resources


def main():
    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            file=dict(type='path',
                      required=True,
                      default=None),
            table=dict(type='str',
                       required=False,
                       default=None),
            path=dict(type='path',
                      required=False,
                      aliases=['directory', 'dir'],
                      default=None),
            kwargs=dict(required=False,
                        aliases=['kwarg', 'args', 'arg'],
                        type='dict',
                        default=None),
            response_type=dict(choices=RESPONSE_CHOICES,
                               type='str',
                               required=False,
                               default='list_of_dicts'),
        ),
        # Check mode is implemented.
        supports_check_mode=True,
        min_yaml_version=juniper_junos_common.MIN_YAML_VERSION,
    )

    # Straight from params
    file = junos_module.params.get('file')
    table = junos_module.params.get('table')
    path = junos_module.params.get('path')
    kwargs = junos_module.params.get('kwargs')
    response_type = junos_module.params.get('response_type')

    if not file.endswith('.yml') and not file.endswith('.yaml'):
        junos_module.fail_json(msg='The value of the file option must end '
                                   'with the .yml or .yaml extension')

    # If needed, get the default path
    if path is None:
        path = os.path.dirname(
                   os.path.abspath(junos_module.pyez_op_table.__file__))

    # file_name is path + file
    file_name = os.path.join(path, file)

    junos_module.logger.debug("Attempting to open: %s.", file_name)
    try:
        with open(file_name, 'r') as fp:
            try:
                junos_module.logger.debug("Attempting to parse YAML from : "
                                          "%s.", file_name)
                table_view = junos_module.yaml.load(fp)
                junos_module.logger.debug("YAML from %s successfully parsed.",
                                          file_name)
            except junos_module.yaml.YAMLError as ex:
                junos_module.fail_json(msg='Failed parsing YAML file %s. '
                                           'Error: %s' % (file_name, str(ex)))
    except IOError:
        junos_module.fail_json(msg='The file name %s could not be opened for'
                                   'reading.' % (file_name))
    junos_module.logger.debug("%s successfully read.", file_name)

    # Initialize the results. Assume failure until we know it's success.
    results = {'msg': '',
               'changed': False,
               'failed': True}

    # Default to the table defined in file_name.
    # Ignore table names which begin with an underscore.
    if table is None:
        for key in table_view:
            if not key.startswith('_') and 'Table' in key:
                if table is not None:
                    junos_module.fail_json(
                        msg='The file name %s contains multiple table '
                            'definitions. Specify the desired table with the '
                            'table option.' % (file_name))
                table = key

    if table is None:
        junos_module.fail_json(
            msg='No table definition was found in the %s file. Specify a '
                'value for the file option which contains a valid table/view '
                'definition.' % (file_name))
    junos_module.logger.debug("Table: %s", table)

    try:
        loader = \
            junos_module.pyez_factory_loader.FactoryLoader().load(table_view)
        junos_module.logger.debug("Loader created successfully.")
    except Exception as ex:
        junos_module.fail_json(msg='Unable to create a table loader from the '
                                   '%s file. Error: %s' % (file_name, str(ex)))
    try:
        data = loader[table](junos_module.dev)
        junos_module.logger.debug("Table %s created successfully.", table)
        if kwargs is None:
            data.get()
        else:
            data.get(**kwargs)
        junos_module.logger.debug("Data retrieved from %s successfully.",
                                  table)
    except KeyError:
        junos_module.fail_json(msg='Unable to find table %s in the '
                                   '%s file.' % (table, file_name))
    except (junos_module.pyez_exception.ConnectError,
            junos_module.pyez_exception.RpcError) as ex:
        junos_module.fail_json(msg='Unable to retrieve data from table %s. '
                                   'Error: %s' % (table, str(ex)))

    if data is not None:
        try:
            len_data = len(data)
        except Exception as ex:
            junos_module.fail_json(msg='Unable to parse table %s data into '
                                       'items. Error: %s' % (table, str(ex)))
        junos_module.logger.debug('Successfully retrieved %d items from %s.',
                                  len_data, table)
        results['msg'] = 'Successfully retrieved %d items from %s.' % \
                         (len_data, table)

    if response_type == 'list_of_dicts':
        junos_module.logger.debug('Converting data to list of dicts.')
        resource = juniper_items_to_list_of_dicts(junos_module, data)
    else:
        resource = expand_items(junos_module, data)

    # If we made it this far, everything was successful.
    results['failed'] = False
    results['resource'] = resource

    # Return response.
    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
