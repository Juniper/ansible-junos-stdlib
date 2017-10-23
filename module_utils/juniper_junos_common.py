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
import json
import logging
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
    import jnpr.junos.utils.sw
    HAS_PYEZ_SW = True
except ImportError:
    HAS_PYEZ_SW = False

try:
    import jnpr.junos.utils.config
    HAS_PYEZ_CONFIG = True
except ImportError:
    HAS_PYEZ_CONFIG = False

try:
    import jnpr.junos.exception as pyez_exception
    HAS_PYEZ_EXCEPTIONS = True
except ImportError:
    HAS_PYEZ_EXCEPTIONS = False

try:
    from lxml import etree
    HAS_LXML_ETREE_VERSION = '.'.join(map(str, etree.LXML_VERSION))
except ImportError:
    HAS_LXML_ETREE_VERSION = None

try:
    import jxmlease
    HAS_JXMLEASE_VERSION = jxmlease.__version__
except ImportError:
    HAS_JXMLEASE_VERSION = None


# Constants
# Minimum PyEZ version required by shared code.
MIN_PYEZ_VERSION = "2.1.7"
# Installation URL for PyEZ.
PYEZ_INSTALLATION_URL = "https://github.com/Juniper/py-junos-eznc#installation"
# Minimum lxml version required by shared code.
MIN_LXML_ETREE_VERSION = "3.2.4"
# Installation URL for LXML.
LXML_ETREE_INSTALLATION_URL = "http://lxml.de/installation.html"
# Minimum jxmlease version required by shared code.
MIN_JXMLEASE_VERSION = "1.0.1"
# Installation URL for jxmlease.
JXMLEASE_INSTALLATION_URL = "http://jxmlease.readthedocs.io/en/stable/install.html"


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

    LOGGING_DOCUMENTATION = '''
  logfile:
    description:
      - The path to a file, on the Ansible control machine, where debugging
        information for the particular task is logged.
      - The log file must be writeable. If the file already exists, it is
        appended. It is the users responsibility to delete/rotate log files.
      - The level of information logged in this file is controlled by Ansible's
        verbosity and debug options:
        1) By default, messages at level WARNING or higher are logged.
        2) If the -v or --verbose command-line options to ansible-playbook are
           specified, messages at level INFO or higher are logged.
        3) If the -vv (or more verbose) command-line option to ansible-playbook
           is specified, or the ANSIBLE_DEBUG environment variable is set,
           then messages at level DEBUG or higher are logged.
      - NOTE: When tasks are executed against more than one target host,
        one process is forked for each target host. (Up to the maximum
        specified by the forks configuration. See
        U(http://docs.ansible.com/ansible/latest/intro_configuration.html#forks)
        for details.) This means that the value of this option must be unique
        per target host. This is usually accomplished by including
        {{ inventory_hostname }} in the C(logfile) value. It is the user's
        responsibility to ensure this value is unique per target host.
      - For this reason, this option is deprecated. It is maintained for
        backwards compatibility. Use the C(logdir) option in new playbooks. The
        C(logfile) and C(logdir) options are mutually exclusive.
    required: false
    default: None
    type: path
    aliases:
      - log_file
  logdir:
    description:
      - The path to a directory, on the Ansible control machine, where
        debugging information for the particular task is logged. Debugging
        information will be logged to a file named {{ inventory_hostname }}.log
        in the C(logdir) directory.
      - The log file must be writeable. If the file already exists, it is
        appended. It is the users responsibility to delete/rotate log files.
      - The level of information logged in this file is controlled by Ansible's
        verbosity and debug options:
        1) By default, messages at level WARNING or higher are logged.
        2) If the -v or --verbose command-line options to ansible-playbook are
           specified, messages at level INFO or higher are logged.
        3) If the -vv (or more verbose) command-line option to ansible-playbook
           is specified, or the ANSIBLE_DEBUG environment variable is set,
           then messages at level DEBUG or higher are logged.
      - The C(logfile) and C(logdir) options are mutually exclusive. The
        C(logdir) option is recommended for all new playbooks.
    required: false
    default: None
    type: path
    aliases:
      - log_dir
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
notes:
  - The NETCONF system service must be enabled on the target Junos device.
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

# Specify the logging spec.
logging_spec = {
    'logfile': dict(type='path', required=False, default=None),
    'logdir': dict(type='path', required=False, default=None)
}

# The logdir and logfile options are mutually exclusive.
logging_spec_mutually_exclusive = ['logfile', 'logdir']

# Other logging names which should be logged to the logfile
additional_logger_names = ['ncclient', 'paramiko']

# top_spec is connection_spec + provider_spec + logging_spec
top_spec = connection_spec
top_spec.update(provider_spec)
top_spec.update(logging_spec)
top_spec_mutually_exclusive = connection_spec_mutually_exclusive
top_spec_mutually_exclusive += provider_spec_mutually_exclusive
top_spec_mutually_exclusive += logging_spec_mutually_exclusive

# "Hidden" arguments which are passed between the action plugin and the
# Junos module, but which should not be visible to users.
internal_spec = {
    '_module_utils_path': dict(type='path',
                               required=True,
                               default=None),
    '_module_name': dict(type='str',
                         required=True,
                         default=None),
}

# Known configuration formats
CONFIG_FORMAT_CHOICES = ['xml', 'set', 'text', 'json']
# Known configuration databases
CONFIG_DATABASE_CHOICES = ['candidate', 'committed']


class JuniperJunosModule(AnsibleModule):
    """A subclass of AnsibleModule used by all juniper_junos_* modules.

    All juniper_junos_* modules share common behavior which is implemented in
    this class.

    Attributes:
        dev: An instance of a PyEZ Device() object.

    Methods:
        exit_json: Close self.dev and call parent's exit_json().
        fail_json: Close self.dev and call parent's fail_json().
        check_pyez: Verify the PyEZ library is present and functional.
        check_lxml_etree: Verify the lxml Etree library is present and
                          functional.
        check_jxmlease: Verify the Jxmlease library is present and functional.
        open: Open self.dev.
        close: Close self.dev.
    """

    # Method overrides
    def __init__(self,
                 argument_spec={},
                 mutually_exclusive=[],
                 min_pyez_version=MIN_PYEZ_VERSION,
                 min_lxml_etree_version=MIN_LXML_ETREE_VERSION,
                 min_jxmlease_version=MIN_JXMLEASE_VERSION,
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
            min_lxml_etree_version: The minimum lxml Etree version required by
                                    the module.
            min_jxmlease_version: The minimum Jxmlease version required by the
                                  module.
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
        self.module_name = self.params.get('_module_name')
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
        self.check_pyez(min_pyez_version,
                        check_device=True,
                        check_sw=True,
                        check_config=True,
                        check_exception=True)
        self.pyez_exception = pyez_exception
        # Check LXML Etree
        self.check_lxml_etree(min_lxml_etree_version)
        self.etree = etree
        # Check jxmlease
        self.check_jxmlease(min_jxmlease_version)
        self.jxmlease = jxmlease
        # Setup logging.
        self.logger = self._setup_logging()
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
        self.logger.debug("Exit JSON: %s", kwargs)
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
        if hasattr(self, 'logger'):
            self.logger.debug("Fail JSON: %s", kwargs)
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

    def _setup_logging(self):
        """Setup logging for the module.

        Performs several tasks to setup logging for the module. This includes:
        1) Creating a Logger instance object for the name
           jnpr.ansible_module.<mod_name>.
        2) Sets the level for the Logger object depending on verbosity and
           debug settings specified by the user.
        3) Sets the level for other Logger objects specified in
           additional_logger_names depending on verbosity and
           debug settings specified by the user.
        4) If the logfile or logdir option is specified, attach a FileHandler
           instance which logs messages from jnpr.ansible_module.<mod_name> or
           any of the names in additional_logger_names.

        Returns:
            Logger instance object for the name jnpr.ansible_module.<mod_name>.
        """
        class CustomAdapter(logging.LoggerAdapter):
            """
            Prepend the hostname, in brackets, to the log message.
            """
            def process(self, msg, kwargs):
                return '[%s] %s' % (self.extra['host'], msg), kwargs

        # Default level to log.
        level = logging.WARNING
        # Log more if ANSIBLE_DEBUG or -v[v] is set.
        if self._debug is True:
            level = logging.DEBUG
        elif self._verbosity == 1:
            level = logging.INFO
        elif self._verbosity > 1:
            level = logging.DEBUG
        # Get the logger object to be used for our logging.
        logger = logging.getLogger('jnpr.ansible_module.' + self.module_name)
        # Attach the NullHandler to avoid any errors if no logging is needed.
        logger.addHandler(logging.NullHandler())
        # Set the logging level for the modules logging. This will also control
        # the amount of logging which goes into Ansible's log file.
        logger.setLevel(level)
        # Set the logging level for additional names. This will also control
        # the amount of logging which goes into Ansible's log file.
        for name in additional_logger_names:
            logging.getLogger(name).setLevel(level)
        # Get the name of the logfile based on logfile or logdir options.
        logfile = None
        if self.params.get('logfile') is not None:
            logfile = self.params.get('logfile')
        elif self.params.get('logdir') is not None:
            logfile = os.path.normpath(self.params.get('logdir') + '/' +
                                       self.params.get('host') + '.log')
        # Create the FileHandler and attach it.
        if logfile is not None:
            try:
                handler = logging.FileHandler(logfile, mode='a')
                handler.setLevel(level)
                # Create a custom formatter.
                formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                # add formatter to handler
                handler.setFormatter(formatter)
                # Handler should log anything from the 'jnpr' namespace to
                # catch PyEZ, JSNAPY, etc. logs.
                jnpr_logger = logging.getLogger('jnpr')
                jnpr_logger.addHandler(handler)
                for name in additional_logger_names:
                    logging.getLogger(name).addHandler(handler)
            except IOError as ex:
                self.fail_json(msg="Unable to open the log file %s. %s" %
                                   (logfile, str(ex)))
        # Use the CustomAdapter to add host information.
        return CustomAdapter(logger, {'host': self.params.get('host')})

    def _check_library(self,
                       library_name,
                       installed_version,
                       installation_url,
                       minimum=None,
                       library_nickname=None):
        """Check if library_name is installed and version is >= minimum.

        Args:
            library_name: The name of the library to check.
            installed_version: The currently installed version, or None if it's
                               not installed.
            installation_url: The URL with instructions on installing
                              library_name
            minimum: The minimum version required.
                     Default = None which means no version check.
            library_nickname: The library name with any nickname.
                     Default = library_name.
        Failures:
            - library_name not installed (unable to import).
            - library_name installed_version < minimum.
        """
        if library_nickname is None:
            library_nickname = library_name
        if installed_version is None:
            if minimum is not None:
                self.fail_json(msg='%s >= %s is required for this module. '
                                   'However, %s does not appear to be '
                                   'currently installed. See %s for '
                                   'details on installing %s.' %
                                   (library_nickname, minimum, library_name,
                                    installation_url, library_name))
            else:
                self.fail_json(msg='%s is required for this module. However, '
                                   '%s does not appear to be currently '
                                   'installed. See %s for details on '
                                   'installing %s.' %
                                   (library_nickname, library_name,
                                    installation_url, library_name))
        elif installed_version is not None and minimum is not None:
            if not LooseVersion(installed_version) >= LooseVersion(minimum):
                self.fail_json(
                    msg='%s >= %s is required for this module. Version %s of '
                        '%s is currently installed. See %s for details on '
                        'upgrading %s.' %
                        (library_nickname, minimum, installed_version,
                         library_name, installation_url, library_name))

    def check_pyez(self, minimum=None,
                   check_device=False,
                   check_sw=False,
                   check_config=False,
                   check_exception=False):
        """Check PyEZ is available and version is >= minimum.

        Args:
            minimum: The minimum PyEZ version required.
                     Default = None which means no version check.
            check_device: Indicates whether to check for PyEZ Device object.
            check_exception: Indicates whether to check for PyEZ exceptions.

        Failures:
            - PyEZ not installed (unable to import).
            - PyEZ version < minimum.
            - check_device and PyEZ Device object can't be imported
            - check_exception and PyEZ excepetions can't be imported
        """
        self._check_library('junos-eznc', HAS_PYEZ_VERSION,
                            PYEZ_INSTALLATION_URL, minimum=minimum,
                            library_nickname='junos-eznc (aka PyEZ)')
        if check_device is True:
            if HAS_PYEZ_DEVICE is False:
                self.fail_json(msg='junos-eznc (aka PyEZ) is installed, but '
                                   'the jnpr.junos.device.Device class could '
                                   'not be imported.')
        if check_sw is True:
            if HAS_PYEZ_SW is False:
                self.fail_json(msg='junos-eznc (aka PyEZ) is installed, but '
                                   'the jnpr.junos.utils.sw class could '
                                   'not be imported.')
        if check_config is True:
            if HAS_PYEZ_CONFIG is False:
                self.fail_json(msg='junos-eznc (aka PyEZ) is installed, but '
                                   'the jnpr.junos.utils.config class could '
                                   'not be imported.')
        if check_exception is True:
            if HAS_PYEZ_EXCEPTIONS is False:
                self.fail_json(msg='junos-eznc (aka PyEZ) is installed, but '
                                   'the jnpr.junos.exception module could not '
                                   'be imported.')

    def check_jxmlease(self, minimum=None):
        """Check jxmlease is available and version is >= minimum.

        Args:
            minimum: The minimum jxmlease version required.
                     Default = None which means no version check.

        Failures:
            - jxmlease not installed.
            - jxmlease version < minimum.
        """
        self._check_library('jxmlease', HAS_JXMLEASE_VERSION,
                            JXMLEASE_INSTALLATION_URL, minimum=minimum)

    def check_lxml_etree(self, minimum=None):
        """Check lxml etree is available and version is >= minimum.

        Args:
            minimum: The minimum lxml version required.
                     Default = None which means no version check.

        Failures:
            - lxml not installed.
            - lxml version < minimum.
        """
        self._check_library('lxml Etree', HAS_LXML_ETREE_VERSION,
                            LXML_ETREE_INSTALLATION_URL, minimum=minimum)

    def open(self):
        """Open the self.dev PyEZ Device instance.

        Failures:
            - ConnectError: When unable to make a PyEZ connection.
        """
        # Move all of the connection arguments into connect_args
        connect_args = {}
        for key in connection_spec:
            if self.params.get(key) is not None:
                connect_args[key] = self.params.get(key)

        try:
            self.close()
            log_connect_args = dict(connect_args)
            log_connect_args['passwd'] = 'NOT_LOGGING_PARAMETER'
            self.logger.debug("Creating device parameters: %s",
                              log_connect_args)
            timeout = connect_args.pop('timeout')
            self.dev = Device(**connect_args)
            self.logger.debug("Opening device.")
            self.dev.open()
            self.logger.debug("Device opened.")
            self.logger.debug("Setting default device timeout to %d.", timeout)
            self.dev.timeout = timeout
            self.logger.debug("Device timeout set.")
        # Exceptions raised by close() or open() are all sub-classes of
        # ConnectError, so this should catch all connection-related exceptions
        # raised from PyEZ.
        except pyez_exception.ConnectError as ex:
            self.fail_json(msg='Unable to make a PyEZ connection: %s' %
                               (str(ex)))

    def add_sw(self):
        """Add an instance of jnp.junos.utils.sw.SW() to self.
        """
        self.sw = jnpr.junos.utils.sw.SW(self.dev)

    def close(self, raise_exceptions=False):
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
                self.logger.debug("Device closed.")
            # Exceptions raised by close() are all sub-classes of
            # ConnectError or RpcError, so this should catch all
            # exceptions raised from PyEZ.
            except (pyez_exception.ConnectError,
                    pyez_exception.RpcError) as ex:
                if raise_exceptions is True:
                    raise ex
                else:
                    # Ignore exceptions from closing. We're about to exit
                    # anyway and they will just mask the real error that
                    # happened.
                    pass

    def get_configuration(self, database='committed', format='text',
                          options={}, filter=None):
        """Return the device configuration in the specified format.

        Return the datbase device configuration datbase in the format format.
        Pass the options specified in the options dict and the filter specified
        in the filter argument.

        Args:
            database: The configuration database to return. Choices are defined
                      in CONFIG_DATABASE_CHOICES.
            format: The format of the configuration to return. Choices are
                    defined in CONFIG_FORMAT_CHOICES.
        Returns:
            A tuple containing:
            - The configuration in the requested format as a single
              multi-line string. Returned for all formats.
            - The "parsed" configuration as a JSON string. Set when
              format == 'xml' or format == 'json'. None when format == 'text'
              or format == 'set'
        Failures:
            - Invalid database.
            - Invalid format.
            - Options not a dict.
            - Invalid filter.
            - Format not understood by device.
        """
        if database not in CONFIG_DATABASE_CHOICES:
            self.fail_json(msg='The configuration database % is not in the '
                               'list of recognized configuration databases: '
                               '%s.' %
                               (database, str(CONFIG_DATABASE_CHOICES)))

        if format not in CONFIG_FORMAT_CHOICES:
            self.fail_json(msg='The configuration format % is not in the list '
                               'of recognized configuration formats: %s.' %
                               (format, str(CONFIG_FORMAT_CHOICES)))

        options.update({'database': database,
                        'format': format})

        if self.dev is None:
            self.open()

        self.logger.debug("Retrieving device configuration. Options: %s  "
                          "Filter %s", str(options), str(filter))
        config = None
        try:
            config = self.dev.rpc.get_config(options=options,
                                             filter_xml=filter)
            self.logger.debug("Configuration retrieved.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            self.fail_json(msg='Unable to retrieve the configuration: %s' %
                               (str(ex)))

        return_val = (None, None)
        if format == 'text':
            if not isinstance(config, self.etree._Element):
                self.fail_json(msg='Unexpected configuration type returned. '
                                   'Configuration is: %s' % (str(config)))
            if config.tag != 'configuration-text':
                self.fail_json(msg='Unexpected XML tag returned. '
                                   'Configuration is: %s' %
                                   (etree.tostring(config, pretty_print=True)))
            return_val = (config.text, None)
        elif format == 'set':
            if not isinstance(config, self.etree._Element):
                self.fail_json(msg='Unexpected configuration type returned. '
                                   'Configuration is: %s' % (str(config)))
            if config.tag != 'configuration-set':
                self.fail_json(msg='Unexpected XML tag returned. '
                                   'Configuration is: %s' %
                                   (etree.tostring(config, pretty_print=True)))
            return_val = (config.text, config.text.splitlines())
        elif format == 'xml':
            if not isinstance(config, self.etree._Element):
                self.fail_json(msg='Unexpected configuration type returned. '
                                   'Configuration is: %s' % (str(config)))
            if config.tag != 'configuration':
                self.fail_json(msg='Unexpected XML tag returned. '
                                   'Configuration is: %s' %
                                   (etree.tostring(config, pretty_print=True)))
            return_val = (etree.tostring(config, pretty_print=True),
                          jxmlease.parse_etree(config))
        elif format == 'json':
            return_val = (json.dumps(config), config)
        else:
            self.fail_json(msg='Unable to return configuration in %s format.' %
                               (format))
        return return_val

    def ping(self, params, acceptable_percent_loss=0, results={}):
        """Execute a ping command with the parameters specified in params.

        Args:
            params: dict of parameters passed directly to the ping RPC.
            acceptable_percent_loss: integer specifying maximum percentage of
                                     packets that may be lost and still
                                     consider the ping not to have failed.
            results: dict of results which should be included in the return
                     value, or which should be included if fail_json() is
                     called due to a failure.

        Returns:
            A dict of results. It contains all key/value pairs in the results
            argument plus the keys below. (The keys below will overwrite
            any corresponding key which exists in the results argument):

            msg: (str) A human-readable message indicating the result.
            packet_loss: (str) The percentage of packets lost.
            packets_sent: (str) The number of packets sent.
            packets_received: (str) The number of packets received.
            rtt_minimum: (str) The minimum round-trip-time, in microseconds,
                               of all ping responses received.
            rtt_maximum: (str) The maximum round-trip-time, in microseconds,
                               of all ping responses received.
            rtt_average: (str) The average round-trip-time, in microseconds,
                               of all ping responses received.
            rtt_stddev: (str) The standard deviation of round-trip-time, in
                              microseconds, of all ping responses received.
            warnings: (list of str) A list of warning strings, if any, produced
                                    from the ping.
            failed: (bool) Indicates if the ping failed. The ping fails
                           when packet_loss > acceptable_percent_loss.

        Fails:
            - If the ping RPC produces an exception.
            - If there are errors present in the results.
        """
        # Assume failure until we know success.
        results['failed'] = True

        # Execute the ping.
        try:
            self.logger.debug("Executing ping with parameters: %s",
                              str(params))
            resp = self.dev.rpc.ping(normalize=True, **params)
            self.logger.debug("Ping executed.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            self.fail_json(msg='Unable to execute ping: %s' % (str(ex)))

        if not isinstance(resp, self.etree._Element):
            self.fail_json(msg='Unexpected ping response: %s' % (str(resp)))

        resp_xml = self.etree.tostring(resp, pretty_print=True)

        # Fail if any errors in the results
        errors = resp.findall(
                     "rpc-error[error-severity='error']/error-message")
        if len(errors) != 0:
            # Create a comma-plus-space-seperated string of the errors.
            # Calls the text attribute of each element in the errors list.
            err_msg = ', '.join(map(lambda err: err.text, errors))
            results['msg'] = "Ping returned errors: %s" % (err_msg)
            self.exit_json(**results)

        # Add any warnings into the results
        warnings = resp.findall(
                       "rpc-error[error-severity='warning']/error-message")
        if len(warnings) != 0:
            # Create list of the text attributes of each element in the
            # warnings list.
            results['warnings'] = list(map(lambda warn: warn.text, warnings))

        # Try to find probe summary
        probe_summary = resp.find('probe-results-summary')
        if probe_summary is None:
            results['msg'] = "Probe-results-summary not found in response: " \
                             "%s" % (resp_xml)
            self.exit_json(**results)

        # Extract some required fields and some optional fields
        r_fields = {}
        r_fields['packet_loss'] = probe_summary.findtext('packet-loss')
        r_fields['packets_sent'] = probe_summary.findtext('probes-sent')
        r_fields['packets_received'] = probe_summary.findtext(
                                           'responses-received')
        o_fields = {}
        o_fields['rtt_minimum'] = probe_summary.findtext('rtt-minimum')
        o_fields['rtt_maximum'] = probe_summary.findtext('rtt-maximum')
        o_fields['rtt_average'] = probe_summary.findtext('rtt-average')
        o_fields['rtt_stddev'] = probe_summary.findtext('rtt-stddev')

        # Make sure we got values for required fields.
        for key in r_fields:
            if r_fields[key] is None:
                results['msg'] = 'Expected field %s not found in ' \
                                 'response: %s' % (key, resp_xml)
                self.exit_json(**results)
        # Add the required fields to the result.
        results.update(r_fields)

        # Extract integer packet loss
        packet_loss = 100
        if results['packet_loss'] is not None:
            try:
                packet_loss = int(results['packet_loss'])
            except ValueError:
                results['msg'] = 'Packet loss %s not an integer. ' \
                                 'Response: %s' % \
                                 (results['packet_loss'], resp_xml)
                self.exit_json(**results)

        if packet_loss < 100:
            # Optional fields are present if packet_loss < 100
            for key in o_fields:
                if o_fields[key] is None:
                    results['msg'] = 'Expected field %s not found in ' \
                                     'response: %s' % (key, resp_xml)
                    self.exit_json(**results)
        # Add the o_fields to the result (even if they're None)
        results.update(o_fields)

        # Set the result message.
        results['msg'] = 'Loss %s%%, (Sent %s | Received %s)' % \
                         (results['packet_loss'],
                          results['packets_sent'],
                          results['packets_received'])

        # Was packet loss within limits? If so, we didn't fail.
        if packet_loss <= acceptable_percent_loss:
            results['failed'] = False

        return results


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
        # Pass the hidden _module_name option
        self._task.args['_module_name'] = self._task.action

        # Call the parent action module.
        return super(JuniperJunosActionModule, self).run(tmp, task_vars)
