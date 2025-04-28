#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# utils
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    validate_config,
)

from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    tostring,
)


try:
    from ncclient.xml_ import new_ele, to_ele

    HAS_NCCLIENT = True
except ImportError:
    HAS_NCCLIENT = False

try:
    from ansible.module_utils.common.parameters import _list_no_log_values as list_no_log_values
except ImportError:
    # TODO: Remove this import when we no longer support ansible < 2.11
    from ansible.module_utils.common.parameters import list_no_log_values


def get_resource_config(connection, config_filter=None, attrib=None):
    if attrib is None:
        attrib = {"inherit": "inherit"}

    get_ele = new_ele("get-configuration", attrib)
    if config_filter:
        get_ele.append(to_ele(config_filter))

    return connection.execute_rpc(tostring(get_ele))


def _validate_config(_module, spec, data, redact=False):
    validated_data = validate_config(spec, data)
    if redact:
        _module.no_log_values.update(list_no_log_values(spec, validated_data))
    return validated_data
