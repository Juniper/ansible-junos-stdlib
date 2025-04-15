.. _junipernetworks.junos.junos_routing_options_module:


*******************************************
junipernetworks.junos.junos_routing_options
*******************************************

**Manage routing-options configuration on Junos devices.**


Version added: 2.8.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages routing-options configuration on devices running Junos.



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
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
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
                        <div>A dictionary of routing-options configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>autonomous_system</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Autonomous system number.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Autonomous system number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>asdot_notation</b>
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
                        <div>Enable AS-Dot notation to display true 4 byte AS numbers.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>loops</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify maximum number of times this AS can be in an AS path.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Router identifier.</div>
                </td>
            </tr>

            <tr>
                <td colspan="3">
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show system routing-options</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
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
                        <div>Refer to examples for more details.</div>
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
    # vagrant@vsrx# show system routing-options
    #
    - name: Merge provided NTP configuration into running configuration.
      junipernetworks.junos.junos_routing_options:
        config:
          autonomous_system:
            as_number: 2
            asdot_notation: true
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true
    #         }
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #           "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #           "<nc:autonomous-system>2<nc:asdot-notation/></nc:autonomous-system></nc:routing-options>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show routing-options
    # autonomous-system 2 asdot-notation;
    #
    #
    # Using Replaced
    # Before state
    # ------------
    #
    # vagrant@vsrx# show routing-options
    # autonomous-system 2 asdot-notation;

    - name: Replaced running routing-options configuration with provided configuration
      junipernetworks.junos.junos_routing_options:
        config:
          autonomous_system:
            as_number: 2
            asdot_notation: true
          router_id: "1.1.1.1"
        state: replaced
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true
    #         },
    #         "router_id": "1.1.1.1"
    #     },
    #     "before": {
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #             "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #             "<nc:autonomous-system delete="delete"/><nc:autonomous-system>2<nc:asdot-notation/>"
    #             "</nc:autonomous-system><nc:router-id>1.1.1.1</nc:router-id></nc:routing-options>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show routing-options
    # router-id 1.1.1.1;
    # autonomous-system 2 asdot-notation;


    # Using overridden
    #
    # vagrant@vsrx# show routing-options
    # autonomous-system 2 asdot-notation;

    - name: Override running routing-options configuration with provided configuration
      junipernetworks.junos.junos_routing_options:
        config:
          autonomous_system:
            as_number: 2
            asdot_notation: true
          router_id: "1.1.1.1"
        state: overridden
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true
    #         },
    #         "router_id": "1.1.1.1"
    #     },
    #     "before": {
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #             "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #             "<nc:autonomous-system delete="delete"/><nc:autonomous-system>2<nc:asdot-notation/>"
    #             "</nc:autonomous-system><nc:router-id>1.1.1.1</nc:router-id></nc:routing-options>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show routing-options
    # router-id 1.1.1.1;
    # autonomous-system 2 asdot-notation;
    #
    # Using deleted
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show routing-options
    # router-id 1.1.1.1;
    # autonomous-system 2 asdot-notation;
    #
    - name: Delete running routing-options configuration
      junipernetworks.junos.junos_routing_options:
        config:
        state: deleted
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {},
    #     "before": {
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true
    #         },
    #         "router_id": "1.1.1.1"
    #     },
    #     "changed": true,
    #     "commands": [
    #               "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #               "<nc:autonomous-system delete="delete"/><nc:router-id delete="delete"/></nc:routing-options>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show routing-options
    #
    # [edit]
    # Using gathered
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show routing-options
    # router-id 1.1.1.1;
    # autonomous-system 2 asdot-notation;

    - name: Gather running routing-options configuration
      junipernetworks.junos.junos_routing_options:
        state: gathered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "gathered": {
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true
    #         },
    #         "router_id": "1.1.1.1"
    #     },
    #     "changed": false,
    # Using rendered
    #
    # Before state
    # ------------
    #
    - name: Render xml for provided facts.
      junipernetworks.junos.junos_routing_options:
        config:
          autonomous_system:
            as_number: 2
            asdot_notation: true
            loops: 4
          router_id: 12.12.12.12
        state: rendered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "rendered": [
    #           "<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #           "<nc:autonomous-system>2<nc:loops>4</nc:loops><nc:asdot-notation/></nc:autonomous-system>
    #           "<nc:router-id>12.12.12.12</nc:router-id></nc:routing-options>"
    #     ]
    #
    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <routing-options>
    #             <router-id>12.12.12.12</router-id>
    #             <autonomous-system>
    #                 <as-number>2</as-number>
    #                 <loops>4</loops>
    #                 <asdot-notation/>
    #             </autonomous-system>
    #         </routing-options>
    #     </configuration>
    # </rpc-reply>
    #
    - name: Parse routing-options running config
      junipernetworks.junos.junos_routing_options:
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
    #         "autonomous_system": {
    #             "as_number": "2",
    #             "asdot_notation": true,
    #             "loops": 4
    #         },
    #         "router_id": "12.12.12.12"
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:autonomous-system delete=&quot;delete&quot;/&gt;&lt;nc:router-id delete=&quot;delete&quot;/&gt;&lt;/nc:routing-options&gt;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
