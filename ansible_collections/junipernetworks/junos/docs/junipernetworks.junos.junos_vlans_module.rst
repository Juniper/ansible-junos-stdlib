.. _junipernetworks.junos.junos_vlans_module:


*********************************
junipernetworks.junos.junos_vlans
*********************************

**VLANs resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module creates and manages VLAN configurations on Junos OS.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of Vlan options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Text description of VLANs</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>l3_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of logical layer 3 interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of VLAN.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IEEE 802.1q VLAN identifier for VLAN (1..4094).</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>running_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option is used only with state <em>parsed</em>.</div>
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show vlans</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>parsed</li>
                                    <li>rendered</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module requires the netconf system service be enabled on the remote device being managed
   - Tested against Junos OS 18.4R1
   - This module works with connection ``netconf``.
   - See `the Junos OS Platform Options <https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html>`_.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show vlans
    #
    # [edit]

    - name: Merge provided Junos vlans config with running-config
      junipernetworks.junos.junos_vlans:
        config:
          - name: vlan1
            vlan_id: 1
          - name: vlan2
            vlan_id: 2
            l3_interface: irb.12
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": [
    #         {
    #             "name": "vlan1",
    #             "vlan_id": 1
    #         },
    #         {
    #             "l3_interface": "irb.12",
    #             "name": "vlan2",
    #             "vlan_id": 2
    #         }
    #     ],
    #     "before": [],
    #     "changed": true,
    #     "commands": [
    #         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #         "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>1</nc:vlan-id></nc:vlan>"
    #         "<nc:vlan><nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id><nc:l3-interface>irb.12</nc:l3-interface>"
    #         "</nc:vlan></nc:vlans>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show vlans
    # vlan1 {
    #     vlan-id 1;
    # }
    # vlan2 {
    #     vlan-id 2;
    #     l3-interface irb.12;
    # }

    # Using replaced
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show vlans
    # vlan1 {
    #     vlan-id 1;
    # }
    # vlan2 {
    #     vlan-id 2;
    #     l3-interface irb.12;
    # }

    - name: Replace Junos vlans running-config with the provided config
      junipernetworks.junos.junos_vlans:
        config:
          - name: vlan1
            vlan_id: 11
            l3_interface: irb.10

          - name: vlan2
            vlan_id: 2
        state: replaced
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": [
    #         {
    #             "l3_interface": "irb.10",
    #             "name": "vlan1",
    #             "vlan_id": 11
    #         },
    #         {
    #             "name": "vlan2",
    #             "vlan_id": 2
    #         }
    #     ],
    #     "before": [
    #         {
    #             "name": "vlan1",
    #             "vlan_id": 1
    #         },
    #         {
    #             "l3_interface": "irb.12",
    #             "name": "vlan2",
    #             "vlan_id": 2
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #         "<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan>"
    #         "<nc:vlan delete="delete"><nc:name>vlan2</nc:name></nc:vlan>"
    #         "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>11</nc:vlan-id>"
    #         "<nc:l3-interface>irb.10</nc:l3-interface></nc:vlan><nc:vlan>"
    #         "<nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id></nc:vlan></nc:vlans>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show vlans
    # vlan1 {
    #     vlan-id 11;
    #     l3-interface irb.10;
    # }
    # vlan2 {
    #     vlan-id 2;
    # }
    #
    # Using overridden
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show vlans
    # vlan1 {
    #     vlan-id 11;
    #     l3-interface irb.10;
    # }
    # vlan2 {
    #     vlan-id 2;
    # }
    - name: Override Junos running-config with provided config
      junipernetworks.junos.junos_vlans:
        config:
          - name: vlan3
            vlan_id: 3
            l3_interface: irb.13
        state: overridden
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": [
    #         {
    #             "l3_interface": "irb.13",
    #             "name": "vlan3",
    #             "vlan_id": 3
    #         }
    #     ],
    #     "before": [
    #         {
    #             "l3_interface": "irb.10",
    #             "name": "vlan1",
    #             "vlan_id": 11
    #         },
    #         {
    #             "name": "vlan2",
    #             "vlan_id": 2
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #         "<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan><nc:vlan delete="delete">"
    #         "<nc:name>vlan2</nc:name></nc:vlan><nc:vlan><nc:name>vlan3</nc:name><nc:vlan-id>3</nc:vlan-id>"
    #         "<nc:l3-interface>irb.13</nc:l3-interface></nc:vlan></nc:vlans>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show vlans
    # vlan3 {
    #     vlan-id 3;
    #     l3-interface irb.13;
    # }
    #
    # Using deleted
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show vlans
    # vlan3 {
    #     vlan-id 3;
    #     l3-interface irb.13;
    # }
    - name: Delete specific vlan
      junipernetworks.junos.junos_vlans:
        config:
          - name: vlan3
        state: deleted
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": [],
    #     "changed": true,
    #     "commands": [
    #         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #         "<nc:vlan delete="delete"><nc:name>vlan3</nc:name></nc:vlan></nc:vlans>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show vlans
    # vlan1 {
    #     vlan-id 11;
    #     l3-interface irb.10;
    # }
    # vlan2 {
    #     vlan-id 2;
    # }


    - name: Gather running vlans configuration
      junipernetworks.junos.junos_vlans:
        state: gathered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "gathered": [
    #         {
    #             "l3_interface": "irb.10",
    #             "name": "vlan1",
    #             "vlan_id": 11
    #         },
    #         {
    #             "name": "vlan2",
    #             "vlan_id": 2
    #         }
    #     ],
    #     "changed": false,
    #
    # Using rendered
    #
    # Before state
    # ------------
    #
    - name: Render xml for provided facts.
      junipernetworks.junos.junos_vlans:
        config:
          - name: vlan1
            vlan_id: 1

          - name: vlan2
            vlan_id: 2
            l3_interface: irb.12
        state: rendered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "rendered": [
    #         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #         "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>1</nc:vlan-id></nc:vlan>"
    #         "<nc:vlan><nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id><nc:l3-interface>irb.12</nc:l3-interface>"
    #         "</nc:vlan></nc:vlans>"
    #     ]
    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <vlans>
    #           <vlan>
    #             <name>vlan1</name>
    #             <vlan-id>1</vlan-id>
    #           </vlan>
    #           <vlan>
    #             <name>vlan2</name>
    #             <vlan-id>2</vlan-id>
    #             <l3-interface>irb.12</l3-interface>
    #           </vlan>
    #        </vlans>
    #     </configuration>
    # </rpc-reply>

    - name: Parse routing instance running config
      junipernetworks.junos.junos_vlans:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "parsed":  [
    #         {
    #             "name": "vlan1",
    #             "vlan_id": 1
    #         },
    #         {
    #             "l3_interface": "irb.12",
    #             "name": "vlan2",
    #             "vlan_id": 2
    #         }
    #     ]
    #



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
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The configuration as structured data after module completion.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration as structured data prior to module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:vlans xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:vlan&gt;&lt;nc:name&gt;vlan1&lt;/nc:name&gt;&lt;nc:vlan-id&gt;1&lt;/nc:vlan-id&gt; &lt;/nc:vlan&gt;&lt;nc:vlan&gt;&lt;nc:name&gt;vlan2&lt;/nc:name&gt;&lt;nc:vlan-id&gt;2&lt;/nc:vlan-id&gt; &lt;nc:l3-interface&gt;irb.12&lt;/nc:l3-interface&gt;&lt;/nc:vlan&gt;&lt;/nc:vlans&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Daniel Mellado (@dmellado)
