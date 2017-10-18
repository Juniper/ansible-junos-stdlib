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
    """Documentation fragment for connection-related parameters.

    All juniper_junos_* modules share a common set of connection parameters
    which are documented in this class.

    Attributes:
        DOCUMENTATION: The documentation string defining the connection-related
                       parameters for juniper_junos_* modules.
    """

    # The connection-specific options. Defined here so it can be re-used as
    # suboptions in provider.
    CONNECTION_DOCUMENTATION = '''
  host:
    description:
      - The hostname or IP address of the Junos device to which the connection
        should be established. This is normally the Junos device itself, but
        is the hostname or IP address of a console server when connecting
        to the console of the device by setting the I(mode) option to the value
        C(telnet). This option is required, but does not have to be specified
        explicitly by the user because it defaults to
        C({{ inventory_hostname }}).
    required: True
    default: {{ inventory_hostname }}
    type: str
    aliases:
      - hostname
      - ip
  user:
    description:
      - The username used to authenticate with the Junos device. This option
        is required, but does not have to be specified explicitly by the user
        due to the below algorithm for determining the default value.
    required: True
    default: The first defined value from the following list:
             1) The ANSIBLE_NET_USERNAME environment variable.
                (used by Ansible Tower)
             2) The remote_user as defined by Ansible. Ansible sets this
                value via several methods including:
                a) -u or --user command line option.
                b) ANSIBLE_REMOTE_USER environment variable.
                c) remote_user configuration setting.
                See the Ansible documentation for the precedence used to set
                the remote_user value.
            3) The USER environment variable.
    type: str
    aliases:
      - username
  passwd:
    description:
      - The password, or ssh key's passphrase, used to authenticate with the
        Junos device. If this option is not specified, authentication is
        attempted using an empty password, or ssh key passphrase. The below
        algorithm is used to determine the default value.
    required: False
    default: The first defined value from the following list:
             1) The ANSIBLE_NET_PASSWORD environment variable.
                (used by Ansible Tower)
             2) The value specified using the -k or --ask-pass command line
                argument.
             3) none
    type: str
    aliases:
      - password
  ssh_private_key_file:
    description:
      - The path to the SSH private key file used to authenticate with the
        Junos device. If this option is not specified, and no default value is
        found using the algorithm below, then the SSH private key file
        specified in the user's SSH configuration, or the
        operating-system-specific default is used.
    default: The first defined value from the following list:
             1) The ANSIBLE_NET_SSH_KEYFILE environment variable.
                (used by Ansible Tower)
             2) The value specified using the --private-key or --key-file
                command line argument.
             3) none
    type: path
    aliases:
      - ssh_keyfile
  mode:
    description:
      - The PyEZ mode used to establish a NETCONF connection to the Junos
        device. A value of C(none) uses the default NETCONF over SSH mode.
        A value of C(telnet) results in either a direct NETCONF over Telnet
        connection to the Junos device, or a NETCONF over serial console
        connection to the Junos device using Telnet to a console server
        depending on the values of the C(host) and C(port) options. Mutually
        exclusive with C(console).
    required: False
    default: none
    choices: [ none, "telnet" ]
  console:
    description:
      - An alternate method of specifying a NETCONF over serial console
        connection to the Junos device using Telnet to a console server.
        Its value must be a string in the format
        '--telnet <console_hostname>,<console_port_number>'.
        This option is deprecated. It is present only for backwards
        compatibility. The string value of this option is exactly equivalent to
        specifying C(host) with a value of I(<console_hostname>), C(mode) with
        a value of I(telnet), and C(port) with a value of
        I(<console_port_number>). Mutually exclusive with C(mode) and C(port).
    required: False
    default: none
    type: str
  port:
    description:
      - The TCP port number used to establish the connection. Mutually
        exclusive with C(console).
    required: False
    default: 830
    type: int
  timeout:
    description:
      - Maximum number of seconds to wait for RPC responses from the Junos
        device. This option does NOT control the initial connection timeout
        value.
    required: False
    default: 30
'''

    # SUB_CONNECTION_DOCUMENTATION is just CONNECTION_DOCUMENTATION with each
    # line indented.
    SUB_CONNECTION_DOCUMENTATION = ''
    for line in CONNECTION_DOCUMENTATION.splitlines(True):
        SUB_CONNECTION_DOCUMENTATION += '    ' + line

    # Build actual DOCUMENTATION string by putting the pieces together.
    DOCUMENTATION = '''
options:''' + CONNECTION_DOCUMENTATION + '''
  provider:
    description:
      - An alternative syntax for specifying the connection options. Rather
        than specifying each connection-related top-level option, the
        connection-related options may be specified as a dictionary of
        suboptions using this option. All connection-related options must
        either be specified as top-level options or as suboptions of the
        C(provider) option. You can not combine the two methods of specifying
        connection-related options.
    required: False
    default: None
    type: dict
    suboptions:''' + SUB_CONNECTION_DOCUMENTATION + '''
requirements:
  - junos-eznc >= ''' + MIN_PYEZ_VERSION + '''
  - Python >= 2.7
'''


# The common argument specification for connecting to Junos devices.
connection_spec = {
    'host': dict(type='str',
                 # Required either in provider or at top-level.
                 required=False,
                 aliases=['hostname', 'ip'],
                 # See documentation for real default behavior.
                 # Default behavior coded in JuniperJunosActionModule.run()
                 default=None),
    'user': dict(type='str',
                 # Required either in provider or at top-level.
                 required=False,
                 aliases=['username'],
                 # See documentation for real default behavior.
                 # Default behavior coded in JuniperJunosActionModule.run()
                 default=None),
    'passwd': dict(type='str',
                   required=False,
                   aliases=['password'],
                   # See documentation for real default behavior.
                   # Default behavior coded in JuniperJunosActionModule.run()
                   default=None,
                   no_log=True),
    'ssh_private_key_file': dict(type='path',
                                 required=False,
                                 aliases=['ssh_keyfile'],
                                 # See documentation for real default behavior.
                                 # Default behavior coded in
                                 # JuniperJunosActionModule.run()
                                 default=None),
    'mode': dict(choices=[None, 'telnet'],
                 default=None),
    'console': dict(type='str',
                    required=False,
                    default=None),
    'port': dict(type='int',
                 required=False,
                 default=830),
    'timeout': dict(type='int',
                    required=False,
                    default=30),
}
# Connection arguments which are mutually exclusive.
connection_spec_mutually_exclusive = [['mode', 'console'], ['port', 'console']]
# Keys are connection options. Values are a list of task_vars to use as the
# default value.
connection_spec_fallbacks = {
    'host': ['inventory_hostname'],
    'user': ['ansible_connection_user', 'ansible_ssh_user', 'ansible_user'],
    'passwd': ['ansible_ssh_pass', 'ansible_pass'],
    'ssh_private_key_file': ['ansible_ssh_private_key_file',
                             'ansible_private_key_file']
}

# Specify the provider spec with options matching connection_spec.
provider_spec = {
    'provider': dict(type='dict',
                     options=connection_spec)
}

# The provider option is mutually exclusive with all top-level connection
# options.
provider_spec_mutually_exclusive = []
for key in connection_spec:
    provider_spec_mutually_exclusive.append(['provider', key])

# top_spec is connection_spec + provider_spec
top_spec = connection_spec
top_spec.update(provider_spec)
top_spec_mutually_exclusive = connection_spec_mutually_exclusive
top_spec_mutually_exclusive += provider_spec_mutually_exclusive

# "Hidden" arguments which are passed between the action plugin and the
# Junos module, but which should not be visible to users.
internal_spec = {
    '_module_utils_path': dict(type='path',
                               required=True,
                               default=None),
}


class JuniperJunosModule(AnsibleModule):
    """A subclass of AnsibleModule used by all juniper_junos_* modules.

    All juniper_junos_* modules share common behavior which is implemented in
    this class.

    Attributes:
        dev: An instance of a PyEZ Device() object.

    Methods:
        exit_json: Close self.dev and call parent's exit_json().
        fail_json: Close self.dev and call parent's fail_json().
        check_pyez_version: Verify installed PyEZ version is >= minimum.
        open: Open self.dev.
        close: Close self.dev.
    """

    # Method overrides
    def __init__(self,
                 argument_spec={},
                 mutually_exclusive=[],
                 min_pyez_version=MIN_PYEZ_VERSION,
                 **kwargs):
        """Initialize a new JuniperJunosModule instance.

        Combines module-specific parameters with the common parameters shared
        by all juniper_junos_* modules. Performs additional checks on options.
        Collapses any provider options to be top-level options. Checks the
        minimum PyEZ version. Creates and opens the PyEZ Device instance.

        Args:
            agument_spec: Module-specific argument_spec added to top_spec.
            mutually_exclusive: Module-specific mutually exclusive added to
                                top_spec_mutually_exclusive.
            min_pyez_version: The minimum PyEZ version required by the module.
            **kwargs: All additional keyword arguments are passed to
                      AnsibleModule.__init__().

        Returns:
            A JuniperJunosModule instance object.
        """
        # Initialize the dev attribute
        self.dev = None
        # Update argument_spec with the internal_spec
        argument_spec.update(internal_spec)
        # Update argument_spec with the top_spec
        argument_spec.update(top_spec)
        # Extend mutually_exclusive with connection_mutually_exclusive
        mutually_exclusive += top_spec_mutually_exclusive
        # Call parent's __init__()
        super(JuniperJunosModule, self).__init__(
            argument_spec=argument_spec,
            mutually_exclusive=mutually_exclusive,
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
        """Close self.dev and call parent's exit_json().

        Args:
            **kwargs: All keyword arguments are passed to
                      AnsibleModule.exit_json().
        """
        # Close the connection.
        self.close()
        # Call the parent's exit_json()
        super(JuniperJunosModule, self).exit_json(**kwargs)

    def fail_json(self, **kwargs):
        """Close self.dev and call parent's fail_json().

        Args:
            **kwargs: All keyword arguments are passed to
                      AnsibleModule.fail_json().
        """
        # Close the connection.
        self.close()
        # Call the parent's fail_json()
        super(JuniperJunosModule, self).fail_json(**kwargs)

    # JuniperJunosModule-specific methods below this point.

    def _parse_console_options(self):
        """Parse the console option value.

        Parse the console option value and turn it into the equivalent:
        host, mode, and port options.
        """
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
        """Check the minimum PyEZ version.

        Args:
            minimum: The minimum PyEZ version required.
        """
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
        """Open the self.dev PyEZ Device instance.
        """
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
        # Exceptions raised by close() or open() are all sub-classes of
        # ConnectError, so this should catch all connection-related exceptions
        # raised from PyEZ.
        except pyez_exception.ConnectError as ex:
            self.fail_json(msg='Unable to make a PyEZ connection: %s' %
                               (str(ex)))

    def close(self):
        """Close the self.dev PyEZ Device instance.
        """
        if self.dev is not None:
            try:
                # Because self.fail_json() calls self.close(), we must set
                # self.dev = None BEFORE calling dev.close() in order to avoid
                # the infinite recursion which would occur if dev.close()
                # raised a ConnectError.
                dev = self.dev
                self.dev = None
                dev.close()
            # Exceptions raised by close() are all sub-classes of
            # ConnectError, so this should catch all connection-related
            # exceptions raised from PyEZ.
            except pyez_exception.ConnectError as ex:
                self.fail_json(msg='Unable to close PyEZ connection: %s' %
                                   (str(ex)))


class JuniperJunosActionModule(ActionNormal):
    """A subclass of ActionNormal used by all juniper_junos_* modules.

    All juniper_junos_* modules share common behavior which is implemented in
    this class. This includes specific option fallback/default behavior and
    passing the "hidden" _module_utils_path option to the module.
    """
    def run(self, tmp=None, task_vars=None):
        # The new connection arguments based on fallback/defaults.
        new_connection_args = dict()

        # Get the current connection args from either provider or the top-level
        if 'provider' in self._task.args:
            connection_args = self._task.args['provider']
        else:
            connection_args = self._task.args

        # The environment variables used by Ansible Tower
        if 'user' not in connection_args:
            net_user = os.getenv('ANSIBLE_NET_USERNAME')
            if net_user is not None:
                new_connection_args['user'] = net_user
                connection_args['user'] = net_user
        if 'passwd' not in connection_args:
            net_passwd = os.getenv('ANSIBLE_NET_PASSWORD')
            if net_passwd is not None:
                new_connection_args['passwd'] = net_passwd
                connection_args['passwd'] = net_passwd
        if 'ssh_private_key_file' not in connection_args:
            net_key = os.getenv('ANSIBLE_NET_SSH_KEYFILE')
            if net_key is not None:
                new_connection_args['ssh_private_key_file'] = net_key
                connection_args['ssh_private_key_file'] = net_key

        # The values set by Ansible command line arguments, configuration
        # settings, or environment variables.
        for key in connection_spec_fallbacks:
            if key not in connection_args:
                for task_var_key in connection_spec_fallbacks[key]:
                    if task_var_key in task_vars:
                        new_connection_args[key] = task_vars[task_var_key]
                        break

        # Backwards compatible behavior to fallback to USER env. variable.
        if 'user' not in connection_args and 'user' not in new_connection_args:
            user = os.getenv('USER')
            if user is not None:
                new_connection_args['user'] = user

        # Copy the new connection arguments back into either top-level or
        # the provider dictionary.
        if 'provider' in self._task.args:
            self._task.args['provider'].update(new_connection_args)
        else:
            self._task.args.update(new_connection_args)

        # Pass the hidden _module_utils_path option
        module_utils_path = os.path.normpath(os.path.dirname(__file__))
        self._task.args['_module_utils_path'] = module_utils_path

        # Call the parent action module.
        return super(JuniperJunosActionModule, self).run(tmp, task_vars)

class JuniperJunosDeprecatedActionModule(JuniperJunosActionModule):
    def run(self, tmp=None, task_vars=None):
        print("I'm running, running, running...")
        for key in task_vars:
            if key == 'junos_get_facts':
                print("Found it: %s" (key))
        # Call the parent action module.
        return super(JuniperJunosActionModule, self).run(tmp, task_vars)
