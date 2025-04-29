# -*- coding: utf-8 -*-

#
# Copyright (c) 2017-2020, Juniper Networks Inc. All rights reserved.
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


class ModuleDocFragment(object):
    """Documentation fragment for connection-related parameters.

    All modules share a common set of connection parameters
    which are documented in this class.

    Attributes:
        CONNECTION_DOCUMENTATION: The documentation string defining the
                                  connection-related parameters for the
                                  modules.
        LOGGING_DOCUMENTATION: The documentation string defining the
                               logging-related parameters for the
                               modules.
    """

    # The connection-specific options. Defined here so it can be re-used as
    # suboptions in provider.
    CONNECTION_DOCUMENTATION = r"""
    options:
      attempts:
        description:
          - The number of times to try connecting and logging in to the Junos
            device. This option is only applicable when using C(mode = 'telnet')
            or C(mode = 'serial'). Mutually exclusive with the I(console)
            option.
        required: false
        default: 10
        type: int
      baud:
        description:
          - The serial baud rate, in bits per second, used to connect to the
            Junos device. This option is only applicable when using
            C(mode = 'serial'). Mutually exclusive with the I(console) option.
        required: false
        default: 9600
        type: int
      console:
        description:
          - An alternate method of specifying a NETCONF over serial console
            connection to the Junos device using Telnet to a console server.
            The value of this option must be a string in the format
            C(--telnet <console_hostname>,<console_port_number>).
            This option is deprecated. It is present only for backwards
            compatibility. The string value of this option is exactly equivalent
            to specifying I(host) with a value of C(<console_hostname>),
            I(mode) with a value of C(telnet), and I(port) with a value of
            C(<console_port_number>). Mutually exclusive with the I(mode),
            I(port), I(baud), and I(attempts) options.
        required: false
        default: none
        type: str
      host:
        description:
          - The hostname or IP address of the Junos device to which the
            connection should be established. This is normally the Junos device
            itself, but is the hostname or IP address of a console server when
            connecting to the console of the device by setting the I(mode)
            option to the value C(telnet). This option is required, but does not
            have to be specified explicitly by the user because it defaults to
            C({{ inventory_hostname }}).
        required: true
        default: C({{ inventory_hostname }})
        type: str
        aliases:
          - hostname
          - ip
      mode:
        description:
          - The PyEZ mode used to establish a NETCONF connection to the Junos
            device. A value of C(none) uses the default NETCONF over SSH mode.
            Depending on the values of the I(host) and I(port) options, a value
            of C(telnet) results in either a direct NETCONF over Telnet
            connection to the Junos device, or a NETCONF over serial console
            connection to the Junos device using Telnet to a console server.
            A value of C(serial) results in a NETCONF over serial console
            connection to the Junos device. Mutually exclusive with the
            I(console) option.
        required: false
        default: none
        type: str
        choices:
          - none
          - telnet
          - serial
      passwd:
        description:
          - The password, or ssh key's passphrase, used to authenticate with the
            Junos device. If this option is not specified, authentication is
            attempted using an empty password, or ssh key passphrase.
        required: false
        default: The first defined value from the following list
                 1) The C(ANSIBLE_NET_PASSWORD) environment variable.
                    (used by Ansible Tower)
                 2) The value specified using the C(-k) or C(--ask-pass)
                    command line arguments to the C(ansible) or
                    C(ansible-playbook) command.
                 3) none (An empty password/passphrase)
        type: str
        aliases:
          - password
      port:
        description:
          - The TCP port number or serial device port used to establish the
            connection. Mutually exclusive with the I(console) option.
        required: false
        default: C(830) if C(mode = none), C(23) if C(mode = 'telnet'),
                 C('/dev/ttyUSB0') if (mode = 'serial')
        type: int or str
      ssh_private_key_file:
        description:
          - The path to the SSH private key file used to authenticate with the
            Junos device. If this option is not specified, and no default value
            is found using the algorithm below, then the SSH private key file
            specified in the user's SSH configuration, or the
            operating-system-specific default is used.
          - This must be in the RSA PEM format, and not the newer OPENSSH
            format. To check if the private key is in the correct format, issue
            the command `head -n1 ~/.ssh/some_private_key` and ensure that
            it's RSA and not OPENSSH. To create a key in the RSA PEM format,
            issue the command `ssh-keygen -m PEM -t rsa -b 4096`. To convert
            an OPENSSH key to an RSA key, issue the command `ssh-keygen -p -m
            PEM -f ~/.ssh/some_private_key`
        required: false
        default: The first defined value from the following list
                 1) The C(ANSIBLE_NET_SSH_KEYFILE) environment variable.
                    (used by Ansible Tower)
                 2) The value specified using the C(--private-key) or
                    C(--key-file) command line arguments to the C(ansible) or
                    C(ansible-playbook) command.
                 3) none (the file specified in the user's SSH configuration,
                          or the operating-system-specific default)
        type: path
        aliases:
          - ssh_keyfile
      ssh_config:
        description:
          - The path to the SSH client configuration file. If this option is not
            specified, then the PyEZ Device instance by default queries file
            ~/.ssh/config.
        required: false
        type: path
      timeout:
        description:
          - The maximum number of seconds to wait for RPC responses from the
            Junos device. This option does NOT control the initial connection
            timeout value.
        required: false
        default: 30
        type: int
      user:
        description:
          - The username used to authenticate with the Junos device. This option
            is required, but does not have to be specified explicitly by the
            user due to the algorithm for determining the default value.
        required: true
        default: The first defined value from the following list
                 1) The C(ANSIBLE_NET_USERNAME) environment variable.
                    (used by Ansible Tower)
                 2) The C(remote_user) as defined by Ansible. Ansible sets this
                    value via several methods including
                    a) C(-u) or C(--user) command line arguments to the
                       C(ansible) or C(ansible-playbook) command.
                    b) C(ANSIBLE_REMOTE_USER) environment variable.
                    c) C(remote_user) configuration setting.
                    See the Ansible documentation for the precedence used to set
                    the C(remote_user) value.
                3) The C(USER) environment variable.
        type: str
        aliases:
          - username
      cs_user:
        description:
          - The username used to authenticate with the console server over SSH.
            This option is only required if you want to connect to a device over console
             using SSH as transport. Mutually exclusive with the I(console) option.
        required: false
        type: str
        aliases:
          - console_username
      cs_passwd:
        description:
          - The password used to authenticate with the console server over SSH.
            This option is only required if you want to connect to a device over console
             using SSH as transport. Mutually exclusive with the I(console) option.
        required: false
        type: str
        aliases:
          - console_password
      huge_tree:
        description:
          - Parse XML with very deep trees and long text content.
        required: false
        type: bool
        default: false
"""

    LOGGING_DOCUMENTATION = """
    options:
      logdir:
        description:
          - The path to a directory, on the Ansible control machine, where
            debugging information for the particular task is logged.
          - If this option is specified, debugging information is logged to a
            file named C({{ inventory_hostname }}.log) in the directory
            specified by the I(logdir) option.
          - The log file must be writeable. If the file already exists, it is
            appended. It is the users responsibility to delete/rotate log files.
          - The level of information logged in this file is controlled by
            Ansible's verbosity, debug options and level option in task
          - 1) By default, messages at level C(WARNING) or higher are logged.
          - 2) If the C(-v) or C(--verbose) command-line options to the
               C(ansible-playbook) command are specified, messages at level
               C(INFO) or higher are logged.
          - 3) If the C(-vv) (or more verbose) command-line option to the
               C(ansible-playbook) command is specified, or the C(ANSIBLE_DEBUG)
               environment variable is set, then messages at level C(DEBUG) or
               higher are logged.
          - 4) If C(level) is mentioned then messages at level C(level) or more are
               logged.
          - The I(logfile) and I(logdir) options are mutually exclusive. The
            I(logdir) option is recommended for all new playbooks.
        required: false
        default: none
        type: path
        aliases:
          - log_dir
      logfile:
        description:
          - The path to a file, on the Ansible control machine, where debugging
            information for the particular task is logged.
          - The log file must be writeable. If the file already exists, it is
            appended. It is the users responsibility to delete/rotate log files.
          - The level of information logged in this file is controlled by
            Ansible's verbosity, debug options and level option in task
          - 1) By default, messages at level C(WARNING) or higher are logged.
          - 2) If the C(-v) or C(--verbose) command-line options to the
               C(ansible-playbook) command are specified, messages at level
               C(INFO) or higher are logged.
          - 3) If the C(-vv) (or more verbose) command-line option to the
               C(ansible-playbook) command is specified, or the C(ANSIBLE_DEBUG)
               environment variable is set, then messages at level C(DEBUG) or
               higher are logged.
          - 4) If C(level) is mentioned then messages at level C(level) or more are
               logged.
          - When tasks are executed against more than one target host,
            one process is forked for each target host. (Up to the maximum
            specified by the forks configuration. See
            U(forks|http://docs.ansible.com/ansible/latest/intro_configuration.html#forks)
            for details.) This means that the value of this option must be
            unique per target host. This is usually accomplished by including
            C({{ inventory_hostname }}) in the I(logfile) value. It is the
            user's responsibility to ensure this value is unique per target
            host.
          - For this reason, this option is deprecated. It is maintained for
            backwards compatibility. Use the I(logdir) option in new playbooks.
            The I(logfile) and I(logdir) options are mutually exclusive.
        required: false
        default: none
        type: path
        aliases:
          - log_file
      level:
        description:
          - The level of information to be logged can be modified using this option
          - 1) By default, messages at level C(WARNING) or higher are logged.
          - 2) If the C(-v) or C(--verbose) command-line options to the
               C(ansible-playbook) command are specified, messages at level
               C(INFO) or higher are logged.
          - 3) If the C(-vv) (or more verbose) command-line option to the
               C(ansible-playbook) command is specified, or the C(ANSIBLE_DEBUG)
               environment variable is set, then messages at level C(DEBUG) or
               higher are logged.
          - 4) If C(level) is mentioned then messages at level C(level) or more are
               logged.
        required: false
        default: WARNING
        type: str
        choices:
          - INFO
          - DEBUG
"""
