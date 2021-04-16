.. _ping:

ping
++++
Execute ping from a Junos device



.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Execute the ping command from a Junos device to a specified destination in order to test network reachability from the Junos device .



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
    <td>acceptable_percent_loss<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>0</td>
    <td></td>
    <td>
        <div>Maximum percentage of packets that may be lost and still consider the task not to have failed.</div>
        </br><div style="font-size: small;">aliases: acceptable_packet_loss</div>
    </td>
    </tr>

    <tr>
    <td>count<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>5</td>
    <td></td>
    <td>
        <div>Number of packets to send.</div>
    </td>
    </tr>

    <tr>
    <td>dest<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The IP address, or hostname if DNS is configured on the Junos device, used as the destination of the ping.</div>
        </br><div style="font-size: small;">aliases: dest_ip, dest_host, destination, destination_ip, destination_host</div>
    </td>
    </tr>

    <tr>
    <td>do_not_fragment<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>False</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Set Do Not Fragment bit on ping packets.</div>
    </td>
    </tr>

    <tr>
    <td>interface<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The source interface from which the the ping is sent. If not specified, the default Junos algorithm for determining the source interface is used.</div>
    </td>
    </tr>

    <tr>
    <td>rapid<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Send ping requests rapidly</div>
    </td>
    </tr>

    <tr>
    <td>routing_instance<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Name of the source routing instance from which the ping is originated. If not specified, the default routing instance is used.</div>
    </td>
    </tr>

    <tr>
    <td>size<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>none (default size for device)</td>
    <td></td>
    <td>
        <div>The size of the ICMP payload of the ping.</div>
        <div>Total size of the IP packet is <em>size</em> + the 20 byte IP header + the 8 byte ICMP header. Therefore, <em>size</em> of <code>1472</code> generates an IP packet of size 1500.</div>
    </td>
    </tr>

    <tr>
    <td>source<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The IP address, or hostname if DNS is configured on the Junos device, used as the source address of the ping. If not specified, the Junos default algorithm for determining the source address is used.</div>
        </br><div style="font-size: small;">aliases: source_ip, source_host, src, src_ip, src_host</div>
    </td>
    </tr>

    <tr>
    <td>ttl<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>none (default ttl for device)</td>
    <td></td>
    <td>
        <div>Maximum number of IP routers (hops) allowed between source and destination.</div>
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

.. _ping-examples-label:

Examples
--------

::

    
    ---
    - name: Examples of ping
      hosts: junos-all
      connection: local
      gather_facts: no
      collections:
        - juniper.device

      tasks:
        - name: Ping 192.68.1.1 with default parameters. Fails if any packets lost.
          ping:
            dest: "192.68.1.1"

        - name: Ping 192.68.1.1 Allow 50% packet loss. Register response.
          ping:
            dest: "192.68.1.1"
            acceptable_percent_loss: 50
          register: response
        - name: Print all keys in the response.
          debug:
            var: response

        - name: Ping 192.68.1.1. Send 20 packets. Register response.
          ping:
            dest: "192.68.1.1"
            count: 20
          register: response
        - name: Print packet sent from the response.
          debug:
            var: response.packets_sent

        - name: Ping 192.68.1.1. Send 10 packets wihtout rapid. Register response.
          ping:
            dest: "192.68.1.1"
            count: 10
            rapid: false
          register: response
        - name: Print the average round-trip-time from the response.
          debug:
            var: response.rtt_average

        - name: Ping www.juniper.net with ttl 15. Register response.
          ping:
            dest: "www.juniper.net"
            ttl: 15
          register: response
        - name: Print the packet_loss percentage from the response.
          debug:
            var: response.packet_loss

        - name: Ping 192.68.1.1 with IP packet size of 1500. Register response.
          ping:
            dest: "192.68.1.1"
            size: 1472
          register: response
        - name: Print the packets_received from the response.
          debug:
            var: response.packets_received

        - name: Ping 192.68.1.1 with do-not-fragment bit set. Register response.
          ping:
            dest: "192.68.1.1"
            do_not_fragment: true
          register: response
        - name: Print the maximum round-trip-time from the response.
          debug:
            var: response.rtt_maximum

        - name: Ping 192.68.1.1 with source set to 192.68.1.2. Register response.
          ping:
            dest: "192.68.1.1"
            source: "192.68.1.2"
          register: response
        - name: Print the source from the response.
          debug:
            var: response.source

        - name: Ping 192.168.1.1 from the red routing-instance.
          ping:
            dest: "192.168.1.1"
            routing_instance: "red"

        - name: Ping the all-hosts multicast address from the ge-0/0/0.0 interface
          ping:
            dest: "224.0.0.1"
            interface: "ge-0/0/0.0"



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
    <td>acceptable_percent_loss</td>
    <td>
        <div>The acceptable packet loss (as a percentage) for this task as specified by the <em>acceptable_percent_loss</em> option.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>changed</td>
    <td>
        <div>Indicates if the device&#x27;s state has changed. Since this module doesn&#x27;t change the operational or configuration state of the device, the value is always set to <code>false</code>.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>bool</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>count</td>
    <td>
        <div>The number of pings sent, as specified by the <em>count</em> option.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>do_not_fragment</td>
    <td>
        <div>Whether or not the do not fragment bit was set on the pings sent, as specified by the <em>do_not_fragment</em> option.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
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
        <div>The destination IP/host of the pings sent as specified by the <em>dest</em> option.</div>
        <div>Keys <em>dest</em> and <em>dest_ip</em> are also returned for backwards compatibility.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>interface</td>
    <td>
        <div>The source interface of the pings sent as specified by the <em>interface</em> option.</div>
    </td>
    <td align=center>when ping successfully executed and the <em>interface</em> option was specified, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>msg</td>
    <td>
        <div>A human-readable message indicating the result.</div>
    </td>
    <td align=center>always</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>packet_loss</td>
    <td>
        <div>The percentage of packets lost.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>packets_received</td>
    <td>
        <div>The number of packets received.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>packets_sent</td>
    <td>
        <div>The number of packets sent.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>rapid</td>
    <td>
        <div>Whether or not the pings were sent rapidly, as specified by the <em>rapid</em> option.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>bool</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>routing_instance</td>
    <td>
        <div>The routing-instance from which the pings were sent as specified by the <em>routing_instance</em> option.</div>
    </td>
    <td align=center>when ping successfully executed and the <em>routing_instance</em> option was specified, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>rtt_average</td>
    <td>
        <div>The average round-trip-time, in microseconds, of all ping responses received.</div>
    </td>
    <td align=center>when ping successfully executed, and <em>packet_loss</em> &lt; 100%.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>rtt_maximum</td>
    <td>
        <div>The maximum round-trip-time, in microseconds, of all ping responses received.</div>
    </td>
    <td align=center>when ping successfully executed, and <em>packet_loss</em> &lt; 100%.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>rtt_minimum</td>
    <td>
        <div>The minimum round-trip-time, in microseconds, of all ping responses received.</div>
    </td>
    <td align=center>when ping successfully executed, and <em>packet_loss</em> &lt; 100%.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>rtt_stddev</td>
    <td>
        <div>The standard deviation of round-trip-time, in microseconds, of all ping responses received.</div>
    </td>
    <td align=center>when ping successfully executed, and <em>packet_loss</em> &lt; 100%.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>size</td>
    <td>
        <div>The size in bytes of the ICMP payload on the pings sent as specified by the <em>size</em> option.</div>
        <div>Total size of the IP packet is <em>size</em> + the 20 byte IP header + the 8 byte ICMP header. Therefore, <em>size</em> of 1472 generates an IP packet of size 1500.</div>
    </td>
    <td align=center>when ping successfully executed and the <em>size</em> option was specified, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>source</td>
    <td>
        <div>The source IP/host of the pings sent as specified by the <em>source</em> option.</div>
        <div>Key <em>source_ip</em> is also returned for backwards compatibility.</div>
    </td>
    <td align=center>when ping successfully executed and the <em>source</em> option was specified, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>timeout</td>
    <td>
        <div>The number of seconds to wait for a response from the ping RPC.</div>
    </td>
    <td align=center>when ping successfully executed, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>ttl</td>
    <td>
        <div>The time-to-live set on the pings sent as specified by the <em>ttl</em> option.</div>
    </td>
    <td align=center>when ping successfully executed and the <em>ttl</em> option was specified, even if the <em>acceptable_percent_loss</em> was exceeded.</td>
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

* Juniper Networks - Stacy Smith (@stacywsmith)




Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that no backward incompatible interface changes will be made.


