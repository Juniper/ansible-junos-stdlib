#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2017-2024, Juniper Networks Inc. All rights reserved.
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


__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "supported_by": "community",
    "status": ["stableinterface"],
}

DOCUMENTATION = """
---
extends_documentation_fragment:
  - juniper.device.juniper_junos_doc.connection_documentation
  - juniper.device.juniper_junos_doc.logging_documentation
module: file_copy
author: "Juniper Networks - Dinesh Babu (@dineshbaburam91)"
short_description: File put and get over SCP/FTP module
description:
  - Copy file over SCP/FTP to and from a Juniper device
options:
  protocol:
    description:
        - Set the protocols to transfer the file
    required: false
    default: scp
    choices:
        - scp
        - ftp
    type: str
  local_dir:
    description:
      - path of the local directory where the file is located
        or needs to be copied to
    required: true
    type: str
  remote_dir:
    description:
      - path of the directory on the remote device where the file is located
        or needs to be copied to
    required: true
    type: str
  file:
    description:
      - Name of the file to copy to/from the remote device
    required: true
    type: str
  transfer_filename:
    description:
      - Name of the transfer file to copy to/from the remote device
    required: false
    type: str
  checksum:
    description:
      - Validate the file using MD5 algorithm check
    required: false
    type: bool
  action:
    description:
      - Type of operation to execute, currently only support get and put
    required: true
    type: str
"""

EXAMPLES = """
---
- name: Examples of juniper_device_file_copy
  hosts: all
  connection: local
  gather_facts: false
  tasks:
    - name: Copy a log file on a remote device locally
      juniper.device.file_copy:
        protocol: scp
        remote_dir: /var/log
        local_dir: /tmp
        action: get
        checksum: True
        file: log.txt
    - name: Copy a local file into /var/tmp on the remote device
      juniper.device.file_copy:
        protocol: ftp
        remote_dir: /var/tmp
        local_dir: /tmp
        action: put
        checksum: False
        file: license.txt
"""

RETURN = """
changed:
  description:
    - Indicates if the device's state has changed.
  returned: when the file has been successfully copied.
  type: bool
"""

"""From Ansible 2.1, Ansible uses Ansiballz framework for assembling modules
But custom module_utils directory is supported from Ansible 2.3
Reference for the issue: https://groups.google.com/forum/#!topic/ansible-project/J8FL7Z1J1Mw """

# Ansiballz packages module_utils into ansible.module_utils

from ansible_collections.juniper.device.plugins.module_utils import configuration as cfg
from ansible_collections.juniper.device.plugins.module_utils import juniper_junos_common


def main():

    # The argument spec for the module.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=dict(
            protocol=dict(
                type="str",
                choices=["scp", "ftp"],
                required=False,
                default="scp",
            ),
            local_dir=dict(type="str", required=True, default=None),
            remote_dir=dict(type="str", required=True, default=None),
            file=dict(type="str", required=True, default=None),
            transfer_filename=dict(type="str", required=False, default=None),
            checksum=dict(type="bool", required=False, default=True),
            action=dict(
                type="str",
                choices=["put", "get"],
                required=True,
                default=None,
            ),
        ),
        supports_check_mode=True,
        min_jxmlease_version=cfg.MIN_JXMLEASE_VERSION,
    )

    # Set initial results values. Assume failure until we know it's success.
    results = {"msg": "", "changed": False, "failed": False}
    output = []
    # We're going to be using params a lot
    params = junos_module.params

    params["remote_dir"]
    transfer_filename = params["transfer_filename"]
    protocol = params["protocol"]
    check_sum = params["checksum"]

    if params["action"] == "put":
        local_file = params["local_dir"] + "/" + params["file"]
        if transfer_filename:
            remote_file = params["remote_dir"] + "/" + transfer_filename
        else:
            remote_file = params["remote_dir"] + "/" + params["file"]
        if protocol == "scp":
            if check_sum is False:
                output = junos_module.scp_file_copy_put_without_checksum(
                    local_file,
                    remote_file,
                )
            else:
                output = junos_module.scp_file_copy_put(local_file, remote_file)
        elif protocol == "ftp":
            if check_sum is False:
                output = junos_module.ftp_file_copy_put_without_checksum(
                    local_file,
                    remote_file,
                )
            else:
                output = junos_module.ftp_file_copy_put(local_file, remote_file)
        results["msg"] = output[0]
        results["changed"] = output[1]
    elif params["action"] == "get":
        remote_file = params["remote_dir"] + "/" + params["file"]
        if transfer_filename:
            local_file = params["local_dir"] + "/" + transfer_filename
        else:
            local_file = params["local_dir"] + "/" + params["file"]
        if params["protocol"] == "scp":
            if check_sum is False:
                output = junos_module.scp_file_copy_get_without_checksum(
                    remote_file,
                    local_file,
                )
            else:
                output = junos_module.scp_file_copy_get(remote_file, local_file)
        elif params["protocol"] == "ftp":
            if check_sum is False:
                output = junos_module.ftp_file_copy_get_without_checksum(
                    remote_file,
                    local_file,
                )
            else:
                output = junos_module.ftp_file_copy_get(remote_file, local_file)
        results["msg"] = output[0]
        results["changed"] = output[1]

    # Return results.
    junos_module.exit_json(**results)


if __name__ == "__main__":
    main()
