.. _junipernetworks.junos.junos_hostname_module:


************************************
junipernetworks.junos.junos_hostname
************************************

**Manage Hostname server configuration on Junos devices.**


Version added: 2.9.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages hostname configuration on devices running Junos.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)


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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of system Hostname configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify the hostname.</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show system hostname</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
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
                                    <li>deleted</li>
                                    <li>overridden</li>
                                    <li>parsed</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required.</div>
                        <div>The states <em>merged</em>, <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
                        <div>The state <em>gathered</em> will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into JSON format as per the resource module parameters and the value is returned in the <em>parsed</em> key within the result. The value of <code>running_config</code> option should be the same format as the output of command <em>show system hostname</em> executed on device. For state <em>parsed</em> active connection to remote host is not required.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module requires the netconf system service be enabled on the device being managed.
   - This module works with connection ``netconf``.
   - See `the Junos OS Platform Options <https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html>`_.
   - Tested against JunOS v18.4R1



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system hostname
    #
    # [edit]
    - name: Merge provided HOSTNAME configuration into running configuration.
      junipernetworks.junos.junos_hostname:
        config:
          hostname: 'vsrx-18.4R1'
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "hostname": "vsrx-18.4R1"
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #           "<nc:host-name>vsrx-18.4R1</nc:host-name></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx-18.4R1# show system host-name
    # host-name vsrx-18.4R1;
    #
    # Using replaced
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx-18.4R1# show system host-name
    # host-name vsrx-18.4R1;
    #
    # [edit]
    - name: Replaced target config with provided config.
      junipernetworks.junos.junos_hostname:
        config:
          hostname: 'vsrx-12'
        state: replaced
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "hostname": "vsrx-12"
    #     },
    #     "before": {
    #         "hostname": "vsrx-18.4R1"
    #     },
    #     "changed": true,
    #     "commands": [
    #           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #           "<nc:host-name>vsrx-12</nc:host-name></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx-18.4R1# show system host-name
    # host-name vsrx-12;
    #
    # Using overridden
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx-18.4R1# show system host-name
    # host-name vsrx-18.4R1;
    #
    # [edit]
    - name: Replaced target config with provided config.
      junipernetworks.junos.junos_hostname:
        config:
          hostname: 'vsrx-12'
        state: overridden
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "hostname": "vsrx-12"
    #     },
    #     "before": {
    #         "hostname": "vsrx-18.4R1"
    #     },
    #     "changed": true,
    #     "commands": [
    #           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #           "<nc:host-name>vsrx-12</nc:host-name></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx-18.4R1# show system host-name
    # host-name vsrx-12;
    #
    # Using deleted
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx-18.4R1# show system host-name
    # host-name vsrx-12;
    #
    - name: Delete running HOSTNAME global configuration
      junipernetworks.junos.junos_hostname:
        config:
        state: deleted
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {},
    #     "before": {
    #         "hostname": "vsrx-12"
    #     },
    #     "changed": true,
    #     "commands": [
    #               "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #                <nc:host-name delete="delete"/></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system ntp
    #
    # [edit]
    # Using gathered
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx-18.4R1# show system host-name
    # host-name vsrx-12;
    #
    - name: Gather running HOSTNAME global configuration
      junipernetworks.junos.junos_hostname:
        state: gathered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "gathered": {
    #         "hostname": "vsrx-12",
    #     },
    #     "changed": false,
    # Using rendered
    #
    # Before state
    # ------------
    #
    - name: Render xml for provided facts.
      junipernetworks.junos.junos_hostname:
        config:
          boot_server: '78.46.194.186'
        state: rendered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "rendered": [
    #           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #           "<nc:host-name>78.46.194.186</nc:host-name></nc:system>"
    #     ]
    #
    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <system xmlns="http://yang.juniper.net/junos-es/conf/system">
    #            <host-name>vsrx-18.4R1</host-name>
    #         </system>
    #     </configuration>
    # </rpc-reply>
    #
    - name: Parse HOSTNAME running config
      junipernetworks.junos.junos_hostname:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "parsed":  {
    #         "hostname": "vsrx-18.4R1"
    #     }
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration model invocation.</div>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the model invocation.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&quot;&lt;nc:host-name&gt;78.46.194.186&lt;/nc:host-name&gt;&lt;/nc:system&gt;&quot;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
