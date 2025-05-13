.. _junipernetworks.junos.junos_l2_interfaces_module:


*****************************************
junipernetworks.junos.junos_l2_interfaces
*****************************************

**L2 interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of a Layer-2 interface on Juniper JUNOS devices.



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
                        <div>A dictionary of Layer-2 interface options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the interface as a Layer 2 access mode.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the access VLAN ID.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enhanced_layer</b>
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
                        <div>True if your device has Enhanced Layer 2 Software (ELS). If the l2 configuration is under <code>interface-mode</code> the value is True else if the l2 configuration is under <code>port-mode</code> value is False</div>
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
                        <div>Full name of interface, e.g. ge-0/0/1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trunk</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the interface as a Layer 2 trunk mode.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allowed_vlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of VLANs to be configured in trunk port. It&#x27;s used as the VLAN range to ADD or REMOVE from the trunk.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>native_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Native VLAN to be configured in trunk port. It is used as the trunk native VLAN ID.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Logical interface number. Value of <code>unit</code> should be of type integer.</div>
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
    # ansible@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #         }
    #     }
    # }
    # ge-0/0/4 {
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }

    - name: Merge provided configuration with device configuration
      junipernetworks.junos.junos_l2_interfaces:
        config:
          - name: ge-0/0/3
            access:
              vlan: v101
          - name: ge-0/0/4
            trunk:
              allowed_vlans:
                - vlan30
              native_vlan: 50
        state: merged

    # Task Output
    # -----------
    #
    # before:
    # - enhanced_layer: true
    #   name: ge-0/0/3
    #   unit: 0
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   unit: 0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # 	<nc:interface>
    # 		<nc:name>ge-0/0/3</nc:name>
    # 		<nc:unit>
    # 			<nc:name>0</nc:name>
    # 			<nc:family>
    # 				<nc:ethernet-switching>
    # 					<nc:interface-mode>access</nc:interface-mode>
    # 					<nc:vlan>
    # 						<nc:members>v101</nc:members>
    # 					</nc:vlan>
    # 				</nc:ethernet-switching>
    # 			</nc:family>
    # 		</nc:unit>
    # 	</nc:interface>
    # 	<nc:interface>
    # 		<nc:name>ge-0/0/4</nc:name>
    # 		<nc:unit>
    # 			<nc:name>0</nc:name>
    # 			<nc:family>
    # 				<nc:ethernet-switching>
    # 					<nc:interface-mode>trunk</nc:interface-mode>
    # 					<nc:vlan>
    # 						<nc:members>vlan30</nc:members>
    # 					</nc:vlan>
    # 				</nc:ethernet-switching>
    # 			</nc:family>
    # 		</nc:unit>
    # 		<nc:native-vlan-id>50</nc:native-vlan-id>
    # 	</nc:interface>
    # </nc:interfaces>
    # after:
    # - access:
    #     vlan: v101
    #   enhanced_layer: true
    #   name: ge-0/0/3
    #   unit: 0
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   trunk:
    #     allowed_vlans:
    #     - vlan30
    #     native_vlan: '50'
    #   unit: 0

    # After state:
    # ------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #             vlan {
    #                 members v101;
    #             }
    #         }
    #     }
    # }
    # ge-0/0/4 {
    #     native-vlan-id 50;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members vlan30;
    #             }
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }


    # Using overridden

    # Before state:
    # -------------
    # ansible@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #             vlan {
    #                 members v101;
    #             }
    #         }
    #     }
    # }
    # ge-0/0/4 {
    #     native-vlan-id 50;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members vlan30;
    #             }
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }

    - name: Override provided configuration with device configuration
      junipernetworks.junos.junos_l2_interfaces:
        config:
          - name: ge-0/0/4
            trunk:
              allowed_vlans:
                - v101
              native_vlan: 30
        state: overridden

    # Task Output
    # -----------
    #
    # before:
    # - access:
    #     vlan: v101
    #   enhanced_layer: true
    #   name: ge-0/0/3
    #   unit: 0
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   trunk:
    #     allowed_vlans:
    #     - vlan30
    #     native_vlan: '50'
    #   unit: 0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:interface>
    #     <nc:name>ge-0/0/4</nc:name>
    #     <nc:unit>
    #       <nc:name>0</nc:name>
    #       <nc:family>
    #         <nc:ethernet-switching>
    #           <nc:interface-mode delete="delete"/>
    #           <nc:vlan delete="delete"/>
    #         </nc:ethernet-switching>
    #       </nc:family>
    #     </nc:unit>
    #     <nc:native-vlan-id delete="delete"/>
    #   </nc:interface>
    #   <nc:interface>
    #     <nc:name>ge-0/0/4</nc:name>
    #     <nc:unit>
    #       <nc:name>0</nc:name>
    #       <nc:family>
    #         <nc:ethernet-switching>
    #           <nc:interface-mode>trunk</nc:interface-mode>
    #           <nc:vlan>
    #             <nc:members>v101</nc:members>
    #           </nc:vlan>
    #         </nc:ethernet-switching>
    #       </nc:family>
    #     </nc:unit>
    #     <nc:native-vlan-id>30</nc:native-vlan-id>
    #   </nc:interface>
    #   <nc:interface>
    #     <nc:name>ge-0/0/3</nc:name>
    #     <nc:unit>
    #       <nc:name>0</nc:name>
    #       <nc:family>
    #         <nc:ethernet-switching>
    #           <nc:interface-mode delete="delete"/>
    #           <nc:vlan delete="delete"/>
    #         </nc:ethernet-switching>
    #       </nc:family>
    #     </nc:unit>
    #     <nc:native-vlan-id delete="delete"/>
    #   </nc:interface>
    # </nc:interfaces>
    # after:
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   trunk:
    #     allowed_vlans:
    #     - v101
    #     native_vlan: '30'
    #   unit: 0

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching;
    #     }
    # }
    # ge-0/0/4 {
    #     native-vlan-id 30;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members v101;
    #             }
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }

    # Using replaced

    # Before state:
    # -------------
    #
    # ansible@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching;
    #     }
    # }
    # ge-0/0/4 {
    #     native-vlan-id 30;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members v101;
    #             }
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }

    - name: Replace provided configuration with device configuration
      junipernetworks.junos.junos_l2_interfaces:
        config:
          - name: ge-0/0/3
            access:
              vlan: v101
          - name: ge-0/0/4
            trunk:
              allowed_vlans:
                - vlan30
              native_vlan: 50
        state: replaced

    # Task Output
    # -----------
    #
    # before:
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   trunk:
    #     allowed_vlans:
    #     - v101
    #     native_vlan: '30'
    #   unit: 0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:interface>
    #     <nc:name>ge-0/0/4</nc:name>
    #     <nc:unit>
    #       <nc:name>0</nc:name>
    #       <nc:family>
    #         <nc:ethernet-switching>
    #           <nc:interface-mode delete="delete"/>
    #           <nc:vlan delete="delete"/>
    #         </nc:ethernet-switching>
    #       </nc:family>
    #     </nc:unit>
    #     <nc:native-vlan-id delete="delete"/>
    #   </nc:interface>
    #   <nc:interface>
    #     <nc:name>ge-0/0/3</nc:name>
    #     <nc:unit>
    #       <nc:name>0</nc:name>
    #       <nc:family>
    #         <nc:ethernet-switching>
    #           <nc:interface-mode>access</nc:interface-mode>
    #           <nc:vlan>
    #             <nc:members>v101</nc:members>
    #           </nc:vlan>
    #         </nc:ethernet-switching>
    #       </nc:family>
    #     </nc:unit>
    #   </nc:interface>
    #   <nc:interface>
    #     <nc:name>ge-0/0/4</nc:name>
    #     <nc:unit>
    #       <nc:name>0</nc:name>
    #       <nc:family>
    #         <nc:ethernet-switching>
    #           <nc:interface-mode>trunk</nc:interface-mode>
    #           <nc:vlan>
    #             <nc:members>vlan30</nc:members>
    #           </nc:vlan>
    #         </nc:ethernet-switching>
    #       </nc:family>
    #     </nc:unit>
    #     <nc:native-vlan-id>50</nc:native-vlan-id>
    #   </nc:interface>
    # </nc:interfaces>
    # after:
    # - access:
    #     vlan: v101
    #   enhanced_layer: true
    #   name: ge-0/0/3
    #   unit: 0
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   trunk:
    #     allowed_vlans:
    #     - vlan30
    #     native_vlan: '50'
    #   unit: 0

    # After state:
    # ------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #             vlan {
    #                 members v101;
    #             }
    #         }
    #     }
    # }
    # ge-0/0/4 {
    #     native-vlan-id 50;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members vlan30;
    #             }
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }

    # Using deleted

    # Before state:
    # -------------
    #
    # ansible@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #             vlan {
    #                 members v101;
    #             }
    #         }
    #     }
    # }
    # ge-0/0/4 {
    #     native-vlan-id 50;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members vlan30;
    #             }
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }

    - name: "Delete L2 attributes of given interfaces (Note: This won't delete the
        interface itself)."
      junipernetworks.junos.junos_l2_interfaces:
        config:
          - name: ge-0/0/1
          - name: ge-0/0/2
        state: deleted

    # Task Output
    # -----------
    #
    # before:
    # - access:
    #     vlan: v101
    #   enhanced_layer: true
    #   name: ge-0/0/3
    #   unit: 0
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   trunk:
    #     allowed_vlans:
    #     - vlan30
    #     native_vlan: '50'
    #   unit: 0
    # commands:
    # - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:interface>
    #     <nc:name>ge-0/0/3</nc:name>
    #     <nc:unit>
    #       <nc:name>0</nc:name>
    #       <nc:family>
    #         <nc:ethernet-switching>
    #           <nc:interface-mode delete="delete"/>
    #           <nc:vlan delete="delete"/>
    #         </nc:ethernet-switching>
    #       </nc:family>
    #     </nc:unit>
    #     <nc:native-vlan-id delete="delete"/>
    #   </nc:interface>
    # </nc:interfaces>
    # after:
    # - enhanced_layer: true
    #   name: ge-0/0/4
    #   trunk:
    #     allowed_vlans:
    #     - vlan30
    #     native_vlan: '50'
    #   unit: 0

    # After state:
    # ------------
    #
    # ansible@junos01# show interfaces
    # ge-0/0/1 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/2 {
    #     unit 0 {
    #         family inet;
    #         family inet6;
    #     }
    # }
    # ge-0/0/3 {
    #     unit 0 {
    #         family ethernet-switching;
    #     }
    # }
    # ge-0/0/4 {
    #     native-vlan-id 50;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members vlan30;
    #             }
    #         }
    #     }
    # }
    # fxp0 {
    #     enable;
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #         family inet6;
    #     }
    # }

    # Using gathered

    # Before state:
    # -------------
    #
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #     description "Configured by Ansible";
    #     disable;
    #     speed 100m;
    #     mtu 1024;
    #     hold-time up 2000 down 2200;
    #     link-mode full-duplex;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #             vlan {
    #                 members vlan100;
    #             }
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "Configured by Ansible";
    #     native-vlan-id 400;
    #     speed 10m;
    #     mtu 2048;
    #     hold-time up 3000 down 3200;
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode trunk;
    #             vlan {
    #                 members [ vlan200 vlan300 ];
    #             }
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

    - name: Gather junos layer 2 interfaces facts
      junipernetworks.junos.junos_l2_interfaces:
        state: gathered

    # Task Output
    # -----------
    #
    # gathered:
    # - access:
    #     vlan: vlan100
    #   enhanced_layer: true
    #   name: ge-0/0/1
    #   unit: 0
    # - enhanced_layer: true
    #   name: ge-0/0/2
    #   trunk:
    #     allowed_vlans:
    #     - vlan200
    #     - vlan300
    #     native_vlan: '400'
    #   unit: 0

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

    - name: Convert interfaces config to argspec without connecting to the appliance
      junipernetworks.junos.junos_l2_interfaces:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # Task Output
    # -----------
    #
    # parsed:
    # - access:
    #     vlan: vlan100
    #   enhanced_layer: true
    #   name: ge-0/0/1
    #   unit: 0
    # - enhanced_layer: true
    #   name: ge-0/0/2
    #   trunk:
    #     allowed_vlans:
    #     - vlan200
    #     - vlan300
    #     native_vlan: '400'
    #   unit: 0

    # Using rendered

    - name: Render platform specific xml from task input using rendered state
      junipernetworks.junos.junos_l2_interfaces:
        config:
          - name: ge-0/0/1
            access:
              vlan: vlan100
          - name: ge-0/0/2
            trunk:
              allowed_vlans:
                - vlan200
                - vlan300
              native_vlan: '400'
        state: rendered

    # Task Output
    # -----------
    #
    # "rendered": "<nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #     <nc:interface>
    #         <nc:name>ge-0/0/1</nc:name>
    #         <nc:unit>
    #             <nc:name>0</nc:name>
    #             <nc:family>
    #                 <nc:ethernet-switching>
    #                     <nc:interface-mode>access</nc:interface-mode>
    #                     <nc:vlan>
    #                         <nc:members>vlan100</nc:members>
    #                     </nc:vlan>
    #                 </nc:ethernet-switching>
    #             </nc:family>
    #         </nc:unit>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ge-0/0/2</nc:name>
    #         <nc:unit>
    #             <nc:name>0</nc:name>
    #             <nc:family>
    #                 <nc:ethernet-switching>
    #                     <nc:interface-mode>trunk</nc:interface-mode>
    #                     <nc:vlan>
    #                         <nc:members>vlan200</nc:members>
    #                         <nc:members>vlan300</nc:members>
    #                     </nc:vlan>
    #                 </nc:ethernet-switching>
    #             </nc:family>
    #         </nc:unit>
    #         <nc:native-vlan-id>400</nc:native-vlan-id>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:interfaces xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/1&lt;/nc:name&gt; &lt;nc:unit&gt; &lt;nc:name&gt;0&lt;/nc:name&gt; &lt;nc:family&gt; &lt;nc:ethernet-switching&gt; &lt;nc:interface-mode&gt;access&lt;/nc:interface-mode&gt; &lt;nc:vlan&gt; &lt;nc:members&gt;vlan100&lt;/nc:members&gt; &lt;/nc:vlan&gt; &lt;/nc:ethernet-switching&gt; &lt;/nc:family&gt; &lt;/nc:unit&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-0/0/2&lt;/nc:name&gt; &lt;nc:unit&gt; &lt;nc:name&gt;0&lt;/nc:name&gt; &lt;nc:family&gt; &lt;nc:ethernet-switching&gt; &lt;nc:interface-mode&gt;trunk&lt;/nc:interface-mode&gt; &lt;nc:vlan&gt; &lt;nc:members&gt;vlan200&lt;/nc:members&gt; &lt;nc:members&gt;vlan300&lt;/nc:members&gt; &lt;/nc:vlan&gt; &lt;/nc:ethernet-switching&gt; &lt;/nc:family&gt; &lt;/nc:unit&gt; &lt;nc:native-vlan-id&gt;400&lt;/nc:native-vlan-id&gt; &lt;/nc:interface&gt; &lt;/nc:interfaces&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
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
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
