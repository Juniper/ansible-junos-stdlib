.. _table:

table
+++++
Retrieve data from a Junos device using a PyEZ table/view



.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Retrieve data from a Junos device using PyEZ's operational table/views. This module may be used with the tables/views which are included in the PyEZ distribution or it may be used with user-defined tables/views.



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
    <td>file<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>yes</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Name of the YAML file, relative to the <em>path</em> option, that contains the table/view definition. The file name must end with the <code>.yml</code> or <code>.yaml</code> extension.</div>
    </td>
    </tr>

    <tr>
    <td>kwargs<br/><div style="font-size: small;"></div></td>
    <td>dict</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Optional keyword arguments and values to the table&#x27;s get() method. The value of this option is a dictionary of keywords and values which are used to refine the data return from performing a get() on the table. The exact keywords and values which are supported are specific to the table&#x27;s definition and the underlying RPC which the table invokes.</div>
        </br><div style="font-size: small;">aliases: kwarg, args, arg</div>
    </td>
    </tr>

    <tr>
    <td>path<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td><code>op</code> directory in <code>jnpr.junos.op</code></td>
    <td></td>
    <td>
        <div>The directory containing the YAML table/view definition file as specified by the <em>file</em> option. The default value is the <code>op</code> directory in <code>jnpr.junos.op</code>. This is the directory containing the table/view definitions which are included in the PyEZ distribution.</div>
        </br><div style="font-size: small;">aliases: directory, dir</div>
    </td>
    </tr>

    <tr>
    <td>response_type<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>list_of_dicts</td>
    <td><ul><li>list_of_dicts</li><li>juniper_items</li></ul></td>
    <td>
        <div>Defines the format of data returned by the module. See RETURN. The value of the <em>resource</em> key in the module&#x27;s response is either a list of dictionaries <code>list_of_dicts</code> or PyEZ&#x27;s native return format <code>juniper_items</code>. Because Ansible module&#x27;s may only return JSON data, PyEZ&#x27;s native return format <code>juniper_items</code> is translated into a list of lists.</div>
    </td>
    </tr>

    <tr>
    <td>table<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>The name of the table defined in the <em>file</em> option.</td>
    <td></td>
    <td>
        <div>Name of the PyEZ table used to retrieve data. If not specified, defaults to the name of the table defined in the <em>file</em> option. Any table names in <em>file</em> which begin with <code>_</code> are ignored. If more than one table is defined in <em>file</em>, the module fails with an error message. In this case, you must manually specify the name of the table by setting this option.</div>
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

.. _table-examples-label:

Examples
--------

::

    
    ---
    - name: Retrieve data from a Junos device using a PyEZ table/view.
      hosts: junos-all
      connection: local
      gather_facts: no
      collections:
        - juniper.device

      tasks:
        - name: Retrieve LLDP Neighbor Information Using PyEZ-included Table
          table:
            file: "lldp.yml"
          register: response
        - name: Print response
          debug:
            var: response

        - name: Retrieve routes within 192.68.1/8
          table:
            file: "routes.yml"
            table: "RouteTable"
            kwargs:
              destination: "192.68.1.0/8"
            response_type: "juniper_items"
          register: response
        - name: Print response
          debug:
            var: response

        - name: Retrieve from custom table in playbook directory
          table:
            file: "fpc.yaml"
            path: "."
          register: response
        - name: Print response
          debug:
            var: response



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
        <div>Indicates if the device&#x27;s configuration has changed. Since this module does not change the operational or configuration state of the device, the value is always set to <code>false</code>.</div>
    </td>
    <td align=center>success</td>
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
    <td>msg</td>
    <td>
        <div>A human-readable message indicating a summary of the result.</div>
    </td>
    <td align=center>always</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>resource</td>
    <td>
        <div>The items retrieved by the table/view.</div>
    </td>
    <td align=center>success</td>
    <td align=center>list of dicts if <em>response_type</em> is <code>list_of_dicts</code> or list of lists if <em>respsonse_type</em> is <code>juniper_items</code>.</td>
    <td align=center># when response_type == &#x27;list_of_dicts&#x27;
    [
      {
         &quot;local_int&quot;: &quot;ge-0/0/3&quot;, 
         &quot;local_parent&quot;: &quot;-&quot;, 
         &quot;remote_chassis_id&quot;: &quot;00:05:86:08:d4:c0&quot;, 
         &quot;remote_port_desc&quot;: null, 
         &quot;remote_port_id&quot;: &quot;ge-0/0/0&quot;, 
         &quot;remote_sysname&quot;: &quot;r5&quot;, 
         &quot;remote_type&quot;: &quot;Mac address&quot;
      }, 
      {
         &quot;local_int&quot;: &quot;ge-0/0/0&quot;, 
         &quot;local_parent&quot;: &quot;-&quot;, 
         &quot;remote_chassis_id&quot;: &quot;00:05:86:18:f3:c0&quot;, 
         &quot;remote_port_desc&quot;: null, 
         &quot;remote_port_id&quot;: &quot;ge-0/0/2&quot;, 
         &quot;remote_sysname&quot;: &quot;r4&quot;, 
         &quot;remote_type&quot;: &quot;Mac address&quot;
      }
    ]
    # when response_type == &#x27;juniper_items&#x27;
    [
      [
        &quot;ge-0/0/3&quot;, 
        [
          [
            &quot;local_parent&quot;, 
            &quot;-&quot;
          ], 
          [
            &quot;remote_port_id&quot;, 
            &quot;ge-0/0/0&quot;
          ], 
          [
            &quot;remote_chassis_id&quot;, 
            &quot;00:05:86:08:d4:c0&quot;
          ], 
          [
            &quot;remote_port_desc&quot;, 
            null
          ], 
          [
            &quot;remote_type&quot;, 
            &quot;Mac address&quot;
          ], 
          [
            &quot;local_int&quot;, 
            &quot;ge-0/0/3&quot;
          ], 
          [
            &quot;remote_sysname&quot;, 
            &quot;r5&quot;
          ]
        ]
      ], 
      [
        &quot;ge-0/0/0&quot;, 
        [
          [
            &quot;local_parent&quot;, 
            &quot;-&quot;
          ], 
          [
            &quot;remote_port_id&quot;, 
            &quot;ge-0/0/2&quot;
          ], 
          [
            &quot;remote_chassis_id&quot;, 
            &quot;00:05:86:18:f3:c0&quot;
          ], 
          [
            &quot;remote_port_desc&quot;, 
            null
          ], 
          [
            &quot;remote_type&quot;, 
            &quot;Mac address&quot;
          ], 
          [
            &quot;local_int&quot;, 
            &quot;ge-0/0/0&quot;
          ], 
          [
            &quot;remote_sysname&quot;, 
            &quot;r4&quot;
          ]
        ]
      ]
    ]
    </td>
    </tr>

    </table>
    </br>
    </br>


Notes
-----

.. note::
    - This module only works with operational tables/views; it does not work with configuration tables/views.
    - The NETCONF system service must be enabled on the target Junos device.


Author
~~~~~~

* Jason Edelman (@jedelman8)
* Updated by Juniper Networks - Stacy Smith (@stacywsmith)




Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that no backward incompatible interface changes will be made.


