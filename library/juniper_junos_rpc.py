#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2016, Nitin Kumar
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
from six import iteritems

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'supported_by': 'community',
                    'status': ['stableinterface']}

DOCUMENTATION = '''
---
extends_documentation_fragment: 
  - juniper_junos_common.connection_documentation
  - juniper_junos_common.logging_documentation
module: juniper_junos_rpc
version_added: "2.0.0" # of Juniper.junos role
author: "Juniper Networks - Stacy Smith (@stacywsmith)"
short_description: Execute one or more NETCONF RPCs on a Junos device
description:
  - Execute one or more NETCONF RPCs on a Junos device.
  - Use the C(| display xml rpc) modifier to determine the equivalent RPC
    name for a Junos CLI command.  For example,
    C(show version | display xml rpc) reveals the equivalent RPC name is
    C(get-software-information).
options:
  attrs:
    description:
      - The attributes and values to the RPCs specified by the
        I(rpcs) option. The value of this option can either be a single
        dictionary of keywords and values, or a list of dictionaries
        containing keywords and values.
      - There is a one-to-one correspondence between the elements in the
        I(kwargs) list and the RPCs in the I(rpcs) list. In other words, the
        two lists must always contain the same number of elements.
    required: false
    default: none
    type: dict or list of dict
    aliases:
      - attr
  dest:
    description:
      - The path to a file, on the Ansible control machine, where the output of
        the RPC will be saved.
      - The file must be writeable. If the file already exists, it is
        overwritten.
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
    default: None
    type: path
    aliases:
      - destination
  dest_dir:
    description:
      - The path to a directory, on the Ansible control machine, where
        the output of the RPC will be saved. The output will be logged
        to a file named C({{ inventory_hostname }}_)I(rpc).I(format)
        in the I(dest_dir) directory.
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
  filter:
    description:
      - This argument only applies if the I(rpcs) option contains a single
        RPC with the value C(get-config). When used, this value specifies an
        XML filter used to restrict the portions of the configuration which are
        retrieved. See the PyEZ
        U(get_config method|http://junos-pyez.readthedocs.io/en/stable/jnpr.junos.html#jnpr.junos.rpcmeta._RpcMetaExec.get_config)
        for details on the value of this option.
    required: false
    default: none
    type: str
    aliases:
      - filter_xml
  formats:
    description:
      - The format of the reply for the RPCs specified by the
        I(rpcs) option.
      - The specified format(s) must be supported by the
        target Junos device.
      - The value of this option can either be a single
        format, or a list of formats. If a single format is specified, it
        applies to all RPCs specified by the I(rpcs) option. If a
        list of formats are specified, there must be one value in the list for
        each RPC specified by the I(rpcs) option.
    required: false
    default: xml
    type: str or list of str
    choices:
      - text
      - xml
      - json
    aliases:
      - format
      - display
      - output
  kwargs:
    description:
      - The keyword arguments and values to the RPCs specified by the
        I(rpcs) option. The value of this option can either be a single
        dictionary of keywords and values, or a list of dictionaries
        containing keywords and values.
      - There must be a one-to-one correspondence between the elements in the
        I(kwargs) list and the RPCs in the I(rpcs) list. In other words, the
        two lists must always contain the same number of elements. For RPC
        arguments which do not require a value, specify the value of True as
        shown in the :ref:`juniper_junos_rpc-examples-label`.
    required: false
    default: none
    type: dict or list of dict
    aliases:
      - kwarg
      - args
      - arg
  return_output:
    description:
      - Indicates if the output of the RPC should be returned in the
        module's response. You might want to set this option to C(false),
        and set the I(dest_dir) option, if the RPC output is very large
        and you only need to save the output rather than using it's content in
        subsequent tasks/plays of your playbook.
    required: false
    default: true
    type: bool
  rpcs:
    description:
      - A list of one or more NETCONF RPCs to execute on the Junos device.
    required: true
    default: none
    type: list
    aliases:
      - rpc
'''

EXAMPLES = '''
---
- name: Examples of juniper_junos_rpc
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: Execute single get-software-information RPC.
      juniper_junos_rpc:
        rpcs: "get-software-information"
      register: response
    - name: Print the RPC's output as a single multi-line string.
      debug:
        var: response.stdout

###### OLD EXAMPLES ##########
- junos_rpc:
  host={{ inventory_hostname }}
  rpc=get-interface-information
  dest=get_interface_information.conf
  register=junos

- junos_rpc:
  host={{ inventory_hostname }}
  rpc=get-interface-information
  kwargs="interface_name=em0"
  format=xml/text/json
  dest=get_interface_information.conf
  register=junos

# Example to fetch device configuration
- name: Get Device Configuration
  junos_rpc:
    host={{ inventory_hostname }}
    rpc=get-config
    dest=get_config.conf

# Fetch configuration over console server connection using PyEZ >= 2.0
- name: Get Device Configuration
  junos_rpc:
    host={{ inventory_hostname }}
    port=7005
    mode='telnet'
    rpc=get-config
    dest=get_config.conf

# Example to fetch device configuration
- name: Get Device Configuration for interface
  junos_rpc:
    host={{ inventory_hostname }}
    rpc=get-config
    filter_xml="<configuration><interfaces/></configuration>"
    dest=get_config.conf
  register: junos

# Example to fetch configuration in json for >=14.2
# and use it with rpc_reply
- name: Get Device Configuration
  hosts: all
  roles:
    - Juniper.junos
  connection: local
  gather_facts: no
  tasks:
    - name: Get interface information
      junos_rpc:
        host: "{{ inventory_hostname }}"
        rpc: get-interface-information
        kwargs:
          interface_name: em0
          media: True
        format: json
        dest: get_interface_information.conf
      register: junos

    - name: Print configuration
      debug: msg="{{ junos.rpc_reply }}"
###### OLD EXAMPLES ##########
'''

RETURN = '''
attrs:
  description:
    - The RPC attributes and values from the list of dictionaries in the
      I(attrs) option. This will be none if no attributes are applied to the
      RPC.
  returned: always
  type: dict
changed:
  description:
    - Indicates if the device's state has changed. Since this module doesn't
      change the operational or configuration state of the device, the value
      is always set to C(false).
    - You could use this module to execute an RPC which
      changes the operational state of the the device. For example,
      C(clear-ospf-neighbor-information). Beware, this module is unable to
      detect this situation, and will still return a I(changed) value of
      C(false) in this case.
  returned: success
  type: bool
failed:
  description:
    - Indicates if the task failed. See the I(results) key for additional
      details.
  returned: always
  type: bool
format:
  description:
    - The format of the RPC response from the list of formats in the I(formats)
      option.
  returned: always
  type: str
  choices:
    - text
    - xml
    - json
kwargs:
  description:
    - The keyword arguments from the list of dictionaries in the I(kwargs)
      option. This will be C(none) if no kwargs are applied to the RPC.
  returned: always
  type: dict
msg:
  description:
    - A human-readable message indicating the result.
  returned: always
  type: str
parsed_output:
  description:
    - The RPC reply from the Junos device parsed into a JSON datastructure.
      For XML replies, the response is parsed into JSON using the
      U(jxmlease|https://github.com/Juniper/jxmlease)
      library. For JSON the response is parsed using the Python
      U(json|https://docs.python.org/2/library/json.html) library.
    - When Ansible converts the jxmlease or native Python data structure
      into JSON, it does not guarantee that the order of dictionary/object keys
      are maintained.
  returned: when RPC executed successfully, I(return_output) is C(true),
            and the RPC format is C(xml) or C(json).
  type: dict
results:
  description:
    - The other keys are returned when a single RPC is specified for the
      I(rpcs) option. When the value of the I(rpcs) option is a list
      of RPCs, this key is returned instead. The value of this key is a
      list of dictionaries. Each element in the list corresponds to the
      RPCs in the I(rpcs) option. The keys for each element in the list
      include all of the other keys listed. The I(failed) key indicates if the
      individual RPC failed. In this case, there is also a top-level
      I(failed) key. The top-level I(failed) key will have a value of C(false)
      if ANY of the RPCs ran successfully. In this case, check the value
      of the I(failed) key for each element in the I(results) list for the
      results of individual RPCs.
  returned: when the I(rpcs) option is a list value.
  type: list of dict
rpc:
  description:
    - The RPC which was executed from the list of RPCs in the I(rpcs) option.
  returned: always
  type: str
stdout:
  description:
    - The RPC reply from the Junos device as a single multi-line string.
  returned: when RPC executed successfully and I(return_output) is C(true).
  type: str
stdout_lines:
  description:
    - The RPC reply from the Junos device as a list of single-line strings.
  returned: when RPC executed successfully and I(return_output) is C(true).
  type: list of str
'''

import os.path


try:
    # Python 2
    basestring
except NameError:
    # Python 3
    basestring = str


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
            rpcs=dict(required=True,
                      type='list',
                      aliases=['rpc'],
                      default=None),
            formats=dict(required=False,
                         type='list',
                         aliases=['format', 'display', 'output'],
                         default=None),
            kwargs=dict(required=False,
                        aliases=['kwarg', 'args', 'arg'],
                        type='str',
                        default=None),
            attrs=dict(required=False,
                       type='str',
                       aliases=['attr'],
                       default=None),
            filter=dict(required=False,
                        type='str',
                        aliases=['filter_xml'],
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
        # RPC executed. See the I(changed) key in the RETURN documentation
        # for more details.
        supports_check_mode=True,
        min_jxmlease_version=juniper_junos_common.MIN_JXMLEASE_VERSION,
    )

    # Check over rpcs
    rpcs = junos_module.params.get('rpcs')
    # Ansible allows users to specify a rpcs argument with no value.
    if rpcs is None:
        junos_module.fail_json(msg="The rpcs option must have a value.")

    # Check over formats
    formats = junos_module.params.get('formats')
    if formats is None:
        # Default to xml format
        formats = ['xml']
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
    if len(formats) != 1 and len(formats) != len(rpcs):
        junos_module.fail_json(msg="The formats option must have a single "
                                   "value, or one value per rpc. There "
                                   "are %d rpcs and %d formats." %
                                   (len(rpcs), len(formats)))
    # Same format for all rpcs
    elif len(formats) == 1 and len(rpcs) > 1:
        formats = formats * len(rpcs)

    # Check over kwargs
    kwstring = junos_module.params.get('kwargs')
    kwargs = junos_module.parse_arg_to_list_of_dicts('kwargs',
                                                     kwstring,
                                                     allow_bool_values=True)
    if kwargs is not None:
        if len(kwargs) != len(rpcs):
            junos_module.fail_json(msg="The kwargs option must have one value "
                                       "per rpc. There are %d rpcs and %d "
                                       "kwargs." %
                                       (len(rpcs), len(kwargs)))
    else:
        kwargs = [None] * len(rpcs)

    # Check over attrs
    attrstring = junos_module.params.get('attrs')
    attrs = junos_module.parse_arg_to_list_of_dicts('attrs',
                                                    attrstring)
    if attrs is not None:
        if len(attrs) != len(rpcs):
            junos_module.fail_json(msg="The attrs option must have one value"
                                       "per rpc. There are %d rpcs and %d "
                                       "attrs." %
                                       (len(rpcs), len(attrs)))
    else:
        attrs = [None] * len(rpcs)

    # Check filter
    if junos_module.params.get('filter') is not None:
        if (len(rpcs) != 1 or (rpcs[0] != 'get-config' and
                               rpcs[0] != 'get_config')):
            junos_module.fail_json(msg="The filter option is only valid "
                                       "when the rpcs option value is a "
                                       "single 'get-config' RPC.")

    results = list()
    for (rpc_string, format, kwarg, attr) in zip(rpcs, formats, kwargs, attrs):
        # Replace underscores with dashes in RPC name.
        rpc_string = rpc_string.replace('_', '-')
        # Set initial result values. Assume failure until we know it's success.
        result = {'msg': '',
                  'rpc': rpc_string,
                  'format': format,
                  'kwargs': kwarg,
                  'attrs': attr,
                  'changed': False,
                  'failed': True}

        # Execute the RPC
        try:
            if rpc_string == 'get-config':
                filter = junos_module.params.get('filter')
                if attr is None:
                    attr = {}
                if kwarg is None:
                    kwarg = {}
                junos_module.logger.debug('Executing "get-config" RPC. '
                                          'filter_xml=%s, options=%s, '
                                          'kwargs=%s',
                                          filter, str(attr), str(kwarg))
                resp = junos_module.dev.rpc.get_config(filter_xml=filter,
                                                       options=attr, **kwarg)
                result['msg'] = 'The "get-config" RPC executed successfully.'
                junos_module.logger.debug('The "get-config" RPC executed '
                                          'successfully.')
            else:
                rpc = junos_module.etree.Element(rpc_string, format=format)
                if kwarg is not None:
                    # Add kwarg
                    for (key, value) in iteritems(kwarg):
                        # Replace underscores with dashes in key name.
                        key = key.replace('_', '-')
                        sub_element = junos_module.etree.SubElement(rpc, key)
                        if not isinstance(value, bool):
                            sub_element.text = value
                if attr is not None:
                    # Add attr
                    for (key, value) in iteritems(attr):
                        # Replace underscores with dashes in key name.
                        key = key.replace('_', '-')
                        rpc.set(key, value)
                junos_module.logger.debug('Executing RPC "%s".',
                                          junos_module.etree.tostring(
                                              rpc,
                                              pretty_print=True))
                resp = junos_module.dev.rpc(rpc,
                                            normalize=bool(format == 'xml'))
                result['msg'] = 'The RPC executed successfully.'
                junos_module.logger.debug('RPC "%s" executed successfully.',
                                          junos_module.etree.tostring(
                                              rpc,
                                              pretty_print=True))
        except (junos_module.pyez_exception.ConnectError,
                junos_module.pyez_exception.RpcError) as ex:
            junos_module.logger.debug('Unable to execute RPC "%s". Error: %s',
                                      junos_module.etree.tostring(
                                          rpc,
                                          pretty_print=True), str(ex))
            result['msg'] = 'Unable to execute the RPC: %s. Error: %s' % \
                            (junos_module.etree.tostring(rpc,
                                                         pretty_print=True),
                             str(ex))
            results.append(result)
            continue

        text_output = None
        parsed_output = None
        if resp is True:
            text_output = ''
        elif (resp, junos_module.etree._Element):
            # Handle the output based on format
            if format == 'text':
                text_output = resp.text
                junos_module.logger.debug('Text output set.')
            elif format == 'xml':
                text_output = junos_module.etree.tostring(resp,
                                                          pretty_print=True)
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
        junos_module.save_text_output(rpc_string, format, text_output)
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
