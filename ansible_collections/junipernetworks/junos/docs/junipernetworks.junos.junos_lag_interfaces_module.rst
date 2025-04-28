.. _junipernetworks.junos.junos_lag_interfaces_module:


******************************************
junipernetworks.junos.junos_lag_interfaces
******************************************

**Link Aggregation Juniper JUNOS resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages properties of Link Aggregation Group on Juniper JUNOS devices.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)


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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of link aggregation group configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_protection</b>
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
                        <div>This boolean option indicates if link protection should be enabled for the LAG interface. If value is <code>True</code> link protection is enabled on LAG and if value is <code>False</code> link protection is disabled.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of member interfaces of the link aggregation group. The value can be single interface or list of interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ether_option_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>ether</b>&nbsp;&larr;</div></li>
                                    <li>gigether</li>
                        </ul>
                </td>
                <td>
                        <div>Specify the type of ethernet interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>primary</li>
                                    <li>backup</li>
                        </ul>
                </td>
                <td>
                        <div>The value of this options configures the member link as either <code>primary</code> or <code>backup</code>. Value <code>primary</code> configures primary interface for link-protection mode and <code>backup</code> configures backup interface for link-protection mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>member</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the member interface.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>active</li>
                                    <li>passive</li>
                        </ul>
                </td>
                <td>
                        <div>LAG mode. A value of <code>passive</code> will enable LACP in <code>passive</code> mode that is it will respond to LACP packets and <code>active</code> configures the link to initiate transmission of LACP packets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Name of the link aggregation group (LAG).</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show interfaces</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result</div>
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
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module requires the netconf system service be enabled on the remote device being managed.
   - Tested against vSRX JUNOS version 18.4R1.
   - This module works with connection ``netconf``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.



Examples
--------

.. code-block:: yaml

    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ae0 {
    #     description "lag interface";
    # }
    # ae1 {
    #     description "lag interface 1";
    # }

    - name: "Delete LAG attributes of given interfaces (Note: This won't delete the interface itself)"
      junipernetworks.junos.junos_lag_interfaces:
        config:
          - name: ae0
          - name: ae1
        state: deleted

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }

    - name: Merge provided configuration with device configuration
      junipernetworks.junos.junos_lag_interfaces:
        config:
          - name: ae0
            members:
              - member: ge-0/0/1
                link_type: primary
              - member: ge-0/0/2
                link_type: backup
        state: merged

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad {
    #            ae0;
    #            primary;
    #        }
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad {
    #            ae0;
    #            backup;
    #        }
    #    }
    # }


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ae0 {
    #     description "lag interface";
    # }
    # ae3 {
    #     description "lag interface 3";
    # }

    - name: Overrides all device LAG configuration with provided configuration
      junipernetworks.junos.junos_lag_interfaces:
        config:
          - name: ae0
            members:
              - member: ge-0/0/2
          - name: ae1
            members:
              - member: ge-0/0/1
            mode: passive
        state: overridden

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae1;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ae0 {
    #     description "lag interface";
    # }
    # ae1 {
    #    aggregated-ether-options {
    #        lacp {
    #            active;
    #        }
    #    }
    # }


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }
    # ge-0/0/3 {
    #    description "Ansible configured interface 3";
    # }

    - name: Replace device LAG configuration with provided configuration
      junipernetworks.junos.junos_lag_interfaces:
        config:
          - name: ae0
            members:
              - member: ge-0/0/1
            mode: active
        state: replaced

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }
    # ae0 {
    #    aggregated-ether-options {
    #        lacp {
    #            active;
    #        }
    #    }
    # }
    # ge-0/0/3 {
    #    description "Ansible configured interface 3";
    # }
    # Using gathered
    # Before state:
    # ------------
    #
    # ansible@cm123456tr21# show interfaces
    # ge-0/0/1 {
    #     ether-options {
    #         802.3ad ae1;
    #     }
    # }
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae1;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             ae2;
    #             primary;
    #         }
    #     }
    # }
    # ge-0/0/4 {
    #     ether-options {
    #         802.3ad {
    #             ae2;
    #             backup;
    #         }
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
    #             active;
    #         }
    #     }
    # }
    # ae2 {
    #     description "Configured by Ansible";
    #     aggregated-ether-options {
    #         link-protection;
    #         lacp {
    #             passive;
    #         }
    #     }
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
    - name: Gather junos lag interfaces as in given arguments
      junipernetworks.junos.junos_lag_interfaces:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": [
    #         {
    #             "members": [
    #                 {
    #                     "member": "ge-0/0/1"
    #                 },
    #                 {
    #                     "member": "ge-0/0/2"
    #                 }
    #             ],
    #             "mode": "active",
    #             "name": "ae1"
    #         },
    #         {
    #             "link_protection": true,
    #             "members": [
    #                 {
    #                     "link_type": "primary",
    #                     "member": "ge-0/0/3"
    #                 },
    #                 {
    #                     "link_type": "backup",
    #                     "member": "ge-0/0/4"
    #                 }
    #             ],
    #             "mode": "passive",
    #             "name": "ae2"
    #         }
    #     ]
    # After state:
    # ------------
    #
    # ansible@cm123456tr21# show interfaces
    # ge-0/0/1 {
    #     ether-options {
    #         802.3ad ae1;
    #     }
    # }
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae1;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             ae2;
    #             primary;
    #         }
    #     }
    # }
    # ge-0/0/4 {
    #     ether-options {
    #         802.3ad {
    #             ae2;
    #             backup;
    #         }
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
    #             active;
    #         }
    #     }
    # }
    # ae2 {
    #     description "Configured by Ansible";
    #     aggregated-ether-options {
    #         link-protection;
    #         lacp {
    #             passive;
    #         }
    #     }
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
    #                     <primary/>
    #                 </ieee-802.3ad>
    #             </ether-options>
    #         </interface>
    #         <interface>
    #             <name>ge-0/0/4</name>
    #             <ether-options>
    #                 <ieee-802.3ad>
    #                     <bundle>ae2</bundle>
    #                     <backup/>
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
    #                     <active/>
    #                 </lacp>
    #             </aggregated-ether-options>
    #         </interface>
    #         <interface>
    #             <name>ae2</name>
    #             <description>Configured by Ansible</description>
    #             <aggregated-ether-options>
    #                 <link-protection>
    #                 </link-protection>
    #                 <lacp>
    #                     <passive/>
    #                 </lacp>
    #             </aggregated-ether-options>
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
    #   junipernetworks.junos.junos_lag_interfaces:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": [
    #         {
    #             "members": [
    #                 {
    #                     "member": "ge-0/0/1"
    #                 },
    #                 {
    #                     "member": "ge-0/0/2"
    #                 }
    #             ],
    #             "mode": "active",
    #             "name": "ae1"
    #         },
    #         {
    #             "link_protection": true,
    #             "members": [
    #                 {
    #                     "link_type": "primary",
    #                     "member": "ge-0/0/3"
    #                 },
    #                 {
    #                     "link_type": "backup",
    #                     "member": "ge-0/0/4"
    #                 }
    #             ],
    #             "mode": "passive",
    #             "name": "ae2"
    #         }
    #     ]
    # Using rendered
    - name: Render platform specific xml from task input using rendered state
      junipernetworks.junos.junos_lag_interfaces:
        config:
          - name: ae1
            members:
              - member: ge-0/0/1
              - member: ge-0/0/2
            mode: active

          - name: ae2
            link_protection: true
            members:
              - member: ge-0/0/3
                link_type: primary
              - member: ge-0/0/4
                link_type: backup
            mode: passive
    # Task Output (redacted)
    # -----------------------
    # "rendered": "<nc:interfaces
    #     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #     <nc:interface>
    #         <nc:name>ae1</nc:name>
    #         <nc:aggregated-ether-options>
    #             <nc:lacp>
    #                 <nc:active/>
    #             </nc:lacp>
    #         </nc:aggregated-ether-options>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ge-0/0/1</nc:name>
    #         <nc:ether-options>
    #             <nc:ieee-802.3ad>
    #                 <nc:bundle>ae1</nc:bundle>
    #             </nc:ieee-802.3ad>
    #         </nc:ether-options>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ge-0/0/2</nc:name>
    #         <nc:ether-options>
    #             <nc:ieee-802.3ad>
    #                 <nc:bundle>ae1</nc:bundle>
    #             </nc:ieee-802.3ad>
    #         </nc:ether-options>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ae2</nc:name>
    #         <nc:aggregated-ether-options>
    #             <nc:lacp>
    #                 <nc:passive/>
    #             </nc:lacp>
    #             <nc:link-protection/>
    #         </nc:aggregated-ether-options>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ge-0/0/3</nc:name>
    #         <nc:ether-options>
    #             <nc:ieee-802.3ad>
    #                 <nc:bundle>ae2</nc:bundle>
    #                 <nc:primary/>
    #             </nc:ieee-802.3ad>
    #         </nc:ether-options>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ge-0/0/4</nc:name>
    #         <nc:ether-options>
    #             <nc:ieee-802.3ad>
    #                 <nc:bundle>ae2</nc:bundle>
    #                 <nc:backup/>
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
                    <b>xml</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of xml rpc payload pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:interfaces xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ae1&lt;/nc:name&gt; &lt;nc:aggregated-ether-options&gt; &lt;nc:lacp&gt; &lt;nc:active/&gt; &lt;/nc:lacp&gt; &lt;/nc:aggregated-ether-options&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/1&lt;/nc:name&gt; &lt;nc:ether-options&gt; &lt;nc:ieee-802.3ad&gt; &lt;nc:bundle&gt;ae1&lt;/nc:bundle&gt; &lt;/nc:ieee-802.3ad&gt; &lt;/nc:ether-options&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/2&lt;/nc:name&gt; &lt;nc:ether-options&gt; &lt;nc:ieee-802.3ad&gt; &lt;nc:bundle&gt;ae1&lt;/nc:bundle&gt; &lt;/nc:ieee-802.3ad&gt; &lt;/nc:ether-options&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ae2&lt;/nc:name&gt; &lt;nc:aggregated-ether-options&gt; &lt;nc:lacp&gt; &lt;nc:passive/&gt; &lt;/nc:lacp&gt; &lt;nc:link-protection/&gt; &lt;/nc:aggregated-ether-options&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/3&lt;/nc:name&gt; &lt;nc:ether-options&gt; &lt;nc:ieee-802.3ad&gt; &lt;nc:bundle&gt;ae2&lt;/nc:bundle&gt; &lt;nc:primary/&gt; &lt;/nc:ieee-802.3ad&gt; &lt;/nc:ether-options&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/4&lt;/nc:name&gt; &lt;nc:ether-options&gt; &lt;nc:ieee-802.3ad&gt; &lt;nc:bundle&gt;ae2&lt;/nc:bundle&gt; &lt;nc:backup/&gt; &lt;/nc:ieee-802.3ad&gt; &lt;/nc:ether-options&gt; &lt;/nc:interface&gt; &lt;/nc:interfaces&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
