.. _junipernetworks.junos.junos_netconf_module:


***********************************
junipernetworks.junos.junos_netconf
***********************************

**Configures the Junos Netconf system service**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides an abstraction that enables and configures the netconf system service running on Junos devices.  This module can be used to easily enable the Netconf API. Netconf provides a programmatic interface for working with configuration and state resources as defined in RFC 6242. If the ``netconf_port`` is not mentioned in the task by default netconf will be enabled on port 830 only.




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
                    <b>netconf_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">830</div>
                </td>
                <td>
                        <div>This argument specifies the port the netconf service should listen on for SSH connections.  The default port as defined in RFC 6242 is 830.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: listens_on</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the state of the <code>junos_netconf</code> resource on the remote device.  If the <em>state</em> argument is set to <em>present</em> the netconf service will be configured.  If the <em>state</em> argument is set to <em>absent</em> the netconf service will be removed from the configuration.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
   - Recommended connection is ``network_cli``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.
   - This module also works with ``local`` connections for legacy playbooks.
   - If ``netconf_port`` value is not mentioned in task by default it will be enabled on port 830 only. Although ``netconf_port`` value can be from 1 through 65535, avoid configuring access on a port that is normally assigned for another service. This practice avoids potential resource conflicts.
   - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
   - For more information on using Ansible to manage Juniper network devices see https://www.ansible.com/ansible-juniper.



Examples
--------

.. code-block:: yaml

    - name: enable netconf service on port 830
      junipernetworks.junos.junos_netconf:
        listens_on: 830
        state: present

    - name: disable netconf service
      junipernetworks.junos.junos_netconf:
        state: absent



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when changed is True</td>
                <td>
                            <div>Returns the command sent to the remote device</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">set system services netconf ssh port 830</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Peter Sprygada (@privateip)
