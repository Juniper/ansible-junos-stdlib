.. _junipernetworks.junos.junos_facts_module:


*********************************
junipernetworks.junos.junos_facts
*********************************

**Collect facts from remote devices running Juniper Junos**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Collects fact information from a remote device running the Junos operating system.  By default, the module will collect basic fact information from the device to be included with the hostvars. Additional fact information can be collected based on the configured set of arguments.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>available_network_resources</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>When &#x27;True&#x27; a list of network resources for which resource modules are available will be provided.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config_format</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>xml</li>
                                    <li><div style="color: blue"><b>text</b>&nbsp;&larr;</div></li>
                                    <li>set</li>
                                    <li>json</li>
                        </ul>
                </td>
                <td>
                        <div>The <em>config_format</em> argument specifies the format of the configuration when serializing output from the device. This argument is applicable only when <code>config</code> value is present in <em>gather_subset</em>. The <em>config_format</em> should be supported by the junos version running on device. This value is not applicable while fetching old style facts that is when <code>ofacts</code> value is present in value if <em>gather_subset</em> value. This option is valid only for <code>gather_subset</code> values.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gather_network_resources</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When supplied, this argument will restrict the facts collected to a given subset. Possible values for this argument include all and the resources like interfaces, vlans etc. Can specify a list of values to include a larger subset. Values can also be used with an initial <code>!</code> to specify that a specific subset should not be collected. Valid subsets are &#x27;all&#x27;, &#x27;interfaces&#x27;, &#x27;lacp&#x27;, &#x27;lacp_interfaces&#x27;, &#x27;lag_interfaces&#x27;, &#x27;l2_interfaces&#x27;, &#x27;l3_interfaces&#x27;, &#x27;lldp_global&#x27;, &#x27;lldp_interfaces&#x27;, &#x27;vlans&#x27;.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gather_subset</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">["min"]</div>
                </td>
                <td>
                        <div>When supplied, this argument will restrict the facts collected to a given subset.  Possible values for this argument include <code>all</code>, <code>hardware</code>, <code>config</code>, <code>interfaces</code> and <code>min</code>. Can specify a list of values to include a larger subset.  Values can also be used with an initial <code>!</code> to specify that a specific subset should not be collected. To maintain backward compatibility old style facts can be retrieved by explicitly adding <code>ofacts</code>  to value, this requires junos-eznc to be installed as a prerequisite. Valid value of gather_subset are default, hardware, config, interfaces, ofacts. If <code>ofacts</code> is present in the list it fetches the old style facts (fact keys without &#x27;ansible_&#x27; prefix) and it requires junos-eznc library to be installed.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Ensure *config_format* used to retrieve configuration from device is supported by junos version running on device.
   - With *config_format = json*, configuration in the results will be a dictionary(and not a JSON string)
   - This module requires the netconf system service be enabled on the remote device being managed.
   - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
   - Recommended connection is ``netconf``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.
   - This module also works with ``local`` connections for legacy playbooks.
   - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
   - For more information on using Ansible to manage Juniper network devices see https://www.ansible.com/ansible-juniper.



Examples
--------

.. code-block:: yaml

    - name: collect default set of facts
      junipernetworks.junos.junos_facts:

    - name: collect default set of facts and configuration
      junipernetworks.junos.junos_facts:
        gather_subset: config

    - name: Gather legacy and resource facts
      junipernetworks.junos.junos_facts:
        gather_subset: all
        gather_network_resources: all




Status
------


Authors
~~~~~~~

- Nathaniel Case (@Qalthos)
