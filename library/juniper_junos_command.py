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
module: juniper_junos_command
version_added: "2.0.0" # of Juniper.junos role
author: "Juniper Networks - Stacy Smith (@stacywsmith)"
short_description: Execute one or more CLI commands on a Junos device
description:
  - Execute one or more CLI commands on a Junos device.
  - This module does NOT use the Junos CLI to execute the CLI command.
    Instead, it uses the C(<command>) RPC over a NETCONF channel. The
    C(<command>) RPC takes a CLI command as it's input and is very similar to
    executing the command on the CLI, but you can NOT include any pipe modifies
    (i.e. C(| match), C(| count), etc.) with the CLI commands executed by this
    module.
options:
  commands:
    description:
      - A list of one or more CLI commands to execute on the Junos device.
    required: true
    default: none
    type: list
    aliases:
      - cli
      - command
      - cmd
      - cmds
  dest:
    description:
      - The path to a file, on the Ansible control machine, where the output of
        the cli command will be saved.
      - The file must be writeable. If the file already exists, it is
        overwritten.
      - When tasks are executed against more than one target host,
        one process is forked for each target host. (Up to the maximum
        specified by the forks configuration. See
        U(forks|http://docs.ansible.com/ansible/latest/intro_configuration.html#forks)
        for details.) This means that the value of this option must be unique
        per target host. This is usually accomplished by including
        C({{ inventory_hostname }}) in the value of the I(dest) option. It is
        the user's responsibility to ensure this value is unique per target
        host.
      - For this reason, this option is deprecated. It is maintained for
        backwards compatibility. Use the I(dest_dir) option in new playbooks.
        The I(dest) and I(dest_dir) options are mutually exclusive.
    required: false
    default: None
    type: path
    aliases:
      - destination
  dest_dir:
    description:
      - The path to a directory, on the Ansible control machine, where
        the output of the cli command will be saved. The output will be logged
        to a file named C({{ inventory_hostname }}_)I(command)C(.)I(format)
        in the directory specified by the value of the I(dest_dir) option.
      - The destination file must be writeable. If the file already exists,
        it is overwritten. It is the users responsibility to ensure a unique
        I(dest_dir) value is provided for each execution of this module
        within a playbook.
      - The I(dest_dir) and I(dest) options are mutually exclusive. The
        I(dest_dir) option is recommended for all new playbooks.
    required: false
    default: None
    type: path
    aliases:
      - destination_dir
      - destdir
  formats:
    description:
      - The format of the reply for the CLI command(s) specified by the
        I(commands) option. The specified format(s) must be supported by the
        target Junos device. The value of this option can either be a single
        format, or a list of formats. If a single format is specified, it
        applies to all command(s) specified by the I(commands) option. If a
        list of formats are specified, there must be one value in the list for
        each command specified by the I(commands) option. Specifying the value
        C(xml) for the I(formats) option is similar to appending
        C(| display xml) to a CLI command, and specifying the value C(json)
        for the I(formats) option is similar to appending C(| display json) to
        a CLI command.
    required: false
    default: text
    type: str or list of str
    choices:
      - text
      - xml
      - json
    aliases:
      - format
      - display
      - output
  return_output:
    description:
      - Indicates if the output of the command should be returned in the
        module's response. You might want to set this option to C(false),
        and set the I(dest_dir) option, if the command output is very large
        and you only need to save the output rather than using it's content in
        subsequent tasks/plays of your playbook.
    required: false
    default: true
    type: bool
'''

EXAMPLES = '''
---
- name: Examples of juniper_junos_command
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: Execute single "show version" command.
      juniper_junos_command:
        commands: "show version"
      register: response

    - name: Print the command output
      debug:
        var: response.stdout

    - name: Execute three commands.
      juniper_junos_command:
        commands:
          - "show version"
          - "show system uptime"
          - "show interface terse"
      register: response

    - name: Print the command output of each.
      debug:
        var: item.stdout
      with_items: "{{ response.results }}"

    - name: Two commands with XML output.
      juniper_junos_command:
        commands:
          - "show route"
          - "show lldp neighbors"
        format: xml

    - name: show route with XML output - show version with JSON output
      juniper_junos_command:
        commands:
          - "show route"
          - "show version"
        formats:
          - "xml"
          - "json"

    - name: save outputs in dest_dir
      juniper_junos_command:
        commands:
          - "show route"
          - "show version"
        dest_dir: "./output"

    - name: save output to dest
      juniper_junos_command:
        command: "show system uptime"
        dest: "/tmp/{{ inventory_hostname }}.uptime.output"

    - name: save output to dest
      juniper_junos_command:
        command:
          - "show route"
          - "show lldp neighbors"
        dest: "/tmp/{{ inventory_hostname }}.commands.output"

    - name: Multiple commands, save outputs, but don't return them
      juniper_junos_command:
        commands:
          - "show route"
          - "show version"
        formats:
          - "xml"
          - "json"
        dest_dir: "/tmp/outputs/"
        return_output: false
'''

RETURN = '''
changed:
  description:
    - Indicates if the device's state has changed. Since this module does not
      change the operational or configuration state of the device, the value
      is always set to false.
    - You could use this module to execute a command which
      changes the operational state of the the device. For example,
      C(clear ospf neighbors). Beware, this module is unable to detect
      this situation, and will still return the value C(false) for I(changed)
      in this case.
  returned: success
  type: bool
  sample: false
command:
  description:
    - The CLI command which was executed.
  returned: always
  type: str
failed:
  description:
    - Indicates if the task failed. See the I(results) key for additional
      details.
  returned: always
  type: bool
format:
  description:
    - The format of the command response.
  returned: always
  type: str
msg:
  description:
    - A human-readable message indicating the result.
  returned: always
  type: str
parsed_output:
  description:
    - The command reply from the Junos device parsed into a JSON data structure.
      For XML replies, the response is parsed into JSON using the
      U(jxmlease|https://github.com/Juniper/jxmlease)
      library. For JSON the response is parsed using the Python
      U(json|https://docs.python.org/2/library/json.html) library.
    - When Ansible converts the jxmlease or native Python data structure
      into JSON, it does not guarantee that the order of dictionary/object keys
      are maintained.
  returned: when command executed successfully, I(return_output) is true,
            and the value of the I(formats) option is C(xml) or C(json).
  type: dict
results:
  description:
    - The other keys are returned when a single command is specified for the
      I(commands) option. When the value of the I(commands) option is a list
      of commands, this key is returned instead. The value of this key is a
      list of dictionaries. Each element in the list corresponds to the
      commands in the I(commands) option. The keys for each element in the list
      include all of the other keys listed. The I(failed) key indicates if the
      individual command failed. In this case, there is also a top-level
      I(failed) key. The top-level I(failed) key will have a value of C(false)
      if ANY of the commands ran successfully. In this case, check the value
      of the I(failed) key for each element in the I(results) list for the
      results of individual commands.
  returned: when the I(commands) option is a list value.
  type: list of dict
stdout:
  description:
    - The command reply from the Junos device as a single multi-line string.
  returned: when command executed successfully and I(return_output) is C(true).
  type: str
stdout_lines:
  description:
    - The command reply from the Junos device as a list of single-line strings.
  returned: when command executed successfully and I(return_output) is C(true).
  type: list of str
'''

import sys


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
            commands=dict(required=True,
                          type='list',
                          aliases=['cli', 'command', 'cmd', 'cmds'],
                          default=None),
            formats=dict(required=False,
                         type='list',
                         aliases=['format', 'display', 'output'],
                         default=None),
            dest=dict(required=False,
                      type='path',
                      aliases=['destination'],
                      default=None),
            dest_dir=dict(required=False,
                          type='path',
                          aliases=['destination_dir', 'destdir'],
                          default=None),
            return_output=dict(required=False,
                               type='bool',
                               default=True)
        ),
        # Since this module doesn't change the device's configuration, there is
        # no additional work required to support check mode. It's inherently
        # supported. Well, that's not completely true. It does depend on the
        # command executed. See the I(changed) key in the RETURN documentation
        # for more details.
        supports_check_mode=True,
        min_jxmlease_version=juniper_junos_common.MIN_JXMLEASE_VERSION,
    )

    # Check over commands
    commands = junos_module.params.get('commands')
    # Ansible allows users to specify a commands argument with no value.
    if commands is None:
        junos_module.fail_json(msg="The commands option must have a value.")
    # Make sure the commands don't include any pipe modifiers.
    for command in commands:
        pipe_index = command.find('|')
        if (pipe_index != -1 and
           command[pipe_index:].strip() != 'display xml rpc'):
            # Allow "show configuration | display set"
            if ('show configuration' in command and
                'display set' in command[pipe_index:] and
                '|' not in command[pipe_index+1:]):
                continue
            # Any other "| display " should use the format option instead.
            for valid_format in juniper_junos_common.RPC_OUTPUT_FORMAT_CHOICES:
                if 'display ' + valid_format in command[pipe_index:]:
                    junos_module.fail_json(
                        msg='The pipe modifier (%s) in the command '
                            '(%s) is not supported. Use format: "%s" '
                            'instead.' %
                            (command[pipe_index:], command, valid_format))
            # Any other "| " is going to produce an error anyway, so fail
            # with a meaningful message.
            junos_module.fail_json(msg='The pipe modifier (%s) in the command '
                                       '(%s) is not supported.' %
                                       (command[pipe_index:], command))

    # Check over formats
    formats = junos_module.params.get('formats')
    if formats is None:
        # Default to text format
        formats = ['text']
    valid_formats = juniper_junos_common.RPC_OUTPUT_FORMAT_CHOICES
    # Check format values
    for format in formats:
        # Is it a valid format?
        if format not in valid_formats:
            junos_module.fail_json(msg="The value %s in formats is invalid. "
                                       "Must be one of: %s" %
                                       (format, ', '.join(map(str,
                                                              valid_formats))))
    # Correct number of format values?
    if len(formats) != 1 and len(formats) != len(commands):
        junos_module.fail_json(msg="The formats option must have a single "
                                   "value, or one value per command. There "
                                   "are %d commands and %d formats." %
                                   (len(commands), len(formats)))
    # Same format for all commands
    elif len(formats) == 1 and len(commands) > 1:
        formats = formats * len(commands)

    results = list()
    for (command, format) in zip(commands, formats):
        # Set initial result values. Assume failure until we know it's success.
        result = {'msg': '',
                  'command': command,
                  'format': format,
                  'changed': False,
                  'failed': True}

        # Execute the CLI command
        try:
            junos_module.logger.debug('Executing command "%s".',
                                      command)
            rpc = junos_module.etree.Element('command', format=format)
            rpc.text = command
            resp = junos_module.dev.rpc(rpc, normalize=bool(format == 'xml'))
            result['msg'] = 'The command executed successfully.'
            junos_module.logger.debug('Command "%s" executed successfully.',
                                      command)
        except (junos_module.pyez_exception.ConnectError,
                junos_module.pyez_exception.RpcError) as ex:
            junos_module.logger.debug('Unable to execute "%s". Error: %s',
                                      command, str(ex))
            result['msg'] = 'Unable to execute the command: %s. Error: %s' % \
                            (command, str(ex))
            results.append(result)
            continue

        text_output = None
        parsed_output = None
        if resp is True:
            text_output = ''
        elif (resp, junos_module.etree._Element):
            # Handle the output based on format
            if format == 'text':
                if resp.tag in ['output', 'rpc-reply']:
                    text_output = resp.text
                    junos_module.logger.debug('Text output set.')
                elif resp.tag == 'configuration-information':
                    text_output = resp.findtext('configuration-output')
                    junos_module.logger.debug('Text configuration output set.')
                else:
                    result['msg'] = 'Unexpected text response tag: %s.' % (
                                    (resp.tag))
                    results.append(result)
                    junos_module.logger.debug('Unexpected text response tag '
                                              '%s.', resp.tag)
                    continue
            elif format == 'xml':
                encode = None if sys.version < '3' else 'unicode'
                text_output = junos_module.etree.tostring(resp,
                                                          pretty_print=True,
                                                          encoding=encode)
                parsed_output = junos_module.jxmlease.parse_etree(resp)
                junos_module.logger.debug('XML output set.')
            elif format == 'json':
                text_output = str(resp)
                parsed_output = resp
                junos_module.logger.debug('JSON output set.')
            else:
                result['msg'] = 'Unexpected format %s.' % (format)
                results.append(result)
                junos_module.logger.debug('Unexpected format %s.', format)
                continue
        else:
            result['msg'] = 'Unexpected response type %s.' % (type(resp))
            results.append(result)
            junos_module.logger.debug('Unexpected response type %s.',
                                      type(resp))
            continue

        # Set the output keys
        if junos_module.params['return_output'] is True:
            if text_output is not None:
                result['stdout'] = text_output
                result['stdout_lines'] = text_output.splitlines()
            if parsed_output is not None:
                result['parsed_output'] = parsed_output
        # Save the output
        junos_module.save_text_output(command, format, text_output)
        # This command succeeded.
        result['failed'] = False
        # Append to the list of results
        results.append(result)

    # Return response.
    if len(results) == 1:
        junos_module.exit_json(**results[0])
    else:
        # Calculate the overall failed. Only failed if all commands failed.
        failed = True
        for result in results:
            if result.get('failed') is False:
                failed = False
                break
        junos_module.exit_json(results=results,
                               changed=False,
                               failed=failed)


if __name__ == '__main__':
    main()
