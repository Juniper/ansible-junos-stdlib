.. _file_copy:

file_copy
+++++++++
File put and get module



.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Copy file over SCP to and from a Juniper device


.. _module-specific-options-label:

Module-specific Options
-----------------------
The following options may be specified for this module:

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">parameter</th>
    <th class="head">type</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>

    <tr>
    <td>action<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Type of operation to execute, currently only support get and put</div>
    </td>
    </tr>

    <tr>
    <td>file<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the file to copy to/from the remote device</div>
    </td>
    </tr>

    <tr>
    <td>local_dir<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>path of the local directory where the file is located or needs to be copied to</div>
    </td>
    </tr>

    <tr>
    <td>remote_dir<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>path of the directory on the remote device where the file is located or needs to be copied to</div>
    </td>
    </tr>

    </table>
    </br>

.. _file_copy-examples-label:

Examples
--------

::


    ---
    - name: Examples of juniper_device_file_copy
      hosts: all
      connection: local
      gather_facts: false
      tasks:
        - name: Copy a log file on a remote device locally
          juniper.device.file_copy:
            remote_dir: /var/log
            local_dir: /tmp
            action: get
            file: log.txt
        - name: Copy a local file into /var/tmp on the remote device
          juniper.device.file_copy:
            remote_dir: /var/tmp
            local_dir: /tmp
            action: put
            file: license.txt





Author
~~~~~~

* Juniper Networks - Dinesh Babu (@dineshbaburam91)




Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that no backward incompatible interface changes will be made.
