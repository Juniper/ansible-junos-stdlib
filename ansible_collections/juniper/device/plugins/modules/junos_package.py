#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_package
author: Peter Sprygada (@privateip)
short_description: Installs packages on remote devices running Junos
description:
- This module can install new and updated packages on remote devices running Junos.  The
  module will compare the specified package with the one running on the remote device
  and install the specified version if there is a mismatch
version_added: 1.0.0
extends_documentation_fragment:
- juniper.device.junos
options:
  src:
    description:
    - The I(src) argument specifies the path to the source package to be installed
      on the remote device in the advent of a version mismatch. The I(src) argument
      can be either a localized path or a full path to the package file to install.
    required: true
    type: path
    aliases:
    - package
  version:
    description:
    - The I(version) argument can be used to explicitly specify the version of the
      package that should be installed on the remote device.  If the I(version) argument
      is not specified, then the version is extracts from the I(src) filename.
    type: str
  reboot:
    description:
    - In order for a package to take effect, the remote device must be restarted.  When
      enabled, this argument will instruct the module to reboot the device once the
      updated package has been installed. If disabled or the remote package does not
      need to be changed, the device will not be started.
    type: bool
    default: true
  no_copy:
    description:
    - The I(no_copy) argument is responsible for instructing the remote device on
      where to install the package from.  When enabled, the package is transferred
      to the remote device prior to installing.
    type: bool
    default: false
  unlink:
    description:
    - The I(unlink) argument is responsible for instructing the remote device to
      remove the installation packages after installation.
    type: bool
    default: false
  validate:
    description:
    - The I(validate) argument is responsible for instructing the remote device to
      skip checking the current device configuration compatibility with the package
      being installed. When set to false validation is not performed.
    type: bool
    default: true
  force:
    description:
    - The I(force) argument instructs the module to bypass the package version check
      and install the packaged identified in I(src) on the remote device.
    type: bool
    default: false
  force_host:
    description:
    - The I(force_host) argument controls the way software package or bundle is added
      on remote JUNOS host and is applicable for JUNOS QFX5100 device. If the value
      is set to C(True) it will ignore any warnings while adding the host software
      package or bundle.
    type: bool
    default: false
  issu:
    description:
    - The I(issu) argument is a boolean flag when set to C(True) allows unified in-service
      software upgrade (ISSU) feature which enables you to upgrade between two different
      Junos OS releases with no disruption on the control plane and with minimal disruption
      of traffic.
    type: bool
    default: false
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
- Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
- Works with C(local) connections only.
- Since this module uses junos-eznc to establish connection with junos device the
  netconf configuration parameters needs to be passed using module options for example
  C(ssh_config) unlike other junos modules that uses C(netconf) connection type.
"""

EXAMPLES = """
# the required set of connection arguments have been purposely left off
# the examples for brevity

- name: install local package on remote device
  junipernetworks.junos.junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz

- name: install local package on remote device without rebooting
  junipernetworks.junos.junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz
    reboot: false

- name: install local package on remote device with jumpost
  junipernetworks.junos.junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz
    ssh_config: /home/user/customsshconfig
"""
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    get_device,
    junos_argument_spec,
)


try:
    from jnpr.junos.utils.sw import SW

    HAS_PYEZ = True
except ImportError:
    HAS_PYEZ = False


def install_package(module, device):
    junos = SW(device)
    package = module.params["src"]
    no_copy = module.params["no_copy"]
    unlink = module.params["unlink"]
    validate = module.params["validate"]
    force_host = module.params["force_host"]
    issu = module.params["issu"]

    def progress_log(dev, report):
        module.log(report)

    module.log("installing package")
    result = junos.install(
        package,
        progress=progress_log,
        no_copy=no_copy,
        unlink=unlink,
        validate=validate,
        force_host=force_host,
        issu=issu,
    )

    if not result:
        module.fail_json(msg="Unable to install package on device")

    if module.params["reboot"]:
        module.log("rebooting system")
        junos.reboot()


def main():
    """Main entry point for Ansible module execution"""
    argument_spec = dict(
        src=dict(type="path", required=True, aliases=["package"]),
        version=dict(),
        reboot=dict(type="bool", default=True),
        no_copy=dict(default=False, type="bool"),
        unlink=dict(default=False, type="bool"),
        validate=dict(default=True, type="bool"),
        force=dict(type="bool", default=False),
        force_host=dict(type="bool", default=False),
        issu=dict(type="bool", default=False),
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
            "It can be installed using `pip  install junos-eznc`",
        )

    result = dict(changed=False)

    do_upgrade = module.params["force"] or False

    device = get_device(module)

    if not module.params["force"]:
        device.facts_refresh()
        has_ver = device.facts.get("version")
        wants_ver = module.params["version"]
        do_upgrade = has_ver != wants_ver

    if do_upgrade:
        if not module.check_mode:
            install_package(module, device)
        result["changed"] = True

    module.exit_json(**result)


if __name__ == "__main__":
    main()
