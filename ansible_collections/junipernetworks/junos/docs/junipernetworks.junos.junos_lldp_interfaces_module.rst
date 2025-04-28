.. _junipernetworks.junos.junos_lldp_interfaces_module:


*******************************************
junipernetworks.junos.junos_lldp_interfaces
*******************************************

**LLDP interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages link layer discovery protocol (LLDP) attributes of interfaces on Juniper JUNOS devices.




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
                        <div>The list of link layer discovery protocol interface attribute configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>This is a boolean value to control disabling of LLDP on the interface <code>name</code></div>
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
                        <div>Name of the interface LLDP needs to be configured on.</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show protocols lldp</b>.</div>
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
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using merged
    # Before state:
    # -------------
    # user@junos01# # show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;

    - name: Merge provided configuration with device configuration
      junipernetworks.junos.junos_lldp_interfaces:
        config:
          - name: ge-0/0/1
          - name: ge-0/0/2
            enabled: false
        state: merged

    # After state:
    # -------------
    # user@junos01# show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;
    # interface ge-0/0/1;
    # interface ge-0/0/2 {
    #     disable;
    # }

    # Using replaced
    # Before state:
    # -------------
    # user@junos01# show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;
    # interface ge-0/0/1;
    # interface ge-0/0/2 {
    #     disable;
    # }

    - name: Replace provided configuration with device configuration
      junipernetworks.junos.junos_lldp_interfaces:
        config:
          - name: ge-0/0/2
            disable: false
          - name: ge-0/0/3
            enabled: false
        state: replaced

    # After state:
    # -------------
    # user@junos01# show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;
    # interface ge-0/0/1;
    # interface ge-0/0/2;
    # interface ge-0/0/3 {
    #     disable;
    # }

    # Using overridden
    # Before state:
    # -------------
    # user@junos01# show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;
    # interface ge-0/0/1;
    # interface ge-0/0/2 {
    #     disable;
    # }

    - name: Override provided configuration with device configuration
      junipernetworks.junos.junos_lldp_interfaces:
        config:
          - name: ge-0/0/2
            enabled: false
        state: overridden

    # After state:
    # -------------
    # user@junos01# show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;
    # interface ge-0/0/2 {
    #     disable;
    # }

    # Using deleted
    # Before state:
    # -------------
    # user@junos01# show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;
    # interface ge-0/0/1;
    # interface ge-0/0/2;
    # interface ge-0/0/3 {
    #     disable;
    # }
    - name: Delete lldp interface configuration (this will not delete other lldp configuration)
      junipernetworks.junos.junos_lldp_interfaces:
        config:
          - name: ge-0/0/1
          - name: ge-0/0/3
        state: deleted

    # After state:
    # -------------
    # user@junos01# show protocols lldp
    # management-address 10.1.1.1;
    # advertisement-interval 10000;
    # interface ge-0/0/2;
    # interface ge-0/0/1;
    # Using gathered
    # Before state:
    # ------------
    #
    # ansible@cm123456tr21# show protocols lldp
    # interface ge-0/0/1;
    # interface ge-0/0/2 {
    #     disable;
    # }
    - name: Gather junos lldp interfaces as in given arguments
      junipernetworks.junos.junos_lldp_interfaces:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": [
    #         {
    #             "name": "ge-0/0/1"
    #         },
    #         {
    #             "enabled": false,
    #             "name": "ge-0/0/2"
    #         }
    #     ]
    # After state:
    # ------------
    #
    # ansible@cm123456tr21# show protocols lldp
    # interface ge-0/0/1;
    # interface ge-0/0/2 {
    #     disable;
    # }
    # Using rendered
    - name: Render platform specific xml from task input using rendered state
      junipernetworks.junos.junos_lldp_interfaces:
        config:
          - name: ge-0/0/1
          - name: ge-0/0/2
            enabled: false
        state: rendered
    # Task Output (redacted)
    # -----------------------
    # "rendered": "<nc:protocols
    #     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #     <nc:lldp>
    #         <nc:interface>
    #             <nc:name>ge-0/0/1</nc:name>
    #             <nc:disable delete="delete"/>
    #         </nc:interface>
    #         <nc:interface>
    #             <nc:name>ge-0/0/2</nc:name>
    #             <nc:disable/>
    #         </nc:interface>
    #     </nc:lldp>
    # </nc:protocols>"
    # Using parsed
    # parsed.cfg
    # ------------
    #
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <protocols>
    #             <ospf>
    #                 <area>
    #                     <name>0.0.0.0</name>
    #                     <interface>
    #                         <name>ge-0/0/0.0</name>
    #                     </interface>
    #                 </area>
    #             </ospf>
    #             <lldp>
    #                 <interface>
    #                     <name>ge-0/0/1</name>
    #                 </interface>
    #                 <interface>
    #                     <name>ge-0/0/2</name>
    #                     <disable/>
    #                 </interface>
    #             </lldp>
    #         </protocols>
    #     </configuration>
    # </rpc-reply>
    # - name: Convert lldp interfaces config to argspec without connecting to the appliance
    #   junipernetworks.junos.junos_lldp_interfaces:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": [
    #         {
    #             "name": "ge-0/0/1"
    #         },
    #         {
    #             "enabled": false,
    #             "name": "ge-0/0/2"
    #         }
    #     ]



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:protocols xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:lldp&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/1&lt;/nc:name&gt; &lt;nc:disable delete=&quot;delete&quot;/&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/2&lt;/nc:name&gt; &lt;nc:disable/&gt; &lt;/nc:interface&gt; &lt;/nc:lldp&gt; &lt;/nc:protocols&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
