#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2017, Martin Komon
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
module: juniper_junos_pmtud
version_added: "2.0.0" # of Juniper.junos role
author:
  - Martin Komon (@mkomon)
  - Juniper Networks - Stacy Smith (@stacywsmith)
short_description: Perform path MTU discovery from a Junos device to a
                   destination
description:
  - Determine the maximum IP MTU supported along a path from a Junos device to
    a user-specified destination by performing path MTU discovery (PMTUD) using
    the ping command. The reported MTU will be between min_test_size and
    I(max_size) where I(min_test_size) = (I(max_size) - I(max_range) + 1).
    If the actual path MTU is greater than I(max_size), then I(max_size) will
    be reported. If the actual path MTU is less than I(min_test_size), then a
    failure will be reported.
options:
  dest:
    description:
      - The IPv4 address, or hostname if DNS is configured on the Junos device,
        used as the destination of the PMTUD.
    required: true
    default: none
    type: str
    aliases:
      - dest_ip
      - dest_host
      - destination
      - destination_ip
      - destination_host
  interface:
    description:
      - The source interface from which the the PMTUD is performed. If not
        specified, the default Junos algorithm for determining the source
        interface is used.
    required: false
    default: none
    type: str
  max_range:
    description:
      - The maximum range of MTU values, in bytes, which will be searched
        when performing path MTU discovery. This value must be C(0) or
        a power of 2 (2^n) between C(2) and C(65536). The minimum IPv4 MTU
        value attempted when performing path MTU discovery is
        I(min_test_size) = (I(max_size) - I(max_range) + 1)
    required: false
    default: 512
    type: int
  max_size:
    description:
      - The maximum IPv4 MTU, in bytes, to attempt when performing path MTU
        discovery.
      - The value returned for I(inet_mtu) will be no more
        than this value even if the path actually supports a higher MTU.
      - This value must be between 68 and 65496.
    required: false
    default: 1500
    type: int
  routing_instance:
    description:
      - Name of the source routing instance from which the ping is
        originated.
      - If not specified, the default routing instance is used.
    required: false
    default: none
    type: str
  source:
    description:
      - The IPv4 address, or hostname if DNS is configured on the Junos device,
        used as the source address of the PMTUD. If not specified, the Junos
        default algorithm for determining the source address is used.
    required: false
    default: none
    type: str
    aliases:
      - source_ip
      - source_host
      - src
      - src_ip
      - src_host
'''

EXAMPLES = '''
---
- name: Examples of juniper_junos_mtud
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: Perform PMTUD to 192.68.1.1 with default parameters.
      juniper_junos_pmtud:
        dest: "192.68.1.1"

    - name: Perform PMTUD to 192.68.1.1. Register response.
      juniper_junos_pmtud:
        dest: "192.68.1.1"
      register: response
    - name: Print the discovered MTU.
      debug:
        var: response.inet_mtu

    - name: Perform PMTUD to 192.68.1.1. Search all possible MTU values.
      juniper_junos_pmtud:
        dest: "192.68.1.1"
        max_size: 65496
        max_range: 65536
      register: response
    - name: Print the discovered MTU.
      debug:
        var: response.inet_mtu

    - name: Perform PMTUD to 192.68.1.1. Source from ge-0/0/0.0 interface.
      juniper_junos_pmtud:
        dest: "192.68.1.1"
        interface: "ge-0/0/0.0"
      register: response
    - name: Print the discovered MTU.
      debug:
        var: response.inet_mtu

    - name: Perform PMTUD to 192.68.1.1. Source from 192.168.1.2.
      juniper_junos_pmtud:
        dest: "192.68.1.1"
        source: "192.168.1.2"
      register: response
    - name: Print the discovered MTU.
      debug:
        var: response.inet_mtu

    - name: Perform PMTUD to 192.68.1.1. Source from the red routing-instance.
      juniper_junos_pmtud:
        dest: "192.68.1.1"
        routing_instance: "red"
      register: response
    - name: Print the discovered MTU.
      debug:
        var: response.inet_mtu
'''

RETURN = '''
changed:
  description:
    - Indicates if the device's state has changed. Since this module
      doesn't change the operational or configuration state of the
      device, the value is always set to C(false).
  returned: when PMTUD successfully executed.
  type: bool
failed:
  description:
    - Indicates if the task failed.
  returned: always
  type: bool
host:
  description:
    - The destination IP/host of the PMTUD as specified by the I(dest)
      option.
    - Keys I(dest) and I(dest_ip) are also returned for backwards
      compatibility.
  returned: when PMTUD successfully executed.
  type: str
inet_mtu:
  description:
    - The IPv4 path MTU size in bytes to the I(dest). This is the lesser of
      I(max_size) and the actual path MTU to I(dest). If the actual path
      MTU is less than I(min_test_size), then a failure is reported. Where
          I(min_test_size) = (I(max_size) - I(max_range) + 1)
  returned: when PMTUD successfully executed.
  type: str
interface:
  description:
    - The source interface of the PMTUD as specified by the I(interface)
      option.
  returned: when the I(interface) option was specified.
  type: str
routing_instance:
  description:
    - The routing-instance from which the PMTUD was performed as specified by
      the I(routing_instance) option.
  returned: when the I(routing_instance) option was specified.
  type: str
source:
  description:
    - The source IP/host of the PMTUD as specified by the I(source)
      option.
    - Key I(source_ip) is also returned for backwards compatibility.
  returned: when the I(source) option was specified.
  type: str
warnings:
  description:
    - A list of warning strings, if any, produced from the ping.
  returned: when warnings are present
  type: list
'''


"""From Ansible 2.1, Ansible uses Ansiballz framework for assembling modules
But custom module_utils directory is supported from Ansible 2.3
Reference for the issue: https://groups.google.com/forum/#!topic/ansible-project/J8FL7Z1J1Mw """

# Ansiballz packages module_utils into ansible.module_utils
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import juniper_junos_common


def main():
    # Constants for MTU size
    INET_MIN_MTU_SIZE = 68  # As prescribed by RFC 791, Section 3.2 -
    # Fragmentation and Reassembly.
    INET_MAX_MTU_SIZE = 65496  # Size of inet header's total length field is
    # 16 bits. Therefore max inet packet size is 2^16
    # or 65536, but Junos only supports max IP size
    # of 65496 for the ping command in order to
    # accomodate a (potentially) maximum sized IP
    # header.

    # Constants for the size of headers
    INET_HEADER_SIZE = 20
    ICMP_HEADER_SIZE = 8
    INET_AND_ICMP_HEADER_SIZE = INET_HEADER_SIZE + ICMP_HEADER_SIZE

    # Choices for max_size
    MAX_SIZE_CHOICES = [0] + list(map(lambda x: 2 ** x, range(1, 17)))

    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            dest=dict(type='str',
                      required=True,
                      aliases=['dest_ip', 'dest_host', 'destination',
                               'destination_ip', 'destination_host'],
                      default=None),
            max_size=dict(type='int',
                          required=False,
                          default=1500),
            max_range=dict(type='int',
                           required=False,
                           choices=MAX_SIZE_CHOICES,
                           default=512),
            source=dict(type='str',
                        required=False,
                        aliases=['source_ip', 'source_host', 'src',
                                 'src_ip', 'src_host'],
                        default=None),
            interface=dict(type='str',
                           required=False,
                           default=None),
            routing_instance=dict(type='str',
                                  required=False,
                                  default=None),
        ),
        # Since this module doesn't change the device's configuration, there is
        # no additional work required to support check mode. It's inherently
        # supported.
        supports_check_mode=True
    )

    # We're going to be using params a lot
    params = junos_module.params

    # max_size must be between INET_MIN_MTU_SIZE and INET_MAX_MTU_SIZE
    if (params['max_size'] < INET_MIN_MTU_SIZE or
       params['max_size'] > INET_MAX_MTU_SIZE):
        junos_module.fail_json(msg='The value of the max_size option(%d) '
                                   'must be between %d and %d.' %
                                   (params['max_size'], INET_MIN_MTU_SIZE,
                                    INET_MAX_MTU_SIZE))

    # Initialize ping parameters.
    ping_params = {'host': params.get('dest'),
                   'count': '3',
                   'rapid': True,
                   'inet': True,
                   'do_not_fragment': True}

    # Add optional ping parameters
    o_ping_params = {}
    if params['source'] is not None:
        o_ping_params['source'] = params['source']
    if params['interface'] is not None:
        o_ping_params['interface'] = params['interface']
    if params['routing_instance'] is not None:
        o_ping_params['routing_instance'] = params['routing_instance']
    ping_params.update(o_ping_params)

    # Set initial results values. Assume failure until we know it's success.
    results = {'changed': False,
               'failed': True,
               'inet_mtu': 0,
               'host': params.get('dest')}
    # Results should include all the o_ping_params.
    for key in o_ping_params:
        results[key] = ping_params.get(key)
    # Add aliases for backwards compatibility
    results.update({'dest': ping_params.get('host'),
                    'dest_ip': ping_params.get('host'),
                    'source_ip': ping_params.get('source')})

    # Execute a minimally-sized ping just to verify basic connectivity.
    junos_module.logger.debug("Verifying basic connectivity.")
    ping_params['size'] = str(INET_MIN_MTU_SIZE -
                              INET_AND_ICMP_HEADER_SIZE)
    results_for_minimal = dict(results)
    results_for_minimal = junos_module.ping(ping_params,
                                            acceptable_percent_loss=100,
                                            results=results_for_minimal)
    if int(results_for_minimal.get('packet_loss', 100)) == 100:
        results['msg'] = "Basic connectivity to %s failed." % (results['host'])
        junos_module.exit_json(**results)

    # Initialize test_size and step
    test_size = params['max_size']
    step = params['max_range']
    min_test_size = test_size - (params['max_range'] - 1)
    if min_test_size < INET_MIN_MTU_SIZE:
        min_test_size = INET_MIN_MTU_SIZE

    while True:
        if test_size < INET_MIN_MTU_SIZE:
            test_size = INET_MIN_MTU_SIZE
        if test_size > params['max_size']:
            test_size = params['max_size']
        junos_module.logger.debug("Probing with size: %d", test_size)
        step = step // 2 if step >= 2 else 0
        ping_params['size'] = str(test_size - INET_AND_ICMP_HEADER_SIZE)
        current_results = dict(results)
        current_results = junos_module.ping(ping_params,
                                            acceptable_percent_loss=100,
                                            results=current_results)
        loss = int(current_results.get('packet_loss', 100))
        if loss < 100 and test_size == params['max_size']:
            # ping success with max test_size, save and break
            results['failed'] = False
            results['inet_mtu'] = test_size
            break
        elif loss < 100:
            # ping success, increase test_size
            results['failed'] = False
            results['inet_mtu'] = test_size
            test_size += step
        else:
            # ping fail, lower size
            test_size -= step
        if step < 1:
            break

    if results.get('inet_mtu', 0) == 0:
        junos_module.fail_json(msg='The MTU of the path to %s is less than '
                                   'the minimum tested size(%d). Try '
                                   'decreasing max_size(%d) or increasing '
                                   'max_range(%d).' % (results['host'],
                                                       min_test_size,
                                                       params['max_size'],
                                                       params['max_range']),
                               **results)

    # Return results.
    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
