.. _junipernetworks.junos.junos_lacp_interfaces_module:


*******************************************
junipernetworks.junos.junos_lacp_interfaces
*******************************************

**LACP interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces on Juniper JUNOS devices.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="4">
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
                        <div>The list of dictionaries of LACP interfaces options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>force_up</b>
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
                        <div>This is a boolean argument to control if the port should be up in absence of received link Aggregation Control Protocol Data Unit (LACPDUS). This value is applicable for member interfaces only.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name Identifier of the interface or link aggregation group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>period</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>fast</li>
                                    <li>slow</li>
                        </ul>
                </td>
                <td>
                        <div>Timer interval for periodic transmission of LACP packets. If the value is set to <code>fast</code> the packets are received every second and if the value is <code>slow</code> the packets are received every 30 seconds. This value is applicable for aggregate interface only.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Priority of the member port. This value is applicable for member interfaces only.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sync_reset</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>disable</li>
                                    <li>enable</li>
                        </ul>
                </td>
                <td>
                        <div>The argument notifies minimum-link failure out of sync to peer. If the value is <code>disable</code> it disables minimum-link failure handling at LACP level and if value is <code>enable</code> it enables minimum-link failure handling at LACP level. This value is applicable for aggregate interface only.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This dict object contains configurable options related to LACP system parameters for the link aggregation group. This value is applicable for aggregate interface only.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the system ID to use in LACP negotiations for the bundle, encoded as a MAC address.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The system ID to use in LACP negotiations.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the system priority to use in LACP negotiations for the bundle.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>


            <tr>
                <td colspan="4">
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show interface</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
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




Examples
--------

.. code-block:: yaml

    # Using merged
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #    ether-options {
    #         802.3ad ae0;
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: Merge provided configuration with device configuration
      junipernetworks.junos.junos_lacp_interfaces:
        config:
          - name: ae0
            period: fast
            sync_reset: enable
            system:
              priority: 100
              mac:
                address: 00:00:00:00:00:02
          - name: ge-0/0/3
            port_priority: 100
            force_up: true
        state: merged

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic fast;
    #             sync-reset enable;
    #             system-priority 100;
    #             system-id 00:00:00:00:00:02;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    # Using replaced
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic fast;
    #             sync-reset enable;
    #             system-priority 100;
    #             system-id 00:00:00:00:00:02;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: Replace device LACP interfaces configuration with provided configuration
      junipernetworks.junos.junos_lacp_interfaces:
        config:
          - name: ae0
            period: slow
        state: replaced

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic slow;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    # Using overridden
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic slow;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: Overrides all device LACP interfaces configuration with provided configuration
      junipernetworks.junos.junos_lacp_interfaces:
        config:
          - name: ae0
            system:
              priority: 300
              mac:
                address: 00:00:00:00:00:03
          - name: ge-0/0/2
            port_priority: 200
            force_up: false
        state: overridden

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 port-priority 200;
    #             }
    #             ae4;
    #         }
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             system-priority 300;
    #             system-id 00:00:00:00:00:03;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    # Using deleted
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 port-priority 200;
    #             }
    #             ae4;
    #         }
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             system-priority 300;
    #             system-id 00:00:00:00:00:03;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: "Delete LACP interfaces attributes of given interfaces (Note: This won't delete the interface itself)"
      junipernetworks.junos.junos_lacp_interfaces:
        config:
          - name: ae0
          - name: ge-0/0/3
          - name: ge-0/0/2
        state: deleted

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #    ether-options {
    #         802.3ad ae0;
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }
    # Using gathered
    # Before state:
    # ------------
    #
    # user@junos01# show interfaces
    # ansible@cm123456tr21# show interfaces
    # ge-0/0/1 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae1;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae1;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad ae2;
    #     }
    # }
    # ge-0/0/4 {
    #     ether-options {
    #         802.3ad ae2;
    #     }
    # }
    # ge-1/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.1/24;
    #             address 10.200.16.20/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-2/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.2/24;
    #             address 10.200.16.21/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-3/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.3/24;
    #             address 10.200.16.22/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ae1 {
    #     description "Configured by Ansible";
    #     aggregated-ether-options {
    #         lacp {
    #             periodic fast;
    #             sync-reset enable;
    #             system-priority 100;
    #             system-id 00:00:00:00:00:02;
    #         }
    #     }
    # }
    # ae2 {
    #     description "Configured by Ansible";
    # }
    # em1 {
    #     description TEST;
    # }
    # fxp0 {
    #     description ANSIBLE;
    #     speed 1g;
    #     link-mode automatic;
    #     unit 0 {
    #         family inet {
    #             address 10.8.38.38/24;
    #         }
    #     }
    # }
    - name: Gather junos lacp interfaces as in given arguments
      junipernetworks.junos.junos_lacp_interfaces:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": [
    #         {
    #             "force_up": true,
    #             "name": "ge-0/0/1",
    #             "port_priority": 100
    #         },
    #         {
    #             "name": "ae1",
    #             "period": "fast",
    #             "sync_reset": "enable",
    #             "system": {
    #                 "mac": {
    #                     "address": "00:00:00:00:00:02"
    #                 },
    #                 "priority": 100
    #             }
    #         }
    #     ]
    # After state:
    # ------------
    #
    # ansible@cm123456tr21# show interfaces
    # ge-0/0/1 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae1;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae1;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad ae2;
    #     }
    # }
    # ge-0/0/4 {
    #     ether-options {
    #         802.3ad ae2;
    #     }
    # }
    # ge-1/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.1/24;
    #             address 10.200.16.20/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-2/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.2/24;
    #             address 10.200.16.21/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-3/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.3/24;
    #             address 10.200.16.22/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ae1 {
    #     description "Configured by Ansible";
    #     aggregated-ether-options {
    #         lacp {
    #             periodic fast;
    #             sync-reset enable;
    #             system-priority 100;
    #             system-id 00:00:00:00:00:02;
    #         }
    #     }
    # }
    # ae2 {
    #     description "Configured by Ansible";
    # }
    # em1 {
    #     description TEST;
    # }
    # fxp0 {
    #     description ANSIBLE;
    #     speed 1g;
    #     link-mode automatic;
    #     unit 0 {
    #         family inet {
    #             address 10.8.38.38/24;
    #         }
    #     }
    # }
    # Using parsed
    # parsed.cfg
    # ------------
    #
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    # <interfaces>
    #         <interface>
    #             <name>ge-0/0/1</name>
    #             <ether-options>
    #                 <ieee-802.3ad>
    #                     <lacp>
    #                         <force-up/>
    #                         <port-priority>100</port-priority>
    #                     </lacp>
    #                     <bundle>ae1</bundle>
    #                 </ieee-802.3ad>
    #             </ether-options>
    #         </interface>
    #         <interface>
    #             <name>ge-0/0/2</name>
    #             <ether-options>
    #                 <ieee-802.3ad>
    #                     <bundle>ae1</bundle>
    #                 </ieee-802.3ad>
    #             </ether-options>
    #         </interface>
    #         <interface>
    #             <name>ge-0/0/3</name>
    #             <ether-options>
    #                 <ieee-802.3ad>
    #                     <bundle>ae2</bundle>
    #                 </ieee-802.3ad>
    #             </ether-options>
    #         </interface>
    #         <interface>
    #             <name>ge-0/0/4</name>
    #             <ether-options>
    #                 <ieee-802.3ad>
    #                     <bundle>ae2</bundle>
    #                 </ieee-802.3ad>
    #             </ether-options>
    #         </interface>
    #         <interface>
    #             <name>ge-1/0/0</name>
    #             <unit>
    #                 <name>0</name>
    #                 <family>
    #                     <inet>
    #                         <address>
    #                             <name>192.168.100.1/24</name>
    #                         </address>
    #                         <address>
    #                             <name>10.200.16.20/24</name>
    #                         </address>
    #                     </inet>
    #                     <inet6>
    #                     </inet6>
    #                 </family>
    #             </unit>
    #         </interface>
    #         <interface>
    #             <name>ge-2/0/0</name>
    #             <unit>
    #                 <name>0</name>
    #                 <family>
    #                     <inet>
    #                         <address>
    #                             <name>192.168.100.2/24</name>
    #                         </address>
    #                         <address>
    #                             <name>10.200.16.21/24</name>
    #                         </address>
    #                     </inet>
    #                     <inet6>
    #                     </inet6>
    #                 </family>
    #             </unit>
    #         </interface>
    #         <interface>
    #             <name>ge-3/0/0</name>
    #             <unit>
    #                 <name>0</name>
    #                 <family>
    #                     <inet>
    #                         <address>
    #                             <name>192.168.100.3/24</name>
    #                         </address>
    #                         <address>
    #                             <name>10.200.16.22/24</name>
    #                         </address>
    #                     </inet>
    #                     <inet6>
    #                     </inet6>
    #                 </family>
    #             </unit>
    #         </interface>
    #         <interface>
    #             <name>ae1</name>
    #             <description>Configured by Ansible</description>
    #             <aggregated-ether-options>
    #                 <lacp>
    #                     <periodic>fast</periodic>
    #                     <sync-reset>enable</sync-reset>
    #                     <system-priority>100</system-priority>
    #                     <system-id>00:00:00:00:00:02</system-id>
    #                 </lacp>
    #             </aggregated-ether-options>
    #         </interface>
    #         <interface>
    #             <name>ae2</name>
    #             <description>Configured by Ansible</description>
    #         </interface>
    #         <interface>
    #             <name>em1</name>
    #             <description>TEST</description>
    #         </interface>
    #         <interface>
    #             <name>fxp0</name>
    #             <description>ANSIBLE</description>
    #             <speed>1g</speed>
    #             <link-mode>automatic</link-mode>
    #             <unit>
    #                 <name>0</name>
    #                 <family>
    #                     <inet>
    #                         <address>
    #                             <name>10.8.38.38/24</name>
    #                         </address>
    #                     </inet>
    #                 </family>
    #             </unit>
    #         </interface>
    #     </interfaces>
    #     </configuration>
    # </rpc-reply>
    # - name: Convert interfaces config to argspec without connecting to the appliance
    #   junipernetworks.junos.junos_lacp_interfaces:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": [
    #         {
    #             "force_up": true,
    #             "name": "ge-0/0/1",
    #             "port_priority": 100
    #         },
    #         {
    #             "name": "ae1",
    #             "period": "fast",
    #             "sync_reset": "enable",
    #             "system": {
    #                 "mac": {
    #                     "address": "00:00:00:00:00:02"
    #                 },
    #                 "priority": 100
    #             }
    #         }
    #     ]
    # Using rendered
    - name: Render platform specific xml from task input using rendered state
      junipernetworks.junos.junos_lacp_interfaces:
        config:
          - name: ae1
            period: fast
            sync_reset: enable
            system:
              priority: 100
              mac:
                address: 00:00:00:00:00:02

          - name: ge-0/0/1
            port_priority: 100
            force_up: true
        state: rendered
    # Task Output (redacted)
    # -----------------------
    # "rendered": "<nc:interfaces
    #     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #     <nc:interface>
    #         <nc:name>ae1</nc:name>
    #         <nc:aggregated-ether-options>
    #             <nc:lacp>
    #                 <nc:periodic>fast</nc:periodic>
    #                 <nc:sync-reset>enable</nc:sync-reset>
    #                 <nc:system-id>00:00:00:00:00:02</nc:system-id>
    #                 <nc:system-priority>100</nc:system-priority>
    #             </nc:lacp>
    #         </nc:aggregated-ether-options>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ge-0/0/1</nc:name>
    #         <nc:ether-options>
    #             <nc:ieee-802.3ad>
    #                 <nc:lacp>
    #                     <nc:port-priority>100</nc:port-priority>
    #                     <nc:force-up/>
    #                 </nc:lacp>
    #             </nc:ieee-802.3ad>
    #         </nc:ether-options>
    #     </nc:interface>
    # </nc:interfaces>"



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:interfaces xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ae1&lt;/nc:name&gt; &lt;nc:aggregated-ether-options&gt; &lt;nc:lacp&gt; &lt;nc:periodic&gt;fast&lt;/nc:periodic&gt; &lt;nc:sync-reset&gt;enable&lt;/nc:sync-reset&gt; &lt;nc:system-id&gt;00:00:00:00:00:02&lt;/nc:system-id&gt; &lt;nc:system-priority&gt;100&lt;/nc:system-priority&gt; &lt;/nc:lacp&gt; &lt;/nc:aggregated-ether-options&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/1&lt;/nc:name&gt; &lt;nc:ether-options&gt; &lt;nc:ieee-802.3ad&gt; &lt;nc:lacp&gt; &lt;nc:port-priority&gt;100&lt;/nc:port-priority&gt; &lt;nc:force-up/&gt; &lt;/nc:lacp&gt; &lt;/nc:ieee-802.3ad&gt; &lt;/nc:ether-options&gt; &lt;/nc:interface&gt; &lt;/nc:interfaces&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
