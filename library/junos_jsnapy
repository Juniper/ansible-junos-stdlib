#!/usr/bin/env python

#Copyright (c) 1999-2015, Juniper Networks Inc.
#               2016, Roslan Zaki
#
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

DOCUMENTATION = '''
---
module: junos_jsnapy
author: Roslan Zaki & Damien Garros, Juniper Networks
version_added: "1.4.0"
version_control:
    13-Apr-2016     v1.0.0      - Basic working model

Short_description: Integrate JSNAPy to ansible.
description:
    - Execute JSNAPy test from Ansible.
      Attention, to not break Ansible behavior, this module only report "failed"
      if the module itself fails, not if a test fails.
      To check the test results you need to subscribe to the result and assert
      the returned value.
      An experimental Callback_Plugin for junos_jsnapy is available to provide
      additional information about tests that failed.
      To enable it, you need to add "callback_whitelist = jsnapy" in your ansible
      configuration file.
requirements:
    - junos-eznc >= 1.2.2
options:
    host:
        description:
            - Set to {{ inventory_hostname }}
        required: true
    user:
        description:
            - Login username
        required: false
        default: $USER
    passwd:
        description:
            - Login password
        required: false
        default: assumes ssh-key active
    port:
        description:
            - port number to use when connecting to the device
        required: false
        default: 830
    ssh_private_key_file:
        description:
            - This can be used if you need to provide a private key rather than
              loading the key into the ssh-key-ring/environment.  if your
              ssh-key requires a password, then you must provide it via
              **passwd**
        required: false
        default: None
    mode:
        description:
            - mode of console connection (telnet/serial). If mode is not
              provided SSH connection is used.
        required: false
        default: None
    logfile:
        description:
            - Path on the local server where the progress status is logged
              for debugging purposes
        required: false
        default: None
    dir:
        description:
            - Path for the JSNAPy yaml testfiles/configuration file
        required: false
        default: '/etc/jsnapy/testfiles'
    action:
        description:
            Possible actions available
            - jsnapcheck
            - check
            - snap_pre
            - snap_post
        required: false
        default: None
    test_files:
        description:
            - Test files which need to executed
        required: False
        type: list
        default: None
    config_file:
        description:
            - The YAML configuration file for the JSNAPy tests
        required: false
        default: None
'''

EXAMPLES = '''
   - name: JUNOS Post Checklist
     junos_jsnapy:
       host: "{{ inventory_hostname}}"
       passwd: "{{ tm1_password }}"
       action: "snap_post"
       config_file: "first_test.yml"
       logfile: "migration_post.log"
     register: test1

   - name: Check JSNAPy tests results
     assert:
     that:
       - "test1.passPercentage == 100"

   - name: Debug jsnapy
     debug: msg=test1

---------
   - name: Test based on a test_file directly
     junos_jsnapy:
       host: "{{ junos_host }}"
       port: "{{ netconf_port }}"
       user: "{{ ansible_ssh_user }}"
       passwd: "{{ ansible_ssh_pass }}"
       test_files: tests/test_junos_interface.yaml
       action: snapcheck
     register: test1

   - name: Check JSNAPy tests results
     assert:
     that:
       - "test1.passPercentage == 100"
---------
   - name: "Collect Pre Snapshot"
    junos_jsnapy:
      host: "{{ junos_host }}"
      port: "{{ netconf_port }}"
      user: "{{ ansible_ssh_user }}"
      passwd: "{{ ansible_ssh_pass }}"
      test_files: tests/test_loopback.yml
      action: snap_pre
    register: test_pre

---------
  - name: "Collect Post Snapshot"
    junos_jsnapy:
      host: "{{ junos_host }}"
      port: "{{ netconf_port }}"
      user: "{{ ansible_ssh_user }}"
      passwd: "{{ ansible_ssh_pass }}"
      test_files: tests/test_loopback.yml
      action: snap_post
    register: test_post

---------
  - name: "Check after PRE - POST check"
    junos_jsnapy:
      host: "{{ junos_host }}"
      port: "{{ netconf_port }}"
      user: "{{ ansible_ssh_user }}"
      passwd: "{{ ansible_ssh_pass }}"
      test_files: tests/test_loopback.yml
      action: check
    register: test_check

    - name: Check Results
      assert:
        that:
          - test_check|succeeded
          - test_check.passPercentage == 100

'''
from distutils.version import LooseVersion
import logging
from lxml.builder import E
import os.path
import os
import time

import_err_message = None

try:
    from jnpr.junos import Device
    from jnpr.junos.version import VERSION
    from jnpr.junos.exception import RpcError
    from jnpr.jsnapy import SnapAdmin
    if not LooseVersion(VERSION) >= LooseVersion('1.2.2'):
        import_err_message = 'junos-eznc >= 1.2.2 is required for this module'
except ImportError as ex:
    import_err_message = 'ImportError: %s' % ex.message

def jsnap_selection(dev, module):

    args = module.params
    action = args['action']
    config_file = args.get('config_file')
    if config_file:
        config_dir = args['dir']
        config_data = config_file
        # in case config file given is not full path
        if not os.path.isfile(config_file):
            config_data = os.path.join(config_dir, config_file)
            if not os.path.isfile(config_data):
                msg = 'unable to find the config file {0} (test directory:{1})'.format(config_file,args['dir'])
                logging.error(msg)
                module.fail_json(msg=msg)

    else:
        test_files = args.get('test_files')

        test_files_validated = []
        ## Check if file is present without and with dir
        for test_file in test_files:
            if not os.path.isfile(test_file):
                test_file_full = os.path.join(args['dir'], test_file)
                if not os.path.isfile(test_file_full):
                    msg = 'unable to find the test file {0} (test directory:{1})'.format(test_file,args['dir'])
                    logging.error(msg)
                    module.fail_json(msg=msg)
                else:
                    test_files_validated.append(test_file_full)
            else:
                test_files_validated.append(test_file)

        ## Check that we have at least one test file
        if len(test_files_validated) == 0:
            msg = 'The list of test file is empty, please check your input'
            logging.error(msg)
            module.fail_json(msg=msg)

        config_data = {'tests': test_files_validated}

    results = {'action': action}
    js = SnapAdmin()

    if action == 'snapcheck':
        snapValue = js.snapcheck(data=config_data, dev=dev)
    elif action == 'snap_pre':
        snapValue = js.snap(data=config_data, dev=dev, file_name='PRE')
    elif action == 'snap_post':
        snapValue = js.snap(data=config_data, dev=dev, file_name='POST')
    elif action == 'check':
        snapValue = js.check(data=config_data, dev=dev, pre_file='PRE', post_file='POST')

    percentagePassed = 0
    if isinstance(snapValue, (list)):
        if action in ['snapcheck', 'check']:
            for snapCheck in snapValue:
                router = snapCheck.device
                results['router'] = router
                results['final_result'] = snapCheck.result
                results['total_passed'] = snapCheck.no_passed
                results['total_failed'] = snapCheck.no_failed
                results['test_results'] = snapCheck.test_results
                total_test = int(snapCheck.no_passed) + int(snapCheck.no_failed)
                results['total_tests'] = total_test
            if total_test != 0:
                percentagePassed = (int(results['total_passed']) * 100 ) / (results['total_tests'])
            results['passPercentage'] = percentagePassed
        elif action in ['snap_pre', 'snap_post']:
            results['changed'] = True
    return results

def main():

    module = AnsibleModule(
        argument_spec=dict(host=dict(required=True, default=None),  # host or ipaddr
                           user=dict(required=False, default=os.getenv('USER')),
                           passwd=dict(required=False, default=None, no_log=True),
                           port=dict(required=False, default=830),
                           ssh_private_key_file=dict(required=False, default=None),
                           mode=dict(required=False, default=None),
                           logfile=dict(required=False, default=None),
                           test_files=dict(required=False, type='list', default=None),
                           config_file=dict(required=False, default=None),
                           dir=dict(required=False, default='/etc/jsnapy/testfiles'),
                           action=dict(required=True, choices=['check', 'snapcheck', 'snap_pre', 'snap_post'], default=None)
                           ),
        mutually_exclusive=[['test_files', 'config_file']],
        required_one_of=[['test_files', 'config_file']],
        supports_check_mode=False)

    args = module.params
    results = {}

    if import_err_message is not None:
        module.fail_json(msg=import_err_message)

    if args['mode'] is not None and LooseVersion(VERSION) < LooseVersion('2.0.0'):
        module.fail_json(msg='junos-eznc >= 2.0.0 is required for console connection.')

    logfile = args['logfile']
    if logfile is not None:
        logging.basicConfig(filename=logfile, level=logging.INFO,
                            format='%(asctime)s:%(name)s:%(message)s')
        logging.getLogger().name = 'JSNAPy:' + args['host']

    logging.info("connecting to host: {0}@{1}:{2}".format(args['user'], args['host'], args['port']))

    try:
        dev = Device(args['host'], user=args['user'], password=args['passwd'],
                     port=args['port'], ssh_private_key_file=args['ssh_private_key_file'],
                     mode=args['mode'], gather_facts=False).open()
    except Exception as err:
        msg = 'unable to connect to {0}: {1}'.format(args['host'], str(err))
        logging.error(msg)
        module.fail_json(msg=msg)
        # --- UNREACHABLE ---

    try:
        logging.info("Main program: ")
        data = jsnap_selection(dev, module)

        if data['action'] in ['check', 'snapcheck'] and data['final_result']=='Failed':
            msg = 'Test Failed: Passed {0}, Failed {1}'.format(
                  data['total_passed'], data['total_failed']
            )
            logging.error(msg)
            dev.close()
            module.exit_json(msg=msg, **data)

    except Exception as err:
        msg = 'Uncaught exception - please report: {0}'.format(str(err))
        logging.error(msg)
        dev.close()
        module.fail_json(msg=msg)

    dev.close()
    module.exit_json(**data)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
