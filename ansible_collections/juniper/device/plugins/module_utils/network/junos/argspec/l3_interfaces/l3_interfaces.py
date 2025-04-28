# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the junos_l3_interfaces module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class L3_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the junos_l3_interfaces module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "ipv4": {
                    "elements": "dict",
                    "options": {"address": {"type": "str"}},
                    "type": "list",
                },
                "ipv6": {
                    "elements": "dict",
                    "options": {"address": {"type": "str"}},
                    "type": "list",
                },
                "name": {"required": True, "type": "str"},
                "unit": {"type": "int", "default": 0},
                "mtu": {"type": "int"},
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
                "parsed",
                "rendered",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
