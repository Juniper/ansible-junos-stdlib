.. _junipernetworks.junos.junos_acl_interfaces_module:


******************************************
junipernetworks.junos.junos_acl_interfaces
******************************************

**ACL interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages adding and removing Access Control Lists (ACLs) from interfaces on devices running Juniper JUNOS.



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
                        <div>A dictionary of ACL options for interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies ACLs attached to the interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acls</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the ACLs for the provided AFI.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>in</li>
                                    <li>out</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the direction of packets that the ACL will be applied on.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specifies the name of the IPv4/IPv4 ACL for the interface.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the AFI for the ACL(s) to be configured on this interface.</div>
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
                        <div>Name/Identifier for the interface.</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show interfaces</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result</div>
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
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module requires the netconf system service be enabled on the device being managed.
   - This module works with connection ``netconf``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.
   - Tested against JunOS v18.4R1



Examples
--------

.. code-block:: yaml

    # Using deleted

    # Before state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface with filter";
    #     unit 0 {
    #         family inet {
    #             filter {
    #                 input inbound_acl;
    #                 output outbound_acl;
    #             }
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }

    - name: Delete JUNOS L3 interface filter
      junipernetworks.junos.junos_acl_interfaces:
        config:
          - name: ge-1/0/0
            access_groups:
              - afi: ipv4
                acls:
                  - name: inbound_acl
                    direction: in
                  - name: outbound_acl
                    direction: out
        state: deleted

    # After state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface with filter";
    #     unit 0 {
    #         family inet {
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }


    # Using merged

    # Before state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface without filter";
    #     unit 0 {
    #         family inet {
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }

    - name: Merge JUNOS L3 interface filter
      junipernetworks.junos.junos_acl_interfaces:
        config:
          - name: ge-1/0/0
            access_groups:
              - afi: ipv4
                acls:
                  - name: inbound_acl
                    direction: in
                  - name: outbound_acl
                    direction: out
        state: merged

    # After state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface with filter";
    #     unit 0 {
    #         family inet {
    #             filter {
    #                 input inbound_acl;
    #                 output outbound_acl;
    #             }
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }


    # Using overridden

    # Before state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface without filter";
    #     unit 0 {
    #         family inet {
    #             filter {
    #                 input foo_acl;
    #             }
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }

    - name: Override JUNOS L3 interface filter
      junipernetworks.junos.junos_acl_interfaces:
        config:
          - name: ge-1/0/0
            access_groups:
              - afi: ipv4
                acls:
                  - name: inbound_acl
                    direction: in
                  - name: outbound_acl
                    direction: out
        state: overridden

    # After state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface with filter";
    #     unit 0 {
    #         family inet {
    #             filter {
    #                 input inbound_acl;
    #                 output outbound_acl;
    #             }
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }


    # Using replaced

    # Before state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface without filter";
    #     unit 0 {
    #         family inet {
    #             filter {
    #                 input foo_acl;
    #                 output outbound_acl;
    #             }
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }

    - name: Replace JUNOS L3 interface filter
      junipernetworks.junos.junos_acl_interfaces:
        config:
          - name: ge-1/0/0
            access_groups:
              - afi: ipv4
                acls:
                  - name: inbound_acl
                    direction: in
        state: replaced

    # After state:
    # -------------
    #
    # admin# show interfaces
    # ge-1/0/0 {
    #     description "L3 interface with filter";
    #     unit 0 {
    #         family inet {
    #             filter {
    #                 input inbound_acl;
    #                 output outbound_acl;
    #             }
    #             address 100.64.0.1/10;
    #             address 100.64.0.2/10;
    #         }
    #         family inet6;
    #     }



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;command 1&#x27;, &#x27;command 2&#x27;, &#x27;command 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Daniel Mellado (@dmellado)
