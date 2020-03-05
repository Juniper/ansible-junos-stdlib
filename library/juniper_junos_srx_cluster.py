#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2014, Patrik Bok
#               2015, Rick Sherman
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
module: juniper_junos_srx_cluster
version_added: "2.0.0" # of Juniper.junos role
author: "Juniper Networks - Stacy Smith (@stacywsmith)"
short_description: Add or remove SRX chassis cluster configuration
description:
  - Add an SRX chassis cluster configuration and reboot the device. Assuming
    the device is capable of forming an SRX cluster and has the correct
    cables connected, this will form an SRX cluster.
  - If an SRX chassis cluster is already present, setting I(cluster_enable) to
    C(false) will remove the SRX chassis cluster configuration and reboot
    the device causing the SRX cluster to be broken and the device to return
    to stand-alone mode.
options:
  enable:
    description:
      - Enable or disable cluster mode. When C(true) cluster mode is enabled
        and I(cluster_id) and I(node_id) must also be specified. When C(false)
        cluster mode is disabled and the device returns to stand-alone mode.
    required: true
    default: none
    type: bool
    aliases:
      - cluster_enable
  cluster_id:
    description:
      - The cluster ID to configure.
      - Required when I(enable) is C(true).
    required: false
    default: none
    type: int
    aliases:
      - cluster
  node_id:
    description:
      - The node ID to configure. (C(0) or C(1))
      - Required when I(enable) is C(true).
    required: false
    default: none
    type: int
    aliases:
      - node
'''

EXAMPLES = '''
---
- name: Manipulate the SRX cluster configuration of Junos SRX devices
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos
  tasks:
    - name: Enable an SRX cluster
      juniper_junos_srx_cluster:
        enable: true
        cluster_id: 4
        node_id: 0
      register: response
    - name: Print the response.
      debug:
        var: response.config_lines

    - name: Disable an SRX cluster
      juniper_junos_srx_cluster:
        enable: false
      register: response
    - name: Print the response.
      debug:
        var: response.config_lines
'''

RETURN = '''
changed:
  description:
    - Indicates if the device's configuration has changed, or would have
      changed when in check mode.
  returned: success
  type: bool
failed:
  description:
    - Indicates if the task failed.
  returned: always
  type: bool
msg:
  description:
    - A human-readable message indicating the result.
  returned: always
  type: str
reboot:
  description:
    - Indicates if a reboot of the device has been initiated.
  returned: success
  type: bool
'''

# Standard library imports


"""From Ansible 2.1, Ansible uses Ansiballz framework for assembling modules
But custom module_utils directory is supported from Ansible 2.3
Reference for the issue: https://groups.google.com/forum/#!topic/ansible-project/J8FL7Z1J1Mw """

# Ansiballz packages module_utils into ansible.module_utils
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import juniper_junos_common


def main():
    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            enable=dict(type='bool',
                        required=True,
                        aliases=['cluster_enable'],
                        default=None),
            cluster_id=dict(type='int',
                            required=False,
                            aliases=['cluster'],
                            default=None),
            node_id=dict(type='int',
                         required=False,
                         aliases=['node'],
                         default=None)
        ),
        # Required if options
        # If enable is True, then cluster_id and node_id must be set.
        required_if=[['enable', True, ['cluster_id', 'node_id']]],
        # Check mode is implemented.
        supports_check_mode=True
    )
    # Do additional argument verification.

    # Straight from params
    enable = junos_module.params.get('enable')
    cluster_id = junos_module.params.get('cluster_id')
    node_id = junos_module.params.get('node_id')

    # cluster_id must be between 0 and 255
    if cluster_id is not None:
        if cluster_id < 0 or cluster_id > 255:
            junos_module.fail_json(msg="The cluster_id option (%s) must have "
                                       "an integer value between 0 and 255." %
                                       (cluster_id))

    # node_id must be between 0 and 1
    if node_id is not None:
        if node_id < 0 or node_id > 1:
            junos_module.fail_json(msg="The node_id option (%s) must have a "
                                       "value of 0 or 1." % (node_id))

    # Initialize the results. Assume failure until we know it's success.
    results = {'msg': '',
               'changed': False,
               'reboot': False,
               'failed': True}

    junos_module.logger.debug("Check current SRX cluster operational state.")
    current_cluster_state = junos_module.dev.facts['srx_cluster']
    current_cluster_id = junos_module.dev.facts['srx_cluster_id']
    if current_cluster_id is not None:
        current_cluster_id = int(current_cluster_id)
    current_node_name = junos_module.dev.re_name
    current_node_id = None
    if current_node_name is not None:
        (_, _, current_node_id) = current_node_name.partition('node')
        if current_node_id:
            current_node_id = int(current_node_id)
    junos_module.logger.debug(
        "Current SRX cluster operational state: %s, cluster_id: %s, "
        "node_id: %s",
        'enabled' if current_cluster_state else 'disabled',
        str(current_cluster_id),
        str(current_node_id))

    # Is a state change needed?
    if current_cluster_state != enable:
        junos_module.logger.debug(
            "SRX cluster configuration change needed. Current state: %s. "
            "Desired state: %s",
            'enabled' if current_cluster_state else 'disabled',
            'enabled' if enable else 'disabled')
        results['changed'] = True

    # Is a cluster ID change needed?
    if (enable is True and current_cluster_id is not None and
       current_cluster_id != cluster_id):
        junos_module.logger.debug(
            "SRX cluster ID change needed. Current cluster ID: %d. "
            "Desired cluster ID: %d",
            current_cluster_id, cluster_id)
        results['changed'] = True

    # Is a node ID change needed?
    if (enable is True and current_node_id is not None and
       current_node_id != node_id):
        junos_module.logger.debug(
            "SRX node ID change needed. Current node ID: %d. "
            "Desired cluster ID: %d",
            current_node_id, node_id)
        results['changed'] = True

    results['msg'] = 'Current state: %s, cluster_id: %s, node_id: %s' % \
                     ('enabled' if current_cluster_state else 'disabled',
                      str(current_cluster_id),
                      str(current_node_id))

    if results['changed'] is True:
        results['msg'] += ' Desired state:  %s, cluster_id: %s, ' \
                          'node_id: %s' % \
                          ('enabled' if enable else 'disabled',
                           str(cluster_id),
                           str(node_id))

        if not junos_module.check_mode:
            results['msg'] += ' Initiating change.'
            try:
                output = None
                if enable is True:
                    resp = junos_module.dev.rpc.set_chassis_cluster_enable(
                        cluster_id=str(cluster_id), node=str(node_id),
                        reboot=True, normalize=True
                    )
                else:
                    resp = junos_module.dev.rpc.set_chassis_cluster_disable(
                        reboot=True, normalize=True
                    )
                if resp is not None:
                    output = resp.getparent().findtext('.//output')
                    if output is None:
                        output = resp.getparent().findtext('.//message')
                results['msg'] += ' Reboot initiated. Response: %s' % (output)
                results['reboot'] = True
            except (junos_module.pyez_exception.ConnectError,
                    junos_module.pyez_exception.RpcError) as ex:
                junos_module.logger.debug('Error: %s', str(ex))
                results['msg'] += ' Error: %s' % (str(ex))
                junos_module.fail_json(**results)

    # If we made it this far, everything was successful.
    results['failed'] = False

    # Return response.
    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
