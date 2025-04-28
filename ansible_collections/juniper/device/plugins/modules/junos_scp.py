#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_scp
author: Christian Giese (@GIC-de)
short_description: Transfer files from or to remote devices running Junos
description:
- This module transfers files via SCP from or to remote devices running Junos.
version_added: 1.0.0
extends_documentation_fragment:
- junipernetworks.junos.junos
deprecated:
  why: Updated modules released with more functionality
  alternative: Use M(ansible.netcommon.net_get), M(ansible.netcommon.net_put) instead.
  removed_at_date: '2025-01-01'
options:
  src:
    description:
    - The C(src) argument takes a single path, or a list of paths to be transferred.
      The argument C(recursive) must be C(true) to transfer directories.
    required: true
    type: list
    elements: path
  dest:
    description:
    - The C(dest) argument specifies the path in which to receive the files.
    type: path
    default: .
  recursive:
    description:
    - The C(recursive) argument enables recursive transfer of files and directories.
    type: bool
    default: no
  remote_src:
    description:
    - The C(remote_src) argument enables the download of files (I(scp get)) from the
      remote device. The default behavior is to upload files (I(scp put)) to the remote
      device.
    type: bool
    default: no
  ssh_private_key_file:
    description:
    - The C(ssh_private_key_file) argument is path to the SSH private key file. This
      can be used if you need to provide a private key rather than loading the key
      into the ssh-key-ring/environment
    type: path
  ssh_config:
    description:
    - The C(ssh_config) argument is path to the SSH configuration file. This can be
      used to load SSH information from a configuration file. If this option is not
      given by default ~/.ssh/config is queried.
    type: path
  provider:
    description:
    - B(Deprecated)
    - 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or
      C(connection: netconf).'
    - For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).
    - HORIZONTALLINE
    - A dict object containing connection details.
    type: dict
    suboptions:
      host:
        description:
        - Specifies the DNS host name or address for connecting to the remote device
          over the specified transport.  The value of host is used as the destination
          address for the transport.
        type: str
      port:
        description:
        - Specifies the port to use when building the connection to the remote device.  The
          port value will default to the well known SSH port of 22 (for C(transport=cli))
          or port 830 (for C(transport=netconf)) device.
        type: int
      username:
        description:
        - Configures the username to use to authenticate the connection to the remote
          device.  This value is used to authenticate the SSH session. If the value
          is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME)
          will be used instead.
        type: str
      password:
        description:
        - Specifies the password to use to authenticate the connection to the remote
          device.   This value is used to authenticate the SSH session. If the value
          is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD)
          will be used instead.
        type: str
      timeout:
        description:
        - Specifies the timeout in seconds for communicating with the network device
          for either connecting or sending commands.  If the timeout is exceeded before
          the operation is completed, the module will error.
        type: int
      ssh_keyfile:
        description:
        - Specifies the SSH key to use to authenticate the connection to the remote
          device.   This value is the path to the key used to authenticate the SSH
          session. If the value is not specified in the task, the value of environment
          variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.
        type: path
      transport:
        description:
        - Configures the transport connection to use when connecting to the remote
          device.
        type: str
        default: netconf
        choices:
        - cli
        - netconf
requirements:
- junos-eznc
- ncclient (>=v0.5.2)
notes:
- This module requires the netconf system service be enabled on the remote device
  being managed.
- Tested against vMX JUNOS version 17.3R1.10.
- Works with C(local) connections only.
- Since this module uses junos-eznc to establish connection with junos device the
  netconf configuration parameters needs to be passed using module options for example
  C(ssh_config) unlike other junos modules that uses C(netconf) connection type.
"""

EXAMPLES = """
# the required set of connection arguments have been purposely left off
# the examples for brevity
- name: upload local file to home directory on remote device
  junipernetworks.junos.junos_scp:
    src: test.tgz

- name: upload local file to tmp directory on remote device
  junipernetworks.junos.junos_scp:
    src: test.tgz
    dest: /tmp/

- name: download file from remote device
  junipernetworks.junos.junos_scp:
    src: test.tgz
    remote_src: true

- name: ssh config file path for jumphost config
  junipernetworks.junos.junos_scp:
    src: test.tgz
    remote_src: true
    ssh_config: /home/user/customsshconfig
"""

RETURN = """
changed:
  description: always true
  returned: always
  type: bool
"""
from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    get_device,
    junos_argument_spec,
)


try:
    from jnpr.junos.utils.scp import SCP

    HAS_PYEZ = True
except ImportError:
    HAS_PYEZ = False


def transfer_files(module, device):
    dest = module.params["dest"]
    recursive = module.params["recursive"]

    with SCP(device) as scp:
        for src in module.params["src"]:
            if module.params["remote_src"]:
                scp.get(src.strip(), local_path=dest, recursive=recursive)
            else:
                scp.put(src.strip(), remote_path=dest, recursive=recursive)


def main():
    """Main entry point for Ansible module execution"""
    argument_spec = dict(
        src=dict(type="list", required=True, elements="path"),
        dest=dict(type="path", required=False, default="."),
        recursive=dict(type="bool", default=False),
        remote_src=dict(type="bool", default=False),
        ssh_private_key_file=dict(type="path"),
        ssh_config=dict(type="path"),
    )

    argument_spec.update(junos_argument_spec)
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if module.params["provider"] is None:
        module.params["provider"] = {}

    if not HAS_PYEZ:
        module.fail_json(
            msg="junos-eznc is required but does not appear to be installed. "
            "It can be installed using `pip install junos-eznc`",
        )

    result = dict(changed=True)

    if not module.check_mode:
        # open pyez connection and transfer files via SCP
        try:
            device = get_device(module)
            transfer_files(module, device)
        except Exception as ex:
            module.fail_json(msg=to_native(ex))
        finally:
            try:
                # close pyez connection and ignore exceptions
                device.close()
            except Exception:
                pass

    module.exit_json(**result)


if __name__ == "__main__":
    main()
