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
module: juniper_junos_system
version_added: "2.0.0" # of Juniper.junos role
author: "Juniper Networks - Stacy Smith (@stacywsmith)"
short_description: Initiate operational actions on the Junos system
description:
  - Initiate an operational action (shutdown, reboot, halt or zeroize) on a
    Junos system. The particular action to execute is defined by the mandatory
    I(action) option.
options:
  action:
    description:
      - The action performed by the module.
      - >
        The following actions are supported:
      - B(shutdown) - Power off the Junos devices. The values C(off),
        C(power-off), and C(power_off) are aliases for this value.
        This is the equivalent of the C(request system power-off) CLI
        command.
      - B(halt) - Stop the Junos OS running on the RE, but do not power off
        the system. Once the system is halted, it will reboot if a
        keystroke is entered on the console. This is the equivalent
        of the C(request system halt) CLI command.
      - B(reboot) - Reboot the system. This is the equivalent of the
        C(request system reboot) CLI command.
      - B(zeroize) - Restore the system (configuration, log files, etc.) to a
        factory default state. This is the equivalent of the
        C(request system zeroize) CLI command.
    required: true
    default: none
    type: str
    choices:
      - shutdown
      - halt
      - reboot
      - zeroize
      - 'off'
      - power-off
      - power_off
  at:
    description:
      - The time at which to shutdown, halt, or reboot the system. 
      - >
        The value may be specified in one of the following ways:
      - B(now) - The action takes effect immediately.
      - B(+minutes) — The action takes effect in C(minutes) minutes from now.
      - B(yymmddhhmm) — The action takes effect at C(yymmddhhmm) absolute
        time, specified as year, month, day, hour, and minute.
      - B(hh:mm) — The action takes effect at C(hh:mm) absolute time on the
        current day, specified in 24-hour time.
      - The I(at) option can not be used when the I(action) option has a
        value of C(zeroize). The I(at) option is mutually exclusive with the
        I(in_min) option.
    required: false
    default: none
    type: str
  in_min:
    description:
      - Specify a delay, in minutes, before the shutdown, halt, or reboot.
      - The I(in_min) option can not be used when the I(action) option has a
        value of C(zeroize). The I(in_min) option is mutually exclusive with
        the I(at) option.
    required: false
    default: none
    type: int
  all_re:
    description:
      - If the system has multiple Routing Engines and this option is C(true),
        then the action is performed on all REs in the system. If the system
        does not have multiple Routing Engines, then this option has no effect.
      - This option applies to all I(action) values.
      - The I(all_re) option is mutually exclusive with the I(other_re) option.
    required: false
    default: true
    type: bool
  other_re:
    description:
      - If the system has dual Routing Engines and this option is C(true),
        then the action is performed on the other REs in the system. If the
        system does not have dual Routing Engines, then this option has no
        effect.
      - The I(other_re) option can not be used when the I(action) option has a
        value of C(zeroize).
      - The I(other_re) option is mutually exclusive with the I(all_re) option.
    required: false
    default: false
    type: bool
  media:
    description:
      - Overwrite media when performing the zeroize operation. This option is
        only valid when the I(action) option has a value of C(zeroize).
    required: false
    default: false
    type: bool
notes:
  - This module only B(INITIATES) the action. It does B(NOT) wait for the
    action to complete.
  - Some Junos devices are effected by a Junos defect which causes this Ansible
    module to hang indefinitely when connected to the Junos device via
    the console. This problem is not seen when connecting to the Junos device
    using the normal NETCONF over SSH transport connection. Therefore, it is
    recommended to use this module only with a NETCONF over SSH transport
    connection. However, this module does still permit connecting to Junos
    devices via the console port and this functionality may still be used for
    Junos devices running Junos versions less than 15.1.
'''

EXAMPLES = '''
---
- name: Examples of juniper_junos_system
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: Reboot all REs of the device
      juniper_junos_system:
        action: "reboot"

    - name: Power off the other RE of the device.
      juniper_junos_system:
        action: "shutdown"
        othe_re: True

    - name: Reboot this RE at 8pm today.
      juniper_junos_system:
        action: "reboot"
        all_re: False
        at: "20:00"

    - name: Halt the system on 25 January 2018 at 4pm.
      juniper_junos_system:
        action: "halt"
        at: "1801251600"

    - name: Reboot the system in 30 minutes.
      juniper_junos_system:
        action: "reboot"
        in_min: 30

    - name: Reboot the system in 30 minutes.
      juniper_junos_system:
        action: "reboot"
        at: "+30m"

    - name: Zeroize the local RE only.
      juniper_junos_system:
        action: "zeroize"
        all_re: False

    - name: Zeroize all REs and overwrite medea.
      juniper_junos_system:
        action: "zeroize"
        media: True
'''

RETURN = '''
action:
  description:
    - The value of the I(action) option.
  returned: always
  type: str
all_re:
  description:
    - The value of the I(all_re) option.
  returned: always
  type: str
changed:
  description:
    - Indicates if the device's state has changed. If the action is performed
      (or if it would have been performed when in check mode) then the value
      will be C(true). If there was an error before the action, then the value
      will be C(false).
  returned: always
  type: bool
failed:
  description:
    - Indicates if the task failed.
  returned: always
  type: bool
media:
  description:
    - The value of the I(media) option.
  returned: always
  type: str
msg:
  description:
    - A human-readable message indicating the result.
  returned: always
  type: str
other_re:
  description:
    - The value of the I(other_re) option.
  returned: always
  type: str
'''


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
            action=dict(type='str',
                        required=True,
                        choices=['shutdown', 'off', 'power-off', 'power_off',
                                 'halt', 'reboot', 'zeroize'],
                        default=None),
            at=dict(type='str',
                    required=False,
                    default=None),
            in_min=dict(type='int',
                        required=False,
                        aliases=['in'],
                        default=None),
            all_re=dict(type='bool',
                        required=False,
                        default=True),
            other_re=dict(type='bool',
                          required=False,
                          default=False),
            media=dict(type='bool',
                       required=False,
                       default=False),
        ),
        mutually_exclusive=[['at', 'in_min'], ['all_re', 'other_re']],
        supports_check_mode=True
    )

    # We're going to be using params a lot
    params = junos_module.params

    action = params['action']
    # Synonymns for shutdown
    if action == 'off' or action == 'power_off' or action == 'power-off':
        action = 'shutdown'

    # at option only applies to reboot, shutdown, or halt actions.
    if (params.get('at') is not None and
       action != 'reboot' and
       action != 'shutdown' and
       action != 'halt'):
        junos_module.fail_json(msg='The at option can only be used when '
                                   'the action option has the value "reboot", '
                                   '"shutdown", or "halt".')

    # in_min option only applies to reboot, shutdown, or halt actions.
    if (params.get('in_min') is not None and
       action != 'reboot' and
       action != 'shutdown' and
       action != 'halt'):
        junos_module.fail_json(msg='The in_min option can only be used when '
                                   'the action option has the value "reboot", '
                                   '"shutdown", or "halt".')

    # other_re option only applies to reboot, shutdown, or halt actions.
    if (params.get('other_re') is True and
       action != 'reboot' and
       action != 'shutdown' and
       action != 'halt'):
        junos_module.fail_json(msg='The other_re option can only be used when '
                                   'the action option has the value "reboot", '
                                   '"shutdown", or "halt".')

    # media option only applies to zeroize action.
    if params['media'] is True and action != 'zeroize':
        junos_module.fail_json(msg='The media option can only be used when '
                                   'the action option has the value '
                                   '"zeroize".')

    # If other_re, then we should turn off all_re
    if params['other_re'] is True:
        params['all_re'] = False

    # Set initial results values. Assume failure until we know it's success.
    # Assume we haven't changed the state until we do.
    results = {'changed': False,
               'msg': '',
               'reboot': bool(action == 'reboot'),
               'action': action,
               'all_re': params.get('all_re'),
               'other_re': params.get('other_re'),
               'media': params.get('media'),
               'failed': True}

    # Map the action to an RPC.
    rpc = None
    xpath_list = []
    if action == 'reboot':
        if junos_module.dev.facts['_is_linux']:
            rpc = junos_module.etree.Element('request-shutdown-reboot')
        else:
            rpc = junos_module.etree.Element('request-reboot')
        xpath_list.append('.//request-reboot-status')
    elif action == 'shutdown':
        if junos_module.dev.facts['_is_linux']:
            rpc = junos_module.etree.Element('request-shutdown-power-off')
        else:
            rpc = junos_module.etree.Element('request-power-off')
        xpath_list.append('.//request-reboot-status')
    elif action == 'halt':
        if junos_module.dev.facts['_is_linux']:
            rpc = junos_module.etree.Element('request-shutdown-halt')
        else:
            rpc = junos_module.etree.Element('request-halt')
        xpath_list.append('.//request-reboot-status')
    elif action == 'zeroize':
        rpc = junos_module.etree.Element('request-system-zeroize')
    else:
        results['msg'] = 'No RPC found for the %s action.' % (action)
        junos_module.fail_json(**results)

    # Add the arguments
    if action == 'zeroize':
        if params['all_re'] is False:
            if junos_module.dev.facts['2RE']:
                junos_module.etree.SubElement(rpc, 'local')
        if params['media'] is True:
            junos_module.etree.SubElement(rpc, 'media')
    else:
        if params['in_min'] is not None:
            junos_module.etree.SubElement(rpc,
                                          'in').text = str(params['in_min'])
        elif params['at'] is not None:
            junos_module.etree.SubElement(rpc,
                                          'at').text = params['at']
        if params['other_re'] is True:
            if junos_module.dev.facts['2RE']:
                junos_module.etree.SubElement(rpc, 'other-routing-engine')
                # At least on some platforms stopping/rebooting the other RE
                # just produces <output> messages.
                xpath_list.append('..//output')
        elif params['all_re'] is True:
            junos_module.add_sw()
            if (junos_module.sw._multi_RE is True and
               junos_module.sw._multi_VC is False):
                junos_module.etree.SubElement(rpc, 'both-routing-engines')
                # At least on some platforms stopping/rebooting both REs
                # produces <output> messages and <request-reboot-status>
                # messages.
                xpath_list.append('..//output')
            elif junos_module.sw._mixed_VC is True:
                junos_module.etree.SubElement(rpc, 'all-members')

    # OK, we're ready to do something. Set changed and log the RPC.
    results['changed'] = True
    junos_module.logger.debug("Ready to execute RPC: %s",
                              junos_module.etree.tostring(rpc,
                                                          pretty_print=True))

    if not junos_module.check_mode:
        if action != 'zeroize':
            # If we're going to do a shutdown, reboot, or halt right away then
            # try to deal with the fact that we might not get the closing
            # </rpc-reply> and therefore might get an RpcTimeout.
            # (This is a known Junos bug.) Set the timeout low so this happens
            # relatively quickly.
            if (params['at'] == 'now' or params['in_min'] == 0 or
               (params['at'] is None and params['in_min'] is None)):
                if junos_module.dev.timeout > 5:
                    junos_module.logger.debug("Decreasing device RPC timeout "
                                              "to 5 seconds.")
                    junos_module.dev.timeout = 5

        # Execute the RPC.
        try:
            junos_module.logger.debug(
                "Executing RPC: %s",
                junos_module.etree.tostring(rpc, pretty_print=True))
            resp = junos_module.dev.rpc(rpc,
                                        ignore_warning=True,
                                        normalize=True)
            junos_module.logger.debug("RPC executed cleanly.")
            if len(xpath_list) > 0:
                for xpath in xpath_list:
                    if junos_module.dev.facts['_is_linux']:
                        got = resp.text
                    else:
                        got = resp.findtext(xpath)
                    if got is not None:
                        results['msg'] = '%s successfully initiated.' % \
                                         (action)
                        results['failed'] = False
                        break
                else:
                    # This is the else clause of the for loop.
                    # It only gets executed if the loop finished without
                    # hitting the break.
                    results['msg'] = 'Did not find expected RPC response.'
                    results['changed'] = False
            else:
                results['msg'] = '%s successfully initiated.' % (action)
                results['failed'] = False
        except (junos_module.pyez_exception.RpcTimeoutError) as ex:
            # This might be OK. It might just indicate the device didn't
            # send the closing </rpc-reply> (known Junos bug).
            # Try to close the device. If it closes cleanly, then it was
            # still reachable, which probably indicates there was a problem.
            try:
                junos_module.close(raise_exceptions=True)
                # This means the device wasn't already disconnected.
                results['changed'] = False
                results['msg'] = '%s failed. %s may not have been ' \
                                 'initiated.' % (action, action)
            except (junos_module.pyez_exception.RpcError,
                    junos_module.pyez_exception.ConnectError):
                # This is expected. The device has already disconnected.
                results['msg'] = '%s succeeded.' % (action)
                results['failed'] = False
        except (junos_module.pyez_exception.RpcError,
                junos_module.pyez_exception.ConnectError) as ex:
            results['changed'] = False
            results['msg'] = '%s failed. Error: %s' % (action, str(ex))

    # Return results.
    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
