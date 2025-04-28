#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_ping
short_description: Tests reachability using ping from devices running Juniper JUNOS
description:
- Tests reachability using ping from devices running Juniper JUNOS to a remote destination.
- Tested against Junos (17.3R1.10)
- For a general purpose network module, see the M(ansible.netcommon.net_ping) module.
- For Windows targets, use the M(ansible.windows.win_ping) module instead.
- For targets running Python, use the M(ansible.builtin.ping) module instead.
version_added: 1.0.0
extends_documentation_fragment:
- junipernetworks.junos.junos
author:
- Nilashish Chakraborty (@NilashishC)
options:
  dest:
    description:
    - The IP Address or hostname (resolvable by the device) of the remote node.
    type: str
    required: true
  df_bit:
    description:
    - Determines whether to set the DF bit.
    type: bool
    default: false
  rapid:
    description:
    - Determines whether to send the packets rapidly.
    type: bool
    default: false
  count:
    description:
    - Number of packets to send to check reachability.
    type: int
    default: 5
  source:
    description:
    - The IP Address to use while sending the ping packet(s).
    type: str
  interface:
    description:
    - The source interface to use while sending the ping packet(s).
    type: str
  ttl:
    description:
    - The time-to-live value for the ICMP packet(s).
    type: int
  size:
    description:
    - Determines the size (in bytes) of the ping packet(s).
    type: int
  interval:
    description:
    - Determines the interval (in seconds) between consecutive pings.
    type: int
  state:
    description:
    - Determines if the expected result is success or fail.
    type: str
    choices:
    - absent
    - present
    default: present
notes:
- For a general purpose network module, see the M(ansible.netcommon.net_ping) module.
- For Windows targets, use the M(ansible.windows.win_ping) module instead.
- For targets running Python, use the M(ansible.builtin.ping) module instead.
- This module works only with connection C(network_cli).
"""

EXAMPLES = """
- name: Test reachability to 10.10.10.10
  junipernetworks.junos.junos_ping:
    dest: 10.10.10.10

- name: Test reachability to 10.20.20.20 using source and size set
  junipernetworks.junos.junos_ping:
    dest: 10.20.20.20
    size: 1024
    ttl: 128

- name: Test unreachability to 10.30.30.30 using interval
  junipernetworks.junos.junos_ping:
    dest: 10.30.30.30
    interval: 3
    state: absent

- name: Test reachability to 10.40.40.40 setting count and interface
  junipernetworks.junos.junos_ping:
    dest: 10.40.40.40
    interface: fxp0
    count: 20
    size: 512

- name: Test reachability to 10.50.50.50 using do-not-fragment and rapid
  junipernetworks.junos.junos_ping:
    dest: 10.50.50.50
    df_bit: true
    rapid: true
"""

RETURN = """
commands:
  description: List of commands sent.
  returned: always
  type: list
  sample: ["ping 10.8.38.44 count 10 source 10.8.38.38 ttl 128"]
packet_loss:
  description: Percentage of packets lost.
  returned: always
  type: str
  sample: "0%"
packets_rx:
  description: Packets successfully received.
  returned: always
  type: int
  sample: 20
packets_tx:
  description: Packets successfully transmitted.
  returned: always
  type: int
  sample: 20
rtt:
  description: The round trip time (RTT) stats.
  returned: when ping succeeds
  type: dict
  sample: {"avg": 2, "max": 8, "min": 1, "stddev": 24}
"""

import re

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    get_connection,
)


def main():
    """main entry point for module execution"""
    argument_spec = dict(
        count=dict(type="int", default=5),
        dest=dict(type="str", required=True),
        df_bit=dict(type="bool", default=False),
        rapid=dict(type="bool", default=False),
        source=dict(),
        interface=dict(),
        ttl=dict(type="int"),
        size=dict(type="int"),
        interval=dict(type="int"),
        state=dict(
            type="str",
            choices=["absent", "present"],
            default="present",
        ),
    )

    module = AnsibleModule(argument_spec=argument_spec)

    count = module.params["count"]
    dest = module.params["dest"]
    df_bit = module.params["df_bit"]
    rapid = module.params["rapid"]
    source = module.params["source"]
    size = module.params["size"]
    ttl = module.params["ttl"]
    interval = module.params["interval"]
    interface = module.params["interface"]
    warnings = list()

    results = {"changed": False}
    if warnings:
        results["warnings"] = warnings

    results["commands"] = build_ping(
        dest,
        count,
        size,
        interval,
        source,
        ttl,
        interface,
        df_bit,
        rapid,
    )
    conn = get_connection(module)

    ping_results = conn.get(results["commands"])

    rtt_info, rate_info = None, None
    for line in ping_results.split("\n"):
        if line.startswith("round-trip"):
            rtt_info = line
        if line.startswith("%s packets transmitted" % count):
            rate_info = line

    if rtt_info:
        rtt = parse_rtt(rtt_info)
        for k, v in rtt.items():
            if rtt[k] is not None:
                rtt[k] = float(v)
        results["rtt"] = rtt

    pkt_loss, rx, tx = parse_rate(rate_info)
    results["packet_loss"] = str(pkt_loss) + "%"
    results["packets_rx"] = int(rx)
    results["packets_tx"] = int(tx)

    validate_results(module, pkt_loss, results)

    module.exit_json(**results)


def build_ping(
    dest,
    count,
    size=None,
    interval=None,
    source=None,
    ttl=None,
    interface=None,
    df_bit=False,
    rapid=False,
):
    cmd = "ping {0} count {1}".format(dest, str(count))

    if source:
        cmd += " source {0}".format(source)

    if interface:
        cmd += " interface {0}".format(interface)

    if ttl:
        cmd += " ttl {0}".format(str(ttl))

    if size:
        cmd += " size {0}".format(str(size))

    if interval:
        cmd += " interval {0}".format(str(interval))

    if df_bit:
        cmd += " do-not-fragment"

    if rapid:
        cmd += " rapid"

    return cmd


def parse_rate(rate_info):
    rate_re = re.compile(
        r"(?P<tx>\d*) packets transmitted,(?:\s*)(?P<rx>\d*) packets received,(?:\s*)(?P<pkt_loss>\d*)% packet loss",
    )
    rate = rate_re.match(rate_info)

    return rate.group("pkt_loss"), rate.group("rx"), rate.group("tx")


def parse_rtt(rtt_info):
    rtt_re = re.compile(
        r"round-trip (?:.*)=(?:\s*)(?P<min>\d+\.\d+).(?:\d*)/(?P<avg>\d+\.\d+).(?:\d*)/(?P<max>\d*\.\d*).(?:\d*)/(?P<stddev>\d*\.\d*)",
    )
    rtt = rtt_re.match(rtt_info)

    return rtt.groupdict()


def validate_results(module, loss, results):
    state = module.params["state"]
    if state == "present" and int(loss) == 100:
        module.fail_json(msg="Ping failed unexpectedly", **results)
    elif state == "absent" and int(loss) < 100:
        module.fail_json(msg="Ping succeeded unexpectedly", **results)


if __name__ == "__main__":
    main()
