# -*- coding: utf-8 -*-

#
# Copyright (c) 2017-2018, Juniper Networks Inc. All rights reserved.
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

DOCUMENTATION = """
"""

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
        connect_args['port'] = self.get_option('port')
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

    def get_re_name(self):
        return self.dev.re_name

    def set_chassis_cluster_enable(self, cluster_id, node_id):
        return self.dev.rpc.set_chassis_cluster_enable(
                            cluster_id=cluster_id, node=node_id,
                            reboot=True, normalize=True)

    def set_chassis_cluster_disable(self):
        return self.dev.rpc.set_chassis_cluster_disable(
                            reboot=True, normalize=True)

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

    def open_configuration(self, mode, ignore_warn=None):
        if self.config is None:
            if mode not in CONFIG_MODE_CHOICES:
                raise AnsibleError("Invalid configuration mode: %s" % mode)
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
            except (pyez_exception.ConnectError,
                    pyez_exception.RpcError) as ex:
                raise AnsibleError('Unable to open the configuration in %s '
                                   'mode: %s' % (config.mode, str(ex)))
            self.config = config
            self.queue_message("log", "Configuration opened in %s mode."% config.mode)

    def close_configuration(self):
        if self.config is not None:
            config = self.config
            self.config = None
            try:
                if config.mode == 'exclusive':
                    config.unlock()
                elif config.mode == 'private':
                    self.dev.rpc.close_configuration()
                self.queue_message("log", "Configuration closed.")
            except (pyez_exception.ConnectError,
                    pyez_exception.RpcError) as ex:
                raise AnsibleError('Unable to close the configuration: %s' %
                                   (str(ex)))

    def rollback_configuration(self, id):
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
        try:
            self.config.commit_check()
            self.queue_message("log", "Configuration checked.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure checking the configuraton: %s' %
                               (str(ex)))

    def diff_configuration(self, ignore_warning=False):
        try:
            diff = self.config.diff(rb_id=0, ignore_warning=ignore_warning)
            self.queue_message("log", "Configuration diff completed.")
            return diff
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure diffing the configuraton: %s' %
                               (str(ex)))

    def load_configuration(self, config, load_args):
        try:
            if config is not None:
                self.config.load(config, **load_args)
            else:
                self.queue_message("log", "Load args %s.", str(load_args))
                self.config.load(**load_args)
            self.queue_message("log", "Configuration loaded.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure loading the configuraton: %s' %
                               (str(ex)))

    def commit_configuration(self, ignore_warning=None, comment=None,
                             confirmed=None):
        try:
            self.config.commit(ignore_warning=ignore_warning,
                               comment=comment,
                               confirm=confirmed)
            self.queue_message("log", "Configuration committed.")
        except (self.pyez_exception.RpcError,
                self.pyez_exception.ConnectError) as ex:
            raise AnsibleError('Failure committing the configuraton: %s' %
                               (str(ex)))

    def system_api(self, action, in_min, at, all_re, vmhost, other_re, media):
        msg = None
        if action != 'zeroize':
            if (at == 'now' or (in_min == 0 and at is None)):
                if self.dev.timeout > 5:
                    self.queue_message("log", "Decreasing device RPC timeout to 5 seconds.")
                    self.dev.timeout = 5

        try:
            self.sw = jnpr.junos.utils.sw.SW(self.dev)
            if action == 'reboot':
                got = self.sw.reboot(in_min, at, all_re, None, vmhost, other_re)
            elif action == 'shutdown':
                got = self.sw.poweroff(in_min, at, None, all_re, other_re)
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

    def reboot_api(self, all_re, vmhost):
        msg = None
        try:
            restore_timeout = self.dev.timeout
            if self.dev.timeout > 5:
                self.dev.timeout = 5
            try:
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