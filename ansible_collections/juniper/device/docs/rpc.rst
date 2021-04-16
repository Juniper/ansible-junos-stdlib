.. _rpc:

rpc
+++
Execute one or more NETCONF RPCs on a Junos device



.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Execute one or more NETCONF RPCs on a Junos device.
* Use the ``| display xml rpc`` modifier to determine the equivalent RPC name for a Junos CLI command.  For example, ``show version | display xml rpc`` reveals the equivalent RPC name is ``get-software-information``.



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
    <td>attrs<br/><div style="font-size: small;"></div></td>
    <td>dict or list of dict</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The attributes and values to the RPCs specified by the <em>rpcs</em> option. The value of this option can either be a single dictionary of keywords and values, or a list of dictionaries containing keywords and values.</div>
        <div>There is a one-to-one correspondence between the elements in the <em>kwargs</em> list and the RPCs in the <em>rpcs</em> list. In other words, the two lists must always contain the same number of elements.</div>
        </br><div style="font-size: small;">aliases: attr</div>
    </td>
    </tr>

    <tr>
    <td>dest<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>None</td>
    <td></td>
    <td>
        <div>The path to a file, on the Ansible control machine, where the output of the RPC will be saved.</div>
        <div>The file must be writeable. If the file already exists, it is overwritten.</div>
        <div>When tasks are executed against more than one target host, one process is forked for each target host. (Up to the maximum specified by the forks configuration. See <a href='http://docs.ansible.com/ansible/latest/intro_configuration.html#forks'>forks</a> for details.) This means that the value of this option must be unique per target host. This is usually accomplished by including <code>{{ inventory_hostname }}</code> in the <em>dest</em> value. It is the user&#x27;s responsibility to ensure this value is unique per target host.</div>
        <div>For this reason, this option is deprecated. It is maintained for backwards compatibility. Use the <em>dest_dir</em> option in new playbooks. The <em>dest</em> and <em>dest_dir</em> options are mutually exclusive.</div>
        </br><div style="font-size: small;">aliases: destination</div>
    </td>
    </tr>

    <tr>
    <td>dest_dir<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>None</td>
    <td></td>
    <td>
        <div>The path to a directory, on the Ansible control machine, where the output of the RPC will be saved. The output will be logged to a file named <code>{{ inventory_hostname }}_</code><em>rpc</em>.<em>format</em> in the <em>dest_dir</em> directory.</div>
        <div>The destination file must be writeable. If the file already exists, it is overwritten. It is the users responsibility to ensure a unique <em>dest_dir</em> value is provided for each execution of this module within a playbook.</div>
        <div>The <em>dest_dir</em> and <em>dest</em> options are mutually exclusive. The <em>dest_dir</em> option is recommended for all new playbooks.</div>
        </br><div style="font-size: small;">aliases: destination_dir, destdir</div>
    </td>
    </tr>

    <tr>
    <td>filter<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>This argument only applies if the <em>rpcs</em> option contains a single RPC with the value <code>get-config</code>. When used, this value specifies an XML filter used to restrict the portions of the configuration which are retrieved. See the PyEZ <a href='http://junos-pyez.readthedocs.io/en/stable/jnpr.junos.html#jnpr.junos.rpcmeta._RpcMetaExec.get_config'>get_config method</a> for details on the value of this option.</div>
        </br><div style="font-size: small;">aliases: filter_xml</div>
    </td>
    </tr>

    <tr>
    <td>formats<br/><div style="font-size: small;"></div></td>
    <td>str or list of str</td>
    <td>no</td>
    <td>xml</td>
    <td><ul><li>text</li><li>xml</li><li>json</li></ul></td>
    <td>
        <div>The format of the reply for the RPCs specified by the <em>rpcs</em> option.</div>
        <div>The specified format(s) must be supported by the target Junos device.</div>
        <div>The value of this option can either be a single format, or a list of formats. If a single format is specified, it applies to all RPCs specified by the <em>rpcs</em> option. If a list of formats are specified, there must be one value in the list for each RPC specified by the <em>rpcs</em> option.</div>
        </br><div style="font-size: small;">aliases: format, display, output</div>
    </td>
    </tr>

    <tr>
    <td>ignore_warning<br/><div style="font-size: small;"></div></td>
    <td>bool, str, or list of str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>A boolean, string or list of strings. If the value is <code>true</code>, ignore all warnings regardless of the warning message. If the value is a string, it will ignore warning(s) if the message of each warning matches the string. If the value is a list of strings, ignore warning(s) if the message of each warning matches at least one of the strings in the list. The value of the <em>ignore_warning</em> option is applied to the load and commit operations performed by this module.</div>
    </td>
    </tr>

    <tr>
    <td>kwargs<br/><div style="font-size: small;"></div></td>
    <td>dict or list of dict</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The keyword arguments and values to the RPCs specified by the <em>rpcs</em> option. The value of this option can either be a single dictionary of keywords and values, or a list of dictionaries containing keywords and values.</div>
        <div>There must be a one-to-one correspondence between the elements in the <em>kwargs</em> list and the RPCs in the <em>rpcs</em> list. In other words, the two lists must always contain the same number of elements. For RPC arguments which do not require a value, specify the value of True as shown in the :ref:`rpc-examples-label`.</div>
        </br><div style="font-size: small;">aliases: kwarg, args, arg</div>
    </td>
    </tr>

    <tr>
    <td>return_output<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Indicates if the output of the RPC should be returned in the module&#x27;s response. You might want to set this option to <code>false</code>, and set the <em>dest_dir</em> option, if the RPC output is very large and you only need to save the output rather than using it&#x27;s content in subsequent tasks/plays of your playbook.</div>
    </td>
    </tr>

    <tr>
    <td>rpcs<br/><div style="font-size: small;"></div></td>
    <td>list</td>
    <td>yes</td>
    <td>none</td>
    <td></td>
    <td>
        <div>A list of one or more NETCONF RPCs to execute on the Junos device.</div>
        </br><div style="font-size: small;">aliases: rpc</div>
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

.. _rpc-examples-label:

Examples
--------

::

    
    ---
    - name: 'Explicit host argument'
      hosts: junos
      connection: local
      gather_facts: no
      collections:
        - juniper.device

      tasks:
        - name: "Execute RPC with filters"
          rpc:
            rpcs:
               - "get-config"
            format: xml
            filter: <configuration><groups><name>re0</name></groups></configuration>
            attr: name=re0
          register: test1
          ignore_errors: True

        - name: Check TEST 1
          debug:
            var: test1

        - name: "Execute RPC with host data and store logging"
          rpc:
            host: "10.x.x.x"
            user: "user"
            passwd: "user123"
            port: "22"
            rpcs:
              - "get-software-information"
            logfile: "/var/tmp/rpc.log"
            ignore_warning: true
          register: test1
          ignore_errors: True

        - name: "Print results - summary"
          debug:
            var: test1.stdout_lines

        - name: "Execute multiple RPC"
          rpc:
            rpcs:
              - "get-config"
              - "get-software-information"

        - name: Get Device Configuration for vlan - 1
          rpc:
            rpc: "get-config"
            filter_xml: "<configuration><vlans/></configuration>"
            dest: "get_config_vlan.conf"
          register: junos

        - name: Get interface information with kwargs
          rpc:
            rpc: get-interface-information
            kwargs:
              interface_name: em1
              media: True
            format: json
            dest: get_interface_information.conf
          register: junos


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
    <td>attrs</td>
    <td>
        <div>The RPC attributes and values from the list of dictionaries in the <em>attrs</em> option. This will be none if no attributes are applied to the RPC.</div>
    </td>
    <td align=center>always</td>
    <td align=center>dict</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>changed</td>
    <td>
        <div>Indicates if the device&#x27;s state has changed. Since this module doesn&#x27;t change the operational or configuration state of the device, the value is always set to <code>false</code>.</div>
        <div>You could use this module to execute an RPC which changes the operational state of the the device. For example, <code>clear-ospf-neighbor-information</code>. Beware, this module is unable to detect this situation, and will still return a <em>changed</em> value of <code>false</code> in this case.</div>
    </td>
    <td align=center>success</td>
    <td align=center>bool</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>failed</td>
    <td>
        <div>Indicates if the task failed. See the <em>results</em> key for additional details.</div>
    </td>
    <td align=center>always</td>
    <td align=center>bool</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>format</td>
    <td>
        <div>The format of the RPC response from the list of formats in the <em>formats</em> option.</div>
    </td>
    <td align=center>always</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>kwargs</td>
    <td>
        <div>The keyword arguments from the list of dictionaries in the <em>kwargs</em> option. This will be <code>none</code> if no kwargs are applied to the RPC.</div>
    </td>
    <td align=center>always</td>
    <td align=center>dict</td>
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
    <td>parsed_output</td>
    <td>
        <div>The RPC reply from the Junos device parsed into a JSON datastructure. For XML replies, the response is parsed into JSON using the <a href='https://github.com/Juniper/jxmlease'>jxmlease</a> library. For JSON the response is parsed using the Python <a href='https://docs.python.org/2/library/json.html'>json</a> library.</div>
        <div>When Ansible converts the jxmlease or native Python data structure into JSON, it does not guarantee that the order of dictionary/object keys are maintained.</div>
    </td>
    <td align=center>when RPC executed successfully, <em>return_output</em> is <code>true</code>, and the RPC format is <code>xml</code> or <code>json</code>.</td>
    <td align=center>dict</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>results</td>
    <td>
        <div>The other keys are returned when a single RPC is specified for the <em>rpcs</em> option. When the value of the <em>rpcs</em> option is a list of RPCs, this key is returned instead. The value of this key is a list of dictionaries. Each element in the list corresponds to the RPCs in the <em>rpcs</em> option. The keys for each element in the list include all of the other keys listed. The <em>failed</em> key indicates if the individual RPC failed. In this case, there is also a top-level <em>failed</em> key. The top-level <em>failed</em> key will have a value of <code>false</code> if ANY of the RPCs ran successfully. In this case, check the value of the <em>failed</em> key for each element in the <em>results</em> list for the results of individual RPCs.</div>
    </td>
    <td align=center>when the <em>rpcs</em> option is a list value.</td>
    <td align=center>list of dict</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>rpc</td>
    <td>
        <div>The RPC which was executed from the list of RPCs in the <em>rpcs</em> option.</div>
    </td>
    <td align=center>always</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>stdout</td>
    <td>
        <div>The RPC reply from the Junos device as a single multi-line string.</div>
    </td>
    <td align=center>when RPC executed successfully and <em>return_output</em> is <code>true</code>.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>stdout_lines</td>
    <td>
        <div>The RPC reply from the Junos device as a list of single-line strings.</div>
    </td>
    <td align=center>when RPC executed successfully and <em>return_output</em> is <code>true</code>.</td>
    <td align=center>list of str</td>
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


