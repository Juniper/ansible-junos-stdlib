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
import xmltodict

__metaclass__ = type

DOCUMENTATION = """author: Juniper Automation Team
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
    - name: host
    - name: hostname
    - name: ip
  port:
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
    - name: port
  mode:
    description:
    - Specifies the mode for the remote device connections.
    vars:
    - name: mode
  baud:
    description:
    - The serial baud rate.
    vars:
    - name: baud
  attempts:
    description:
    - The number of times to try connecting and logging in to the Junos device.
    vars:
    - name: attempts
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
    - name: user
    - name: username
  password:
    description:
    - Configures the user password used to authenticate to the remote device when
      first establishing the SSH connection.
    vars:
    - name: ansible_password
    - name: ansible_ssh_pass
    - name: ansible_ssh_password
    - name: passwd
    - name: password
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
    - name: ssh_private_key_file
    - name: ssh_keyfile
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
    - name: timeout
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
    - name: ssh_config

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
CONFIG_MODE_CHOICES = ['exclusive', 'private', 'dynamic', 'batch', 'ephemeral']


class Connection(NetworkConnectionBase):
    """NetConf connections"""

    transport = "juniper.device.pyez"
    has_pipelining = False

    def __init__(self, play_context, new_stdin, *args, **kwargs):
        super(Connection, self).__init__(play_context, new_stdin, *args, **kwargs)
        self.dev = None
        self.config = None

    @property
    @ensure_connect
    def manager(self):
        return self.dev

    def _connect(self):
        """Connect with the device.

        Establish the connection with the device.
        """
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

        # check for mode
        if self.get_option('port') is None:
            if self.get_option('mode') == 'telnet':
                connect_args['port'] = 23
            elif self.get_option('mode') == 'serial':
                connect_args['port'] = '/dev/ttyUSB0'
            else:
                connect_args['port'] = 830
        else:
            connect_args['port'] = self.get_option('port')

        if (self.get_option('mode') == 'telnet' or
                self.get_option('mode') == 'serial'):
            if self.get_option('baud') is None:
                # Default baud if serial or telnet mode
                connect_args['baud'] = 9600
            if self.get_option('attempts') is None:
                # Default attempts if serial or telnet mode
                connect_args['attempts'] = 10

        connect_args['host'] = self.get_option('host')
        # connect_args['port'] = self.get_option('port')
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
            raise AnsibleError("Unable to make a PyEZ connection: %s" % (str(ex)))

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
        """Get the capabilities for network api..
        """
        return json.dumps({'network_api': 'pyez'})

    def get_config(self, filter_xml=None, options=None, model=None,
                         namespace=None, remove_ns=True, **kwarg):
        """Get Configuration.

        Args:
            filter_xml: A string of XML, or '/'-separated configuration hierarchies,
                which specifies a filter used to restrict the portions of the
                configuration which are retrieved.
            options: Additional options, specified as a dictionary of key/value pairs, used
                when retrieving the configuration.
            model: the model of the configuration
            namespace: namespace to be used.
            remove_ns: if namespace is to be removed from the end output.

        Returns:
            - The configuration in the requested format as a single
              multi-line string. Returned for all formats.

        Fails:
            - Invalid database.
            - Invalid filter.
            - Format not understood by device.
        """
        resp = self.dev.rpc.get_config(filter_xml, options, model, namespace, remove_ns, **kwarg)
        return etree.tostring(resp)

    def get_rpc_resp(self,rpc, ignore_warning, format):
        """Execute rpc on the device and get response.

        Args:
            rpc: the rpc to be executed on the device
            ignore_warning: flag to check if warning received by device are to be ignored or not.
            format: the format of the response received.

        Returns:
            - Response in the requested format as a single multi-line string.
            - if format is json then return in json format

        Fails:
            - If the RPC produces an exception.
        """
        # data comes in JSON format, needs to be converted
        rpc_val = xmltodict.unparse(rpc)
        rpc_val = rpc_val.encode('utf-8')
        parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
        rpc_etree = etree.fromstring(rpc_val, parser=parser)
        resp = self.dev.rpc(rpc_etree, normalize=bool(format == 'xml'), ignore_warning=ignore_warning)
        if(format == 'json'):
            return resp
        return etree.tostring(resp)

    def get_facts(self):
        """Get device facts.
        """
        return dict(self.dev.facts)

    def ping_device(self, normalize=True, **params):
        """Ping the device.

        Args:
            params: dict of parameters passed directly to the ping RPC.
            normalize: flag to check if to normalize the results.

        Returns:
            Response in the requested format as a single multi-line string.

        Fails:
            - If the ping RPC produces an exception.
        """
        resp = self.dev.rpc.ping(normalize, **params)
        rpc_str = etree.tostring(resp)
        return rpc_str

    def get_chassis_inventory(self):
        """Get chassis inventory details from the device.
        """

        resp = self.dev.rpc.get_chassis_inventory()
        return etree.tostring(resp)

    def get_re_name(self):
        """Get re name from the device.
        """
        return self.dev.re_name

    def set_chassis_cluster_enable(self, cluster_id, node_id):
        """send set chassis cluster enable rpc to the device.
        """
        return self.dev.rpc.set_chassis_cluster_enable(
                            cluster_id=cluster_id, node=node_id,
                            reboot=True, normalize=True)

    def set_chassis_cluster_disable(self):
        """send set chassis cluster disable rpc to the device.
        """
        return self.dev.rpc.set_chassis_cluster_disable(
                            reboot=True, normalize=True)

    def invoke_jsnapy(self, data, action):
        """invoke jsnapy for persistent connection.
        """
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
                                          dev=self.dev,
                                          file_name='PRE')
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

        results = {}
        if isinstance(responses, list) and len(responses) == 1:
            if action in ('snapcheck', 'check'):
                for response in responses:
                    results['device'] = response.device
                    results['router'] = response.device
                    results['final_result'] = response.result
                    results['total_passed'] = response.no_passed
                    results['total_failed'] = response.no_failed
                    results['test_results'] = response.test_results
                    total_tests = int(response.no_passed) + int(response.no_failed)
                    results['total_tests'] = total_tests
                pass_percentage = 0
                if total_tests > 0:
                    pass_percentage = ((int(response.no_passed) * 100) //
                                       total_tests)
                results['passPercentage'] = pass_percentage
                results['pass_percentage'] = pass_percentage
                if results['final_result'] == 'Failed':
                    results['msg'] = 'Test Failed: Passed %s, Failed %s' % \
                                     (results['total_passed'],
                                      results['total_failed'])
                else:
                    results['msg'] = 'Test Passed: Passed %s, Failed %s' % \
                                     (results['total_passed'],
                                      results['total_failed'])
            elif action in ('snap_pre', 'snap_post'):
                results['msg'] = "The %s action successfully executed." % (action)
        else:
            raise AnsibleError("Unexpected JSNAPy responses. Type: %s."
                                   "Responses: %s" %
                                   (type(responses), str(responses)))
        return results

    def open_configuration(self, mode, ignore_warn=None, ephemeral_instance=None):
        """Open candidate configuration database in exclusive or private mode.

        Failures:
            - When there's a problem with the PyEZ connection.
            - When there's a RPC problem including an already locked
                        config or an already opened private config.
        """
        if self.config is None:
            if mode not in CONFIG_MODE_CHOICES:
                raise AnsibleError("Invalid configuration mode: %s" % mode)
            if mode != 'ephemeral' and ephemeral_instance is not None:
                self.fail_json(msg='Ephemeral instance is specified while the mode '
                                   'is not ephemeral. Specify the mode as ephemeral '
                                   'or do not specify the instance.')
            if self.dev is None:
                self.open()
            config = jnpr.junos.utils.config.Config(self.dev, mode=mode)
            try:
                if config.mode == 'exclusive':
                    config.lock()
                elif config.mode == 'private':
                    self.dev.rpc.open_configuration(
                        private=True,
                        ignore_warning=ignore_warn)
                elif config.mode == 'dynamic':
                    self.dev.rpc.open_configuration(
                        dynamic=True,
                        ignore_warning=ignore_warn)
                elif config.mode == 'batch':
                    self.dev.rpc.open_configuration(
                        batch=True,
                        ignore_warning=ignore_warn)
                elif config.mode == 'ephemeral':
                    if ephemeral_instance is None:
                        self.dev.rpc.open_configuration(
                           ephemeral=True,
                           ignore_warning=ignore_warn)
                    else:
                        self.dev.rpc.open_configuration(
                           ephemeral_instance = ephemeral_instance,
                           ignore_warning=ignore_warn)
            except (pyez_exception.ConnectError,
                    pyez_exception.RpcError) as ex:
                raise AnsibleError('Unable to open the configuration in %s '
                                   'mode: %s' % (config.mode, str(ex)))
            self.config = config
            self.queue_message("log", "Configuration opened in %s mode."% config.mode)

    def close_configuration(self):
        """Close candidate configuration database.

        Failures:
            - When there's a problem with the PyEZ connection.
            - When there's a RPC problem closing the config.
        """
        if self.config is not None:
            config = self.config
            self.config = None
            try:
                if config.mode == 'exclusive':
                    config.unlock()
                elif config.mode in ['batch', 'dynamic', 'private', 'ephemeral']:
                    self.dev.rpc.close_configuration()
                self.queue_message("log", "Configuration closed.")
            except (pyez_exception.ConnectError,
                    pyez_exception.RpcError) as ex:
                raise AnsibleError('Unable to close the configuration: %s' %
                                   (str(ex)))

    def rollback_configuration(self, id):
        """Rollback the device configuration to the specified id.

        Rolls back the configuration to the specified id. Assumes the
        configuration is already opened. Does NOT commit the configuration.

        Args:
            id: The id to which the configuration should be rolled back. Either
                an integer rollback value or the string 'rescue' to roll back
                to the previously saved rescue configuration.

        Failures:
            - Unable to rollback the configuration due to an RpcError or ConnectError
        """
        if self.dev is None or self.config is None:
            raise AnsibleError('The device or configuration is not open.')

        if id == 'rescue':
            self.queue_message("log", "Rolling back to the rescue configuration.")
            try:
                self.config.rescue(action='reload')
                self.queue_message("log", "Rescue configuration loaded.")
            except (self.pyez_exception.RpcError,
                    self.pyez_exception.ConnectError) as ex:
                raise AnsibleError('Unable to load the rescue configuraton: '
                                   '%s' % (str(ex)))
        elif id >= 0 and id <= 49:
            self.queue_message("log", "Loading rollback %d configuration.", id)
            try:
                self.config.rollback(rb_id=id)
                self.queue_message("log", "Rollback %d configuration loaded.", id)
            except (self.pyez_exception.RpcError,
                    self.pyez_exception.ConnectError) as ex:
                raise AnsibleError('Unable to load the rollback %d '
                                   'configuraton: %s' % (id, str(ex)))
        else:
            raise AnsibleError('Unrecognized rollback configuraton value: %s'
                               % (id))

    def check_configuration(self):
        """Check the candidate configuration. Assumes the configuration is already opened.
        Performs the equivalent of a "commit check", but does NOT commit the
        configuration.

        Failures:
            - An error returned from checking the configuration.
        """
        try:
            self.config.commit_check()
            self.queue_message("log", "Configuration checked.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure checking the configuraton: %s' %
                               (str(ex)))

    def diff_configuration(self, ignore_warning=False):
        """Diff the candidate and committed configurations.

        Returns:
            A string with the configuration differences in text "diff" format.

        Failures:
            - An error returned from diffing the configuration.
        """
        try:
            diff = self.config.diff(rb_id=0, ignore_warning=ignore_warning)
            self.queue_message("log", "Configuration diff completed.")
            return diff
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure diffing the configuraton: %s' %
                               (str(ex)))

    def load_configuration(self, config, load_args):
        """Load the candidate configuration from the specified src file using the
        specified action.

        Failures:
            - An error returned from loading the configuration.
        """
        try:
            if config is not None:
                self.config.load(config, **load_args)
            else:
                self.queue_message("log", "Load args %s." %str(load_args))
                self.config.load(**load_args)
            self.queue_message("log", "Configuration loaded.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure loading the configuraton: %s' %
                               (str(ex)))

    def commit_configuration(self, ignore_warning=None, comment=None,
                             confirmed=None, timeout=30, full=False,
                             force_sync=False, sync=False):
        """Commit the candidate configuration.
        Assumes the configuration is already opened.

        Args:
            ignore_warning - Which warnings to ignore.
            comment - The commit comment
            confirmed - Number of minutes for commit confirmed.

        Failures:
            - An error returned from committing the configuration.
        """
        try:
            self.config.commit(ignore_warning=ignore_warning,
                               comment=comment,
                               confirm=confirmed,
                               timeout=timeout,
                               full=full,
                               force_sync=force_sync,
                               sync=sync)
            self.queue_message("log", "Configuration committed.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure committing the configuraton: %s' %
                               (str(ex)))

    def system_api(self, action, in_min, at, all_re, vmhost, other_re, media, member_id):
        """Triggers the system calls like reboot, shutdown, halt and zeroize to device.
        """
        msg = None
        if action != 'zeroize':
            if (at == 'now' or (in_min == 0 and at is None)):
                if self.dev.timeout > 5:
                    self.queue_message("log", "Decreasing device RPC timeout to 5 seconds.")
                    self.dev.timeout = 5

        try:
            self.sw = jnpr.junos.utils.sw.SW(self.dev)
            if action == 'reboot':
                if member_id is not None:
                    for m_id in member_id:
                        got = self.sw.reboot(in_min, at, all_re, None, vmhost, other_re, member_id=m_id)
                else:
                    got = self.sw.reboot(in_min, at, all_re, None, vmhost, other_re)
            elif action == 'shutdown':
                got = self.sw.poweroff(in_min, at, None, all_re, other_re, vmhost)
            elif action == 'halt':
                got = self.sw.halt(in_min, at, all_re, other_re)
            elif action == 'zeroize':
                got = self.sw.zeroize(all_re, media)
            else:
                raise AnsibleError('Relevant action not found')

            self.queue_message("log", "RPC executed")
            if got is None:
                msg = 'Did not find expected RPC response.'
            else:
                msg = '%s successfully initiated. Response got %s' % (action, got)
        except (self.pyez_exception.RpcTimeoutError) as ex:
            try:
                self.close(raise_exceptions=True)
                # This means the device wasn't already disconnected.
                raise AnsibleError('%s failed. %s may not have been ' \
                                 'initiated.' % (action, action))
            except (self.pyez_exception.RpcError,
                    self.pyez_exception.ConnectError):
                # This is expected. The device has already disconnected.
                msg = '%s succeeded.' % (action)
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('%s failed. Error: %s' % (action, str(ex)))
        return msg

    def software_api(self, install_params):
        """Installs package to device.
        """
        try:
            self.sw = jnpr.junos.utils.sw.SW(self.dev)
            ok, msg_ret = self.sw.install(**install_params)
            if ok is not True:
                raise AnsibleError('Unable to install the software %s' % msg_ret)
            msg = 'Package %s successfully installed. Response from device is: %s' % (
                install_params.get('package') or
                install_params.get('pkg_set'),
                msg_ret)
            self.queue_message("log", "%s" % msg)
            return msg
        except (self.pyez_exception.ConnectError,
                self.pyez_exception.RpcError) as ex:
            raise AnsibleError('Installation failed. Error: %s' % str(ex))

    def reboot_api(self, all_re, vmhost, member_id):
        """reboots the device.
        """
        msg = None
        try:
            restore_timeout = self.dev.timeout
            if self.dev.timeout > 5:
                self.dev.timeout = 5
            try:
                if member_id is not None:
                    for m_id in member_id:
                        got = self.sw.reboot(0, None, all_re, None, vmhost, member_id=m_id)
                else:
                    got = self.sw.reboot(0, None, all_re, None, vmhost)
                self.dev.timeout = restore_timeout
            except Exception:  # pylint: disable=broad-except
                self.dev.timeout = restore_timeout
                raise
            self.queue_message("log", "Reboot RPC executed.")

            if got is not None:
                msg += ' Reboot successfully initiated. ' \
                                  'Reboot message: %s' % got
            else:
                raise AnsibleError(' Did not find expected response ' \
                                  'from reboot RPC. ')
        except (self.pyez_exception.RpcTimeoutError) as ex:
            try:
                self.close(raise_exceptions=True)
                # This means the device wasn't already disconnected.
                raise AnsibleError(' Reboot failed. It may not have been ' \
                                  'initiated.')
            except (self.pyez_exception.RpcError,
                    self.pyez_exception.RpcTimeoutError,
                    self.pyez_exception.ConnectError):
                # This is expected. The device has already disconnected.
                msg += ' Reboot succeeded.'
            except (self.ncclient_exception.TimeoutExpiredError):
                # This is not really expected. Still consider reboot success as
                # Looks like rpc was consumed but no response as its rebooting.
                msg += ' Reboot succeeded. Ignoring close error.'
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError(' Reboot failed. Error: %s' % (str(ex)))
        else:
            try:
                self.close()
            except (self.ncclient_exception.TimeoutExpiredError):
                self.queue_message("log", "Ignoring TimeoutError for close call")

        self.queue_message("log", "Reboot RPC successfully initiated.")

        return msg
