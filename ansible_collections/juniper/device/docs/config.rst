.. _config:

config
++++++
Manipulate the configuration of a Junos device



.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Manipulate the configuration of a Junos device. This module allows a combination of loading or rolling back, checking, diffing, retrieving, and committing the configuration of a Junos device. It performs the following steps in order:
#. Open a candidate configuration database.

   * If the *config_mode* option has a value of ``exclusive``, the default,
     take a lock on the candidate configuration database. If the lock fails
     the module fails and reports an error.
   * If the *config_mode* option has a value of ``private``, open a private
     candidate configuration database. If opening the private configuration
     database fails the module fails and reports an error.
#. Load configuration data into the candidate configuration database.
   
   * Configuration data may be loaded using the *load* or *rollback*
     options. If either of these options are specified, new configuration
     data is loaded. If neither option is specified, this step is skipped.
   * If the *rollback* option is specified, replace the candidate
     configuration with the previous configuration specified by the value
     of the *rollback* option.
   * If the *load* option is specified, load new configuration data.
   * The value of the *load* option defines the type of load which is
     performed.
   * The source of the new configuration data is one of the following:
   
     * *src*      - A file path on the local Ansible control machine.
     * *lines*    - A list of strings containing the configuration data.
     * *template* - A file path to a Jinja2 template on the local
       Ansible control machine. This template is rendered with the variables
       specified by the *vars* option. If the *template* option is
       specified, the *vars* option must also be specified.
     * *url*      - A URL reachable from the target Junos device.
   * If the *format* option is specified, the configuration file being
     loaded is in the specified format, rather than the format determined
     from the file name.
#. Check the validity of the candidate configuration database.

   * If the *check* option is ``true``, the default, check the validity
     of the configuration by performing a "commit check" operation.
   * This option may be specified with *diff* ``false`` and *commit*
     ``false`` to confirm a previous "commit confirmed <min>" operation
     without actually performing an additional commit.
   * If the configuration check fails, further processing stops, the module
     fails, and an error is reported.
#. Determine differences between the candidate and committed configuration
   databases.
   
   * If step 2 was not skipped, and the *diff* option is ``true``,
     the default, perform a diff between the candidate and committed
     configuration databases.
   * If the *diffs_file* or *dest_dir* option is specified, save the
     generated configuration differences.
   * If the *return_output* option is ``true``, the default, include the
     generated configuration difference in the *diff* and *diff_lines*
     keys of the module's response.
#. Retrieve the configuration database from the Junos device.
   
   * If the *retrieve* option is specified, retrieve the configuration
     database specified by the *retrieve* value from the target Junos
     device to the local Ansible control machine.
   * The format in which the configuration is retrieved is specified by the
     value of the *format* option.
   * The optional *filter* controls which portions of the configuration
     are retrieved.
   * If *options* are specified, they control the content of the
     configuration retrieved.
   * If the *dest* or *dest_dir* option is specified, save the
     retrieved configuration to a file on the local Ansible control
     machine.
   * If the *return_output* option is ``true``, the default, include the
     retrieved configuration in the *config*, *config_lines*, and
     *config_parsed* keys of the module's response.
#. Commit the configuration changes.

   * If the *commit* option is ``true``, the default, commit the
     configuration changes.
   * This option may be specified with *diff* ``false`` and *check*
     ``false`` to confirm a previous "commit confirmed <min>" operation.
   * If the *comment* option is specified, add the comment to the commit.
   * If the *confirmed* option is specified, perform a
     ``commit confirmed`` *min* operation where *min* is the value of the
     *confirmed* option.
   * If the *check* option is ``true`` and the *check_commit_wait*
     option is specified, wait *check_commit_wait* seconds before
     performing the commit.
#. Close the candidate configuration database.
   
   * Close and discard the candidate configuration database.
   * If the *config_mode* option has a value of ``exclusive``, the default,
     unlock the candidate configuration database.




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
    <td>check<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>true (false if retrieve is set and load and rollback are not set)</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Perform a commit check operation.</div>
        </br><div style="font-size: small;">aliases: check_commit, commit_check</div>
    </td>
    </tr>

    <tr>
    <td>check_commit_wait<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The number of seconds to wait between check and commit operations.</div>
        <div>This option is only valid if <em>check</em> is <code>true</code> and <em>commit</em> is <code>true</code>.</div>
        <div>This option should not normally be needed. It works around an issue in some versions of Junos.</div>
    </td>
    </tr>

    <tr>
    <td>comment<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Provide a comment to be used with the commit operation.</div>
        <div>This option is only valid if the <em>commit</em> option is true.</div>
    </td>
    </tr>

    <tr>
    <td>commit<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>true (false if retrieve is set and load and rollback are not set)</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Perform a commit operation.</div>
    </td>
    </tr>

    <tr>
    <td>commit_empty_changes<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>False</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Perform a commit operation, even if there are no changes between the candidate configuration and the committed configuration.</div>
    </td>
    </tr>

    <tr>
    <td>config_mode<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>exclusive</td>
    <td><ul><li>exclusive</li><li>private</li></ul></td>
    <td>
        <div>The mode used to access the candidate configuration database.</div>
        </br><div style="font-size: small;">aliases: config_access, edit_mode, edit_access</div>
    </td>
    </tr>

    <tr>
    <td>confirmed<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Provide a confirmed timeout, in minutes, to be used with the commit operation.</div>
        <div>This option is only valid if the <em>commit</em> option is <code>true</code>.</div>
        <div>The value of this option is the number of minutes to wait for another commit operation before automatically rolling back the configuration change performed by this task. In other words, this option causes the module to perform a <code>commit confirmed </code><em>min</em> where <em>min</em> is the value of the <em>confirmed</em> option. This option DOES NOT confirm a previous <code>commit confirmed </code><em>min</em> operation. To confirm a previous commit operation, invoke this module with the <em>check</em> or <em>commit</em> option set to <code>true</code>.</div>
        </br><div style="font-size: small;">aliases: confirm</div>
    </td>
    </tr>

    <tr>
    <td>dest<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The path to a file, on the local Ansible control machine, where the configuration will be saved if the <em>retrieve</em> option is specified.</div>
        <div>The file must be writeable. If the file already exists, it is overwritten.</div>
        <div>This option is only valid if the <em>retrieve</em> option is not <code>none</code>.</div>
        <div>When tasks are executed against more than one target host, one process is forked for each target host. (Up to the maximum specified by the forks configuration. See <a href='http://docs.ansible.com/ansible/latest/intro_configuration.html#forks'>forks</a> for details.) This means that the value of this option must be unique per target host. This is usually accomplished by including <code>{{ inventory_hostname }}</code> in the <em>dest</em> value. It is the user&#x27;s responsibility to ensure this value is unique per target host.</div>
        <div>For this reason, this option is deprecated. It is maintained for backwards compatibility. Use the <em>dest_dir</em> option in new playbooks. The <em>dest</em> and <em>dest_dir</em> options are mutually exclusive.</div>
        </br><div style="font-size: small;">aliases: destination</div>
    </td>
    </tr>

    <tr>
    <td>dest_dir<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The path to a directory, on the Ansible control machine. This is the directory where the configuration will be saved if the <em>retrieve</em> option is specified. It is also the directory where the configuration diff will be specified if the <em>diff</em> option is <code>true</code>.</div>
        <div>This option is only valid if the <em>retrieve</em> option is not <code>none</code> or the <em>diff</em> option is <code>true</code>.</div>
        <div>The retrieved configuration will be saved to a file named <code>{{ inventory_hostname }}.</code><em>format_extension</em> in the <em>dest_dir</em> directory. Where <em>format_extension</em> is <code>conf</code> for text format, <code>xml</code> for XML format, <code>json</code> for JSON format, and <code>set</code> for set format.</div>
        <div>If the <em>diff</em> option is <code>true</code>, the configuration diff will be saved to a file named <code>{{ inventory_hostname }}.diff</code> in the <em>dest_dir</em> directory.</div>
        <div>The destination file must be writeable. If the file already exists, it is overwritten. It is the users responsibility to ensure a unique <em>dest_dir</em> value is provided for each execution of this module within a playbook.</div>
        <div>The <em>dest_dir</em> and <em>dest</em> options are mutually exclusive. The <em>dest_dir</em> option is recommended for all new playbooks.</div>
        <div>The <em>dest_dir</em> and <em>diff_file</em> options are mutually exclusive. The <em>dest_dir</em> option is recommended for all new playbooks.</div>
        </br><div style="font-size: small;">aliases: destination_dir, destdir, savedir, save_dir</div>
    </td>
    </tr>

    <tr>
    <td>diff<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>true (false if retrieve is set and load and rollback are not set)</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Perform a configuration compare (aka diff) operation.</div>
        </br><div style="font-size: small;">aliases: compare, diffs</div>
    </td>
    </tr>

    <tr>
    <td>diffs_file<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>None</td>
    <td></td>
    <td>
        <div>The path to a file, on the Ansible control machine, where the configuration differences will be saved if the <em>diff</em> option is specified.</div>
        <div>The file must be writeable. If the file already exists, it is overwritten.</div>
        <div>This option is only valid if the <em>diff</em> option is <code>true</code>.</div>
        <div>When tasks are executed against more than one target host, one process is forked for each target host. (Up to the maximum specified by the forks configuration. See <a href='http://docs.ansible.com/ansible/latest/intro_configuration.html#forks'>forks</a> for details.) This means that the value of this option must be unique per target host. This is usually accomplished by including <code>{{ inventory_hostname }}</code> in the <em>diffs_file</em> value. It is the user&#x27;s responsibility to ensure this value is unique per target host.</div>
        <div>For this reason, this option is deprecated. It is maintained for backwards compatibility. Use the <em>dest_dir</em> option in new playbooks.</div>
        <div>The <em>diffs_file</em> and <em>dest_dir</em> options are mutually exclusive.</div>
    </td>
    </tr>

    <tr>
    <td>filter<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>A string of XML, or &#x27;/&#x27;-separated configuration hierarchies, which specifies a filter used to restrict the portions of the configuration which are retrieved. See <a href='http://junos-pyez.readthedocs.io/en/stable/jnpr.junos.html#jnpr.junos.rpcmeta._RpcMetaExec.get_config'>PyEZ&#x27;s get_config method documentation</a> for details on the value of this option.</div>
        </br><div style="font-size: small;">aliases: filter_xml</div>
    </td>
    </tr>

    <tr>
    <td>format<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none (auto-detect on load, text on retrieve)</td>
    <td><ul><li>xml</li><li>set</li><li>text</li><li>json</li></ul></td>
    <td>
        <div>Specifies the format of the configuration retrieved, if <em>retrieve</em> is not <code>none</code>.</div>
        <div>Specifies the format of the configuration to be loaded, if <em>load</em> is not <code>none</code>.</div>
        <div>The specified format must be supported by the target Junos device.</div>
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
    <td>lines<br/><div style="font-size: small;"></div></td>
    <td>list</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Used with the <em>load</em> option. Specifies a list of list of configuration strings containing the configuration to be loaded.</div>
        <div>The <em>src</em>, <em>lines</em>, <em>template</em>, and <em>url</em> options are mutually exclusive.</div>
        <div>By default, the format of the configuration data is auto-dectected by the content of the first line in the <em>lines</em> list.</div>
        <div>If the <em>format</em> option is specified, the <em>format</em> value overrides the format auto-detection.</div>
    </td>
    </tr>

    <tr>
    <td>load<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td><ul><li>none</li><li>set</li><li>merge</li><li>update</li><li>replace</li><li>override</li><li>overwrite</li></ul></td>
    <td>
        <div>Specifies the type of load operation to be performed.</div>
        <div>The <em>load</em> and <em>rollback</em> options are mutually exclusive.</div>
        <div>The choices have the following meanings:
    </div>
        <div><b>none</b> - Do not perform a load operation.</div>
        <div><b>merge</b> - Combine the new configuration with the existing configuration. If statements in the new configuration conflict with statements in the existing configuration, the statements in the new configuration replace those in the existing configuration.</div>
        <div><b>replace</b> - This option is a superset of the <b>merge</b> option. It combines the new configuration with the existing configuration. If the new configuration is in text format and a hierarchy level in the new configuartion is prefixed with the string <code>replace:</code>, then the hierarchy level in the new configuration replaces the entire corresponding hierarchy level in the existing configuration, regardles of the existence or content of that hierarchy level in the existing configuration. If the configuration is in XML format, the XML attribute <code>replace = &quot;replace&quot;</code> is equivalent to the text format&#x27;s <code>replace:</code> prefix. If a configuration hierarchy in the new configuration is not prefixed with <code>replace:</code>, then the <b>merge</b> behavior is used. Specifically, for any statements in the new configuration which conflict with statements in the existing configuration, the statements in the new configuration replace those in the existing configuration.</div>
        <div><b>override</b> - Discard the entire existing configuration and replace it with the new configuration. When the configuration is later committed, all system processes are notified and the entire new configuration is marked as &#x27;changed&#x27; even if some statements previously existed in the configuration. The value <b>overwrite</b> is a synonym for <b>override</b>.</div>
        <div><b>update</b> - This option is similar to the <b>override</b> option. The new configuration completely replaces the existing configuration. The difference comes when the configuration is later committed. This option performs a &#x27;diff&#x27; between the new candidate configuration and the existing committed configuration. It then only notifies system processes repsonsible for the changed portions of the configuration, and only marks the actual configuration changes as &#x27;changed&#x27;.</div>
        <div><b>set</b> - This option is used when the new configuration data is in set format (a series of configuration mode commands). The new configuration data is loaded line by line and may contain any configuration mode commands, such as set, delete, edit, or deactivate. This value must be specified if the new configuration is in set format.</div>
    </td>
    </tr>

    <tr>
    <td>options<br/><div style="font-size: small;"></div></td>
    <td>dict</td>
    <td>no</td>
    <td>None</td>
    <td></td>
    <td>
        <div>Additional options, specified as a dictionary of key/value pairs, used when retrieving the configuration. See the <a href='https://www.juniper.net/documentation/en_US/junos/topics/reference/tag-summary/junos-xml-protocol-get-configuration.html'>&lt;get-configuration&gt; RPC documentation</a> for information on available options.</div>
    </td>
    </tr>

    <tr>
    <td>retrieve<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td><ul><li>none</li><li>candidate</li><li>committed</li></ul></td>
    <td>
        <div>The configuration database to be retrieved.</div>
    </td>
    </tr>

    <tr>
    <td>return_output<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Indicates if the output of the <em>diff</em> and <em>retreive</em> options should be returned in the module&#x27;s response. You might want to set this option to <code>false</code>, and set the <em>dest_dir</em> option, if the configuration or diff output is very large and you only need to save the output rather than using it&#x27;s content in subsequent tasks/plays of your playbook.</div>
    </td>
    </tr>

    <tr>
    <td>rollback<br/><div style="font-size: small;"></div></td>
    <td>int or str</td>
    <td>no</td>
    <td>none</td>
    <td><ul><li>0-49</li><li>rescue</li></ul></td>
    <td>
        <div>Populate the candidate configuration from a previously committed configuration. This value can be a configuration number between 0 and 49, or the keyword <code>rescue</code> to load the previously saved rescue configuration.</div>
        <div>By default, some Junos platforms store fewer than 50 previous configurations. Specifying a value greater than the number of previous configurations available, or specifying <code>rescue</code> when no rescue configuration has been saved, will result in an error when the module attempts to perform the rollback.</div>
        <div>The <em>rollback</em> and <em>load</em> options are mutually exclusive.</div>
    </td>
    </tr>

    <tr>
    <td>src<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>Used with the <em>load</em> option. Specifies the path to a file, on the local Ansible control machine, containing the configuration to be loaded.</div>
        <div>The <em>src</em>, <em>lines</em>, <em>template</em>, and <em>url</em> options are mutually exclusive.</div>
        <div>By default, the format of the configuration data is determined by the file extension of this path name. If the file has a <code>.conf</code> extension, the content is treated as text format. If the file has a <code>.xml</code> extension, the content is treated as XML format. If the file has a <code>.set</code> extension, the content is treated as Junos <b>set</b> commands.</div>
        <div>If the <em>format</em> option is specified, the <em>format</em> value overrides the file-extension based format detection.</div>
        </br><div style="font-size: small;">aliases: source, file</div>
    </td>
    </tr>

    <tr>
    <td>template<br/><div style="font-size: small;"></div></td>
    <td>path</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>The path to a Jinja2 template file, on the local Ansible control machine. This template file, along with the <em>vars</em> option, is used to generate the configuration to be loaded on the target Junos device.</div>
        <div>The <em>src</em>, <em>lines</em>, <em>template</em>, and <em>url</em> options are mutually exclusive.</div>
        <div>The <em>template</em> and <em>vars</em> options are required together. If one is specified, the other must be specified.</div>
        </br><div style="font-size: small;">aliases: template_path</div>
    </td>
    </tr>

    <tr>
    <td>url<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>A URL which specifies the configuration data to load on the target Junos device.</div>
        <div>The Junos device uses this URL to load the configuration, therefore this URL must be reachable by the target Junos device.</div>
        <div>The possible formats of this value are documented in the &#x27;url&#x27; section of the <a href='https://www.juniper.net/documentation/en_US/junos/topics/reference/tag-summary/junos-xml-protocol-load-configuration.html'>&lt;load-configuration&gt; RPC documentation</a>.</div>
        <div>The <em>src</em>, <em>lines</em>, <em>template</em>, and <em>url</em> options are mutually exclusive.</div>
    </td>
    </tr>

    <tr>
    <td>vars<br/><div style="font-size: small;"></div></td>
    <td>dict</td>
    <td>no</td>
    <td>none</td>
    <td></td>
    <td>
        <div>A dictionary of keys and values used to render the Jinja2 template specified by the <em>template</em> option.</div>
        <div>The <em>template</em> and <em>vars</em> options are required together. If one is specified, the other must be specified.</div>
        </br><div style="font-size: small;">aliases: template_vars</div>
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

.. _config-examples-label:

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
        - name: Retrieve the committed configuration
          config:
            retrieve: 'committed'
            diff: false
            check: false
            commit: false
          register: response

        - name: Print the lines in the config.
          debug:
            var: response.config_lines

        - name: Append .foo to the hostname using private config mode.
          config:
            config_mode: 'private'
            load: 'merge'
            lines:
              - "set system host-name {{ inventory_hostname }}.foo"
          register: response

        - name: Print the config changes.
          debug:
            var: response.diff_lines

        - name: Rollback to the previous config.
          config:
            config_mode: 'private'
            rollback: 1
          register: response

        - name: Print the config changes.
          debug:
            var: response.diff_lines

        - name: Rollback to the rescue config.
          config:
            rollback: 'rescue'
          register: response
        - name: Print the complete response.
          debug:
            var: response

        - name: Load override from a file.
          config:
            load: 'override'
            src: "{{ inventory_hostname }}.conf"
          register: response

        - name: Print the complete response.
          debug:
            var: response

        - name: Load from a Jinja2 template.
          config:
            load: 'merge'
            format: 'xml'
            template: "{{ inventory_hostname }}.j2"
            vars:
              host: "{{ inventory_hostname }}"
          register: response
        - name: Print the complete response.
          debug:
            var: response

        - name: Load from a file on the Junos device.
          config:
            load: 'merge'
            url: "{{ inventory_hostname }}.conf"
          register: response
        - name: Print the complete response.
          debug:
            var: response

        - name: Load from a file on the Junos device, skip the commit check
          config:
            load: 'merge'
            url: "{{ inventory_hostname }}.conf"
            check: false
          register: response
        - name: Print the msg.
          debug:
            var: response.msg

        - name: Print diff between current and rollback 10. No check. No commit.
          config:
            rollback: 11
            diff: true
            check: false
            commit: false
          register: response

        - name: Print the msg.
          debug:
            var: response

        - name: Retrieve [edit system services] of current committed config.
          config:
            retrieve: 'committed'
            filter: 'system/services'
            diff: true
            check: false
            commit: false
          register: response

        - name: Print the resulting config lines.
          debug:
            var: response.config_lines

        - name: Enable NETCONF SSH and traceoptions, save config, and diffs.
          config:
            load: 'merge'
            lines:
              - 'set system services netconf ssh'
              - 'set system services netconf traceoptions flag all'
              - 'set system services netconf traceoptions file netconf.log'
            format: 'set'
            retrieve: 'candidate'
            filter: 'system/services'
            comment: 'Enable NETCONF with traceoptions'
            dest_dir: './output'
          register: response

        - name: Print the complete response
          debug:
            var: response

        - name: Load conf. Confirm within 5 min. Wait 3 secs between chk and commit
          config:
            load: 'merge'
            url: "{{ inventory_hostname }}.conf"
            confirm: 5
            check_commit_wait: 3
          register: response

        - name: Print the complete response
          debug:
            var: response

        - name: Confirm the previous commit with a commit check (but no commit)
          config:
            check: true
            diff: false
            commit: false
          register: response

        - name: Print the complete response
          debug:
            var: response

        - name: fetch config from the device with filter and login credentials
          config:
            host: "10.x.x.x"
            user: "user"
            passwd: "user123"
            port: "22"
            retrieve: 'committed'
            format: xml
            commit: no
            check: no
            diff: no
            dest_dir: "/tmp/"
            filter: <configuration><groups><name>re0</name></groups></configuration>
            return_output: True
          register: config_output



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
        <div>Indicates if the device&#x27;s configuration has changed, or would have changed when in check mode.</div>
    </td>
    <td align=center>success</td>
    <td align=center>bool</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>config</td>
    <td>
        <div>The retrieved configuration. The value is a single multi-line string in the format specified by the <em>format</em> option.</div>
    </td>
    <td align=center>when <em>retrieved</em> is not <code>none</code> and <em>return_output</em> is <code>true</code>.</td>
    <td align=center>str</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>config_lines</td>
    <td>
        <div>The retrieved configuration. The value is a list of single-line strings in the format specified by the <em>format</em> option.</div>
    </td>
    <td align=center>when <em>retrieved</em> is not <code>none</code> and <em>return_output</em> is <code>true</code>.</td>
    <td align=center>list</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>config_parsed</td>
    <td>
        <div>The retrieved configuration parsed into a JSON datastructure. For XML replies, the response is parsed into JSON using the jxmlease library. For JSON the response is parsed using the Python json library.</div>
        <div>When Ansible converts the jxmlease or native Python data structure into JSON, it does not guarantee that the order of dictionary/object keys are maintained.</div>
    </td>
    <td align=center>when <em>retrieved</em> is not <code>none</code>, the <em>format</em> option is <code>xml</code> or <code>json</code> and <em>return_output</em> is <code>true</code>.</td>
    <td align=center>dict</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>diff</td>
    <td>
        <div>The configuration differences between the previous and new configurations. The value is a dict that contains a single key named &quot;prepared&quot;. Value associated with that key is a single multi-line string in &quot;diff&quot; format.</div>
    </td>
    <td align=center>when <em>load</em>  or <em>rollback</em> is specified, <em>diff</em> is <code>true</code>, and <em>return_output</em> is <code>true</code>.</td>
    <td align=center>dict</td>
    <td align=center></td>
    </tr>

    <tr>
    <td>diff_lines</td>
    <td>
        <div>The configuration differences between the previous and new configurations. The value is a list of single-line strings in &quot;diff&quot; format.</div>
    </td>
    <td align=center>when <em>load</em>  or <em>rollback</em> is specified, <em>diff</em> is <code>true</code>, and <em>return_output</em> is <code>true</code>.</td>
    <td align=center>list</td>
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
    <td>file</td>
    <td>
        <div>The value of the <em>src</em> option.</div>
    </td>
    <td align=center>when <em>load</em> is not <code>none</code> and <em>src</em> is not <code>none</code></td>
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


