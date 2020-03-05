#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2016, Damien Garros
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
module: juniper_junos_ping
version_added: "2.0.0" # of Juniper.junos role
author: Juniper Networks - Stacy Smith (@stacywsmith)
short_description: Execute ping from a Junos device
description:
  - Execute the ping command from a Junos device to a specified destination in
    order to test network reachability from the Junos device .
options:
  acceptable_percent_loss:
    description:
        - Maximum percentage of packets that may be lost and still consider the
          task not to have failed.
    required: false
    default: 0
    type: int
    aliases:
      - acceptable_packet_loss
  count:
    description:
      - Number of packets to send.
    required: false
    default: 5
    type: int
  dest:
    description:
      - The IP address, or hostname if DNS is configured on the Junos device,
        used as the destination of the ping.
    required: true
    default: none
    type: str
    aliases:
      - dest_ip
      - dest_host
      - destination
      - destination_ip
      - destination_host
  do_not_fragment:
    description:
      - Set Do Not Fragment bit on ping packets.
    required: false
    default: false
    type: bool
  interface:
    description:
      - The source interface from which the the ping is sent. If not
        specified, the default Junos algorithm for determining the source
        interface is used.
    required: false
    default: none
    type: str
  rapid:
    description:
      - Send ping requests rapidly
    required: false
    default: true
    type: bool
  routing_instance:
    description:
      - Name of the source routing instance from which the ping is
        originated. If not specified, the default routing instance is used.
    required: false
    default: none
    type: str
  size:
    description:
      - The size of the ICMP payload of the ping.
      - Total size of the IP packet is I(size) + the 20 byte IP header +
        the 8 byte ICMP header. Therefore, I(size) of C(1472) generates an IP
        packet of size 1500.
    required: false
    default: none (default size for device)
    type: int
  source:
    description:
      - The IP address, or hostname if DNS is configured on the Junos device,
        used as the source address of the ping. If not specified, the Junos
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
  ttl:
    description:
      - Maximum number of IP routers (hops) allowed between source and
        destination.
    required: false
    default: none (default ttl for device)
    type: int
'''

EXAMPLES = '''
---
- name: Examples of juniper_junos_ping
  hosts: junos-all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: Ping 192.68.1.1 with default parameters. Fails if any packets lost.
      juniper_junos_ping:
        dest: "192.68.1.1"

    - name: Ping 192.68.1.1 Allow 50% packet loss. Register response.
      juniper_junos_ping:
        dest: "192.68.1.1"
        acceptable_percent_loss: 50
      register: response
    - name: Print all keys in the response.
      debug:
        var: response

    - name: Ping 192.68.1.1. Send 20 packets. Register response.
      juniper_junos_ping:
        dest: "192.68.1.1"
        count: 20
      register: response
    - name: Print packet sent from the response.
      debug:
        var: response.packets_sent

    - name: Ping 192.68.1.1. Send 10 packets wihtout rapid. Register response.
      juniper_junos_ping:
        dest: "192.68.1.1"
        count: 10
        rapid: false
      register: response
    - name: Print the average round-trip-time from the response.
      debug:
        var: response.rtt_average

    - name: Ping www.juniper.net with ttl 15. Register response.
      juniper_junos_ping:
        dest: "www.juniper.net"
        ttl: 15
      register: response
    - name: Print the packet_loss percentage from the response.
      debug:
        var: response.packet_loss

    - name: Ping 192.68.1.1 with IP packet size of 1500. Register response.
      juniper_junos_ping:
        dest: "192.68.1.1"
        size: 1472
      register: response
    - name: Print the packets_received from the response.
      debug:
        var: response.packets_received

    - name: Ping 192.68.1.1 with do-not-fragment bit set. Register response.
      juniper_junos_ping:
        dest: "192.68.1.1"
        do_not_fragment: true
      register: response
    - name: Print the maximum round-trip-time from the response.
      debug:
        var: response.rtt_maximum

    - name: Ping 192.68.1.1 with source set to 192.68.1.2. Register response.
      juniper_junos_ping:
        dest: "192.68.1.1"
        source: "192.68.1.2"
      register: response
    - name: Print the source from the response.
      debug:
        var: response.source

    - name: Ping 192.168.1.1 from the red routing-instance.
      juniper_junos_ping:
        dest: "192.168.1.1"
        routing_instance: "red"

    - name: Ping the all-hosts multicast address from the ge-0/0/0.0 interface
      juniper_junos_ping:
        dest: "224.0.0.1"
        interface: "ge-0/0/0.0"
'''

RETURN = '''
acceptable_percent_loss:
  description:
    - The acceptable packet loss (as a percentage) for this task as specified
      by the I(acceptable_percent_loss) option.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: str
changed:
  description:
    - Indicates if the device's state has changed. Since this module
      doesn't change the operational or configuration state of the
      device, the value is always set to C(false).
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: bool
count:
  description:
    - The number of pings sent, as specified by the I(count) option.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: str
do_not_fragment:
  description:
    - Whether or not the do not fragment bit was set on the pings sent, as
      specified by the I(do_not_fragment) option.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: bool
failed:
  description:
    - Indicates if the task failed.
  returned: always
  type: bool
host:
  description:
    - The destination IP/host of the pings sent as specified by the I(dest)
      option.
    - Keys I(dest) and I(dest_ip) are also returned for backwards
      compatibility.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: str
interface:
  description:
    - The source interface of the pings sent as specified by the
      I(interface) option.
  returned: when ping successfully executed and the I(interface) option was
            specified, even if the I(acceptable_percent_loss) was exceeded.
  type: str
msg:
  description:
    - A human-readable message indicating the result.
  returned: always
  type: str
packet_loss:
  description:
    - The percentage of packets lost.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: str
packets_sent:
  description:
    - The number of packets sent.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: str
packets_received:
  description:
    - The number of packets received.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: str
rapid:
  description:
    - Whether or not the pings were sent rapidly, as specified by the
      I(rapid) option.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: bool
routing_instance:
  description:
    - The routing-instance from which the pings were sent as specified by
      the I(routing_instance) option.
  returned: when ping successfully executed and the I(routing_instance)
            option was specified, even if the I(acceptable_percent_loss) was
            exceeded.
  type: str
rtt_average:
  description:
    - The average round-trip-time, in microseconds, of all ping responses
      received.
  returned: when ping successfully executed, and I(packet_loss) < 100%.
  type: str
rtt_maximum:
  description:
    - The maximum round-trip-time, in microseconds, of all ping responses
      received.
  returned: when ping successfully executed, and I(packet_loss) < 100%.
  type: str
rtt_minimum:
  description:
    - The minimum round-trip-time, in microseconds, of all ping responses
      received.
  returned: when ping successfully executed, and I(packet_loss) < 100%.
  type: str
rtt_stddev:
  description:
    - The standard deviation of round-trip-time, in microseconds, of all ping
      responses received.
  returned: when ping successfully executed, and I(packet_loss) < 100%.
  type: str
size:
  description:
    - The size in bytes of the ICMP payload on the pings sent as specified
      by the I(size) option.
    - Total size of the IP packet is I(size) + the 20 byte IP header + the 8
      byte ICMP header. Therefore, I(size) of 1472 generates an IP packet of
      size 1500.
  returned: when ping successfully executed and the I(size) option was
            specified, even if the I(acceptable_percent_loss) was exceeded.
  type: str
source:
  description:
    - The source IP/host of the pings sent as specified by the I(source)
      option.
    - Key I(source_ip) is also returned for backwards compatibility.
  returned: when ping successfully executed and the I(source) option was
            specified, even if the I(acceptable_percent_loss) was exceeded.
  type: str
timeout:
  description:
    - The number of seconds to wait for a response from the ping RPC.
  returned: when ping successfully executed, even if the
            I(acceptable_percent_loss) was exceeded.
  type: str
ttl:
  description:
    - The time-to-live set on the pings sent as specified by the
      I(ttl) option.
  returned: when ping successfully executed and the I(ttl) option was
            specified, even if the I(acceptable_percent_loss) was exceeded.
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
    # The argument spec for the module.
    argument_spec = dict(
        dest=dict(type='str',
                  required=True,
                  aliases=['dest_ip', 'dest_host', 'destination',
                           'destination_ip', 'destination_host'],
                  default=None),
        acceptable_percent_loss=dict(type='int',
                                     required=False,
                                     aliases=['acceptable_packet_loss'],
                                     default=0),
    )

    # The portion of the argument spec that's specifically a parameter
    # to the ping RPC.
    ping_argument_spec = dict(
        count=dict(type='int',
                   required=False,
                   default=5),
        rapid=dict(type='bool',
                   required=False,
                   default=True),
        ttl=dict(type='int',
                 required=False,
                 default=None),
        size=dict(type='int',
                  required=False,
                  default=None),
        do_not_fragment=dict(type='bool',
                             required=False,
                             default=False),
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
    )

    # Add the ping RPC parameter argument spec fo the full argument_spec.
    argument_spec.update(ping_argument_spec)

    argument_spec_keys = list(argument_spec.keys())

    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=argument_spec,
        # Since this module doesn't change the device's configuration, there is
        # no additional work required to support check mode. It's inherently
        # supported.
        supports_check_mode=True
    )

    # We're going to be using params a lot
    params = junos_module.params

    # acceptable packet loss is a percentage. Check to make sure it's between
    # 0 and 100 inclusive
    if (params['acceptable_percent_loss'] > 100 or
       params['acceptable_percent_loss'] < 0):
        junos_module.fail_json(msg='The value of the acceptable_percent_loss'
                                   'option (%d) is a percentage and must have '
                                   'a value between 0 and 100.' %
                                   (params['acceptable_percent_loss']))

    # All of the params keys which are also keys in ping_argument_spec are the
    # ping_params. Omit None and False values because they don't need to be
    # passed to the RPC.
    ping_params = {'host': params.get('dest')}
    for key in ping_argument_spec:
        value = params.get(key)
        # Convert int (but not bool) to str
        if not isinstance(value, bool) and isinstance(value, int):
            params[key] = str(params[key])
            value = params.get(key)
        # None and False values are the default for the RPC and shouldn't be
        # passed to the device.
        if value is not None and value is not False:
            ping_params.update({key: value})

    # Set initial results values. Assume failure until we know it's success.
    results = {'msg': '', 'changed': False, 'failed': True}
    # Results should include all the ping params in argument_spec_keys.
    for key in argument_spec_keys:
        results[key] = params.get(key)
    # Overwrite to be a string in the results
    results['acceptable_percent_loss'] = str(
        params.get('acceptable_percent_loss'))
    # Add timeout to the response even though it's a connect parameter.
    results['timeout'] = str(params.get('timeout'))
    # Add aliases for backwards compatibility
    results.update({'host': params.get('dest'),
                    'dest_ip': params.get('dest'),
                    'source_ip': params.get('source')})

    # Execute the ping.
    results = junos_module.ping(
                  ping_params,
                  acceptable_percent_loss=params['acceptable_percent_loss'],
                  results=results)

    # Return results.
    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
