.. _junipernetworks.junos.junos_interfaces_module:


**************************************
junipernetworks.junos.junos_interfaces
**************************************

**Junos Interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the interfaces on Juniper Junos OS network devices.



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
                        <div>The provided configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Interface description.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>duplex</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>automatic</li>
                                    <li>full-duplex</li>
                                    <li>half-duplex</li>
                        </ul>
                </td>
                <td>
                        <div>Interface link status. Applicable for Ethernet interfaces only, either in half duplex, full duplex or in automatic state which negotiates the duplex automatically.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Administrative state of the interface.</div>
                        <div>Set the value to <code>true</code> to administratively enabled the interface or <code>false</code> to disable it.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hold_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The hold time for given interface name.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>down</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The link down hold time in milliseconds.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>up</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The link up hold time in milliseconds.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MTU for a specific interface.</div>
                        <div>Applicable for Ethernet interfaces only.</div>
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
                        <div>Full name of interface, e.g. ge-0/0/0.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface link speed. Applicable for Ethernet interfaces only.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>units</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Logical interfaces units.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify logical interface description.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify interface unit number.</div>
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
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>parsed</li>
                                    <li>rendered</li>
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
   - This module works with connection ``netconf``. See https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html
   - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.



Examples
--------

.. code-block:: yaml

    # Using merged

    # Before state:
    # -------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     description "test interface";
    #     speed 1g;
    # }
    # fe-0/0/2 {
    #     vlan-tagging;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/3 {
    #     description "Configured by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    - name: Merge provided configuration with device configuration (default operation
        is merge)
      junipernetworks.junos.junos_interfaces:
        config:
          - name: ge-0/0/1
            description: Configured by Ansible-1
            enabled: true
            units:
              - name: 0
                description: "This is logical intf unit0"
            mtu: 1800
          - name: ge-0/0/2
            description: Configured by Ansible-2
            enabled: false
        state: merged

    # Task Output
    # -----------
    #
    # before:
    # - description: test interface
    #   enabled: true
    #   name: ge-0/0/1
    #   speed: 1g
    # - enabled: true
    #   name: fe-0/0/2
    # - description: Configured by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface><nc:name>ge-0/0/1</nc:name>
    #   <nc:description>Configured by Ansible-1</nc:description><nc:mtu>1800</nc:mtu><nc:unit><nc:name>0</nc:name>
    #   <nc:description>This is logical intf unit0</nc:description></nc:unit></nc:interface><nc:interface><nc:name>ge-0/0/2</nc:name>
    #   <nc:description>Configured by Ansible-2</nc:description><nc:disable/></nc:interface></nc:interfaces>
    # after:
    # - description: Configured by Ansible-1
    #   enabled: true
    #   mtu: 1800
    #   name: ge-0/0/1
    #   speed: 1g
    #   units:
    #   - description: This is logical intf unit0
    #     name: 0
    # - enabled: true
    #   name: fe-0/0/2
    # - description: Configured by Ansible-2
    #   enabled: false
    #   name: ge-0/0/2
    # - description: Configured by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0

    # After state:
    # ------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     description "Configured by Ansible-1";
    #     speed 1g;
    #     mtu 1800;
    #     unit 0 {
    #         description "This is logical intf unit0";
    #     }
    # }
    # fe-0/0/2 {
    #     vlan-tagging;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    # }
    # ge-0/0/3 {
    #     description "Configured by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    # Using deleted

    # Before state:
    # -------------
    #
    # ge-0/0/1 {
    #     description "Configured by Ansible-1";
    #     speed 1g;
    #     mtu 1800;
    #     unit 0 {
    #         description "This is logical intf unit0";
    #     }
    # }
    # fe-0/0/2 {
    #     vlan-tagging;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    # }
    # ge-0/0/3 {
    #     description "Configured by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    - name: "Delete given options for the interface (Note: This won't delete the interface itself if any other values are configured for interface)"
      junipernetworks.junos.junos_interfaces:
        config:
          - name: ge-0/0/1
            description: Configured by Ansible-1
            speed: 1g
            mtu: 1800
          - name: ge-0/0/2
            description: Configured by Ansible -2
        state: deleted

    # Task Output
    # -----------
    #
    # before:
    # - description: Configured by Ansible-1
    #   enabled: true
    #   mtu: 1800
    #   name: ge-0/0/1
    #   speed: 1g
    #   units:
    #   - description: This is logical intf unit0
    #     name: 0
    # - enabled: true
    #   name: fe-0/0/2
    # - description: Configured by Ansible-2
    #   enabled: false
    #   name: ge-0/0/2
    # - description: Configured by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>
    #   <nc:name>ge-0/0/1</nc:name><nc:description delete="delete"/>
    #   <nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/>
    #   <nc:disable delete="delete"/><nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time><nc:unit>
    #   <nc:name>0</nc:name><nc:description delete="delete"/></nc:unit></nc:interface><nc:interface><nc:name>ge-0/0/2</nc:name>
    #   <nc:description delete="delete"/><nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/>
    #   <nc:disable delete="delete"/><nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface>
    #   </nc:interfaces>
    # after:
    # - enabled: true
    #   name: ge-0/0/1
    # - enabled: true
    #   name: fe-0/0/2
    # - description: Configured by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0

    # After state:
    # ------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0;
    # }
    # fe-0/0/2 {
    #     vlan-tagging;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/3 {
    #     description "Configured by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    # Using overridden

    # Before state:
    # -------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0;
    # }
    # fe-0/0/2 {
    #     vlan-tagging;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/3 {
    #     description "Configured by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    - name: Override device configuration of all interfaces with provided configuration
      junipernetworks.junos.junos_interfaces:
        config:
          - enabled: true
            name: ge-0/0/1
          - name: fe-0/0/2
            description: Configured by Ansible-2
            enabled: false
            mtu: 2800
          - description: Updated by Ansible-3
            enabled: true
            name: ge-0/0/3
          - enabled: true
            name: fxp0
          - enabled: true
            name: lo0
        state: overridden

    # Task Output
    # -----------
    #
    # before:
    # - enabled: true
    #   name: ge-0/0/1
    # - enabled: true
    #   name: fe-0/0/2
    # - description: Configured by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:interface><nc:name>ge-0/0/1</nc:name><nc:description delete="delete"/>
    #   <nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/>
    #   <nc:disable delete="delete"/><nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/>
    #   </nc:hold-time></nc:interface><nc:interface><nc:name>fe-0/0/2</nc:name><nc:description delete="delete"/>
    #   <nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/><nc:disable delete="delete"/>
    #   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface><nc:interface>
    #   <nc:name>ge-0/0/3</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/><nc:mtu delete="delete"/>
    #   <nc:link-mode delete="delete"/><nc:disable delete="delete"/><nc:hold-time>
    #   <nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface>
    #   <nc:interface><nc:name>fxp0</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/>
    #   <nc:link-mode delete="delete"/><nc:disable delete="delete"/>
    #   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/>
    #   </nc:hold-time></nc:interface><nc:interface><nc:name>lo0</nc:name>
    #   <nc:description delete="delete"/><nc:disable delete="delete"/>
    #   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/>
    #   </nc:hold-time></nc:interface><nc:interface><nc:name>ge-0/0/1</nc:name>
    #   </nc:interface><nc:interface><nc:name>fe-0/0/2</nc:name>
    #   <nc:description>Configured by Ansible-2</nc:description>
    #   <nc:mtu>2800</nc:mtu><nc:disable/></nc:interface><nc:interface>
    #   <nc:name>ge-0/0/3</nc:name><nc:description>Updated by Ansible-3</nc:description>
    #   </nc:interface><nc:interface><nc:name>fxp0</nc:name></nc:interface><nc:interface>
    #   <nc:name>lo0</nc:name></nc:interface></nc:interfaces>
    # after:
    # - enabled: true
    #   name: ge-0/0/1
    # - description: Configured by Ansible-2
    #   enabled: false
    #   mtu: 2800
    #   name: fe-0/0/2
    # - description: Updated by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0

    # After state:
    # ------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0;
    # }
    # fe-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    #     vlan-tagging;
    #     mtu 2800;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/3 {
    #     description "Updated by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }


    # Using replaced

    # Before state:
    # -------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0;
    # }
    # fe-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    #     vlan-tagging;
    #     mtu 2800;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/3 {
    #     description "Updated by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    - name: Replace device configuration of listed interfaces with provided configuration
      junipernetworks.junos.junos_interfaces:
        config:
          - name: ge-0/0/2
            description: Configured by Ansible-2
            enabled: false
            mtu: 2800
          - name: ge-0/0/3
            description: Configured by Ansible-3
        state: replaced

    # Task Output
    # -----------
    #
    # before:
    # - enabled: true
    #   name: ge-0/0/1
    # - description: Configured by Ansible-2
    #   enabled: false
    #   mtu: 2800
    #   name: fe-0/0/2
    # - description: Updated by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>
    #   <nc:name>ge-0/0/2</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/>
    #   <nc:mtu delete="delete"/><nc:link-mode delete="delete"/><nc:disable delete="delete"/>
    #   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface>
    #   <nc:interface><nc:name>ge-0/0/3</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/>
    #   <nc:mtu delete="delete"/><nc:link-mode delete="delete"/><nc:disable delete="delete"/><nc:hold-time>
    #   <nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface><nc:interface><nc:name>ge-0/0/2</nc:name>
    #   <nc:description>Configured by Ansible-2</nc:description><nc:mtu>2800</nc:mtu><nc:disable/></nc:interface><nc:interface>
    #   <nc:name>ge-0/0/3</nc:name><nc:description>Configured by Ansible-3</nc:description></nc:interface></nc:interfaces>
    # after:
    # - enabled: true
    #   name: ge-0/0/1
    # - description: Configured by Ansible-2
    #   enabled: false
    #   mtu: 2800
    #   name: fe-0/0/2
    # - description: Configured by Ansible-2
    #   enabled: false
    #   mtu: 2800
    #   name: ge-0/0/2
    # - description: Configured by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0

    # After state:
    # ------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0;
    # }
    # fe-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    #     vlan-tagging;
    #     mtu 2800;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    #     mtu 2800;
    # }
    # ge-0/0/3 {
    #     description "Configured by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    # Using gathered

    # Before state:
    # ------------
    #
    # vagrant@vsrx# show interfaces
    # ge-0/0/1 {
    #     unit 0;
    # }
    # fe-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    #     vlan-tagging;
    #     mtu 2800;
    #     unit 10 {
    #         vlan-id 10;
    #     }
    #     unit 11 {
    #         vlan-id 11;
    #     }
    # }
    # ge-0/0/2 {
    #     description "Configured by Ansible-2";
    #     disable;
    #     mtu 2800;
    # }
    # ge-0/0/3 {
    #     description "Configured by Ansible-3";
    # }
    # fxp0 {
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # lo0 {
    #     unit 0 {
    #         family inet {
    #             address 192.0.2.1/32;
    #         }
    #     }
    # }

    - name: Gather junos interfaces as in given arguments
      junipernetworks.junos.junos_interfaces:
        state: gathered

    # Task Output
    # -----------
    #
    # gathered:
    # - enabled: true
    #   name: ge-0/0/1
    # - description: Configured by Ansible-2
    #   enabled: false
    #   mtu: 2800
    #   name: fe-0/0/2
    # - description: Configured by Ansible-2
    #   enabled: false
    #   mtu: 2800
    #   name: ge-0/0/2
    # - description: Configured by Ansible-3
    #   enabled: true
    #   name: ge-0/0/3
    # - enabled: true
    #   name: fxp0
    # - enabled: true
    #   name: lo0

    # Using parsed

    # parsed.cfg
    # ------------
    #
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <interfaces>
    #             <interface>
    #                 <name>ge-0/0/1</name>
    #                 <description>Configured by Ansible</description>
    #                 <disable/>
    #                 <speed>100m</speed>
    #                 <mtu>1024</mtu>
    #                 <hold-time>
    #                     <up>2000</up>
    #                     <down>2200</down>
    #                 </hold-time>
    #                 <link-mode>full-duplex</link-mode>
    #                 <unit>
    #                     <name>0</name>
    #                     <family>
    #                         <ethernet-switching>
    #                             <interface-mode>access</interface-mode>
    #                             <vlan>
    #                                 <members>vlan100</members>
    #                             </vlan>
    #                         </ethernet-switching>
    #                     </family>
    #                 </unit>
    #             </interface>
    #         </interfaces>
    #     </configuration>
    # </rpc-reply>

    # - name: Convert interfaces config to structured data without connecting to the appliance
    #   junipernetworks.junos.junos_interfaces:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed

    # Task Output
    # -----------
    #
    # parsed:
    # - description: Configured by Ansible
    #   duplex: full-duplex
    #   enabled: false
    #   hold_time:
    #     down: 2200
    #     up: 2000
    #   mtu: 1024
    #   name: ge-0/0/1
    #   speed: 100m

    # Using rendered

    - name: Render platform specific xml from task input using rendered state
      junipernetworks.junos.junos_interfaces:
        config:
          - name: ge-0/0/2
            description: Configured by Ansible
            mtu: 2048
            speed: 20m
            hold_time:
              up: 3200
              down: 3200
        state: rendered

    # Task Output
    # -----------
    #
    # rendered: <nc:interfaces
    #     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #     <nc:interface>
    #         <nc:name>ge-0/0/2</nc:name>
    #         <nc:description>Configured by Ansible</nc:description>
    #         <nc:speed>20m</nc:speed>
    #         <nc:mtu>2048</nc:mtu>
    #         <nc:hold-time>
    #             <nc:up>3200</nc:up>
    #             <nc:down>3200</nc:down>
    #         </nc:hold-time>
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
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>gathered</code></td>
                <td>
                            <div>Facts about the network resource gathered from the remote device as structured data.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>parsed</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>parsed</code></td>
                <td>
                            <div>The device native config provided in <em>running_config</em> option parsed into structured data as per module argspec.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>rendered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>rendered</code></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:protocols xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt;&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt; &lt;rpc-reply message-id=&quot;urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f&quot;&gt; &lt;configuration changed-seconds=&quot;1590139550&quot; changed-localtime=&quot;2020-05-22 09:25:50 UTC&quot;&gt; &lt;interfaces&gt; &lt;interface&gt; &lt;name&gt;ge-0/0/1&lt;/name&gt; &lt;description&gt;Configured by Ansible&lt;/description&gt; &lt;disable/&gt; &lt;speed&gt;100m&lt;/speed&gt; &lt;mtu&gt;1024&lt;/mtu&gt; &lt;hold-time&gt; &lt;up&gt;2000&lt;/up&gt; &lt;down&gt;2200&lt;/down&gt; &lt;/hold-time&gt; &lt;link-mode&gt;full-duplex&lt;/link-mode&gt; &lt;unit&gt; &lt;name&gt;0&lt;/name&gt; &lt;family&gt; &lt;ethernet-switching&gt; &lt;interface-mode&gt;access&lt;/interface-mode&gt; &lt;vlan&gt; &lt;members&gt;vlan100&lt;/members&gt; &lt;/vlan&gt; &lt;/ethernet-switching&gt; &lt;/family&gt; &lt;/unit&gt; &lt;/interface&gt; &lt;/interfaces&gt; &lt;/configuration&gt; &lt;/rpc-reply&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
