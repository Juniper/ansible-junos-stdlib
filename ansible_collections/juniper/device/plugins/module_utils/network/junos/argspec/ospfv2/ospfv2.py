# Copyright (C) 2020  Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
The arg spec for the junos_ospfv2 module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class Ospfv2Args(object):  # pylint: disable=R0903
    """The arg spec for the junos_ospfv2 module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "router_id": {"type": "str"},
                "areas": {
                    "elements": "dict",
                    "options": {
                        "area_id": {"required": True, "type": "str"},
                        "area_range": {"type": "str"},
                        "area_ranges": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "address": {"type": "str"},
                                "exact": {"type": "bool"},
                                "restrict": {"type": "bool"},
                                "override_metric": {"type": "int"},
                            },
                        },
                        "stub": {
                            "type": "dict",
                            "options": {
                                "default_metric": {"type": "int"},
                                "set": {"type": "bool"},
                            },
                        },
                        "interfaces": {
                            "elements": "dict",
                            "options": {
                                "authentication": {
                                    "type": "dict",
                                    "options": {
                                        "type": {"type": "dict"},
                                        "password": {
                                            "type": "str",
                                            "no_log": False,
                                        },
                                        "md5": {
                                            "type": "list",
                                            "elements": "dict",
                                            "options": {
                                                "key_id": {"type": "int"},
                                                "key": {
                                                    "type": "str",
                                                    "no_log": False,
                                                },
                                                "start_time": {"type": "str"},
                                            },
                                        },
                                    },
                                },
                                "bandwidth_based_metrics": {
                                    "elements": "dict",
                                    "options": {
                                        "bandwidth": {
                                            "choices": ["1g", "10g"],
                                            "type": "str",
                                        },
                                        "metric": {"type": "int"},
                                    },
                                    "type": "list",
                                },
                                "name": {"required": True, "type": "str"},
                                "priority": {"type": "int"},
                                "metric": {"type": "int"},
                                "flood_reduction": {"type": "bool"},
                                "passive": {"type": "bool"},
                                "timers": {
                                    "type": "dict",
                                    "options": {
                                        "dead_interval": {"type": "int"},
                                        "hello_interval": {"type": "int"},
                                        "poll_interval": {"type": "int"},
                                        "retransmit_interval": {"type": "int"},
                                        "transit_delay": {"type": "int"},
                                    },
                                },
                            },
                            "type": "list",
                        },
                    },
                    "type": "list",
                },
                "external_preference": {"type": "int"},
                "overload": {
                    "type": "dict",
                    "options": {
                        "timeout": {"type": "int"},
                        "allow_route_leaking": {"type": "bool"},
                        "as_external": {"type": "bool"},
                        "stub_network": {"type": "bool"},
                    },
                },
                "preference": {"type": "int"},
                "prefix_export_limit": {"type": "int"},
                "reference_bandwidth": {
                    "choices": ["1g", "10g"],
                    "type": "str",
                },
                "rfc1583compatibility": {"type": "bool"},
                "spf_options": {
                    "type": "dict",
                    "options": {
                        "delay": {"type": "int"},
                        "holddown": {"type": "int"},
                        "rapid_runs": {"type": "int"},
                        "no_ignore_our_externals": {"type": "bool"},
                    },
                },
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
