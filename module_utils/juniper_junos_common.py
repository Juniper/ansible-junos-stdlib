# -*- coding: utf-8 -*-

#
# Copyright (c) 2017, Juniper Networks Inc. All rights reserved.
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

# Ansible imports
from ansible.module_utils.basic import AnsibleModule
from ansible.plugins.action.normal import ActionModule as ActionNormal

# Standard library imports
from distutils.version import LooseVersion
import os

# Non-standard library imports and checks
try:
    from jnpr.junos.version import VERSION
    HAS_PYEZ_VERSION = VERSION
except ImportError:
    HAS_PYEZ_VERSION = None

try:
    from jnpr.junos.device import Device
    HAS_PYEZ_DEVICE = True
except ImportError:
    HAS_PYEZ_DEVICE = False

try:
    import jnpr.junos.exception as pyez_exception
    HAS_PYEZ_EXCEPTIONS = True
except ImportError:
    HAS_PYEZ_EXCEPTIONS = False


# Constants
# Minimum PyEZ version required by shared code.
MIN_PYEZ_VERSION = "2.1.7"
# Installation URL for PyEZ.
PYEZ_INSTALLATION_URL = "https://github.com/Juniper/py-junos-eznc#installation"


class ModuleDocFragment(object):
    DOCUMENTATION = '''
options:
  host:
    description:
      - The hostname or IP address of the Junos device to which the connection 
        should be established.
    required: True
    default: {{ inventory_hostname }}
    aliases:
      - hostname
      - ip
  user:
    description:
      - The username which should be used to authenticate to the Junos device.
    required: True
    default: The first defined value from the following list:
             1) The ANSIBLE_NET_USERNAME environment variable.
                (used by Ansible Tower)
             2) 
             
             
    aliases:
      - username
  passwd:
    description:
      - The password which should be used to authenticate. Defaults to
        ANSIBLE_NET_PASSWORD environment variable if defined. If not, defaults
        to None which means that SSH key-based authentication with an empty
        passphrase is attempted.
    required: False
    default: None
    aliases:
      - password
  ssh_private_key_file:
    description:
      - The path to the SSH private key file which should be used to
        authenticate. Default to ANSIBLE_NET_SSH_KEYFILE environment variable
        if defined. If not, defaults to None which means the default path to
        the SSH private key file is tried.
    required: False
    default: None
    aliases:
      - ssh_keyfile
  port:
    description:
      - The TCP port number to which the NETCONF connection should be 
        established.
    required: False
    default: 830
  timeout:
    description:
      - Number of seconds to wait for RPC responses from the Junos device.
    required: False
    default: 30
requirements:
  - junos-eznc >= ''' + MIN_PYEZ_VERSION + '''
'''


# The common specification for connecting to Junos devices.
connection_spec = {
    'host': dict(type='str',
                 # Required either in provider or at top-level.
                 required=False,
                 aliases=['hostname', 'ip'],
                 # See documentation for real default behavior.
                 # Default behavior is coded in JuniperJunosActionModule.run()
                 default=None),
    'port': dict(type='int',
                 required=False,
                 default=830),
    'timeout': dict(type='int',
                    required=False,
                    default=30),
    'user': dict(type='str',
                 # Required either in provider or at top-level.
                 required=False,
                 aliases=['username'],
                 # See documentation for real default behavior.
                 # Default behavior is coded in JuniperJunosActionModule.run()
                 default=None),
    'passwd': dict(type='str',
                   required=False,
                   aliases=['password'],
                   # See documentation for real default behavior.
                   # Default behavior is coded in JuniperJunosActionModule.run()
                   default=None,
                   no_log=True),
    'ssh_private_key_file': dict(type='path',
                                 required=False,
                                 aliases=['ssh_keyfile'],
                                 # See documentation for real default behavior.
                                 # Default behavior is coded in
                                 # JuniperJunosActionModule.run()
                                 default=None),
    'mode': dict(choices=[None, 'telnet'],
                 default=None),
    'console': dict(type='str',
                    required=False,
                    default=None),
}

connection_spec_mutually_exclusive = [['mode', 'console']]
connection_spec_required_one_of = []
connection_spec_fallbacks = {
    'host': ['inventory_hostname'],
    'user': ['ansible_connection_user', 'ansible_ssh_user', 'ansible_user'],
    'passwd': ['ansible_ssh_pass', 'ansible_pass'],
    'ssh_private_key_file': ['ansible_ssh_private_key_file',
                             'ansible_private_key_file']
}

provider_spec = {
    'provider': dict(type='dict',
                     options=connection_spec)
}

provider_spec_mutually_exclusive = []
for key in connection_spec:
    provider_spec_mutually_exclusive.append(['provider',key])

provider_spec_required_one_of = []

top_spec = connection_spec
top_spec.update(provider_spec)

top_spec_mutually_exclusive = connection_spec_mutually_exclusive
top_spec_mutually_exclusive += provider_spec_mutually_exclusive

top_spec_required_one_of = connection_spec_required_one_of
top_spec_required_one_of += provider_spec_required_one_of

# "Hidden" arguments which are passed between the action plugin and the
# Junos module, but which should not be visible to users.
internal_spec = {
    'module_utils_path': dict(type='path',
                              required=True,
                              default=None),
}


class JuniperJunosModule(AnsibleModule):
    # Method overrides
    def __init__(self,
                 argument_spec={},
                 mutually_exclusive=[],
                 required_one_of=[],
                 min_pyez_version=MIN_PYEZ_VERSION,
                 **kwargs):
        # Initialize the dev attribute
        self.dev = None
        # Update argument_spec with the internal_spec
        argument_spec.update(internal_spec)
        # Update argument_spec with the top_spec
        argument_spec.update(top_spec)
        # Extend mutually_exclusive with connection_mutually_exclusive
        mutually_exclusive += top_spec_mutually_exclusive
        required_one_of += top_spec_required_one_of
        # Call parent's __init__()
        super(JuniperJunosModule, self).__init__(
            argument_spec=argument_spec,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of,
            **kwargs)
        # Remove any arguments in internal_spec
        for arg_name in internal_spec:
            self.params.pop(arg_name)
        # Promote any provider arg_name into params
        if 'provider' in self.params and self.params['provider'] is not None:
            for arg_name, arg_value in self.params['provider'].items():
                if arg_name in self.aliases:
                    arg_name = self.aliases[arg_name]
                self.params[arg_name] = arg_value
            self.params.pop('provider')
        # Parse the console option
        self._parse_console_options()
        # Check that we have a user and host
        if not self.params.get('host'):
            self.fail_json(msg="missing required arguments: host")
        if not self.params.get('user'):
            self.fail_json(msg="missing required arguments: user")
        # Check PyEZ version
        self.check_pyez_version(min_pyez_version)
        # Open the PyEZ connection
        self.open()

    def exit_json(self, **kwargs):
        # Close the connection.
        self.close()
        # Call the parent's exit_json()
        super(JuniperJunosModule, self).exit_json(**kwargs)

    def fail_json(self, **kwargs):
        # Close the connection.
        self.close()
        # Call the parent's fail_json()
        super(JuniperJunosModule, self).fail_json(**kwargs)


    # JuniperJunosModule-specific methods below this point.

    def _parse_console_options(self):
        if self.params.get('console') is not None:
            try:
                console_string = self.params.get('console')
                # We only care about the value after --telnet
                (_, _, after) = console_string.partition('--telnet')
                # Split on ,
                host_port = after.split(',', 1)
                # Strip any leading/trailing whitespace or equal sign
                # from host
                host = host_port[0].strip('= ')
                # Try to convert port to an int.
                port = int(host_port[1])
                # Successfully parsed. Set params values
                self.params['mode'] = 'telnet'
                self.params['host'] = host
                self.params['port'] = port
                self.params.pop('console')
            except Exception:
                self.fail_json(msg="Unable to parse the console value: '%s'. "
                                   "The value of the console argument should "
                                   "be in the format '--telnet "
                                   "<console_hostname>,"
                                   "<console_port_number>'." %
                                   (console_string))

    def check_pyez_version(self, minimum):
        if HAS_PYEZ_VERSION is None:
            self.fail_json(msg='junos-eznc (aka PyEZ) >= %s is required for '
                               'this module. However junos-eznc does not '
                               'appear to be currently installed. See %s for '
                               'details on installing junos-eznc.' %
                               (minimum, PYEZ_INSTALLATION_URL))
        elif HAS_PYEZ_VERSION is not None:
            if not LooseVersion(HAS_PYEZ_VERSION) >= LooseVersion(minimum):
                self.fail_json(
                    msg='junos-eznc (aka PyEZ) >= %s is required for '
                        'this module. Version %s of junos-eznc is '
                        'currently installed. See %s for details on '
                        'upgrading junos-eznc.' %
                        (minimum,
                         HAS_PYEZ_VERSION,
                         PYEZ_INSTALLATION_URL))

    def open(self):
        if HAS_PYEZ_DEVICE is False:
            self.fail_json(msg='junos-eznc (aka PyEZ) is installed, but the '
                                 'jnpr.junos.device.Device class could not be '
                                 'imported.')
        if HAS_PYEZ_EXCEPTIONS is False:
            self.fail_json(msg='junos-eznc (aka PyEZ) is installed, but the '
                                 'jnpr.junos.exception module could not be '
                                 'imported.')

        # Move all of the connection arguments into connect_args
        connect_args = {}
        for key in connection_spec:
            if self.params.get(key) is not None:
                connect_args[key] = self.params.get(key)

        try:
            self.close()
            self.dev = Device(**connect_args)
            self.dev.open()
        except pyez_exception.ConnectError as ex:
            self.fail_json(msg='Unable to make a PyEZ connection: %s' %
                               (str(ex)))

    def close(self):
        if self.dev is not None:
            try:
                # Because self.fail_json() calls self.close(), we must set
                # self.dev = None BEFORE calling dev.close() in order to avoid
                # the infinite recursion which would occur if dev.close()
                # raised a ConnectError.
                dev = self.dev
                self.dev = None
                dev.close()
            except pyez_exception.ConnectError as ex:
                self.fail_json(msg='Unable to close PyEZ connection: %s' %
                                   (str(ex)))


class JuniperJunosActionModule(ActionNormal):
    def run(self, tmp=None, task_vars=None):
        new_connection_args = dict()
        if 'provider' in self._task.args:
            connection_args = self._task.args['provider']
        else:
            connection_args = self._task.args

        if not 'user' in connection_args:
            net_user = os.getenv('ANSIBLE_NET_USERNAME')
            if net_user is not None:
                new_connection_args['user'] = net_user
                connection_args['user'] = net_user

        if not 'passwd' in connection_args:
            net_passwd = os.getenv('ANSIBLE_NET_PASSWORD')
            if net_passwd is not None:
                new_connection_args['passwd'] = net_passwd
                connection_args['passwd'] = net_passwd

        if not 'ssh_private_key_file' in connection_args:
            net_key = os.getenv('ANSIBLE_NET_SSH_KEYFILE')
            if net_key is not None:
                new_connection_args['ssh_private_key_file'] = net_key
                connection_args['ssh_private_key_file'] = net_key

        for key in connection_spec_fallbacks:
            if not key in connection_args:
                for task_var_key in connection_spec_fallbacks[key]:
                    if task_var_key in task_vars:
                        new_connection_args[key] = task_vars[task_var_key]
                        break

        if not 'user' in new_connection_args:
            user = os.getenv('USER')
            if user is not None:
                new_connection_args['user'] = user

        if 'provider' in self._task.args:
            self._task.args['provider'].update(new_connection_args)
        else:
            self._task.args.update(new_connection_args)

        module_utils_path = os.path.normpath(os.path.dirname(__file__))
        self._task.args['module_utils_path'] = module_utils_path

        return super(JuniperJunosActionModule, self).run(tmp, task_vars)
