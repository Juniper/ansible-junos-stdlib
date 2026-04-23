.. _file_copy:

file_copy
+++++++++
File put and get module



.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Copy file over SCP/FTP to and from a Juniper device


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
    <td>put, get</td>
    <td>
        <div>Type of operation to execute, currently only support get and put</div>
    </td>
    </tr>

    <tr>
    <td>checksum<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>True</td>
    <td></td>
    <td>
        <div>Validate the file using MD5 algorithm check</div>
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
    <td>protocol<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>scp</td>
    <td>scp, ftp</td>
    <td>
        <div>Set the protocol to transfer the file</div>
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

    <tr>
    <td>transfer_filename<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the transfer file to copy to/from the remote device. If not specified, the value of <em>file</em> is used.</div>
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
            protocol: scp
            remote_dir: /var/log
            local_dir: /tmp
            action: get
            checksum: true
            file: log.txt
        - name: Copy a local file into /var/tmp on the remote device
          juniper.device.file_copy:
            protocol: ftp
            remote_dir: /var/tmp
            local_dir: /tmp
            action: put
            checksum: false
            file: license.txt
        - name: Copy a local file to the remote device with a different filename
          juniper.device.file_copy:
            protocol: scp
            remote_dir: /var/tmp
            local_dir: /tmp
            action: put
            file: license.txt
            transfer_filename: license_copy.txt





Author
~~~~~~

* Juniper Networks - Dinesh Babu (@dineshbaburam91)




Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that no backward incompatible interface changes will be made.
