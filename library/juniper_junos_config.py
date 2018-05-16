#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2014, Jeremy Schulman
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
module: juniper_junos_config
version_added: "2.0.0" # of Juniper.junos role
author: "Juniper Networks - Stacy Smith (@stacywsmith)"
short_description: Manipulate the configuration of a Junos device
description:
  - >
    Manipulate the configuration of a Junos device. This module allows a
    combination of loading or rolling back, checking, diffing, retrieving, and
    committing the configuration of a Junos device. It performs the following
    steps in order:


    #. Open a candidate configuration database.
    
       * If the I(config_mode) option has a value of C(exclusive), the default,
         take a lock on the candidate configuration database. If the lock fails
         the module fails and reports an error.
       * If the I(config_mode) option has a value of C(private), open a private
         candidate configuration database. If opening the private configuration
         database fails the module fails and reports an error.
    #. Load configuration data into the candidate configuration database.
       
       * Configuration data may be loaded using the I(load) or I(rollback)
         options. If either of these options are specified, new configuration
         data is loaded. If neither option is specified, this step is skipped.
       * If the I(rollback) option is specified, replace the candidate
         configuration with the previous configuration specified by the value
         of the I(rollback) option.
       * If the I(load) option is specified, load new configuration data.
       * The value of the I(load) option defines the type of load which is
         performed.
       * The source of the new configuration data is one of the following:
       
         * I(src)      - A file path on the local Ansible control machine.
         * I(lines)    - A list of strings containing the configuration data.
         * I(template) - A file path to a Jinja2 template on the local
           Ansible control machine. This template is rendered with the variables
           specified by the I(vars) option. If the I(template) option is
           specified, the I(vars) option must also be specified.
         * I(url)      - A URL reachable from the target Junos device.
       * If the I(format) option is specified, the configuration file being
         loaded is in the specified format, rather than the format determined
         from the file name.
    #. Check the validity of the candidate configuration database.
    
       * If the I(check) option is C(true), the default, check the validity
         of the configuration by performing a "commit check" operation.
       * This option may be specified with I(diff) C(false) and I(commit)
         C(false) to confirm a previous "commit confirmed <min>" operation
         without actually performing an additional commit.
       * If the configuration check fails, further processing stops, the module
         fails, and an error is reported.
    #. Determine differences between the candidate and committed configuration
       databases.
       
       * If step 2 was not skipped, and the I(diff) option is C(true),
         the default, perform a diff between the candidate and committed
         configuration databases.
       * If the I(diffs_file) or I(dest_dir) option is specified, save the
         generated configuration differences.
       * If the I(return_output) option is C(true), the default, include the
         generated configuration difference in the I(diff) and I(diff_lines)
         keys of the module's response.
    #. Retrieve the configuration database from the Junos device.
       
       * If the I(retrieve) option is specified, retrieve the configuration
         database specified by the I(retrieve) value from the target Junos
         device to the local Ansible control machine.
       * The format in which the configuration is retrieved is specified by the
         value of the I(format) option.
       * The optional I(filter) controls which portions of the configuration
         are retrieved.
       * If I(options) are specified, they control the content of the
         configuration retrieved.
       * If the I(dest) or I(dest_dir) option is specified, save the
         retrieved configuration to a file on the local Ansible control
         machine.
       * If the I(return_output) option is C(true), the default, include the
         retrieved configuration in the I(config), I(config_lines), and
         I(config_parsed) keys of the module's response.
    #. Commit the configuration changes.
    
       * If the I(commit) option is C(true), the default, commit the
         configuration changes.
       * This option may be specified with I(diff) C(false) and I(check)
         C(false) to confirm a previous "commit confirmed <min>" operation.
       * If the I(comment) option is specified, add the comment to the commit.
       * If the I(confirmed) option is specified, perform a
         C(commit confirmed) I(min) operation where I(min) is the value of the
         I(confirmed) option.
       * If the I(check) option is C(true) and the I(check_commit_wait)
         option is specified, wait I(check_commit_wait) seconds before
         performing the commit.
    #. Close the candidate configuration database.
       
       * Close and discard the candidate configuration database.
       * If the I(config_mode) option has a value of C(exclusive), the default,
         unlock the candidate configuration database.
options:
  check:
    description:
      - Perform a commit check operation.
    required: false
    default: true (false if retrieve is set and load and rollback are not set)
    type: bool
    aliases:
      - check_commit
      - commit_check
  check_commit_wait:
    description:
      - The number of seconds to wait between check and commit operations.
      - This option is only valid if I(check) is C(true) and I(commit) is
        C(true).
      - This option should not normally be needed. It works around an issue in
        some versions of Junos.
    required: false
    default: none
    type: int
  comment:
    description:
      - Provide a comment to be used with the commit operation.
      - This option is only valid if the I(commit) option is true.
    required: false
    default: none
    type: str
  commit:
    description:
      - Perform a commit operation.
    required: false
    default: true (false if retrieve is set and load and rollback are not set)
    type: bool
  commit_empty_changes:
    description:
      - Perform a commit operation, even if there are no changes between the
        candidate configuration and the committed configuration.
    required: false
    default: false
    type: bool
  config_mode:
    description:
      - The mode used to access the candidate configuration database.
    required: false
    default: exclusive
    type: str
    choices:
      - exclusive
      - private
    aliases:
      - config_access
      - edit_mode
      - edit_access
  confirmed:
    description:
      - Provide a confirmed timeout, in minutes, to be used with the commit
        operation.
      - This option is only valid if the I(commit) option is C(true).
      - The value of this option is the number of minutes to wait for another
        commit operation before automatically rolling back the configuration
        change performed by this task. In other words, this option causes the
        module to perform a C(commit confirmed )I(min) where I(min) is the
        value of the I(confirmed) option. This option DOES NOT confirm a
        previous C(commit confirmed )I(min) operation. To confirm a previous
        commit operation, invoke this module with the I(check) or I(commit)
        option set to C(true).
    required: false
    default: none
    type: int
    aliases:
      - confirm
  dest:
    description:
      - The path to a file, on the local Ansible control machine, where the
        configuration will be saved if the I(retrieve) option is specified.
      - The file must be writeable. If the file already exists, it is
        overwritten.
      - This option is only valid if the I(retrieve) option is not C(none).
      - When tasks are executed against more than one target host,
        one process is forked for each target host. (Up to the maximum
        specified by the forks configuration. See
        U(forks|http://docs.ansible.com/ansible/latest/intro_configuration.html#forks)
        for details.) This means that the value of this option must be unique
        per target host. This is usually accomplished by including
        C({{ inventory_hostname }}) in the I(dest) value. It is the user's
        responsibility to ensure this value is unique per target host.
      - For this reason, this option is deprecated. It is maintained for
        backwards compatibility. Use the I(dest_dir) option in new playbooks.
        The I(dest) and I(dest_dir) options are mutually exclusive.
    required: false
    default: none
    type: path
    aliases:
      - destination
  dest_dir:
    description:
      - The path to a directory, on the Ansible control machine. This is the
        directory where the configuration will be saved if the I(retrieve)
        option is specified. It is also the directory where the configuration
        diff will be specified if the I(diff) option is C(true).
      - This option is only valid if the I(retrieve) option is not C(none) or
        the I(diff) option is C(true).
      - The retrieved configuration will be saved to a file named
        C({{ inventory_hostname }}.)I(format_extension) in the I(dest_dir)
        directory. Where I(format_extension) is C(conf) for text format, C(xml)
        for XML format, C(json) for JSON format, and C(set) for set format.
      - If the I(diff) option is C(true), the configuration diff will be saved
        to a file named C({{ inventory_hostname }}.diff) in the I(dest_dir)
        directory.
      - The destination file must be writeable. If the file already exists,
        it is overwritten. It is the users responsibility to ensure a unique
        I(dest_dir) value is provided for each execution of this module
        within a playbook.
      - The I(dest_dir) and I(dest) options are mutually exclusive. The
        I(dest_dir) option is recommended for all new playbooks.
      - The I(dest_dir) and I(diff_file) options are mutually exclusive. The
        I(dest_dir) option is recommended for all new playbooks.
    required: false
    default: none
    type: path
    aliases:
      - destination_dir
      - destdir
      - savedir
      - save_dir
  diff:
    description:
      - Perform a configuration compare (aka diff) operation.
    required: false
    default: true (false if retrieve is set and load and rollback are not set)
    type: bool
    aliases:
      - compare
      - diffs
  diffs_file:
    description:
      - The path to a file, on the Ansible control machine, where the
        configuration differences will be saved if the I(diff) option is
        specified.
      - The file must be writeable. If the file already exists, it is
        overwritten.
      - This option is only valid if the I(diff) option is C(true).
      - When tasks are executed against more than one target host,
        one process is forked for each target host. (Up to the maximum
        specified by the forks configuration. See
        U(forks|http://docs.ansible.com/ansible/latest/intro_configuration.html#forks)
        for details.) This means that the value of this option must be unique
        per target host. This is usually accomplished by including
        C({{ inventory_hostname }}) in the I(diffs_file) value. It is the
        user's responsibility to ensure this value is unique per target host.
      - For this reason, this option is deprecated. It is maintained for
        backwards compatibility. Use the I(dest_dir) option in new playbooks.
      - The I(diffs_file) and I(dest_dir) options are mutually exclusive.
    required: false
    default: None
    type: path
  format:
    description:
      - Specifies the format of the configuration retrieved, if I(retrieve)
        is not C(none).
      - Specifies the format of the configuration to be loaded, if I(load) is
        not C(none).
      - The specified format must be supported by the target Junos device.
    required: false
    default: none (auto-detect on load, text on retrieve)
    type: str
    choices:
      - xml
      - set
      - text
      - json
  filter:
    description:
      - A string of XML, or '/'-separated configuration hierarchies,
        which specifies a filter used to restrict the portions of the
        configuration which are retrieved. See
        U(PyEZ's get_config method documentation|http://junos-pyez.readthedocs.io/en/stable/jnpr.junos.html#jnpr.junos.rpcmeta._RpcMetaExec.get_config)
        for details on the value of this option.
    required: false
    default: none
    type: 'str'
    aliases:
      - filter_xml
  ignore_warning:
    description:
      - A boolean, string or list of strings. If the value is C(true),
        ignore all warnings regardless of the warning message. If the value
        is a string, it will ignore warning(s) if the message of each warning
        matches the string. If the value is a list of strings, ignore
        warning(s) if the message of each warning matches at least one of the
        strings in the list. The value of the I(ignore_warning) option is
        applied to the load and commit operations performed by this module.
    required: false
    default: none
    type: bool, str, or list of str
  lines:
    description:
      - Used with the I(load) option. Specifies a list of list of
        configuration strings containing the configuration to be loaded.
      - The I(src), I(lines), I(template), and I(url) options are mutually
        exclusive.
      - By default, the format of the configuration data is auto-dectected by
        the content of the first line in the I(lines) list.
      - If the I(format) option is specified, the I(format) value overrides the
        format auto-detection.
    required: false
    default: none
    type: list
  load:
    description:
      - Specifies the type of load operation to be performed.
      - The I(load) and I(rollback) options are mutually exclusive.
      - >
        The choices have the following meanings:
      - B(none) - Do not perform a load operation.
      - B(merge) - Combine the new configuration with the existing
        configuration. If statements in the new configuration conflict with
        statements in the existing configuration, the statements in
        the new configuration replace those in the existing
        configuration.
      - B(replace) - This option is a superset of the B(merge) option. It
        combines the new configuration with the existing configuration. If the
        new configuration is in text format and a hierarchy level in the new
        configuartion is prefixed with the string C(replace:), then the
        hierarchy level in the new configuration replaces the entire
        corresponding hierarchy level in the existing configuration, regardles
        of the existence or content of that hierarchy level in the existing
        configuration. If the configuration is in XML format, the XML attribute
        C(replace = "replace") is equivalent to the text format's C(replace:)
        prefix. If a configuration hierarchy in the new configuration is not
        prefixed with C(replace:), then the B(merge) behavior is used.
        Specifically, for any statements in the new configuration which
        conflict with statements in the existing configuration, the statements
        in the new configuration replace those in the existing configuration.
      - B(override) - Discard the entire existing configuration and replace it
        with the new configuration. When the configuration is later committed,
        all system processes are notified and the entire new configuration is
        marked as 'changed' even if some statements previously existed in the
        configuration. The value B(overwrite) is a synonym for B(override).
      - B(update) - This option is similar to the B(override) option. The new
        configuration completely replaces the existing configuration. The
        difference comes when the configuration is later committed. This option
        performs a 'diff' between the new candidate configuration and the
        existing committed configuration. It then only notifies system
        processes repsonsible for the changed portions of the configuration,
        and only marks the actual configuration changes as 'changed'.
      - B(set) - This option is used when the new configuration data is in set
        format (a series of configuration mode commands). The new configuration
        data is loaded line by line and may contain any configuration mode
        commands, such as set, delete, edit, or deactivate. This value must be
        specified if the new configuration is in set format.  
    required: false
    default: none
    choices:
      - none
      - set
      - merge
      - update
      - replace
      - override
      - overwrite
    type: str
  options:
    description:
      - Additional options, specified as a dictionary of key/value pairs, used
        when retrieving the configuration. See the
        U(<get-configuration> RPC documentation|https://www.juniper.net/documentation/en_US/junos/topics/reference/tag-summary/junos-xml-protocol-get-configuration.html)
        for information on available options.
    required: false
    default: None
    type: dict
  retrieve:
    description:
      - The configuration database to be retrieved.
    required: false
    default: none
    choices: 
      - none
      - candidate
      - committed
    type: str
  return_output:
    description:
      - Indicates if the output of the I(diff) and I(retreive) options should
        be returned in the module's response. You might want to set this option
        to C(false), and set the I(dest_dir) option, if the configuration or
        diff output is very large and you only need to save the output rather
        than using it's content in subsequent tasks/plays of your playbook.
    required: false
    default: true
    type: bool
  rollback:
    description:
      - Populate the candidate configuration from a previously committed
        configuration. This value can be a configuration number between 0 and
        49, or the keyword C(rescue) to load the previously saved rescue
        configuration.
      - By default, some Junos platforms store fewer than 50 previous
        configurations. Specifying a value greater than the number
        of previous configurations available, or specifying C(rescue) when no
        rescue configuration has been saved, will result in an error when the
        module attempts to perform the rollback.
      - The I(rollback) and I(load) options are mutually exclusive.
    required: false
    default: none
    choices:
      - 0-49
      - rescue
    type: int or str
  src:
    description:
      - Used with the I(load) option. Specifies the path to a file, on the
        local Ansible control machine, containing the configuration to be
        loaded.
      - The I(src), I(lines), I(template), and I(url) options are mutually
        exclusive.
      - By default, the format of the configuration data is determined by the
        file extension of this path name. If the file has a C(.conf)
        extension, the content is treated as text format. If the file has a
        C(.xml) extension, the content is treated as XML format. If the file
        has a C(.set) extension, the content is treated as Junos B(set)
        commands.
      - If the I(format) option is specified, the I(format) value overrides the
        file-extension based format detection.
    required: false
    default: none
    type: 'path'
    aliases:
      - source
      - file
  template:
    description:
      - The path to a Jinja2 template file, on the local Ansible control
        machine. This template file, along with the I(vars) option, is used to
        generate the configuration to be loaded on the target Junos device.
      - The I(src), I(lines), I(template), and I(url) options are mutually
        exclusive.
      - The I(template) and I(vars) options are required together. If one is
        specified, the other must be specified.
    required: false
    default: none
    type: path
    aliases:
      - template_path
  url:
    description:
      - A URL which specifies the configuration data to load on the target
        Junos device.
      - The Junos device uses this URL to load the configuration, therefore
        this URL must be reachable by the target Junos device.
      - The possible formats of this value are documented in the 'url' section
        of the 
        U(<load-configuration> RPC documentation|https://www.juniper.net/documentation/en_US/junos/topics/reference/tag-summary/junos-xml-protocol-load-configuration.html).
      - The I(src), I(lines), I(template), and I(url) options are mutually
        exclusive.
    required: false
    default: none
    type: str
  vars:
    description:
      - A dictionary of keys and values used to render the Jinja2 template
        specified by the I(template) option.
      - The I(template) and I(vars) options are required together. If one is
        specified, the other must be specified.
    required: false
    default: none
    type: dict
    aliases:
      - template_vars
'''

EXAMPLES = '''
---
- name: Manipulate the configuration of Junos devices
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos
  tasks:
    - name: Retrieve the committed configuration
      juniper_junos_config:
        retrieve: 'committed'
        diff: false
        check: false
        commit: false
      register: response
    - name: Print the lines in the config.
      debug:
        var: response.config_lines

    - name: Append .foo to the hostname using private config mode.
      juniper_junos_config:
        config_mode: 'private'
        load: 'merge'
        lines:
          - "set system host-name {{ inventory_hostname }}.foo"
      register: response
    - name: Print the config changes.
      debug:
        var: response.diff_lines

    - name: Rollback to the previous config.
      juniper_junos_config:
        config_mode: 'private'
        rollback: 1
      register: response
    - name: Print the config changes.
      debug:
        var: response.diff_lines

    - name: Rollback to the rescue config.
      juniper_junos_config:
        rollback: 'rescue'
      register: response
    - name: Print the complete response.
      debug:
        var: response

    - name: Load override from a file.
      juniper_junos_config:
        load: 'override'
        src: "{{ inventory_hostname }}.conf"
      register: response
    - name: Print the complete response.
      debug:
        var: response

    - name: Load from a Jinja2 template.
      juniper_junos_config:
        load: 'merge'
        format: 'xml'
        template: "{{ inventory_hostname }}.j2"
        vars:
          host: "{{ inventory_hostname }}"
      register: response
    - name: Print the complete response.
      debug:
        var: response

    - name: Load from a file on the Junos device.
      juniper_junos_config:
        load: 'merge'
        url: "{{ inventory_hostname }}.conf"
      register: response
    - name: Print the complete response.
      debug:
        var: response

    - name: Load from a file on the Junos device, skip the commit check
      juniper_junos_config:
        load: 'merge'
        url: "{{ inventory_hostname }}.conf"
        check: false
      register: response
    - name: Print the msg.
      debug:
        var: response.msg

    - name: Print diff between current and rollback 10. No check. No commit.
      juniper_junos_config:
        rollback: 11
        diff: true
        check: false
        commit: false
      register: response
    - name: Print the msg.
      debug:
        var: response

    - name: Retrieve [edit system services] of current committed config.
      juniper_junos_config:
        retrieve: 'committed'
        filter: 'system/services'
        diff: true
        check: false
        commit: false
      register: response
    - name: Print the resulting config lines.
      debug:
        var: response.config_lines

    - name: Enable NETCONF SSH and traceoptions, save config, and diffs.
      juniper_junos_config:
        load: 'merge'
        lines:
          - 'set system services netconf ssh'
          - 'set system services netconf traceoptions flag all'
          - 'set system services netconf traceoptions file netconf.log'
        format: 'set'
        retrieve: 'candidate'
        filter: 'system/services'
        comment: 'Enable NETCONF with traceoptions'
        dest_dir: './output'
      register: response
    - name: Print the complete response
      debug:
        var: response

    - name: Load conf. Confirm within 5 min. Wait 3 secs between chk and commit
      juniper_junos_config:
        load: 'merge'
        url: "{{ inventory_hostname }}.conf"
        confirm: 5
        check_commit_wait: 3
      register: response
    - name: Print the complete response
      debug:
        var: response
    - name: Confirm the previous commit with a commit check (but no commit)
      juniper_junos_config:
        check: true
        diff: false
        commit: false
      register: response
    - name: Print the complete response
      debug:
        var: response
'''

RETURN = '''
changed:
  description:
    - Indicates if the device's configuration has changed, or would have
      changed when in check mode.
  returned: success
  type: bool
config:
  description:
    - The retrieved configuration. The value is a single multi-line
      string in the format specified by the I(format) option.
  returned: when I(retrieved) is not C(none) and I(return_output) is C(true).
  type: str
config_lines:
  description:
    - The retrieved configuration. The value is a list of single-line
      strings in the format specified by the I(format) option.
  returned: when I(retrieved) is not C(none) and I(return_output) is C(true).
  type: list
config_parsed:
  description:
    - The retrieved configuration parsed into a JSON datastructure.
      For XML replies, the response is parsed into JSON using the
      jxmlease library. For JSON the response is parsed using the
      Python json library.
    - When Ansible converts the jxmlease or native Python data
      structure into JSON, it does not guarantee that the order of
      dictionary/object keys are maintained.
  returned: when I(retrieved) is not C(none), the I(format) option is C(xml) or
            C(json) and I(return_output) is C(true).
  type: dict
diff:
  description: 
    - The configuration differences between the previous and new
      configurations. The value is a single multi-line string in "diff" format.
  returned: when I(load)  or I(rollback) is specified, I(diff) is C(true), and
            I(return_output) is C(true).
  type: str
diff_lines:
  description:
    - The configuration differences between the previous and new
      configurations. The value is a list of single-line strings in "diff"
      format.
  returned: when I(load)  or I(rollback) is specified, I(diff) is C(true), and
            I(return_output) is C(true).
  type: list
failed:
  description: 
    - Indicates if the task failed.
  returned: always
  type: bool
file:
  description:
    - The value of the I(src) option.
  returned: when I(load) is not C(none) and I(src) is not C(none)
  type: str
msg:
  description:
    - A human-readable message indicating the result.
  returned: always
  type: str
'''


# Standard library imports
import time


"""From Ansible 2.1, Ansible uses Ansiballz framework for assembling modules
But custom module_utils directory is supported from Ansible 2.3
Reference for the issue: https://groups.google.com/forum/#!topic/ansible-project/J8FL7Z1J1Mw """

# Ansiballz packages module_utils into ansible.module_utils
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import juniper_junos_common


def main():
    # Choices which are defined in the common module.
    config_format_choices = juniper_junos_common.CONFIG_FORMAT_CHOICES
    config_database_choices = [None] + \
        juniper_junos_common.CONFIG_DATABASE_CHOICES
    config_action_choices = [None] + juniper_junos_common.CONFIG_ACTION_CHOICES
    config_mode_choices = juniper_junos_common.CONFIG_MODE_CHOICES

    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            ignore_warning=dict(required=False,
                                type='list',
                                default=None),
            config_mode=dict(choices=config_mode_choices,
                             type='str',
                             required=False,
                             aliases=['config_access', 'edit_mode',
                                      'edit_access'],
                             default='exclusive'),
            rollback=dict(type='str',
                          required=False,
                          default=None),
            load=dict(choices=config_action_choices,
                      type='str',
                      required=False,
                      default=None),
            src=dict(type='path',
                     required=False,
                     aliases=['source', 'file'],
                     default=None),
            lines=dict(type='list',
                       required=False,
                       default=None),
            template=dict(type='path',
                          required=False,
                          aliases=['template_path'],
                          default=None),
            vars=dict(type='dict',
                      required=False,
                      aliases=['template_vars'],
                      default=None),
            url=dict(type='str',
                     required=False,
                     default=None),
            format=dict(choices=config_format_choices,
                        type='str',
                        required=False,
                        default=None),
            check=dict(required=False,
                       type='bool',
                       aliases=['check_commit', 'commit_check'],
                       default=None),
            diff=dict(required=False,
                      type='bool',
                      aliases=['compare', 'diffs'],
                      default=None),
            diffs_file=dict(type='path',
                            required=False,
                            default=None),
            dest_dir=dict(required=False,
                          type='path',
                          aliases=['destination_dir', 'destdir', 'savedir',
                                   'save_dir'],
                          default=None),
            return_output=dict(required=False,
                               type='bool',
                               default=True),
            retrieve=dict(choices=config_database_choices,
                          type='str',
                          required=False,
                          default=None),
            options=dict(type='dict',
                         required=False,
                         default={}),
            filter=dict(required=False,
                        type='str',
                        aliases=['filter_xml'],
                        default=None),
            dest=dict(type='path',
                      required=False,
                      aliases=['destination'],
                      default=None),
            commit=dict(required=False,
                        type='bool',
                        default=None),
            commit_empty_changes=dict(required=False,
                                      type='bool',
                                      default=False),
            confirmed=dict(required=False,
                           type='int',
                           aliases=['confirm'],
                           default=None),
            comment=dict(required=False,
                         type='str',
                         default=None),
            check_commit_wait=dict(required=False,
                                   type='int',
                                   default=None)
        ),
        # Mutually exclusive options.
        mutually_exclusive=[['load', 'rollback'],
                            ['src', 'lines', 'template', 'url'],
                            ['diffs_file', 'dest_dir'],
                            ['dest', 'dest_dir']],
        # Required together options.
        required_together=[['template', 'vars']],
        # Check mode is implemented.
        supports_check_mode=True,
        min_jxmlease_version=juniper_junos_common.MIN_JXMLEASE_VERSION,
    )
    # Do additional argument verification.

    # Parse ignore_warning value
    ignore_warning = junos_module.parse_ignore_warning_option()

    # Straight from params
    config_mode = junos_module.params.get('config_mode')

    # Parse rollback value
    rollback = junos_module.parse_rollback_option()

    # Straight from params
    load = junos_module.params.get('load')
    src = junos_module.params.get('src')
    lines = junos_module.params.get('lines')
    template = junos_module.params.get('template')
    vars = junos_module.params.get('vars')
    url = junos_module.params.get('url')
    format = junos_module.params.get('format')
    check = junos_module.params.get('check')
    diff = junos_module.params.get('diff')
    diffs_file = junos_module.params.get('diffs_file')
    dest_dir = junos_module.params.get('dest_dir')
    return_output = junos_module.params.get('return_output')
    retrieve = junos_module.params.get('retrieve')
    options = junos_module.params.get('options')
    filter = junos_module.params.get('filter')
    dest = junos_module.params.get('dest')
    commit = junos_module.params.get('commit')
    commit_empty_changes = junos_module.params.get('commit_empty_changes')
    confirmed = junos_module.params.get('confirmed')
    comment = junos_module.params.get('comment')
    check_commit_wait = junos_module.params.get('check_commit_wait')

    # If retrieve is set and load and rollback are not set, then
    # check, diff, and commit default to False.
    if retrieve is not None and load is None and rollback is None:
        if diff is None:
            diff = False
        if check is None:
            check = False
        if commit is None:
            commit = False
    # Otherwise, diff, check, and commit default to True.
    else:
        if diff is None:
            diff = True
        if check is None:
            check = True
        if commit is None:
            commit = True

    # If load is not None, must have one of src, template, url, lines
    if load is not None:
        for option in ['src', 'lines', 'template', 'url']:
            if junos_module.params.get(option) is not None:
                break
        # for/else only executed if we didn't break out of the loop.
        else:
            junos_module.fail_json(msg="The load option (%s) is specified, "
                                       "but none of 'src', 'lines', "
                                       "'template', or 'url' are specified. "
                                       "Must specify one of the 'src', "
                                       "'lines', 'template', or 'url' options."
                                       % (load))

    # format is valid if retrieve is not None or load is not None.
    if format is not None:
        if load is None and retrieve is None:
            junos_module.fail_json(msg="The format option (%s) is specified, "
                                       "but neither 'load' or 'retrieve' are "
                                       "specified. Must specify one of "
                                       "'load' or 'retrieve' options."
                                       % (format))

    # dest_dir is valid if retrieve is not None or diff is True.
    if dest_dir is not None:
        if retrieve is None and diff is False:
            junos_module.fail_json(msg="The dest_dir option (%s) is specified,"
                                       " but neither 'retrieve' or 'diff' "
                                       "are specified. Must specify one of "
                                       "'retrieve' or 'diff' options."
                                       % (dest_dir))

    # dest is valid if retrieve is not None
    if dest is not None:
        if retrieve is None:
            junos_module.fail_json(msg="The dest option (%s) is specified,"
                                       " but 'retrieve' is not specified. "
                                       "Must specify the 'retrieve' option."
                                       % (dest))

    # diffs_file is valid if diff is True
    if diffs_file is not None:
        if diff is False:
            junos_module.fail_json(msg="The diffs_file option (%s) is "
                                       "specified, but 'diff' is false."
                                       % (diffs_file))

    # commit_empty_changes is valid if commit is True
    if commit_empty_changes is True:
        if commit is False:
            junos_module.fail_json(msg="The commit_empty_changes option "
                                       "is true, but 'commit' is false. "
                                       "The commit_empty_changes option "
                                       "may only be specified when "
                                       "'commit' is true.")

    # comment is valid if commit is True
    if comment is not None:
        if commit is False:
            junos_module.fail_json(msg="The comment option (%s) is "
                                       "specified, but 'commit' is false."
                                       % (comment))

    # confirmed is valid if commit is True
    if confirmed is not None:
        if commit is False:
            junos_module.fail_json(msg="The confirmed option (%s) is "
                                       "specified, but 'commit' is false."
                                       % (confirmed))
        # Must be greater >= 1.
        if confirmed < 1:
            junos_module.fail_json(msg="The confirmed option (%s) must have a "
                                       "positive integer value." % (confirmed))

    # check_commit_wait is valid if check is True and commit is True
    if check_commit_wait is not None:
        if commit is False:
            junos_module.fail_json(msg="The check_commit_wait option (%s) is "
                                       "specified, but 'commit' is false."
                                       % (check_commit_wait))
        if check is False:
            junos_module.fail_json(msg="The check_commit_wait option (%s) is "
                                       "specified, but 'check' is false."
                                       % (check_commit_wait))
        # Must be greater >= 1.
        if check_commit_wait < 1:
            junos_module.fail_json(msg="The check_commit_wait option (%s) "
                                       "must have a positive integer value." %
                                       (check_commit_wait))

    # Initialize the results. Assume failure until we know it's success.
    results = {'msg': 'Configuration has been: ',
               'changed': False,
               'failed': True}

    junos_module.logger.debug("Step 1 - Open a candidate configuration "
                              "database.")
    junos_module.open_configuration(mode=config_mode)
    results['msg'] += 'opened'

    junos_module.logger.debug("Step 2 - Load configuration data into the "
                              "candidate configuration database.")
    if rollback is not None:
        junos_module.rollback_configuration(id=rollback)
        # Assume configuration changed in case we don't perform a diff later.
        # If diff is set, we'll check for actual differences later.
        results['changed'] = True
        results['msg'] += ', rolled back'
    elif load is not None:
        if src is not None:
            junos_module.load_configuration(action=load,
                                            src=src,
                                            ignore_warning=ignore_warning,
                                            format=format)
            results['file'] = src
        elif lines is not None:
            junos_module.load_configuration(action=load,
                                            lines=lines,
                                            ignore_warning=ignore_warning,
                                            format=format)
        elif template is not None:
            junos_module.load_configuration(action=load,
                                            template=template,
                                            vars=vars,
                                            ignore_warning=ignore_warning,
                                            format=format)
        elif url is not None:
            junos_module.load_configuration(action=load,
                                            url=url,
                                            ignore_warning=ignore_warning,
                                            format=format)
        else:
            junos_module.fail_json(msg="The load option was set to: %s, but "
                                       "no 'src', 'lines', 'template', or "
                                       "'url' option was set." %
                                       (load))
        # Assume configuration changed in case we don't perform a diff later.
        # If diff is set, we'll check for actual differences later.
        results['changed'] = True
        results['msg'] += ', loaded'

    junos_module.logger.debug("Step 3 - Check the validity of the candidate "
                              "configuration database.")
    if check is True:
        junos_module.check_configuration()
        results['msg'] += ', checked'

    junos_module.logger.debug("Step 4 - Determine differences between the "
                              "candidate and committed configuration "
                              "databases.")
    if diff is True:
        diff = junos_module.diff_configuration()
        if diff is not None:
            results['changed'] = True
            if return_output is True:
                results['diff'] = diff
                results['diff_lines'] = diff.splitlines()
            # Save the diff output
            junos_module.save_text_output('diff', 'diff', diff)
        else:
            results['changed'] = False
        results['msg'] += ', diffed'

    junos_module.logger.debug("Step 5 - Retrieve the configuration database "
                              "from the Junos device.")
    if retrieve is not None:
        if format is None:
            format = 'text'
        (config, config_parsed) = junos_module.get_configuration(
                                      database=retrieve,
                                      format=format,
                                      options=options,
                                      filter=filter)
        if return_output is True:
            if config is not None:
                results['config'] = config
                results['config_lines'] = config.splitlines()
            if config_parsed is not None:
                results['config_parsed'] = config_parsed
        # Save the output
        format_extension = 'config' if format == 'text' else format
        junos_module.save_text_output('config', format_extension, config)
        results['msg'] += ', retrieved'

    junos_module.logger.debug("Step 6 - Commit the configuration changes.")
    if commit is True and not junos_module.check_mode:
        # Perform the commit if:
        # 1) commit_empty_changes is True
        # 2) Neither rollback or load is set. i.e. confirming a previous commit
        # 3) rollback or load is set, and there were actual changes.
        if (commit_empty_changes is True or
            (rollback is None and load is None) or
            ((rollback is not None or load is not None) and
             results['changed'] is True)):
            if check_commit_wait is not None:
                time.sleep(check_commit_wait)
            junos_module.commit_configuration(ignore_warning=ignore_warning,
                                              comment=comment,
                                              confirmed=confirmed)
            results['msg'] += ', committed'
        else:
            junos_module.logger.debug("Skipping commit. Nothing changed.")

    junos_module.logger.debug("Step 7 - Close the candidate configuration "
                              "database.")
    junos_module.close_configuration()
    results['msg'] += ', closed.'

    # If we made it this far, everything was successful.
    results['failed'] = False

    # Return response.
    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
