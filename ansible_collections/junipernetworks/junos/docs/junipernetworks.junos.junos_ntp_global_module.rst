.. _junipernetworks.junos.junos_ntp_global_module:


**************************************
junipernetworks.junos.junos_ntp_global
**************************************

**Manage NTP configuration on Junos devices.**


Version added: 2.6.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages NTP configuration on devices running Junos.



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
                        <div>A dictionary of NTP configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP authentication key.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>md5</li>
                                    <li>sha1</li>
                                    <li>sha256</li>
                        </ul>
                </td>
                <td>
                        <div>Authentication key type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Authentication key number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Authentication key value.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>boot_server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Server to query during boot sequence.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcast_client</b>
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
                        <div>Listen to broadcast NTP.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcasts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Broadcast parameters.</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Broadcast or multicast address to use.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Authentication key.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>routing_instance_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Routing intance name in which interface has address in broadcast subnet.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ttl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>TTL value to transmit.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP version to use.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval_range</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set the minpoll and maxpoll interval range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multicast_client</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Listen to multicast NTP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP Peers.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Key-id to be used while communicating.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hostname/IP address of the NTP Peer.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefer</b>
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
                        <div>Prefer this peer.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP version to use.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP Servers.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Key-id to be used while communicating.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefer</b>
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
                        <div>Prefer this peer_serv.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>routing_instance</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Routing instance through which server is reachable.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address or hostname of the server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP version to use.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source-Address parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>routing_instance</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Routing intance name in which source address is defined.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use specified address as source address.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set the maximum threshold(sec) allowed for NTP adjustment.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>accept</li>
                                    <li>reject</li>
                        </ul>
                </td>
                <td>
                        <div>Select actions for NTP abnormal adjustment.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The maximum value(sec) allowed for NTP adjustment.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trusted_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of trusted authentication keys.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Trusted-Key number.</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show system syslog</b>.</div>
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
                        <div>The states <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
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
    # vagrant@vsrx# show system ntp
    #
    # [edit]
    # vagrant@vsrx# show routing-instances
    # rt1 {
    #     description rt1;
    # }
    # rt2 {
    - name: Merge provided NTP configuration into running configuration.
      junipernetworks.junos.junos_ntp_global:
        config:
          boot_server: '78.46.194.186'
          broadcasts:
            - address: '172.16.255.255'
              key: '50'
              ttl: 200
              version: 3
              routing_instance_name: 'rt1'
            - address: '192.16.255.255'
              key: '50'
              ttl: 200
              version: 3
              routing_instance_name: 'rt2'
          broadcast_client: true
          interval_range: 2
          multicast_client: "224.0.0.1"
          peers:
            - peer: "78.44.194.186"
            - peer: "172.44.194.186"
              key_id: 10000
              prefer: true
              version: 3
          servers:
            - server: "48.46.194.186"
              key_id: 34
              prefer: true
              version: 2
              routing_instance: 'rt1'
            - server: "48.45.194.186"
              key_id: 34
              prefer: true
              version: 2
          source_addresses:
            - source_address: "172.45.194.186"
              routing_instance: 'rt1'
            - source_address: "171.45.194.186"
              routing_instance: 'rt2'
          threshold:
            value: 300
            action: "accept"
          trusted_keys:
            - key_id: 3000
            - key_id: 2000
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "boot_server": "78.46.194.186",
    #         "broadcast_client": true,
    #         "broadcasts": [
    #             {
    #                 "address": "172.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt1",
    #                 "ttl": 200,
    #                 "version": 3
    #             },
    #             {
    #                 "address": "192.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt2",
    #                 "ttl": 200,
    #                 "version": 3
    #             }
    #         ],
    #         "interval_range": 2,
    #         "multicast_client": "224.0.0.1",
    #         "peers": [
    #             {
    #                 "peer": "78.44.194.186"
    #             },
    #             {
    #                 "key_id": 10000,
    #                 "peer": "172.44.194.186",
    #                 "prefer": true,
    #                 "version": 3
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "routing_instance": "rt1",
    #                 "server": "48.46.194.186",
    #                 "version": 2
    #             },
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "server": "48.45.194.186",
    #                 "version": 2
    #             }
    #         ],
    #         "source_addresses": [
    #             {
    #                 "routing_instance": "rt1",
    #                 "source_address": "172.45.194.186"
    #             },
    #             {
    #                 "routing_instance": "rt2",
    #                 "source_address": "171.45.194.186"
    #             }
    #         ],
    #         "threshold": {
    #             "action": "accept",
    #             "value": 300
    #         },
    #         "trusted_keys": [
    #             {"key_id": 2000},
    #             {"key_id": 3000}
    #         ]
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #           "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server><nc:broadcast>"
    #           "<nc:name>172.16.255.255</nc:name><nc:key>50</nc:key><nc:routing-instance-name>rt1</nc:routing-instance-name>"
    #           "<nc:ttl>200</nc:ttl><nc:version>3</nc:version></nc:broadcast><nc:broadcast><nc:name>192.16.255.255</nc:name>"
    #           "<nc:key>50</nc:key><nc:routing-instance-name>rt2</nc:routing-instance-name><nc:ttl>200</nc:ttl>"
    #           "<nc:version>3</nc:version></nc:broadcast><nc:broadcast-client/><nc:interval-range>2</nc:interval-range>"
    #           "<nc:multicast-client>224.0.0.1</nc:multicast-client><nc:peer><nc:name>78.44.194.186</nc:name></nc:peer>"
    #           "<nc:peer><nc:name>172.44.194.186</nc:name><nc:key>10000</nc:key><nc:prefer/><nc:version>3</nc:version>"
    #           "</nc:peer><nc:server><nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>"
    #           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name><nc:key>34</nc:key>"
    #           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:source-address><nc:name>172.45.194.186</nc:name>"
    #           "<nc:routing-instance>rt1</nc:routing-instance></nc:source-address><nc:source-address>"
    #           "<nc:name>171.45.194.186</nc:name><nc:routing-instance>rt2</nc:routing-instance></nc:source-address>"
    #           "<nc:threshold><nc:value>300</nc:value><nc:action>accept</nc:action></nc:threshold>"
    #           "<nc:trusted-key>3000</nc:trusted-key><nc:trusted-key>2000</nc:trusted-key></nc:ntp></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system ntp
    # boot-server 78.46.194.186;
    # interval-range 2;
    # peer 78.44.194.186;
    # peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
    # server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
    # server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
    # broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
    # broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
    # broadcast-client;
    # multicast-client 224.0.0.1;
    # trusted-key [ 3000 2000 ];
    # threshold 300 action accept;
    # source-address 172.45.194.186 routing-instance rt1;
    # source-address 171.45.194.186 routing-instance rt2;
    #
    #
    # Using Replaced
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system ntp
    # boot-server 78.46.194.186;
    # interval-range 2;
    # peer 78.44.194.186;
    # peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
    # server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
    # server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
    # broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
    # broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
    # broadcast-client;
    # multicast-client 224.0.0.1;
    # trusted-key [ 3000 2000 ];
    # threshold 300 action accept;
    # source-address 172.45.194.186 routing-instance rt1;
    # source-address 171.45.194.186 routing-instance rt2;

    - name: Replaced running ntp global configuration with provided configuration
      junipernetworks.junos.junos_ntp_global:
        config:
          authentication_keys:
            - id: 2
              algorithm: 'md5'
              key: 'asdfghd'
            - id: 5
              algorithm: 'sha1'
              key: 'aasdad'
          servers:
            - server: "48.46.194.186"
              key_id: 34
              prefer: true
              version: 2
              routing_instance: 'rt1'
            - server: "48.45.194.186"
              key_id: 34
              prefer: true
              version: 2
        state: replaced
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "md5",
    #                 "id": 2,
    #                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
    #             },
    #             {
    #                 "algorithm": "sha1",
    #                 "id": 5,
    #                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "routing_instance": "rt1",
    #                 "server": "48.46.194.186",
    #                 "version": 2
    #             },
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "server": "48.45.194.186",
    #                 "version": 2
    #             }
    #         ]
    #     },
    #     "before": {
    #         "boot_server": "78.46.194.186",
    #         "broadcast_client": true,
    #         "broadcasts": [
    #             {
    #                 "address": "172.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt1",
    #                 "ttl": 200,
    #                 "version": 3
    #             },
    #             {
    #                 "address": "192.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt2",
    #                 "ttl": 200,
    #                 "version": 3
    #             }
    #         ],
    #         "interval_range": 2,
    #         "multicast_client": "224.0.0.1",
    #         "peers": [
    #             {
    #                 "peer": "78.44.194.186"
    #             },
    #             {
    #                 "key_id": 10000,
    #                 "peer": "172.44.194.186",
    #                 "prefer": true,
    #                 "version": 3
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "routing_instance": "rt1",
    #                 "server": "48.46.194.186",
    #                 "version": 2
    #             },
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "server": "48.45.194.186",
    #                 "version": 2
    #             }
    #         ],
    #         "source_addresses": [
    #             {
    #                 "routing_instance": "rt1",
    #                 "source_address": "172.45.194.186"
    #             },
    #             {
    #                 "routing_instance": "rt2",
    #                 "source_address": "171.45.194.186"
    #             }
    #         ],
    #         "threshold": {
    #             "action": "accept",
    #             "value": 300
    #         },
    #         "trusted_keys": [
    #             {"key_id": 2000},
    #             {"key_id": 3000}
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #             "<nc:ntp delete="delete"/><nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type>
    #             "<nc:value>asdfghd</nc:value></nc:authentication-key><nc:authentication-key><nc:name>5</nc:name>
    #             "<nc:type>sha1</nc:type><nc:value>aasdad</nc:value></nc:authentication-key><nc:server>
    #             "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>
    #             "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>
    #             "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server></nc:ntp></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system ntp
    # authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
    # authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
    # server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
    # server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA

    # Using overridden
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system ntp
    # boot-server 78.46.194.186;
    # interval-range 2;
    # peer 78.44.194.186;
    # peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
    # server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
    # server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
    # broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
    # broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
    # broadcast-client;
    # multicast-client 224.0.0.1;
    # trusted-key [ 3000 2000 ];
    # threshold 300 action accept;
    # source-address 172.45.194.186 routing-instance rt1;
    # source-address 171.45.194.186 routing-instance rt2;

    - name: Override running ntp global configuration with provided configuration
      junipernetworks.junos.junos_ntp_global:
        config:
          authentication_keys:
            - id: 2
              algorithm: 'md5'
              key: 'asdfghd'
            - id: 5
              algorithm: 'sha1'
              key: 'aasdad'
          servers:
            - server: "48.46.194.186"
              key_id: 34
              prefer: true
              version: 2
              routing_instance: 'rt1'
            - server: "48.45.194.186"
              key_id: 34
              prefer: true
              version: 2
        state: overridden
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "md5",
    #                 "id": 2,
    #                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
    #             },
    #             {
    #                 "algorithm": "sha1",
    #                 "id": 5,
    #                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "routing_instance": "rt1",
    #                 "server": "48.46.194.186",
    #                 "version": 2
    #             },
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "server": "48.45.194.186",
    #                 "version": 2
    #             }
    #         ]
    #     },
    #     "before": {
    #         "boot_server": "78.46.194.186",
    #         "broadcast_client": true,
    #         "broadcasts": [
    #             {
    #                 "address": "172.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt1",
    #                 "ttl": 200,
    #                 "version": 3
    #             },
    #             {
    #                 "address": "192.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt2",
    #                 "ttl": 200,
    #                 "version": 3
    #             }
    #         ],
    #         "interval_range": 2,
    #         "multicast_client": "224.0.0.1",
    #         "peers": [
    #             {
    #                 "peer": "78.44.194.186"
    #             },
    #             {
    #                 "key_id": 10000,
    #                 "peer": "172.44.194.186",
    #                 "prefer": true,
    #                 "version": 3
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "routing_instance": "rt1",
    #                 "server": "48.46.194.186",
    #                 "version": 2
    #             },
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "server": "48.45.194.186",
    #                 "version": 2
    #             }
    #         ],
    #         "source_addresses": [
    #             {
    #                 "routing_instance": "rt1",
    #                 "source_address": "172.45.194.186"
    #             },
    #             {
    #                 "routing_instance": "rt2",
    #                 "source_address": "171.45.194.186"
    #             }
    #         ],
    #         "threshold": {
    #             "action": "accept",
    #             "value": 300
    #         },
    #         "trusted_keys": [
    #             {"key_id": 2000},
    #             {"key_id": 3000}
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #             "<nc:ntp delete="delete"/><nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type>
    #             "<nc:value>asdfghd</nc:value></nc:authentication-key><nc:authentication-key><nc:name>5</nc:name>
    #             "<nc:type>sha1</nc:type><nc:value>aasdad</nc:value></nc:authentication-key><nc:server>
    #             "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>
    #             "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>
    #             "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server></nc:ntp></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system ntp
    # authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
    # authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
    # server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
    # server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
    #
    # Using deleted
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system ntp
    # authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
    # authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
    # server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
    # server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
    #
    - name: Delete running NTP global configuration
      junipernetworks.junos.junos_ntp_global:
        config:
        state: deleted
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {},
    #     "before": {
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "md5",
    #                 "id": 2,
    #                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
    #             },
    #             {
    #                 "algorithm": "sha1",
    #                 "id": 5,
    #                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "routing_instance": "rt1",
    #                 "server": "48.46.194.186",
    #                 "version": 2
    #             },
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "server": "48.45.194.186",
    #                 "version": 2
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #               "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #               "<nc:ntp delete="delete"/></nc:system>"
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
    # vagrant@vsrx# show system ntp
    # boot-server 78.46.194.186;
    # interval-range 2;
    # peer 78.44.194.186;
    # peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
    # server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
    # server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
    # broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
    # broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
    # broadcast-client;
    # multicast-client 224.0.0.1;
    # trusted-key [ 3000 2000 ];
    # threshold 300 action accept;
    # source-address 172.45.194.186 routing-instance rt1;
    # source-address 171.45.194.186 routing-instance rt2;
    - name: Gather running NTP global configuration
      junipernetworks.junos.junos_ntp_global:
        state: gathered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "gathered": {
    #         "boot_server": "78.46.194.186",
    #         "broadcast_client": true,
    #         "broadcasts": [
    #             {
    #                 "address": "172.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt1",
    #                 "ttl": 200,
    #                 "version": 3
    #             },
    #             {
    #                 "address": "192.16.255.255",
    #                 "key": "50",
    #                 "routing_instance_name": "rt2",
    #                 "ttl": 200,
    #                 "version": 3
    #             }
    #         ],
    #         "interval_range": 2,
    #         "multicast_client": "224.0.0.1",
    #         "peers": [
    #             {
    #                 "peer": "78.44.194.186"
    #             },
    #             {
    #                 "key_id": 10000,
    #                 "peer": "172.44.194.186",
    #                 "prefer": true,
    #                 "version": 3
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "routing_instance": "rt1",
    #                 "server": "48.46.194.186",
    #                 "version": 2
    #             },
    #             {
    #                 "key_id": 34,
    #                 "prefer": true,
    #                 "server": "48.45.194.186",
    #                 "version": 2
    #             }
    #         ],
    #         "source_addresses": [
    #             {
    #                 "routing_instance": "rt1",
    #                 "source_address": "172.45.194.186"
    #             },
    #             {
    #                 "routing_instance": "rt2",
    #                 "source_address": "171.45.194.186"
    #             }
    #         ],
    #         "threshold": {
    #             "action": "accept",
    #             "value": 300
    #         },
    #         "trusted_keys": [
    #             {"key_id": 2000},
    #             {"key_id": 3000}
    #         ]
    #     },
    #     "changed": false,
    # Using rendered
    #
    # Before state
    # ------------
    #
    - name: Render xml for provided facts.
      junipernetworks.junos.junos_ntp_global:
        config:
          boot_server: '78.46.194.186'
          broadcasts:
            - address: '172.16.255.255'
              key: '50'
              ttl: 200
              version: 3
              routing_instance_name: 'rt1'
            - address: '192.16.255.255'
              key: '50'
              ttl: 200
              version: 3
              routing_instance_name: 'rt2'
          broadcast_client: true
          interval_range: 2
          multicast_client: "224.0.0.1"
          peers:
            - peer: "78.44.194.186"
            - peer: "172.44.194.186"
              key_id: 10000
              prefer: true
              version: 3
          servers:
            - server: "48.46.194.186"
              key_id: 34
              prefer: true
              version: 2
              routing_instance: 'rt1'
            - server: "48.45.194.186"
              key_id: 34
              prefer: true
              version: 2
          source_addresses:
            - source_address: "172.45.194.186"
              routing_instance: 'rt1'
            - source_address: "171.45.194.186"
              routing_instance: 'rt2'
          threshold:
            value: 300
            action: "accept"
          trusted_keys:
            - 3000
            - 2000
        state: rendered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "rendered": [
    #           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #           "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server><nc:broadcast><nc:name>172.16.255.255</nc:name>"
    #           "<nc:key>50</nc:key><nc:routing-instance-name>rt1</nc:routing-instance-name><nc:ttl>200</nc:ttl>"
    #           "<nc:version>3</nc:version></nc:broadcast><nc:broadcast><nc:name>192.16.255.255</nc:name>"
    #           "<nc:key>50</nc:key><nc:routing-instance-name>rt2</nc:routing-instance-name>"
    #           "<nc:ttl>200</nc:ttl><nc:version>3</nc:version></nc:broadcast><nc:broadcast-client/>"
    #           "<nc:interval-range>2</nc:interval-range><nc:multicast-client>224.0.0.1</nc:multicast-client><nc:peer>"
    #           "<nc:name>78.44.194.186</nc:name></nc:peer><nc:peer><nc:name>172.44.194.186</nc:name>"
    #           "<nc:key>10000</nc:key><nc:prefer/><nc:version>3</nc:version></nc:peer><nc:server>"
    #           "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>"
    #           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>"
    #           "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server><nc:source-address>"
    #           "<nc:name>172.45.194.186</nc:name><nc:routing-instance>rt1</nc:routing-instance></nc:source-address>"
    #           "<nc:source-address><nc:name>171.45.194.186</nc:name><nc:routing-instance>rt2</nc:routing-instance>"
    #           "</nc:source-address><nc:threshold><nc:value>300</nc:value><nc:action>accept</nc:action></nc:threshold>"
    #           "<nc:trusted-key>3000</nc:trusted-key><nc:trusted-key>2000</nc:trusted-key></nc:ntp></nc:system>"
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
    #            <ntp>
    #               <authentication-key>
    #                  <name>2</name>
    #                  <type>md5</type>
    #                  <value>$9$GxDjqfT3CA0UjfzF6u0RhS</value>
    #               </authentication-key>
    #               <authentication-key>
    #                  <name>5</name>
    #                  <type>sha1</type>
    #                  <value>$9$ZsUDk.mT3/toJGiHqQz</value>
    #               </authentication-key>
    #           </ntp>
    #     </system>
    #     </configuration>
    # </rpc-reply>
    #
    - name: Parse NTP global running config
      junipernetworks.junos.junos_ntp_global:
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
    #         "authentication_keys": [
    #             {
    #                 "algorithm": "md5",
    #                 "id": 2,
    #                 "key": "$9$GxDjqfT3CA0UjfzF6u0RhS"
    #             },
    #             {
    #                 "algorithm": "sha1",
    #                 "id": 5,
    #                 "key": "$9$ZsUDk.mT3/toJGiHqQz"
    #             }
    #         ]
    #     }
    #
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:name&gt;78.44.194.186&lt;/nc:name&gt;&lt;/nc:peer&gt;&lt;nc:peer&gt;&lt;nc:name&gt;172.44.194.186&lt;/nc:name&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
