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
from ansible.plugins.action.normal import ActionModule as ActionNormal
import os


connection_spec_fallbacks = {
    'host': ['ansible_host', 'inventory_hostname'],
    'user': ['ansible_connection_user', 'ansible_ssh_user', 'ansible_user'],
    'passwd': ['ansible_ssh_pass', 'ansible_pass'],
    'port': ['ansible_ssh_port', 'ansible_port'],
    'ssh_private_key_file': ['ansible_ssh_private_key_file',
                             'ansible_private_key_file']
}


# Moved the defintion from module_utils/juniper_junos_common.py to action_plugins/juniper_junos_common_action.py
# Use the custom behavior defined below as our ActionModule.
# The Ansible core engine will call ActionModule.run()
class ActionModule(ActionNormal):
    """A subclass of ansible.plugins.action.network.ActionModule used by all juniper_junos_* modules.

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
        # Pass the hidden _inventory_hostname option
        self._task.args['_inventory_hostname'] = task_vars['inventory_hostname']

        # Call the parent action module.
        return super(ActionModule, self).run(tmp, task_vars)
