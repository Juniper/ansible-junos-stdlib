# (c) 2016 Red Hat Inc.
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
import xmltodict

__metaclass__ = type

DOCUMENTATION = """author: Ansible Networking Team
connection: pyez
short_description: Use pyez to run command on JUNOS appliances
description:
- This connection plugin provides a connection to remote devices over the junos-pyez library.
options:
  host:
    description:
    - Specifies the remote device FQDN or IP address to establish the SSH connection
      to.
    default: inventory_hostname
    vars:
    - name: ansible_host
  port:
    type: int
    description:
    - Specifies the port on the remote device that listens for connections when establishing
      the SSH connection.
    ini:
    - section: defaults
      key: remote_port
    env:
    - name: ANSIBLE_REMOTE_PORT
    vars:
    - name: ansible_port
  remote_user:
    description:
    - The username used to authenticate to the remote device when the SSH connection
      is first established.  If the remote_user is not specified, the connection will
      use the username of the logged in user.
    - Can be configured from the CLI via the C(--user) or C(-u) options.
    ini:
    - section: defaults
      key: remote_user
    env:
    - name: ANSIBLE_REMOTE_USER
    vars:
    - name: ansible_user
  password:
    description:
    - Configures the user password used to authenticate to the remote device when
      first establishing the SSH connection.
    vars:
    - name: ansible_password
    - name: ansible_ssh_pass
    - name: ansible_ssh_password
  pyez_console:
    description:
    - console option.
    ini:
    - section: pyez_connection
      key: console
    env:
    - name: ANSIBLE_PYEZ_CONSOLE
    vars:
    - name: ansible_pyez_console    
  private_key_file:
    description:
    - The private SSH key or certificate file used to authenticate to the remote device
      when first establishing the SSH connection.
    ini:
    - section: defaults
      key: private_key_file
    env:
    - name: ANSIBLE_PRIVATE_KEY_FILE
    vars:
    - name: ansible_private_key_file
  host_key_auto_add:
    type: boolean
    description:
    - By default, Ansible will prompt the user before adding SSH keys to the known
      hosts file.  Since persistent connections such as network_cli run in background
      processes, the user will never be prompted.  By enabling this option, unknown
      host keys will automatically be added to the known hosts file.
    - Be sure to fully understand the security implications of enabling this option
      on production systems as it could create a security vulnerability.
    default: false
    ini:
    - section: pyez_connection
      key: host_key_auto_add
    env:
    - name: ANSIBLE_HOST_KEY_AUTO_ADD
  persistent_connect_timeout:
    type: int
    description:
    - Configures, in seconds, the amount of time to wait when trying to initially
      establish a persistent connection.  If this value expires before the connection
      to the remote device is completed, the connection will fail.
    default: 30
    ini:
    - section: persistent_connection
      key: connect_timeout
    env:
    - name: ANSIBLE_PERSISTENT_CONNECT_TIMEOUT
    vars:
    - name: ansible_connect_timeout
  persistent_command_timeout:
    type: int
    description:
    - Configures, in seconds, the amount of time to wait for a command to return from
      the remote device.  If this timer is exceeded before the command returns, the
      connection plugin will raise an exception and close.
    default: 30
    ini:
    - section: persistent_connection
      key: command_timeout
    env:
    - name: ANSIBLE_PERSISTENT_COMMAND_TIMEOUT
    vars:
    - name: ansible_command_timeout
  persistent_log_messages:
    type: boolean
    description:
    - This flag will enable logging the command executed and response received from
      target device in the ansible log file. For this option to work 'log_path' ansible
      configuration option is required to be set to a file path with write access.
    - Be sure to fully understand the security implications of enabling this option
      as it could create a security vulnerability by logging sensitive information
      in log file.
    default: false
    ini:
    - section: persistent_connection
      key: log_messages
    env:
    - name: ANSIBLE_PERSISTENT_LOG_MESSAGES
    vars:
    - name: ansible_persistent_log_messages
  pyez_ssh_config:
    description:
    - This variable is used to enable bastion/jump host with netconf connection. If
      set to True the bastion/jump host ssh settings should be present in ~/.ssh/config
      file, alternatively it can be set to custom ssh configuration file path to read
      the bastion/jump host settings.
    ini:
    - section: pyez_connection
      key: ssh_config
    env:
    - name: ANSIBLE_PYEZ_SSH_CONFIG
    vars:
    - name: ansible_pyez_ssh_config
"""
import pickle

from ansible.errors import AnsibleConnectionFailure, AnsibleError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.connection import NetworkConnectionBase, ensure_connect

import json
import logging

# Non-standard library imports and checks
try:
    from jnpr.junos.version import VERSION

    HAS_PYEZ_VERSION = VERSION
except ImportError:
    HAS_PYEZ_VERSION = None

try:
    import jnpr.junos.device

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
    import jnpr.junos.op
    import jnpr.junos.factory.factory_loader
    import jnpr.junos.factory.table

    HAS_PYEZ_OP_TABLE = True
except ImportError:
    HAS_PYEZ_OP_TABLE = False

try:
    import jnpr.junos.exception as pyez_exception

    HAS_PYEZ_EXCEPTIONS = True
except ImportError:
    HAS_PYEZ_EXCEPTIONS = False

try:
    from jnpr.jsnapy import SnapAdmin, __version__

    HAS_JSNAPY_VERSION = __version__
except ImportError:
    HAS_JSNAPY_VERSION = None
# Most likely JSNAPy 1.2.0 with https://github.com/Juniper/jsnapy/issues/263
except TypeError:
    HAS_JSNAPY_VERSION = "possibly 1.2.0"

try:
    from lxml import etree

    HAS_LXML_ETREE_VERSION = ".".join(map(str, etree.LXML_VERSION))
except ImportError:
    HAS_LXML_ETREE_VERSION = None

try:
    import jxmlease

    HAS_JXMLEASE_VERSION = jxmlease.__version__
except ImportError:
    HAS_JXMLEASE_VERSION = None

try:
    import yaml

    HAS_YAML_VERSION = yaml.__version__
except ImportError:
    HAS_YAML_VERSION = None

try:
    # Python 2
    basestring
except NameError:
    # Python 3
    basestring = str

#import q
logging.getLogger("ncclient").setLevel(logging.INFO)

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)

# Supported configuration modes
CONFIG_MODE_CHOICES = ['exclusive', 'private']


class Connection(NetworkConnectionBase):
    """NetConf connections"""

    transport = "junipernetworks.pyez.pyez"
    has_pipelining = False

    def __init__(self, play_context, new_stdin, *args, **kwargs):
        super(Connection, self).__init__(play_context, new_stdin, *args, **kwargs)
        self.dev = None

    @property
    @ensure_connect
    def manager(self):
        return self.dev

    def _connect(self):

        self.queue_message("log", "ssh connection done, starting junos-eznc")
        self.open()
        if not self.dev.connected:
            return 1, b"", b"not connected"

        self._connected = True

        super(Connection, self)._connect()

        self._sub_plugin = {"name": "pyez", "obj": self.dev}
        self.queue_message(
            "vvvv",
            "created pyez connection type"
        )
        return (
            0,
            to_bytes(self.dev._conn.session_id, errors="surrogate_or_strict"),
            b"",
        )

    def open(self):
        """Open the self.dev PyEZ Device instance.
        Failures:
            - ConnectError: When unable to make a PyEZ connection.
        """
        # Move all of the connection arguments into connect_args
        connect_args = {}
        connect_args['host'] = self.get_option('host')
        connect_args['user'] = self.get_option('remote_user')
        connect_args['passwd'] = self.get_option('password')
        connect_args['ssh_private_key_file'] = self.get_option('private_key_file')
        connect_args['ssh_config'] = self.get_option('pyez_ssh_config')
        connect_args['timeout'] = self.get_option('persistent_connect_timeout')
        try:
            log_connect_args = dict(connect_args)
            log_connect_args["passwd"] = "NOT_LOGGING_PARAMETER"

            self.queue_message("vvvv", "Creating device parameters: %s" % log_connect_args)
            timeout = connect_args.pop("timeout")
            self.dev = jnpr.junos.device.Device(**connect_args)
            self.queue_message("vvvv", "Opening device.")
            self.dev.open()
            self.queue_message("vvvv", "Device opened.")

            self.dev.timeout = self.get_option('persistent_command_timeout')
            self.queue_message("vvvv", "Setting default device timeout to %d." % timeout)
        # Exceptions raised by close() or open() are all sub-classes of
        # ConnectError, so this should catch all connection-related exceptions
        # raised from PyEZ.
        except pyez_exception.ConnectError as ex:
            raise AnsibleError(msg="Unable to make a PyEZ connection: %s" % (str(ex)))

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
            # ConnectError or RpcError, so this should catch all
            # exceptions raised from PyEZ.
            except (pyez_exception.ConnectError, pyez_exception.RpcError) as ex:
                # Ignore exceptions from closing. We're about to exit
                # anyway and they will just mask the real error that
                # happened.
                pass
        super(Connection, self).close()

    @ensure_connect
    def get_capabilities(self):
        return json.dumps({'network_api': 'pyez'})

    def get_config(self, filter_xml=None, options=None, model=None,
                         namespace=None, remove_ns=True, **kwarg):
        resp = self.dev.rpc.get_config(filter_xml, options, model, namespace, remove_ns, **kwarg)
        return etree.tostring(resp)

    def get_rpc_resp(self,rpc, ignore_warning=None):
        # data comes in JSON format, needs to be converted
        rpc_val = xmltodict.unparse(rpc)
        rpc_val = rpc_val.encode('utf-8')
        parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
        rpc_etree = etree.fromstring(rpc_val, parser=parser)
        resp = self.dev.rpc(rpc_etree, normalize=bool(format == 'xml'), ignore_warning=ignore_warning)
        return etree.tostring(resp)

    def get_facts(self):
        return dict(self.dev.facts)

    def ping_device(self, normalize=True, **params):
        resp = self.dev.rpc.ping(normalize, **params)
        rpc_str = etree.tostring(resp)
        return rpc_str

    def get_chassis_inventory(self):
        resp = self.dev.rpc.get_chassis_inventory()
        return etree.tostring(resp)

    def invoke_jsnapy(self, data, action):
        try:
            self.queue_message("vvvv", "Creating jnpr.jsnapy.SnapAdmin instance.")
            jsa = jnpr.jsnapy.SnapAdmin()
            self.queue_message("vvvv", 'Executing %s action.' % action)
            if action == 'check':
                responses = jsa.check(data=data,
                                      dev=self.dev,
                                      pre_file='PRE',
                                      post_file='POST')
            elif action == 'snapcheck':
                responses = jsa.snapcheck(data=data,
                                          dev=self.dev)
            elif action == 'snap_pre':
                responses = jsa.snap(data=data,
                                     dev=self.dev,
                                     file_name='PRE')
            elif action == 'snap_post':
                responses = jsa.snap(data=data,
                                     dev=self.dev,
                                     file_name='POST')
            else:
                raise AnsibleError("Unexpected action: %s." % (action))
            self.queue_message("vvvv", 'The %s action executed successfully' % action)
        except (pyez_exception.RpcError, pyez_exception.ConnectError) as ex:
            raise AnsibleError("Error communicating with the device: %s" % str(ex))

        if isinstance(responses, list) and len(responses) == 1:
            if action in ('snapcheck', 'check'):
                results = []
                for response in to_list(responses):
                    result = {}
                    result['device'] = response.device
                    result['result'] = response.result
                    result['no_passed'] = response.no_passed
                    result['no_failed'] = response.no_failed
                    result['test_results'] = response.test_results
                    results.append(result)
            else:
                results = [to_text(responses)]
        else:
            results = responses
        return json.dumps(results)
