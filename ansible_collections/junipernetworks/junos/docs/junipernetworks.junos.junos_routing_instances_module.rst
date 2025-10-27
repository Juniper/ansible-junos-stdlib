.. _junipernetworks.junos.junos_routing_instances_module:


*********************************************
junipernetworks.junos.junos_routing_instances
*********************************************

**Manage routing instances on Junos devices.**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage routing instances on Junos network devices.



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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The provided Routing instance configuration list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bridge_domains</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Bridge domain configuration.</div>
                        <div>This has been tested for junos MX204.</div>
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
                        <div>Specify domain description.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide the domain ID.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable_mac_move_action</b>
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
                        <div>Enable blocking action due to mac-move in this Bridge Domain.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mcae_mac_flush</b>
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
                        <div>Enable IRB MAC synchronization in this bridge domain</div>
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
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify the name of the bridge domain.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_irb_layer_2_copy</b>
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
                        <div>Disable transmission of layer-2 copy of packets of irb routing-interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_local_switching</b>
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
                        <div>Disable local switching within CE-facing interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>service_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify service id.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>IEEE 802.1q VLAN identifier for bridging domain (1..4094)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>connector_id_advertise</b>
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
                        <div>Advertise connector-id attribute.</div>
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
                        <div>Specify text description of routing instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>egress_protection</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Egress instance protection dictionary.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>context_identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify context identifier.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protector</b>
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
                        <div>Enable Edge Protector functionality for this VPN.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>instance_role</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>access</li>
                                    <li>nni</li>
                        </ul>
                </td>
                <td>
                        <div>Primary role of L2Backhaul-vpn router.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface name for this routing instance.</div>
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
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify name of the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protect_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify name of the protected interface.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>l2vpn_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Layer-2 vpn-id for this instance.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify routing instance name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_irb_layer_2_copy</b>
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
                        <div>Disable transmission of layer-2 copy of packets of irb routing-interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_local_switching</b>
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
                        <div>Disable vlan id normalization for interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_normalization</b>
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
                        <div>Disable vlan id normalization for interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_vrf_advertise</b>
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
                        <div>Disable vlan id normalization for interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_vrf_propagate_ttl</b>
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
                        <div>Disable TTL propagation from IP to MPLS (on push) and MPLS to IP (on pop).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>qualified_bum_pruning_mode</b>
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
                        <div>Enable BUM pruning for VPLS instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_distinguisher</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route distinguisher for this instance</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>routing_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Routing interface name for this routing-instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>evpn</li>
                                    <li>evpn-vpws</li>
                                    <li>forwarding</li>
                                    <li>l2backhaul-vpn</li>
                                    <li>l2vpn</li>
                                    <li>layer2-control</li>
                                    <li>mac-vrf</li>
                                    <li>mpls-forwarding</li>
                                    <li>mpls-internet-multicast</li>
                                    <li>no-forwarding</li>
                                    <li>virtual-router</li>
                                    <li>virtual-switch</li>
                                    <li>vpls</li>
                                    <li>vrf</li>
                        </ul>
                </td>
                <td>
                        <div>Specify instance type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_exports</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Export policy for VRF instance RIBs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_imports</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Import policy for VRF instance RIBs.</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show routing-instances</b>.</div>
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
                                    <li>parsed</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
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

    # Using merged
    #
    # Before state
    # ------------
    #
    # admin# show routing-instances
    #
    # [edit]
    # vagrant@vsrx# show policy-options
    # policy-statement test-policy {
    #     term t1 {
    #         then reject;
    #     }
    # }
    # policy-statement test-policy-1 {
    #     term t1 {
    #         then reject;
    #     }
    # }

    - name: Merge Junos BGP address family configuration
      junipernetworks.junos.junos_routing_instances:
        config:
          - name: "test"
            type: "vrf"
            route_distinguisher: "10.58.255.1:37"
            vrf_imports:
              - "test-policy"
            vrf_exports:
              - "test-policy"
              - "test-policy-1"
            interfaces:
              - name: "sp-0/0/0.0"
              - name: "gr-0/0/0.0"
            connector_id_advertise: true
          - name: "forwardinst"
            type: "forwarding"
            description: "Configured by Ansible Content Team"
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    # After state
    # -----------
    #
    # admin# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.58.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export [ test-policy test-policy-1 ];
    #     connector-id-advertise;
    # }
    #
    # Using gathered
    #
    # Before state
    # ------------
    #
    # admin# show routing-instances
    #
    # [edit]
    # admin# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.58.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export [ test-policy test-policy-1 ];
    #     connector-id-advertise;
    # }
    - name: Gather Junos routing-instances
      junipernetworks.junos.junos_routing_instances:
        state: gathered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "gathered": [
    #         {
    #             "description": "Configured by Ansible Content Team",
    #             "name": "forwardinst",
    #             "type": "forwarding"
    #         },
    #         {
    #             "connector_id_advertise": true,
    #             "interfaces": [
    #                 {
    #                     "name": "gr-0/0/0.0"
    #                 },
    #                 {
    #                     "name": "sp-0/0/0.0"
    #                 }
    #             ],
    #             "name": "test",
    #             "route_distinguisher": "10.58.255.1:37",
    #             "type": "vrf",
    #             "vrf_exports": [
    #                 "test-policy",
    #                 "test-policy-1"
    #             ],
    #             "vrf_imports": [
    #                 "test-policy"
    #             ]
    #         }
    #     ]
    #
    # Using replaced
    #
    # Before state
    # ------------
    #
    # admin# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.58.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export [ test-policy test-policy-1 ];
    #     connector-id-advertise;
    # }

    - name: Replace existing Junos routing instance config with provided config
      junipernetworks.junos.junos_routing_instances:
        config:
          address_family:
            - name: "test"
              type: "vrf"
              route_distinguisher: "10.57.255.1:37"
              vrf_imports:
                - "test-policy"
              vrf_exports:
                - "test-policy"
              interfaces:
                - name: "sp-0/0/0.0"
                - name: "gr-0/0/0.0"
              connector_id_advertise: false
              description: "Configured by Ansible Content Team"
        state: replaced

    # After state
    # -----------
    #
    # admin@vsrx# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     description "Configured by Ansible Content Team";
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.57.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export test-policy;
    # }

    # Using overridden
    #
    # Before state
    # ------------
    #
    # admin@vsrx# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     description "Configured by Ansible Content Team";
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.57.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export test-policy;
    # }

    - name: Override Junos routing-instances configuration
      junipernetworks.junos.junos_routing_instances:
        config:
          - name: "test"
            type: "vrf"
            route_distinguisher: "10.58.255.1:37"
            vrf_imports:
              - "test-policy"
            vrf_exports:
              - "test-policy"
              - "test-policy-1"
            interfaces:
              - name: "sp-0/0/0.0"
              - name: "gr-0/0/0.0"
            connector_id_advertise: true
          - name: "forwardinst"
            type: "forwarding"
            description: "Configured by Ansible Content Team"
          - name: "vtest1"
            type: "virtual-router"
        state: overridden

    # After state
    # -----------
    #
    # admin@vsrx# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.58.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export [ test-policy test-policy-1 ];
    #     connector-id-advertise;
    # }
    # vtest1 {
    #     instance-type virtual-router;
    # }


    # Using deleted
    #
    # Before state
    # ------------
    #
    # admin@vsrx# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.58.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export [ test-policy test-policy-1 ];
    #     connector-id-advertise;
    # }

    - name: Delete provided junos routing-instamce
      junipernetworks.junos.junos_routing_instances:
        config:
          - name: "test"
        state: deleted

    # After state
    # -----------
    #
    # admin@vsrx# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }

    # Using deleted without config
    #
    # Before state
    # ------------
    #
    # admin@vsrx# show routing-instances
    # forwardinst {
    #     description "Configured by Ansible Content Team";
    #     instance-type forwarding;
    # }
    # test {
    #     instance-type vrf;
    #     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
    #     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
    #     route-distinguisher 10.58.255.1:37;
    #     vrf-import test-policy;
    #     vrf-export [ test-policy test-policy-1 ];
    #     connector-id-advertise;
    # }
    # vtest1 {
    #     instance-type virtual-router;
    # }

    - name: Delete complete Junos routing-instances config
      junipernetworks.junos.junos_routing_instances:
        config:
        state: deleted

    # After state
    # -----------
    #
    # admin@vsrx# show routing-instances
    #
    # [edit]

    - name: Gather Junos BGP address family config
      junipernetworks.junos.junos_routing_instances:
        config:
        state: gathered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "gathered": {
    #         "address_family": [
    #             {
    #                 "af_type": [
    #                     {
    #                         "accepted_prefix_limit": {
    #                             "idle_timeout_value": 2001,
    #                             "limit_threshold": 98,
    #                             "maximum": 20
    #                         },
    #                         "damping": true,
    #                         "defer_initial_multipath_build": {
    #                             "maximum_delay": 2
    #                         },
    #                         "type": "signaling"
    #                     }
    #                 ],
    #                 "afi": "evpn"
    #             },
    #             {
    #                 "af_type": [
    #                     {
    #                         "accepted_prefix_limit": {
    #                             "idle_timeout_value": 2000,
    #                             "limit_threshold": 99,
    #                             "maximum": 20
    #                         },
    #                         "damping": true,
    #                         "defer_initial_multipath_build": {
    #                             "maximum_delay": 2
    #                         },
    #                         "delay_route_advertisements": {
    #                             "max_delay_route_age": 20,
    #                             "max_delay_routing_uptime": 32000,
    #                             "min_delay_inbound_convergence": 32000,
    #                             "min_delay_routing_uptime": 23000
    #                         },
    #                         "graceful_restart_forwarding_state_bit": "from-fib",
    #                         "type": "any"
    #                     },
    #                     {
    #                         "legacy_redirect_ip_action": {
    #                             "receive": true,
    #                             "send": true
    #                         },
    #                         "loops": 4,
    #                         "no_install": true,
    #                         "output_queue_priority_expedited": true,
    #                         "secondary_independent_resolution": true,
    #                         "type": "flow"
    #                     },
    #                     {
    #                         "entropy_label": {
    #                             "no_next_hop_validation": true
    #                         },
    #                         "explicit_null": {
    #                             "connected_only": true
    #                         },
    #                         "per_group_label": true,
    #                         "per_prefix_label": true,
    #                         "prefix_limit": {
    #                             "forever": true,
    #                             "limit_threshold": 99,
    #                             "maximum": 20
    #                         },
    #                         "resolve_vpn": true,
    #                         "rib": "inet.3",
    #                         "route_refresh_priority_priority": 3,
    #                         "type": "labeled-unicast"
    #                     },
    #                     {
    #                         "extended_nexthop": true,
    #                         "extended_nexthop_color": true,
    #                         "local_ipv4_address": "9.9.9.9",
    #                         "type": "unicast"
    #                     }
    #                 ],
    #                 "afi": "inet"
    #             }
    #         ]
    #     }
    #
    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <routing-instances>
    #             <instance>
    #                 <name>forwardinst</name>
    #                 <description>Configured by Ansible Content Team</description>
    #                 <instance-type>forwarding</instance-type>
    #             </instance>
    #             <instance>
    #                 <name>test</name>
    #                 <instance-type>vrf</instance-type>
    #                 <interface>
    #                     <name>gr-0/0/0.0</name>
    #                 </interface>
    #                 <interface>
    #                     <name>sp-0/0/0.0</name>
    #                 </interface>
    #                 <route-distinguisher>
    #                     <rd-type>10.58.255.1:37</rd-type>
    #                 </route-distinguisher>
    #                 <vrf-import>test-policy</vrf-import>
    #                 <vrf-export>test-policy</vrf-export>
    #                 <vrf-export>test-policy-1</vrf-export>
    #                 <connector-id-advertise/>
    #             </instance>
    #         </routing-instances>
    #     </configuration>
    # </rpc-reply>

    - name: Parse routing instance running config
      junipernetworks.junos.junos_routing_instances:
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
    #             "description": "Configured by Ansible Content Team",
    #             "name": "forwardinst",
    #             "type": "forwarding"
    #         },
    #         {
    #             "connector_id_advertise": true,
    #             "interfaces": [
    #                 {
    #                     "name": "gr-0/0/0.0"
    #                 },
    #                 {
    #                     "name": "sp-0/0/0.0"
    #                 }
    #             ],
    #             "name": "test",
    #             "route_distinguisher": "10.58.255.1:37",
    #             "type": "vrf",
    #             "vrf_exports": [
    #                 "test-policy",
    #                 "test-policy-1"
    #             ],
    #             "vrf_imports": [
    #                 "test-policy"
    #             ]
    #         }
    #     ]
    #
    #
    # Using rendered
    #
    #
    - name: Render the xml for provided  configuration
      junipernetworks.junos.junos_routing_instances:
        config:
          - name: "test"
            type: "vrf"
            route_distinguisher: "10.58.255.1:37"
            vrf_imports:
              - "test-policy"
            vrf_exports:
              - "test-policy"
              - "test-policy-1"
            interfaces:
              - name: "sp-0/0/0.0"
              - name: "gr-0/0/0.0"
            connector_id_advertise: true
          - name: "forwardinst"
            type: "forwarding"
            description: "Configured by Ansible Content Team"
        state: rendered

    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "rendered": "<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # <nc:instance><nc:name>test</nc:name><nc:connector-id-advertise/><nc:instance-type>vrf</nc:instance-type>
    # <nc:interface><nc:name>sp-0/0/0.0</nc:name></nc:interface><nc:interface><nc:name>gr-0/0/0.0</nc:name></nc:interface>
    # <nc:route-distinguisher><nc:rd-type>10.58.255.1:37</nc:rd-type></nc:route-distinguisher>
    # <nc:vrf-import>test-policy</nc:vrf-import><nc:vrf-export>test-policy</nc:vrf-export>
    # <nc:vrf-export>test-policy-1</nc:vrf-export></nc:instance>
    # <nc:instance><nc:name>forwardinst</nc:name><nc:description>Configured by Ansible Content Team</nc:description>
    # <nc:instance-type>forwarding</nc:instance-type></nc:instance></nc:routing-instances>"



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
                      <span style="color: purple">list</span>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:routing-instances xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:instance&gt; &lt;nc:name&gt;test&lt;/nc:name&gt; &lt;nc:connector-id-advertise/&gt; &lt;nc:instance-type&gt;vrf&lt;/nc:instance-type&gt; &lt;nc:interface&gt; &lt;nc:name&gt;sp-0/0/0.0&lt;/nc:name&gt; &lt;/nc:interface&gt; &lt;nc:interface&gt; &lt;nc:name&gt;gr-0/0/0.0&lt;/nc:name&gt; &lt;/nc:interface&gt; &lt;nc:route-distinguisher&gt; &lt;nc:rd-type&gt;10.58.255.1:37&lt;/nc:rd-type&gt; &lt;/nc:route-distinguisher&gt; &lt;nc:vrf-import&gt;test-policy&lt;/nc:vrf-import&gt; &lt;nc:vrf-export&gt;test-policy&lt;/nc:vrf-export&gt; &lt;nc:vrf-export&gt;test-policy-1&lt;/nc:vrf-export&gt; &lt;/nc:instance&gt; &lt;/routing-instances&gt; &lt;/configuration&gt; &lt;/rpc-reply&gt;&#x27;, &#x27;xml2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
