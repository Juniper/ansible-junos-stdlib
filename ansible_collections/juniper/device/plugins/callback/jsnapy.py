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

DOCUMENTATION = """
---
name: jsnapy
type: callback
author: Juniper Networks, Roslan Zaki, Damien Garros, Stacy Smith (@stacywsmith)
short_description: Formats and prints JSNAPy test results for Junos devices
description: |
  This callback plugin provides extra logging and human-readable output for JSNAPy test results executed via Ansible.
  It collects and displays pass/fail details for each JSNAPy test when the action is snapcheck or check.
  The jsnapy callback plugin is disabled by default. To enable the jsnapy callback plugin, add the
  callbacks_enabled = juniper.device.jsnapy statement to the Ansible configuration file.
  Example:
    [defaults]
    callbacks_enabled = juniper.device.jsnapy
  For more information on JSNAPy, see https://github.com/Juniper/jsnapy and
  https://www.juniper.net/documentation/en_US/day-one-books/DO_JSNAPy.zip.
options: {}
"""


EXAMPLES = """
- name: Run JSNAPy snapcheck
  hosts: junos-all
  connection: local
  gather_facts: false
  tasks:
    - name: Run JSNAPy snapcheck
      juniper.device.jsnapy:
        action: "snapcheck"
        test_files: "tests/test_junos_interface.yaml"
      register: test_result
    - name: Print JSNAPy test results
      ansible.builtin.debug:
        var: test_result
"""

RETURN = """
test_results:
  description:
    - Detailed results of each JSNAPy test executed, including pass/fail counts and test details.
  returned: always
  type: dict
msg:
  description:
    - Human-readable summary of JSNAPy validation, printed to the console by the callback plugin.
  returned: always
  type: str
"""


import json
import pprint

from ansible import constants as C
from ansible.module_utils.six import iteritems
from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    """
    This callback add extra logging for the module junos_jsnapy .
    """

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = "aggregate"
    CALLBACK_NAME = "jsnapy"

    # callback needs to be enabled with config-file to use jsnapy callback during execution
    CALLBACK_NEEDS_WHITELIST = True

    # useful links regarding Callback
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/callback/__init__.py

    def __init__(self):
        self._pp = pprint.PrettyPrinter(indent=4)
        self._results = {}

        super(CallbackModule, self).__init__()

    def v2_runner_on_ok(self, result):
        """
        Collect test results for all tests executed if action is snapcheck or check
        """

        # Extract module name
        module_args = {}
        if "invocation" in result._result:
            if "module_args" in result._result["invocation"]:
                module_args = result._result["invocation"]["module_args"]

        # Check if dic return has all valid information
        if "action" not in module_args:
            return None

        if module_args["action"] == "snapcheck" or module_args["action"] == "check":

            # Check if dict entry already exist for this host
            host = result._host.name
            if host not in self._results.keys():
                self._results[host] = []

            self._results[host].append(result)

    def v2_playbook_on_stats(self, stats):

        # Go over all results for all hosts
        for host, results in iteritems(self._results):
            has_printed_banner = False
            for result in results:
                # self._pp.pprint(result.__dict__)
                res = result._result
                if res.get("final_result") == "Failed":
                    for test_name, test_results in iteritems(res["test_results"]):
                        for testlet in test_results:
                            if ("count" in testlet) and testlet["count"]["fail"] != 0:
                                if not has_printed_banner:
                                    self._display.banner(
                                        "JSNAPy Results for: " + str(host),
                                    )
                                    has_printed_banner = True

                                for test in testlet["failed"]:

                                    # Check if POST exist in the response
                                    data = ""
                                    if "post" in test:
                                        data = test["post"]
                                    else:
                                        data = test

                                    self._display.display(
                                        "Value of '{0}' not '{1}' at '{2}' with {3}".format(
                                            str(testlet["node_name"]),
                                            str(testlet["testoperation"]),
                                            str(testlet["xpath"]),
                                            json.dumps(data),
                                        ),
                                        color=C.COLOR_ERROR,
                                    )

                            elif testlet["count"]["pass"] != 0:
                                if not has_printed_banner:
                                    self._display.banner(
                                        "JSNAPy Results for: " + str(host),
                                    )
                                    has_printed_banner = True

                                for test in testlet["passed"]:

                                    # Check if POST exist in the response
                                    data = ""
                                    if "post" in test:
                                        data = test["post"]
                                    else:
                                        data = test

                                    self._display.display(
                                        "Value of '{0}' '{1}' at '{2}' with {3}".format(
                                            str(testlet["node_name"]),
                                            str(testlet["testoperation"]),
                                            str(testlet["xpath"]),
                                            json.dumps(data),
                                        ),
                                        color=C.COLOR_DEBUG,
                                    )
