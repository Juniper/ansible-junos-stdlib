#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos logging_global fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from copy import deepcopy

from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils.six import string_types
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.logging_global.logging_global import (
    Logging_globalArgs,
)


try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False

try:
    import xmltodict

    HAS_XMLTODICT = True
except ImportError:
    HAS_XMLTODICT = False


class Logging_globalFacts(object):
    """The junos logging_global fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Logging_globalArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_device_data(self, connection, config_filter):
        """
        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for logging_gloabl
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            config_filter = """
                        <configuration>
                            <system>
                                <syslog>
                                </syslog>
                            </system>
                        </configuration>
                        """
            data = self.get_device_data(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/system/syslog")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"logging_global": {}}
        if objs:
            facts["logging_global"] = {}
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["logging_global"] = utils.remove_empties(params["config"])
        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root),
            dict_constructor=dict,
        )
        return xml_dict

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        logging_gloabl_config = {}

        # Parse facts for BGP address-family global node
        conf = conf.get("syslog")

        # Read allow-duplicates node
        if "allow-duplicates" in conf.keys():
            logging_gloabl_config["allow_duplicates"] = True

        # Read archive node
        if "archive" in conf.keys():
            archive_dict = self.parse_archive_node(conf.get("archive"))
            logging_gloabl_config["archive"] = archive_dict

        # Read console node
        if "console" in conf.keys():
            console_dict = self.parse_console_node(conf.get("console"))
            logging_gloabl_config["console"] = console_dict

        # Read file node
        if "file" in conf.keys():
            files_list = self.parse_file_node(conf.get("file"))
            logging_gloabl_config["files"] = files_list

        # Read host node
        if "host" in conf.keys():
            hosts_list = self.parse_host_node(conf.get("host"))
            logging_gloabl_config["hosts"] = hosts_list

        # Read log-rotate-frequency node
        if "log-rotate-frequency" in conf.keys():
            logging_gloabl_config["log_rotate_frequency"] = conf.get(
                "log-rotate-frequency",
            )

        # Read routing-instance node
        if "routing-instance" in conf.keys():
            logging_gloabl_config["routing_instance"] = conf.get(
                "routing-instance",
            )

        # Read source-address node
        if "source-address" in conf.keys():
            logging_gloabl_config["source_address"] = conf.get(
                "source-address",
            )

        # Read user node
        if "user" in conf.keys():
            users_list = self.parse_user_node(conf.get("user"))
            logging_gloabl_config["users"] = users_list

        # Read time-format
        if "time-format" in conf.keys():
            time_format_dict = {}
            time_format = conf.get("time-format")
            if time_format is None:
                time_format_dict["set"] = True
            else:
                if "millisecond" in time_format.keys():
                    time_format_dict["millisecond"] = True
                if "year" in time_format.keys():
                    time_format_dict["year"] = True
            logging_gloabl_config["time_format"] = time_format_dict

        return utils.remove_empties(logging_gloabl_config)

    def parse_archive_node(self, conf):
        archive_dict = {}
        if conf is not None:
            # Read child attributes
            if "binary-data" in conf.keys():
                archive_dict["binary_data"] = True
            if "files" in conf.keys():
                archive_dict["files"] = conf.get("files")
            if "no-binary-data" in conf.keys():
                archive_dict["no_binary_data"] = True
            if "no-world-readable" in conf.keys():
                archive_dict["no_world_readable"] = True
            if "size" in conf.keys():
                archive_dict["file_size"] = conf.get("size")
            if "world-readable" in conf.keys():
                archive_dict["world_readable"] = True
            if "archive-sites" in conf.keys():
                archive_sites_list = []
                archive_sites = conf.get("archive-sites")
                if isinstance(archive_sites, list):
                    for item in archive_sites:
                        archive_sites_list.append(item["name"])
                else:
                    archive_sites_list.append(archive_sites["name"])
                archive_dict["archive_sites"] = archive_sites_list
        else:
            archive_dict["set"] = True

        return archive_dict

    def parse_console_node(self, conf, console_dict=None):
        console_loggings = [
            "any",
            "authorization",
            "change-log",
            "conflict-log",
            "daemon",
            "dfc",
            "external",
            "firewall",
            "ftp",
            "interactive-commands",
            "kernel",
            "ntp",
            "pfe",
            "security",
            "user",
        ]
        if console_dict is None:
            console_dict = {}
        # Read any node
        if isinstance(conf, dict):
            for item in console_loggings:
                if item in conf.get("name"):
                    any_dict = {}
                    for k, v in conf.items():
                        if k != "name":
                            any_dict["level"] = k
                    console_dict[item.replace("-", "_")] = any_dict
        else:
            for console in conf:
                for item in console_loggings:
                    if item in console.get("name"):
                        any_dict = {}
                        for k, v in console.items():
                            if k != "name":
                                any_dict["level"] = k
                        console_dict[item.replace("-", "_")] = any_dict

        return console_dict

    def parse_file_node(self, conf):
        files_list = []
        files = []
        if isinstance(conf, dict):
            files.append(conf)
        else:
            files = conf
        for file in files:
            file_dict = {}
            # Read file name node
            file_dict["name"] = file.get("name")
            # Read allow-duplicates node
            if "allow-duplicates" in file:
                file_dict["allow_duplicates"] = True
            # Read contents
            if "contents" in file.keys():
                contents = file.get("contents")
                if isinstance(contents, list):
                    for content in contents:
                        file_dict = self.parse_console_node(content, file_dict)
                else:
                    file_dict = self.parse_console_node(contents, file_dict)
            # Read archives
            if "archive" in file.keys():
                archive_dict = self.parse_archive_node(file.get("archive"))
                file_dict["archive"] = archive_dict
            # Read explicit priority
            if "explicit-priority" in file.keys():
                file_dict["explicit_priority"] = True
            # Read match
            if "match" in file.keys():
                file_dict["match"] = file.get("match")
            # Read match-strings
            if "match-strings" in file.keys():
                match_strings = file.get("match-strings")
                match_strings_list = []
                if isinstance(match_strings, list):
                    for item in match_strings:
                        match_strings_list.append(item)
                else:
                    match_strings_list.append(match_strings)
                file_dict["match_strings"] = match_strings_list
            # Read srtructured-data
            if "structured-data" in file.keys():
                structured_data_dict = {}
                if file.get("structured-data"):
                    structured_data_dict["brief"] = True
                else:
                    structured_data_dict["set"] = True
                file_dict["structured_data"] = structured_data_dict
            files_list.append(file_dict)
        return files_list

    def parse_host_node(self, conf):
        hosts_list = []
        hosts = []
        if isinstance(conf, dict):
            hosts.append(conf)
        else:
            hosts = conf
        for host in hosts:
            host_dict = {}
            # Read file name node
            host_dict["name"] = host.get("name")
            # Read allow-duplicates node
            if "allow-duplicates" in host:
                host_dict["allow_duplicates"] = True
            # Read contents
            if "contents" in host.keys():
                contents = host.get("contents")
                if isinstance(contents, list):
                    for content in contents:
                        host_dict = self.parse_console_node(content, host_dict)
                else:
                    host_dict = self.parse_console_node(contents, host_dict)
            # Read exclude-hostname node
            if "exclude-hostname" in host.keys():
                host_dict["exclude_hostname"] = True
            # Read facility-override node
            if "facility-override" in host.keys():
                host_dict["facility_override"] = host.get("facility-override")
            # Read log-prefix node
            if "log-prefix" in host.keys():
                host_dict["log_prefix"] = host.get("log-prefix")
            # Read match
            if "match" in host.keys():
                host_dict["match"] = host.get("match")
            # Read match-strings
            if "match-strings" in host.keys():
                match_strings = host.get("match-strings")
                match_strings_list = []
                if isinstance(match_strings, list):
                    for item in match_strings:
                        match_strings_list.append(item)
                else:
                    match_strings_list.append(match_strings)
                host_dict["match_strings"] = match_strings_list
            # Read port node
            if "port" in host.keys():
                host_dict["port"] = host.get("port")
            # Read routing-instance node
            if "routing-instance" in host.keys():
                host_dict["routing_instance"] = host.get("routing-instance")
            # Read source-address node
            if "source-address" in host.keys():
                host_dict["source_address"] = host.get("source-address")
            # Read srtructured-data
            if "structured-data" in host.keys():
                structured_data_dict = {}
                if host.get("structured-data"):
                    structured_data_dict["brief"] = True
                else:
                    structured_data_dict["set"] = True
                host_dict["structured_data"] = structured_data_dict

            hosts_list.append(host_dict)

        return hosts_list

    def parse_user_node(self, conf):
        users_list = []
        users = []
        if isinstance(conf, dict):
            users.append(conf)
        else:
            users = conf
        for user in users:
            user_dict = {}
            # Read file name node
            user_dict["name"] = user.get("name")
            # Read allow-duplicates node
            if "allow-duplicates" in user:
                user_dict["allow_duplicates"] = True
            # Read contents
            if "contents" in user.keys():
                contents = user.get("contents")
                if isinstance(contents, list):
                    for content in contents:
                        user_dict = self.parse_console_node(content, user_dict)
                else:
                    user_dict = self.parse_console_node(contents, user_dict)
            # Read match
            if "match" in user.keys():
                user_dict["match"] = user.get("match")
            # Read match-strings
            if "match-strings" in user.keys():
                match_strings = user.get("match-strings")
                match_strings_list = []
                if isinstance(match_strings, list):
                    for item in match_strings:
                        match_strings_list.append(item)
                else:
                    match_strings_list.append(match_strings)
                user_dict["match_strings"] = match_strings_list

            users_list.append(user_dict)

        return users_list
