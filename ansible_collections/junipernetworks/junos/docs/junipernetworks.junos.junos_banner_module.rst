.. _junipernetworks.junos.junos_banner_module:


**********************************
junipernetworks.junos.junos_banner
**********************************

**Manage multiline banners on Juniper JUNOS devices**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This will configure both login and motd banners on network devices. It allows playbooks to add or remote banner text from the active running configuration.



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
                    <b>active</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Specifies whether or not the configuration is active or deactivated</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>banner</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>login</li>
                                    <li>motd</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies which banner that should be configured on the remote device. Value <code>login</code> indicates system login message prior to authenticating, <code>motd</code> is login announcement after successful authentication.</div>
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
                        <div>Specifies whether or not the configuration is present in the current devices active running configuration.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The banner text that should be present in the remote device running configuration.  This argument accepts a multiline string, with no empty lines. Requires <em>state=present</em>.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
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

    - name: configure the login banner
      junipernetworks.junos.junos_banner:
        banner: login
        text: |
          this is my login banner
          that contains a multiline
          string
        state: present

    - name: remove the motd banner
      junipernetworks.junos.junos_banner:
        banner: motd
        state: absent

    - name: deactivate the motd banner
      junipernetworks.junos.junos_banner:
        banner: motd
        state: present
        active: false

    - name: activate the motd banner
      junipernetworks.junos.junos_banner:
        banner: motd
        state: present
        active: true

    - name: Configure banner from file
      junipernetworks.junos.junos_banner:
        banner: motd
        text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
        state: present



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
                    <b>diff.prepared</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when configuration is changed and diff option is enabled.</td>
                <td>
                            <div>Configuration difference before and after applying change.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[edit system login] +   message &quot;this is my login banner&quot;;</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
