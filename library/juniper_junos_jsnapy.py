#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2016, Roslan Zaki
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
module: juniper_junos_jsnapy
version_added: "2.0.0" # of Juniper.junos role
author:
  - Juniper Networks
  - Roslan Zaki
  - Damien Garros
  - Stacy Smith (@stacywsmith)"
short_description: Execute JSNAPy tests on a Junos device
description:
  - Execute Junos SNAPshot Adminsitrator (JSNAPy) tests against a Junos device.
    JSNAPy is documented on U(Github|https://github.com/Juniper/jsnapy) and
    this
    U(Day One Book|https://www.juniper.net/uk/en/training/jnbooks/day-one/automation-series/jsnapy/)
  - This module only reports C(failed) if the module encounters an error and
    fails to execute the JSNAPy tests. If does NOT report C(failed) if one or
    more of the JSNAPy tests fail. To check the test results, register the
    module's response and use the assert module to verify the expected result
    in the response. (See :ref:`juniper_junos_jsnapy-examples-label`.)
  - A callback plugin which formats and prints JSNAPy test results for human
    consumption is also available. This callback plugin is enabled by adding
    C(callback_whitelist = jsnapy) to the Ansible configuration file.
options:
  action:
    description:
      - The JSNAPy action to perform.
    required: true
    default: none
    type: str
    choices:
      - check
      - snapcheck
      - snap_pre
      - snap_post
  config_file:
    description:
      - The filename of a JSNAPy configuration file (in YAML format). The
        I(test_files) option and the I(config_file) option are mutually
        exclusive. Either the I(test_files) option or the I(config_file)
        option is required.
    required: false
    type: path
    default: none
  dir:
    description:
      - The path to the directory containing the JSNAPy test file(s) specified
        by the I(test_files) option or the JSNAPy configuration file specified
        by the I(config_file) option.
    required: false
    type: path
    default: /etc/jsnapy/testfiles
    aliases:
      - directory
  test_files:
    description:
      - The filename of file(s) in the I(dir) directory. Each file contains
        JSNAPy test case definitions. The I(test_files) option and the
        I(config_file) option are mutually exclusive. Either the I(test_files)
        option or the I(config_file) option is required.
    required: false
    type: list of path
    default: none
'''


EXAMPLES = '''
---
- name: Examples of juniper_junos_jsnapy
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: JUNOS Post Checklist
      juniper_junos_jsnapy:
        action: "snap_post"
        config_file: "first_test.yml"
        logfile: "migration_post.log"
      register: test1
    - name: Verify all JSNAPy tests passed
      assert:
        that:
          - "test1.passPercentage == 100"
    - name: Print the full test response
      debug:
        var: test1

    - name: Test based on a test_file directly
      juniper_junos_jsnapy:
       action: "snapcheck"
       test_files: "tests/test_junos_interface.yaml"
      register: test2
    - name: Verify all JSNAPy tests passed
      assert:
        that:
          - "test2.passPercentage == 100"
    - name: Print the full test response
      debug:
        var: test2

    - name: "Collect Pre Snapshot"
      juniper_junos_jsnapy:
        action: "snap_pre"
        test_files: "tests/test_loopback.yml"

    - name: "Collect Post Snapshot"
      juniper_junos_jsnapy:
        action: "snap_post"
        test_files: "tests/test_loopback.yml"

    - name: "Check after Pre and Post Snapshots"
      juniper_junos_jsnapy:
        action: "check"
        test_files: "tests/test_loopback.yml"
      register: test3
    - name: Verify all JSNAPy tests passed
      assert:
        that:
          - "test3.|succeeded"
          - "test3.passPercentage == 100"
    - name: Print the full test response
      debug:
        var: test3
'''

RETURN = '''
action:
  description:
    - The JSNAPy action performed as specified by the I(action) option.
  returned: success
  type: str
changed:
  description:
    - Indicates if the device's state has changed. Since this module doesn't
      change the operational or configuration state of the device, the value
      is always set to C(false).
  returned: success
  type: bool
failed:
  description:
    - Indicates if the task failed.
  returned: always
  type: bool
# final_result:
msg:
  description:
    - A human-readable message indicating the result of the JSNAPy tests.
  returned: always
  type: str
# total_passed:
# total_failed:
'''

# Standard Library imports
import os.path


"""From Ansible 2.1, Ansible uses Ansiballz framework for assembling modules
But custom module_utils directory is supported from Ansible 2.3
Reference for the issue: https://groups.google.com/forum/#!topic/ansible-project/J8FL7Z1J1Mw """

# Ansiballz packages module_utils into ansible.module_utils
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import juniper_junos_common


def main():
    JSNAPY_ACTION_CHOICES = ['check', 'snapcheck', 'snap_pre', 'snap_post']

    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            action=dict(required=True,
                        choices=JSNAPY_ACTION_CHOICES,
                        type='str',
                        default=None),
            test_files=dict(required=False,
                            type='list',
                            default=None),
            config_file=dict(required=False,
                             type='path',
                             default=None),
            dir=dict(required=False,
                     type='path',
                     aliases=['directory'],
                     default='/etc/jsnapy/testfiles')),
        # Mutually exclusive options.
        mutually_exclusive=[['test_files', 'config_file']],
        # One of test_files or config_file is required.
        required_one_of=[['test_files', 'config_file']],
        supports_check_mode=True,
        min_jsnapy_version=juniper_junos_common.MIN_JSNAPY_VERSION,
    )

    # Straight from params
    action = junos_module.params.get('action')
    test_files = junos_module.params.get('test_files')
    config_file = junos_module.params.get('config_file')
    dir = junos_module.params.get('dir')

    # Initialize the results. Assume failure until we know otherwise.
    results = {'msg': '',
               'action': action,
               'changed': False,
               'failed': True}

    if config_file is not None:
        junos_module.logger.debug('Checking config file: %s.', config_file)
        config_file_path = os.path.abspath(config_file)
        config_dir_file_path = os.path.abspath(os.path.join(dir, config_file))
        if os.path.isfile(config_file_path):
            data = config_file_path
        elif os.path.isfile(config_dir_file_path):
            data = config_dir_file_path
        else:
            junos_module.fail_json(msg="Unable to locate the %s config file "
                                       "at %s or %s." % (config_file,
                                                         config_file_path,
                                                         config_dir_file_path))
    elif test_files is not None and len(test_files) > 0:
        data = {'tests': []}
        for test_file in test_files:
            junos_module.logger.debug('Checking test file: %s.', test_file)
            test_file_path = os.path.abspath(test_file)
            test_dir_file_path = os.path.abspath(os.path.join(dir, test_file))
            if os.path.isfile(test_file_path):
                data['tests'].append(test_file_path)
            elif os.path.isfile(test_dir_file_path):
                data['tests'].append(test_dir_file_path)
            else:
                junos_module.fail_json(msg="Unable to locate the %s test file "
                                           "at %s or %s." %
                                           (test_file,
                                            test_file_path,
                                            test_dir_file_path))
    else:
        junos_module.fail_json(msg="No config_file or test_files specified.")

    try:
        junos_module.logger.debug('Creating jnpr.jsnapy.SnapAdmin instance.')
        jsa = junos_module.jsnapy.SnapAdmin()
        junos_module.logger.debug('Executing %s action.', action)
        if action == 'check':
            responses = jsa.check(data=data,
                                  dev=junos_module.dev,
                                  pre_file='PRE',
                                  post_file='POST')
        elif action == 'snapcheck':
            responses = jsa.snapcheck(data=data,
                                      dev=junos_module.dev)
        elif action == 'snap_pre':
            responses = jsa.snap(data=data,
                                 dev=junos_module.dev,
                                 file_name='PRE')
        elif action == 'snap_post':
            responses = jsa.snap(data=data,
                                 dev=junos_module.dev,
                                 file_name='POST')
        else:
            junos_module.fail_json(msg="Unexpected action: %s." % (action))
        junos_module.logger.debug('The %s action executed successfully.',
                                  action)
    except (junos_module.pyez_exception.RpcError,
            junos_module.pyez_exception.ConnectError) as ex:
        junos_module.fail_json(msg="Error communicating with the device: %s" %
                                   (str(ex)))
    except Exception as ex:
        junos_module.fail_json(msg="Uncaught exception - please report: %s" %
                                   (str(ex)))

    if isinstance(responses, list) and len(responses) == 1:
        if action in ('snapcheck', 'check'):
            for response in responses:
                results['device'] = response.device
                results['router'] = response.device
                results['final_result'] = response.result
                results['total_passed'] = response.no_passed
                results['total_failed'] = response.no_failed
                results['test_results'] = response.test_results
                total_tests = int(response.no_passed) + int(response.no_failed)
                results['total_tests'] = total_tests
            pass_percentage = 0
            if total_tests > 0:
                pass_percentage = ((int(response.no_passed) * 100) //
                                   total_tests)
            results['passPercentage'] = pass_percentage
            results['pass_percentage'] = pass_percentage
            if results['final_result'] == 'Failed':
                results['msg'] = 'Test Failed: Passed %s, Failed %s' % \
                                 (results['total_passed'],
                                  results['total_failed'])
            else:
                results['msg'] = 'Test Passed: Passed %s, Failed %s' % \
                                 (results['total_passed'],
                                  results['total_failed'])
        elif action in ('snap_pre', 'snap_post'):
            results['msg'] = "The %s action successfully executed." % (action)
    else:
        junos_module.fail_json(msg="Unexpected JSNAPy responses. Type: %s."
                                   "Responses: %s" %
                                   (type(responses), str(responses)))

    # If we made it this far, it's success.
    results['failed'] = False

    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
