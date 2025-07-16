#
# (c) 2016 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

import copy
import sys

from ansible.utils.display import Display
from ansible_collections.ansible.netcommon.plugins.action.network import (
    ActionModule as ActionNetworkModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    load_provider,
)

from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    junos_provider_spec,
)


display = Display()

CLI_SUPPORTED_MODULES = ["junos_netconf", "junos_ping", "junos_command"]


class ActionModule(ActionNetworkModule):
    def run(self, tmp=None, task_vars=None):
        del tmp  # tmp no longer has any effect

        module_name = self._task.action.split(".")[-1]
        # module_name = "device_facts"
        # self._task.action = "device_facts"
        self._task.collections.append("juniper.device")
        self._config_module = True if module_name in ["junos_config", "config"] else False
        persistent_connection = self._play_context.connection.split(".")[-1]
        warnings = []

        if self._play_context.connection == "local":
            provider = load_provider(junos_provider_spec, self._task.args)
            pc = copy.deepcopy(self._play_context)
            pc.network_os = "junipernetworks.junos.junos"
            pc.remote_addr = provider["host"] or self._play_context.remote_addr

            if provider["transport"] == "cli" and module_name not in CLI_SUPPORTED_MODULES:
                return {
                    "failed": True,
                    "msg": "Transport type '%s' is not valid for '%s' module. "
                    "Please see https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html"
                    % (provider["transport"], module_name),
                }

            if module_name == "junos_netconf" or (
                provider["transport"] == "cli" and module_name == "junos_command"
            ):
                pc.connection = "ansible.netcommon.network_cli"
                pc.port = int(
                    provider["port"] or self._play_context.port or 22,
                )
            else:
                pc.connection = "ansible.netcommon.netconf"
                pc.port = int(
                    provider["port"] or self._play_context.port or 830,
                )

            pc.remote_user = provider["username"] or self._play_context.connection_user
            pc.password = provider["password"] or self._play_context.password
            pc.private_key_file = provider["ssh_keyfile"] or self._play_context.private_key_file

            connection = self._shared_loader_obj.connection_loader.get(
                "ansible.netcommon.persistent",
                pc,
                sys.stdin,
                task_uuid=self._task._uuid,
            )

            # TODO: Remove below code after ansible minimal is cut out
            if connection is None:
                pc.network_os = "junos"
                if pc.connection.split(".")[-1] == "netconf":
                    pc.connection = "netconf"
                else:
                    pc.connection = "network_cli"

                connection = self._shared_loader_obj.connection_loader.get(
                    "persistent",
                    pc,
                    sys.stdin,
                    task_uuid=self._task._uuid,
                )

            display.vvv(
                "using connection plugin %s (was local)" % pc.connection,
                pc.remote_addr,
            )

            command_timeout = (
                int(provider["timeout"])
                if provider["timeout"]
                else connection.get_option("persistent_command_timeout")
            )
            connection.set_options(
                direct={"persistent_command_timeout": command_timeout},
            )

            socket_path = connection.run()
            display.vvvv("socket_path: %s" % socket_path, pc.remote_addr)
            if not socket_path:
                return {
                    "failed": True,
                    "msg": "unable to open shell. Please see: "
                    + "https://docs.ansible.com/ansible/network_debug_troubleshooting.html#unable-to-open-shell",
                }

            task_vars["ansible_socket"] = socket_path
            warnings.append(
                [
                    "connection local support for this module is deprecated and will be removed in version 2.14, use connection %s"
                    % pc.connection,
                ],
            )
        elif persistent_connection in ("netconf", "network_cli"):
            provider = self._task.args.get("provider", {})
            if any(provider.values()):
                # for legacy reasons provider value is required for junos_facts(optional) and junos_package
                # modules as it uses junos_eznc library to connect to remote host
                if not (
                    module_name == "junos_facts"
                    or module_name == "junos_package"
                    or module_name == "junos_scp"
                ):
                    display.warning(
                        "provider is unnecessary when using %s and will be ignored"
                        % self._play_context.connection,
                    )
                    del self._task.args["provider"]

            if (
                persistent_connection == "network_cli" and module_name not in CLI_SUPPORTED_MODULES
            ) or (persistent_connection == "netconf" and module_name in CLI_SUPPORTED_MODULES[0:2]):
                return {
                    "failed": True,
                    "msg": "Connection type '%s' is not valid for '%s' module. "
                    "Please see https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html"
                    % (self._play_context.connection, module_name),
                }
        result = super(ActionModule, self).run(task_vars=task_vars)
        if warnings:
            if "warnings" in result:
                result["warnings"].extend(warnings)
            else:
                result["warnings"] = warnings
        return result
