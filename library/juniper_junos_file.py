#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 1999-2018, Juniper Networks Inc.
#               2018, Damien Garros
#
# All rights reserved.
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
import hashlib
from jnpr.junos.utils.scp import SCP

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'supported_by': 'community',
                    'status': ['stableinterface']}

DOCUMENTATION = '''
---
extends_documentation_fragment: 
  - juniper_junos_common.connection_documentation
  - juniper_junos_common.logging_documentation
module: juniper_junos_file
version_added: "2.0.3" # of Juniper.junos role
author: Damien Garros / Boris Renet
short_description: Copy file to and from device
description:
  - Copy file over SCP to and from a Juniper device
options:
        local_dir=dict(type='str',
                  required=True,
                  default=None),
        remote_dir=dict(type='str',
                  required=True,
                  default=None),
        file=dict(type='str',
                  required=True,
                  default=None), 
        action=dict(type='str',
                  choices=['put', 'get'], 
                  required=True,
                  default=None)
  local_dir:
    description:
        - path of the local directory where the file is located 
          or needs to be copied to
    required: True
    type: str
  remote_dir:
    description:
        - path of the directory on the remote device where the file is located 
          or needs to be copied to
    required: True
    type: str
  file:
    description:
      - Name of the file to copy to/from the remote device.
    required: true
    type: str
  Action:
    description:
      - Type of operation to execute, currently only support get and put
    required: True
    type: str
'''

EXAMPLES = '''
---
- name: Examples of juniper_junos_file
  hosts: all
  connection: local
  gather_facts: no
  roles:
    - Juniper.junos

  tasks:
    - name: Copy a log file on a remote device locally
      juniper_junos_file:
        remote_dir: /var/log
        local_dir: /tmp
        action: get
        file: log.txt

    - name: Copy a local file into /var/tmp on the remote device
      juniper_junos_file:
        remote_dir: /var/tmp
        local_dir: /tmp
        action: put
        file: license.txt

'''

RETURN = '''

changed:
  description:
    - Indicates if the device's state has changed.
  returned: when the file has been successfully copied.
  type: bool

'''


def import_juniper_junos_common():
    """Imports the juniper_junos_common module from _module_utils_path.

    Ansible versions < 2.4 do not provide a way to package common code in a
    role. This function solves that problem for juniper_junos_* modules by
    reading the module arguments passed on stdin and interpreting the special
    option _module_utils_path as a path to the the directory where the
    juniper_junos_common module resides. It temporarily inserts this path at
    the head of sys.path, imports the juniper_junos_common module, and removes
    the path from sys.path. It then returns the imported juniper_junos_common
    module object. All juniper_junos_* modules must include this boilerplate
    function in order to import the shared juniper_junos_common module.

    Args:
        None.

    Returns:
        The juniper_junos_common module object.

    Raises:
        ImportError: If the juniper_junos_common object can not be imported
                     from the path specified by the module_utils_path argument.
    """
    from ansible.module_utils.basic import AnsibleModule
    import sys
    
    juniper_junos_common = None
    module = AnsibleModule(
        argument_spec={
            '_module_utils_path': dict(type='path', default=None),
            # Avoids a warning about not specifying no_log for passwd.
            'passwd': dict(no_log=True)
        },
        # Doesn't really work due to Ansible bug. Keeping it here for when
        # Ansible bug is fixed.
        no_log=True,
        check_invalid_arguments=False,
        bypass_checks=True
    )
    import_path = module.params.get('_module_utils_path')
    if import_path is not None:
        sys.path.insert(0, import_path)
        import juniper_junos_common
        del sys.path[0]
    return juniper_junos_common


def _hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()


def local_md5(junos_module, package):
    """
    Computes the MD5 checksum value on the local package file.

    :param str package:
      File-path to the package (\*.tgz) file on the local server

    :returns: MD5 checksum (str)
    :raises IOError: when **package** file does not exist
    """
    try:
        checksum=_hashfile(open(package, 'rb'), hashlib.md5())
    except Exception as err:
        junos_module.logger.error("unable to get the hash due to:{0}".format(err))
        if (("No such file" in format(err)) and (junos_module.params['action']=="get")):
            checksum="no_file"
        else:
            raise err
        return checksum

    junos_module.logger.info("local hash calculated")
    return checksum


def remote_md5(junos_module, remote_file):
    try:
        rpc_reply=junos_module.dev.rpc.get_checksum_information(path=remote_file)
        checksum=rpc_reply.findtext('.//checksum').strip() 
    except Exception as err:
       junos_module.logger.error("unable to get rpc due to:{0}".format(err.message))
       if (("No such file or directory" in err.message) and (junos_module.params['action']=="put")):
           checksum="no_file" 
       else:
           raise err
       return checksum
    junos_module.logger.info("rpc reponse recvd")
    return checksum


def main():
    # Import juniper_junos_common
    juniper_junos_common = import_juniper_junos_common()

    # The argument spec for the module.
    argument_spec = dict(
        local_dir=dict(type='str',
                  required=True,
                  default=None),
        remote_dir=dict(type='str',
                  required=True,
                  default=None),
        file=dict(type='str',
                  required=True,
                  default=None), 
        action=dict(type='str',
                  choices=['put', 'get'], 
                  required=True,
                  default=None)
    )

    # Create the module instance.
    junos_module = juniper_junos_common.JuniperJunosModule(
        argument_spec=argument_spec,
        supports_check_mode=False ## TODO Need to add support for Check
    )

    # Set initial results values. Assume failure until we know it's success.
    results = {'msg': '', 'changed': False, 'failed': False}

    # We're going to be using params a lot
    params = junos_module.params

    junos_module.logger.info("Starting the file transfer: {0}".format(params['file']))

    remote_path=params['remote_dir']
    
    local_file=params['local_dir']+"/"+params['file']
    remote_file=params['remote_dir']+"/"+params['file']
    if (params['action'] == "put"):
        junos_module.logger.info('computing local MD5 checksum on: %s' % local_file)
        local_checksum = local_md5(junos_module, local_file)
        junos_module.logger.info('Local checksum: %s' % local_checksum) 
        remote_checksum = remote_md5(junos_module, remote_file)
        if ((remote_checksum == "no_file") or (remote_checksum != local_checksum)):
            status="File not present, need to transfert" 
            junos_module.logger.info(status)

            with SCP(junos_module.dev) as scp1:
                scp1.put(local_file,remote_path)

            # validate checksum:
            junos_module.logger.info('computing remote MD5 checksum on: %s' % remote_file)
            remote_checksum = remote_md5(junos_module, remote_file)
            junos_module.logger.info('Remote checksum: %s' % remote_checksum)
            if remote_checksum != local_checksum:
                status="Transfer failed (different MD5 between local and remote) {} | {}".format( 
                        local_checksum,
                        remote_checksum
                    )
                junos_module.logger.error(status)
                junos_module.fail_json(msg=status)
                return False
            else:
                junos_module.logger.info("checksum check passed.")
                status="File pushed OK"
                results['changed'] = True
        else: 
            status="File already present, skipping the scp" 
            junos_module.logger.info(status)

    elif (params['action'] == "get"): 
        junos_module.logger.info('computing remote MD5 checksum on: %s' % remote_file)
        remote_checksum = remote_md5(junos_module, remote_file)
        junos_module.logger.info('Remote checksum: %s' % remote_checksum)
        local_checksum = local_md5(junos_module, local_file)
        if ((local_checksum == "no_file") or (remote_checksum != local_checksum)):

            with SCP(junos_module.dev) as scp1:
                scp1.get(remote_file,local_file)

            # validate checksum:
            junos_module.logger.info('Computing local MD5 checksum on: %s' % local_file)
            local_checksum = local_md5(junos_module, local_file)
            junos_module.logger.info('Local checksum: %s' % local_checksum)

            if remote_checksum != local_checksum:
                junos_module.logger.error("Checksum check failed.")
                status="Transfer failed (different MD5 between local and remote) {} | {}".format( 
                        local_checksum,
                        remote_checksum
                    )
                junos_module.fail_json(msg=status)
                return False
            else:
                junos_module.logger.info("Checksum check passed.")

                status="File retrieved OK"
                results['changed'] = True

        else:
            status="File already present, skipping the scp"
            junos_module.logger.info(status)

    results['msg'] = status

    # Return results.
    junos_module.exit_json(**results)


if __name__ == '__main__':
    main()
