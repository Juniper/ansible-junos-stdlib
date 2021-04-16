.. _pmtud:

pmtud
+++++
Perform path MTU discovery from a Junos device to a destination



.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Determine the maximum IP MTU supported along a path from a Junos device to a user-specified destination by performing path MTU discovery (PMTUD) using the ping command. The reported MTU will be between min_test_size and *max_size* where *min_test_size* = (*max_size* - *max_range* + 1). If the actual path MTU is greater than *max_size*, then *max_size* will be reported. If the actual path MTU is less than *min_test_size*, then a failure will be reported.



Requirements
------------
The following software packages must be installed on hosts that execute this module:

* `junos-eznc <https://github.com/Juniper/py-junos-eznc>`_ >= 2.5.2
* Python >= 3.5



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
    <td>dest<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The IPv4 address, or hostname if DNS is configured on the Junos device, used as the destination of the PMTUD.</div>
        </br><div style="font-size: small;">aliases: dest_ip, dest_host, destination, destination_ip, destination_host</div>
    </td>
    </tr>

    <tr>
    <td>interface<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The source interface from which the the PMTUD is performed. If not specified, the default Junos algorithm for determining the source interface is used.</div>
    </td>
    </tr>

    <tr>
    <td>max_range<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>512</td>
    <td></td>
    <td>
        <div>The maximum range of MTU values, in bytes, which will be searched when performing path MTU discovery. This value must be <code>0</code> or a power of 2 (2^n) between <code>2</code> and <code>65536</code>. The minimum IPv4 MTU value attempted when performing path MTU discovery is <em>min_test_size</em> = (<em>max_size</em> - <em>max_range</em> + 1)</div>
    </td>
    </tr>

    <tr>
    <td>max_size<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>1500</td>
    <td></td>
    <td>
        <div>The maximum IPv4 MTU, in bytes, to attempt when performing path MTU discovery.</div>
        <div>The value returned for <em>inet_mtu</em> will be no more than this value even if the path actually supports a higher MTU.</div>
        <div>This value must be between 68 and 65496.</div>
    </td>
    </tr>

    <tr>
    <td>routing_instance<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Name of the source routing instance from which the ping is originated.</div>
        <div>If not specified, the default routing instance is used.</div>
    </td>
    </tr>

    <tr>
    <td>source<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The IPv4 address, or hostname if DNS is configured on the Junos device, used as the source address of the PMTUD. If not specified, the Junos default algorithm for determining the source address is used.</div>
        </br><div style="font-size: small;">aliases: source_ip, source_host, src, src_ip, src_host</div>
    </td>
    </tr>

    </table>
    </br>

Common Connection-related Options
---------------------------------
In addition to the :ref:`module-specific-options-label`, the following connection-related options are also supported by this module:

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
    <td>attempts<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>10</td>
    <td></td>
    <td>
        <div>The number of times to try connecting and logging in to the Junos device. This option is only applicable when using <code>mode = &#x27;telnet&#x27;</code> or <code>mode = &#x27;serial&#x27;</code>. Mutually exclusive with the <em>console</em> option.</div>
    </td>
    </tr>

    <tr>
    <td>baud<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>9600</td>
    <td></td>
    <td>
        <div>The serial baud rate, in bits per second, used to connect to the Junos device. This option is only applicable when using <code>mode = &#x27;serial&#x27;</code>. Mutually exclusive with the <em>console</em> option.</div>
    </td>
    </tr>

    <tr>
    <td>console<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>An alternate method of specifying a NETCONF over serial console connection to the Junos device using Telnet to a console server. The value of this option must be a string in the format <code>--telnet &lt;console_hostname&gt;,&lt;console_port_number&gt;</code>. This option is deprecated. It is present only for backwards compatibility. The string value of this option is exactly equivalent to specifying <em>host</em> with a value of <code>&lt;console_hostname&gt;</code>, <em>mode</em> with a value of <code>telnet</code>, and <em>port</em> with a value of <code>&lt;console_port_number&gt;</code>. Mutually exclusive with the <em>mode</em>, <em>port</em>, <em>baud</em>, and <em>attempts</em> options.</div>
    </td>
    </tr>

    <tr>
    <td>cs_passwd<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The password used to authenticate with the console server over SSH. This option is only required if you want to connect to a device over console using SSH as transport. Mutually exclusive with the <em>console</em> option.</div>
        </br><div style="font-size: small;">aliases: console_password</div>
    </td>
    </tr>

    <tr>
    <td>cs_user<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The username used to authenticate with the console server over SSH. This option is only required if you want to connect to a device over console using SSH as transport. Mutually exclusive with the <em>console</em> option.</div>
        </br><div style="font-size: small;">aliases: console_username</div>
    </td>
    </tr>

    <tr>
    <td>host<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td><code>{{ inventory_hostname }}</code></td>
    <td></td>
    <td>
        <div>The hostname or IP address of the Junos device to which the connection should be established. This is normally the Junos device itself, but is the hostname or IP address of a console server when connecting to the console of the device by setting the <em>mode</em> option to the value <code>telnet</code>. This option is required, but does not have to be specified explicitly by the user because it defaults to <code>{{ inventory_hostname }}</code>.</div>
        </br><div style="font-size: small;">aliases: hostname, ip</div>
    </td>
    </tr>

    <tr>
    <td>mode<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td><ul><li>none</li><li>telnet</li><li>serial</li></ul></td>
    <td>
        <div>The PyEZ mode used to establish a NETCONF connection to the Junos device. A value of <code>none</code> uses the default NETCONF over SSH mode. Depending on the values of the <em>host</em> and <em>port</em> options, a value of <code>telnet</code> results in either a direct NETCONF over Telnet connection to the Junos device, or a NETCONF over serial console connection to the Junos device using Telnet to a console server. A value of <code>serial</code> results in a NETCONF over serial console connection to the Junos device. Mutually exclusive with the <em>console</em> option.</div>
    </td>
    </tr>

    <tr>
    <td>passwd<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>The first defined value from the following list 1) The <code>ANSIBLE_NET_PASSWORD</code> environment variable. (used by Ansible Tower) 2) The value specified using the <code>-k</code> or <code>--ask-pass</code> command line arguments to the <code>ansible</code> or <code>ansible-playbook</code> command. 3) none (An empty password/passphrase)</td>
    <td></td>
    <td>
        <div>The password, or ssh key&#x27;s passphrase, used to authenticate with the Junos device. If this option is not specified, authentication is attempted using an empty password, or ssh key passphrase.</div>
        </br><div style="font-size: small;">aliases: password</div>
    </td>
    </tr>

    <tr>
    <td>port<br/><div style="font-size: small;"></div></td>
    <td>int or str</td>
    <td>no</td>
    <td><code>830</code> if <code>mode = none</code>, <code>23</code> if <code>mode = &#x27;telnet&#x27;</code>, <code>&#x27;/dev/ttyUSB0&#x27;</code> if (mode = &#x27;serial&#x27;)</td>
    <td></td>
    <td>
        <div>The TCP port number or serial device port used to establish the connection. Mutually exclusive with the <em>console</em> option.</div>
    </td>
    </tr>

    <tr>
    <td>ssh_config<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The path to the SSH client configuration file. If this option is not specified, then the PyEZ Device instance by default queries file ~/.ssh/config.</div>
    </td>
    </tr>

    <tr>
    <td>ssh_private_key_file<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>The first defined value from the following list 1) The <code>ANSIBLE_NET_SSH_KEYFILE</code> environment variable. (used by Ansible Tower) 2) The value specified using the <code>--private-key</code> or <code>--key-file</code> command line arguments to the <code>ansible</code> or <code>ansible-playbook</code> command. 3) none (the file specified in the user&#x27;s SSH configuration, or the operating-system-specific default)</td>
    <td></td>
    <td>
        <div>The path to the SSH private key file used to authenticate with the Junos device. If this option is not specified, and no default value is found using the algorithm below, then the SSH private key file specified in the user&#x27;s SSH configuration, or the operating-system-specific default is used.</div>
        <div>This must be in the RSA PEM format, and not the newer OPENSSH format. To check if the private key is in the correct format, issue the command `head -n1 ~/.ssh/some_private_key` and ensure that it&#x27;s RSA and not OPENSSH. To create a key in the RSA PEM format, issue the command `ssh-keygen -m PEM -t rsa -b 4096`. To convert an OPENSSH key to an RSA key, issue the command `ssh-keygen -p -m PEM -f ~/.ssh/some_private_key`</div>
        </br><div style="font-size: small;">aliases: ssh_keyfile</div>
    </td>
    </tr>

    <tr>
    <td>timeout<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>30</td>
    <td></td>
    <td>
        <div>The maximum number of seconds to wait for RPC responses from the Junos device. This option does NOT control the initial connection timeout value.</div>
    </td>
    </tr>

    <tr>
    <td>user<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td>The first defined value from the following list 1) The <code>ANSIBLE_NET_USERNAME</code> environment variable. (used by Ansible Tower) 2) The <code>remote_user</code> as defined by Ansible. Ansible sets this value via several methods including a) <code>-u</code> or <code>--user</code> command line arguments to the <code>ansible</code> or <code>ansible-playbook</code> command. b) <code>ANSIBLE_REMOTE_USER</code> environment variable. c) <code>remote_user</code> configuration setting. See the Ansible documentation for the precedence used to set the <code>remote_user</code> value. 3) The <code>USER</code> environment variable.</td>
    <td></td>
    <td>
        <div>The username used to authenticate with the Junos device. This option is required, but does not have to be specified explicitly by the user due to the algorithm for determining the default value.</div>
        </br><div style="font-size: small;">aliases: username</div>
    </td>
    </tr>

    </table>
    </br>

Common Logging-related Options
------------------------------
In addition to the :ref:`module-specific-options-label`, the following logging-related options are also supported by this module:

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
    <td>level<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>WARNING</td>
    <td><ul><li>INFO</li><li>DEBUG</li></ul></td>
    <td>
        <div>The level of information to be logged can be modified using this option</div>
        <div>1) By default, messages at level <code>WARNING</code> or higher are logged.</div>
        <div>2) If the <code>-v</code> or <code>--verbose</code> command-line options to the <code>ansible-playbook</code> command are specified, messages at level <code>INFO</code> or higher are logged.</div>
        <div>3) If the <code>-vv</code> (or more verbose) command-line option to the <code>ansible-playbook</code> command is specified, or the <code>ANSIBLE_DEBUG</code> environment variable is set, then messages at level <code>DEBUG</code> or higher are logged.</div>
        <div>4) If <code>level</code> is mentioned then messages at level <code>level</code> or more are logged.</div>
    </td>
    </tr>

    <tr>
    <td>logdir<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The path to a directory, on the Ansible control machine, where debugging information for the particular task is logged.</div>
        <div>If this option is specified, debugging information is logged to a file named <code>{{ inventory_hostname }}.log</code> in the directory specified by the <em>logdir</em> option.</div>
        <div>The log file must be writeable. If the file already exists, it is appended. It is the users responsibility to delete/rotate log files.</div>
        <div>The level of information logged in this file is controlled by Ansible&#x27;s verbosity, debug options and level option in task</div>
        <div>1) By default, messages at level <code>WARNING</code> or higher are logged.</div>
        <div>2) If the <code>-v</code> or <code>--verbose</code> command-line options to the <code>ansible-playbook</code> command are specified, messages at level <code>INFO</code> or higher are logged.</div>
        <div>3) If the <code>-vv</code> (or more verbose) command-line option to the <code>ansible-playbook</code> command is specified, or the <code>ANSIBLE_DEBUG</code> environment variable is set, then messages at level <code>DEBUG</code> or higher are logged.</div>
        <div>4) If <code>level</code> is mentioned then messages at level <code>level</code> or more are logged.</div>
        <div>The <em>logfile</em> and <em>logdir</em> options are mutually exclusive. The <em>logdir</em> option is recommended for all new playbooks.</div>
        </br><div style="font-size: small;">aliases: log_dir</div>
    </td>
    </tr>

    <tr>
    <td>logfile<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The path to a file, on the Ansible control machine, where debugging information for the particular task is logged.</div>
        <div>The log file must be writeable. If the file already exists, it is appended. It is the users responsibility to delete/rotate log files.</div>
        <div>The level of information logged in this file is controlled by Ansible&#x27;s verbosity, debug options and level option in task</div>
        <div>1) By default, messages at level <code>WARNING</code> or higher are logged.</div>
        <div>2) If the <code>-v</code> or <code>--verbose</code> command-line options to the <code>ansible-playbook</code> command are specified, messages at level <code>INFO</code> or higher are logged.</div>
        <div>3) If the <code>-vv</code> (or more verbose) command-line option to the <code>ansible-playbook</code> command is specified, or the <code>ANSIBLE_DEBUG</code> environment variable is set, then messages at level <code>DEBUG</code> or higher are logged.</div>
        <div>4) If <code>level</code> is mentioned then messages at level <code>level</code> or more are logged.</div>
        <div>When tasks are executed against more than one target host, one process is forked for each target host. (Up to the maximum specified by the forks configuration. See <a href='http://docs.ansible.com/ansible/latest/intro_configuration.html#forks'>forks</a> for details.) This means that the value of this option must be unique per target host. This is usually accomplished by including <code>{{ inventory_hostname }}</code> in the <em>logfile</em> value. It is the user&#x27;s responsibility to ensure this value is unique per target host.</div>
        <div>For this reason, this option is deprecated. It is maintained for backwards compatibility. Use the <em>logdir</em> option in new playbooks. The <em>logfile</em> and <em>logdir</em> options are mutually exclusive.</div>
        </br><div style="font-size: small;">aliases: log_file</div>
    </td>
    </tr>

    </table>
    </br>

.. _pmtud-examples-label:

Examples
--------

::

    
    ---
    - name: Examples of pmtud
      hosts: junos-all
      connection: local
      gather_facts: no
      collections:
        - juniper.device

      tasks:
        - name: Perform PMTUD to 192.68.1.1 with default parameters.
          pmtud:
            dest: "192.68.1.1"

        - name: Perform PMTUD to 192.68.1.1. Register response.
          pmtud:
            dest: "192.68.1.1"
          register: response
        - name: Print the discovered MTU.
          debug:
            var: response.inet_mtu

        - name: Perform PMTUD to 192.68.1.1. Search all possible MTU values.
          pmtud:
            dest: "192.68.1.1"
            max_size: 65496
            max_range: 65536
          register: response
        - name: Print the discovered MTU.
          debug:
            var: response.inet_mtu

        - name: Perform PMTUD to 192.68.1.1. Source from ge-0/0/0.0 interface.
          pmtud:
            dest: "192.68.1.1"
            interface: "ge-0/0/0.0"
          register: response
        - name: Print the discovered MTU.
          debug:
            var: response.inet_mtu

        - name: Perform PMTUD to 192.68.1.1. Source from 192.168.1.2.
          pmtud:
            dest: "192.68.1.1"
            source: "192.168.1.2"
          register: response
        - name: Print the discovered MTU.
          debug:
            var: response.inet_mtu

        - name: Perform PMTUD to 192.68.1.1. Source from the red routing-instance.
          pmtud:
            dest: "192.68.1.1"
            routing_instance: "red"
          register: response
        - name: Print the discovered MTU.
          debug:
            var: response.inet_mtu



Return Values
-------------

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">name</th>
    <th class="head">description</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>


    <tr>
    <td>changed</td>
    <td>
        <div>Indicates if the device&#x27;s state has changed. Since this module doesn&#x27;t change the operational or configuration state of the device, the value is always set to <code>false</code>.</div>
    </td>
    <td align=center>when PMTUD successfully executed.</td>
    <td align=center>bool</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>failed</td>
    <td>
        <div>Indicates if the task failed.</div>
    </td>
    <td align=center>always</td>
    <td align=center>bool</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>host</td>
    <td>
        <div>The destination IP/host of the PMTUD as specified by the <em>dest</em> option.</div>
        <div>Keys <em>dest</em> and <em>dest_ip</em> are also returned for backwards compatibility.</div>
    </td>
    <td align=center>when PMTUD successfully executed.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>inet_mtu</td>
    <td>
        <div>The IPv4 path MTU size in bytes to the <em>dest</em>. This is the lesser of <em>max_size</em> and the actual path MTU to <em>dest</em>. If the actual path MTU is less than <em>min_test_size</em>, then a failure is reported. Where <em>min_test_size</em> = (<em>max_size</em> - <em>max_range</em> + 1)</div>
    </td>
    <td align=center>when PMTUD successfully executed.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>interface</td>
    <td>
        <div>The source interface of the PMTUD as specified by the <em>interface</em> option.</div>
    </td>
    <td align=center>when the <em>interface</em> option was specified.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>routing_instance</td>
    <td>
        <div>The routing-instance from which the PMTUD was performed as specified by the <em>routing_instance</em> option.</div>
    </td>
    <td align=center>when the <em>routing_instance</em> option was specified.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>source</td>
    <td>
        <div>The source IP/host of the PMTUD as specified by the <em>source</em> option.</div>
        <div>Key <em>source_ip</em> is also returned for backwards compatibility.</div>
    </td>
    <td align=center>when the <em>source</em> option was specified.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>warnings</td>
    <td>
        <div>A list of warning strings, if any, produced from the ping.</div>
    </td>
    <td align=center>when warnings are present</td>
    <td align=center>list</td>
    <td align=center></td>
    </tr>

    </table>
    </br>
    </br>


Notes
-----

.. note::
    - The NETCONF system service must be enabled on the target Junos device.


Author
~~~~~~

* Martin Komon (@mkomon)
* Juniper Networks - Stacy Smith (@stacywsmith)




Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that no backward incompatible interface changes will be made.


