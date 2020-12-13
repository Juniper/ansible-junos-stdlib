# -*- coding: utf-8 -*-

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

from distutils.version import LooseVersion
import os

# Non-standard library imports and checks
try:
    from jnpr.junos.version import VERSION
    HAS_PYEZ_VERSION = VERSION
except ImportError:
    HAS_PYEZ_VERSION = None

try:
    import jnpr.junos.op
    import jnpr.junos.factory.factory_loader
    import jnpr.junos.factory.table
    HAS_PYEZ_OP_TABLE = True
except ImportError:
    HAS_PYEZ_OP_TABLE = False

try:
    import ncclient.operations.errors as ncclient_exception
    HAS_NCCLIENT_EXCEPTIONS = True
except ImportError:
    HAS_NCCLIENT_EXCEPTIONS = False

try:
    import jnpr.jsnapy
    HAS_JSNAPY_VERSION = jnpr.jsnapy.__version__
except ImportError:
    HAS_JSNAPY_VERSION = None
# Most likely JSNAPy 1.2.0 with https://github.com/Juniper/jsnapy/issues/263
except TypeError:
    HAS_JSNAPY_VERSION = 'possibly 1.2.0'

try:
    from lxml import etree
    HAS_LXML_ETREE_VERSION = '.'.join(map(str, etree.LXML_VERSION))
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

# Constants
# Minimum PyEZ version required by shared code.
MIN_PYEZ_VERSION = "2.5.2"
# Installation URL for PyEZ.
PYEZ_INSTALLATION_URL = "https://github.com/Juniper/py-junos-eznc#installation"
# Minimum lxml version required by shared code.
MIN_LXML_ETREE_VERSION = "3.2.4"
# Installation URL for LXML.
LXML_ETREE_INSTALLATION_URL = "http://lxml.de/installation.html"
# Minimum JSNAPy version required by shared code.
MIN_JSNAPY_VERSION = "1.3.4"
# Installation URL for JSNAPy.
JSNAPY_INSTALLATION_URL = "https://github.com/Juniper/jsnapy#installation"
# Minimum jxmlease version required by shared code.
MIN_JXMLEASE_VERSION = "1.0.1"
# Installation URL for jxmlease.
JXMLEASE_INSTALLATION_URL = \
    "http://jxmlease.readthedocs.io/en/stable/install.html"
# Minimum yaml version required by shared code.
MIN_YAML_VERSION = "3.08"
YAML_INSTALLATION_URL = "http://pyyaml.org/wiki/PyYAMLDocumentation"


def _check_library(
                   library_name,
                   installed_version,
                   installation_url,
                   minimum=None,
                   library_nickname=None):
    """Check if library_name is installed and version is >= minimum.

    Args:
        library_name: The name of the library to check.
        installed_version: The currently installed version, or None if it's
                           not installed.
        installation_url: The URL with instructions on installing
                          library_name
        minimum: The minimum version required.
                 Default = None which means no version check.
        library_nickname: The library name with any nickname.
                 Default = library_name.
    Failures:
        - library_name not installed (unable to import).
        - library_name installed_version < minimum.
    """
    if library_nickname is None:
        library_nickname = library_name
    if installed_version is None:
        if minimum is not None:
            return('%s >= %s is required for this module. '
                               'However, %s does not appear to be '
                               'currently installed. See %s for '
                               'details on installing %s.' %
                               (library_nickname, minimum, library_name,
                                installation_url, library_name))
        else:
            return('%s is required for this module. However, '
                               '%s does not appear to be currently '
                               'installed. See %s for details on '
                               'installing %s.' %
                               (library_nickname, library_name,
                                installation_url, library_name))
    elif installed_version is not None and minimum is not None:
        if not LooseVersion(installed_version) >= LooseVersion(minimum):
            return(
                '%s >= %s is required for this module. Version %s of '
                    '%s is currently installed. See %s for details on '
                    'upgrading %s.' %
                    (library_nickname, minimum, installed_version,
                     library_name, installation_url, library_name))
    return "success"

def check_pyez(minimum=None):
    """Check PyEZ is available and version is >= minimum.

    Args:
        minimum: The minimum PyEZ version required.
                 Default = None which means no version check.
        check_device: Indicates whether to check for PyEZ Device object.
        check_exception: Indicates whether to check for PyEZ exceptions.

    Failures:
        - PyEZ not installed (unable to import).
        - PyEZ version < minimum.
    """
    if HAS_NCCLIENT_EXCEPTIONS is False:
            return('ncclient.operations.errors module could not '
                               'be imported.')
    return _check_library('junos-eznc', HAS_PYEZ_VERSION,
                        PYEZ_INSTALLATION_URL, minimum=minimum,
                        library_nickname='junos-eznc (aka PyEZ)')

def check_jsnapy(minimum=None):
    """Check jsnapy is available and version is >= minimum.

    Args:
        minimum: The minimum jsnapy version required.
                 Default = None which means no version check.

    Failures:
        - jsnapy not installed.
        - jsnapy version < minimum.
    """
    return _check_library('jsnapy', HAS_JSNAPY_VERSION,
                        JSNAPY_INSTALLATION_URL, minimum=minimum)

def check_jxmlease(minimum=None):
    """Check jxmlease is available and version is >= minimum.

    Args:
        minimum: The minimum jxmlease version required.
                 Default = None which means no version check.

    Failures:
        - jxmlease not installed.
        - jxmlease version < minimum.
    """
    return _check_library('jxmlease', HAS_JXMLEASE_VERSION,
                        JXMLEASE_INSTALLATION_URL, minimum=minimum)

def check_lxml_etree(minimum=None):
    """Check lxml etree is available and version is >= minimum.

    Args:
        minimum: The minimum lxml version required.
                 Default = None which means no version check.

    Failures:
        - lxml not installed.
        - lxml version < minimum.
    """
    return _check_library('lxml Etree', HAS_LXML_ETREE_VERSION,
                        LXML_ETREE_INSTALLATION_URL, minimum=minimum)

def check_yaml(minimum=None):
    """Check yaml is available and version is >= minimum.

    Args:
        minimum: The minimum PyYAML version required.
                 Default = None which means no version check.

    Failures:
        - yaml not installed.
        - yaml version < minimum.
    """
    return _check_library('yaml', HAS_YAML_VERSION,
                        YAML_INSTALLATION_URL, minimum=minimum)

def check_sw_compatibility(min_pyez_version,
                        min_lxml_etree_version,
                        min_jsnapy_version=None,
                        min_jxmlease_version=None,
                        min_yaml_version=None):
    """Check yaml is available and version is >= minimum.

        Args:
            minimum: The minimum PyYAML version required.
                     Default = None which means no version check.
        Returns:
            string as success or the error
    """
    ret_output = check_pyez(min_pyez_version)
    if ret_output != "success":
        return ret_output

    ret_output = check_lxml_etree(min_lxml_etree_version)
    if ret_output != "success":
        return ret_output

    if min_jsnapy_version is not None:
        ret_output = check_jsnapy(min_jsnapy_version)
        if ret_output != "success":
            return ret_output

    if min_jxmlease_version is not None:
        ret_output = check_jxmlease(min_jxmlease_version)
        if ret_output != "success":
            return ret_output

    if min_yaml_version is not None:
        ret_output = check_yaml(min_yaml_version)

    return ret_output


