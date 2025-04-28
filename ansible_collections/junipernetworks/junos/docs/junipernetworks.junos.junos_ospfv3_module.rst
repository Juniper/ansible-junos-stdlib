.. _junipernetworks.junos.junos_ospfv3_module:


**********************************
junipernetworks.junos.junos_ospfv3
**********************************

**OSPFv3 resource module**


Version added: 1.2.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages global OSPFv3 configuration on devices running Juniper JUNOS.



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
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
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
                        <div>A list of OSPFv3 process configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>areas</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of OSPFv3 areas&#x27; configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>area_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The Area ID as an integer or IP Address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>area_range</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure an address range for the area.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>List of interfaces in this area.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify authentication type</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Type of authentication to use.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bandwidth_based_metrics</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify list of bandwidth based metrics</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bandwidth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>1g</li>
                                    <li>10g</li>
                        </ul>
                </td>
                <td>
                        <div>BW to apply metric to.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify metric</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>flood_reduction</b>
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
                        <div>Enable flood reduction.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Metric applied to the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Name of the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive</b>
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
                        <div>Specify passive</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Priority for the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify timers</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dead_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Dead interval (seconds).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hello_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hello interval (seconds).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>poll_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Poll interval (seconds).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retransmit_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Retransmit interval (seconds).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transit_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Transit delay (seconds).</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stub</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Settings for configuring the area as a stub.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Metric for the default route in this area.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>set</b>
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
                        <div>Configure the area as a stub.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Preference of external routes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>overload</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify time for overload mode reset</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time after which overload mode is reset (seconds).</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Preference of internal routes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_export_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum number of external prefixes that can be exported.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>reference_bandwidth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>1g</li>
                                    <li>10g</li>
                        </ul>
                </td>
                <td>
                        <div>Bandwidth for calculating metric defaults.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rfc1583compatibility</b>
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
                        <div>Set RFC1583 compatibility</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>The OSPFv3 router id.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>spf_options</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure options for SPF.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time to wait before running an SPF (seconds).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>holddown</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time to hold down before running an SPF (seconds).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rapid_runs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of maximum rapid SPF runs before holddown (seconds).</div>
                </td>
            </tr>


            <tr>
                <td colspan="5">
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show protocols ospf</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result</div>
                </td>
            </tr>
            <tr>
                <td colspan="5">
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

    # Using merged
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf3

    - name: Merge Junos OSPFv3 config
      junipernetworks.junos.junos_ospfv3:
        config:
          - router_id: 10.200.16.75
            areas:
              - area_id: 0.0.0.100
                interfaces:
                  - metric: 5
                    name: so-0/0/0.0
                    priority: 3
                  - metric: 6
                    name: so-0/0/1.0
                    priority: 2
                stub:
                  default_metric: 200
                  set: true
        state: merged

    # Task Output:
    # ------------
    #
    # before: []
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf3><nc:area><nc:name>0.0.0.100</nc:name><nc:interface><nc:name>so-0/0/0.0</nc:name>
    #   <nc:priority>3</nc:priority><nc:metric>5</nc:metric></nc:interface><nc:interface>
    #   <nc:name>so-0/0/1.0</nc:name><nc:priority>2</nc:priority><nc:metric>6</nc:metric>
    #   </nc:interface><nc:stub><nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf3></nc:protocols>
    # - <nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:router-id>10.200.16.75</nc:router-id></nc:routing-options>
    #
    # after:
    # - areas:
    #     - area_id: 0.0.0.100
    #       interfaces:
    #       - metric: 5
    #         name: so-0/0/0.0
    #         priority: 3
    #       - metric: 6
    #         name: so-0/0/1.0
    #         priority: 2
    #       stub:
    #         default_metric: 200
    #         set: true
    #     router_id: 10.200.16.75

    # After state
    # -----------
    #
    # admin# show protocols ospf3
    # area 0.0.0.100 {
    #     stub default-metric 200;
    #     interface so-0/0/0.0 {
    #         metric 5;
    #         priority 3;
    #     }
    #     interface so-0/0/1.0 {
    #         metric 6;
    #         priority 2;
    #     }
    # }
    #
    # Using replaced
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf3
    # admin# show protocols ospf3
    # area 0.0.0.100 {
    #     stub default-metric 200;
    #     interface so-0/0/0.0 {
    #         metric 5;
    #         priority 3;
    #     }
    #     interface so-0/0/1.0 {
    #         metric 6;
    #         priority 2;
    #     }
    # }

    - name: Replace existing Junos OSPFv3 config with provided config
      junipernetworks.junos.junos_ospfv3:
        config:
          - router_id: 10.200.16.75
            areas:
              - area_id: 0.0.0.100
                interfaces:
                  - name: so-0/0/0.0
        state: replaced

    # Task Output:
    # ------------
    #
    # before:
    # - areas:
    #     - area_id: 0.0.0.100
    #       interfaces:
    #       - metric: 5
    #         name: so-0/0/0.0
    #         priority: 3
    #       - metric: 6
    #         name: so-0/0/1.0
    #         priority: 2
    #       stub:
    #         default_metric: 200
    #         set: true
    #     router_id: 10.200.16.75
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf3><nc:area><nc:name>0.0.0.100</nc:name><nc:interface delete="delete">
    #   <nc:name>so-0/0/0.0</nc:name></nc:interface></nc:area></nc:ospf3><nc:ospf3>
    #   <nc:area><nc:name>0.0.0.100</nc:name><nc:interface><nc:name>so-0/0/0.0</nc:name>
    #   </nc:interface></nc:area></nc:ospf3></nc:protocols>
    # - <nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:router-id>10.200.16.75</nc:router-id><nc:router-id>10.200.16.75</nc:router-id></nc:routing-options>
    #
    # after:
    # - areas:
    #     - area_id: 0.0.0.100
    #       interfaces:
    #       - metric: 6
    #         name: so-0/0/1.0
    #         priority: 2
    #       - name: so-0/0/0.0
    #       stub:
    #         default_metric: 200
    #         set: true
    #     router_id: 10.200.16.75
    #
    # After state
    # -----------
    #
    # admin# show protocols ospf3
    # area 0.0.0.100 {
    #     stub default-metric 200;
    #     interface so-0/0/1.0 {
    #         metric 6;
    #         priority 2;
    #     }
    #     interface so-0/0/0.0;
    # }
    #
    # Using overridden
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf3
    # area 0.0.0.100 {
    #     stub default-metric 200;
    #     interface so-0/0/1.0 {
    #         metric 6;
    #         priority 2;
    #     }
    #     interface so-0/0/0.0;
    # }

    - name: Override runnig OSPFv3 config with provided config
      junipernetworks.junos.junos_ospfv3:
        config:
          - router_id: 10.200.16.75
            areas:
              - area_id: 0.0.0.100
                stub:
                  default_metric: 200
                  set: true
                interfaces:
                  - name: so-0/0/0.0
                    priority: 3
                    metric: 5
                    flood_reduction: true
                    passive: true
              - area_id: 0.0.0.200
                interfaces:
                  - name: ge-1/1/0.0
                  - name: ge-2/2/0.0
        state: overridden

    # Task Output:
    # ------------
    #
    # before:
    # - areas:
    #     - area_id: 0.0.0.100
    #       interfaces:
    #       - metric: 6
    #         name: so-0/0/1.0
    #         priority: 2
    #       - name: so-0/0/0.0
    #       stub:
    #         default_metric: 200
    #         set: true
    #     router_id: 10.200.16.75
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf3 delete="delete"/><nc:ospf3><nc:area><nc:name>0.0.0.100</nc:name>
    #   <nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority><nc:flood-reduction/>
    #   <nc:metric>5</nc:metric><nc:passive/></nc:interface>
    #   <nc:stub><nc:default-metric>200</nc:default-metric></nc:stub></nc:area>
    #   <nc:area><nc:name>0.0.0.200</nc:name><nc:interface><nc:name>ge-1/1/0.0</nc:name>
    #   </nc:interface><nc:interface><nc:name>ge-2/2/0.0</nc:name></nc:interface></nc:area>
    #   </nc:ospf3></nc:protocols>
    # - <nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:router-id delete="delete"/><nc:router-id>10.200.16.75</nc:router-id></nc:routing-options>
    #
    # after:
    # - areas:
    #     - area_id: 0.0.0.100
    #       interfaces:
    #       - flood_reduction: true
    #         metric: 5
    #         name: so-0/0/0.0
    #         passive: true
    #         priority: 3
    #       stub:
    #         default_metric: 200
    #         set: true
    #     - area_id: 0.0.0.200
    #       interfaces:
    #       - name: ge-1/1/0.0
    #       - name: ge-2/2/0.0
    #     router_id: 10.200.16.75

    # After state
    # -----------
    #
    # admin# show protocols ospf3
    # area 0.0.0.100 {
    #     stub default-metric 200;
    #     interface so-0/0/0.0 {
    #         passive;
    #         metric 5;
    #         priority 3;
    #         flood-reduction;
    #     }
    # }
    # area 0.0.0.200 {
    #     interface ge-1/1/0.0;
    #     interface ge-2/2/0.0;
    # }
    # Using deleted
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf3
    # area 0.0.0.100 {
    #     stub default-metric 200;
    #     interface so-0/0/0.0 {
    #         passive;
    #         metric 5;
    #         priority 3;
    #         flood-reduction;
    #     }
    # }
    # area 0.0.0.200 {
    #     interface ge-1/1/0.0;
    #     interface ge-2/2/0.0;
    # }

    - name: Delete OSPFv3 running config.
      junipernetworks.junos.junos_ospfv3:
        config:
        state: deleted

    # Task Output:
    # ------------
    #
    # before:
    # - areas:
    #     - area_id: 0.0.0.100
    #       interfaces:
    #       - flood_reduction: true
    #         metric: 5
    #         name: so-0/0/0.0
    #         passive: true
    #         priority: 3
    #       stub:
    #         default_metric: 200
    #         set: true
    #     - area_id: 0.0.0.200
    #       interfaces:
    #       - name: ge-1/1/0.0
    #       - name: ge-2/2/0.0
    #     router_id: 10.200.16.75
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf3 delete="delete"/></nc:protocols>
    # - <nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:router-id delete="delete"/></nc:routing-options>
    #
    # after: []
    #
    #
    # After state
    # -----------
    #
    # admin# show protocols ospf3

    # Using gathered
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf3
    # area 0.0.0.100 {
    #     stub default-metric 200;
    #     interface so-0/0/0.0 {
    #         metric 5;
    #         priority 3;
    #     }
    #     interface so-0/0/1.0 {
    #         metric 6;
    #         priority 2;
    #     }

    - name: Gather Junos OSPFv3 running-configuration
      junipernetworks.junos.junos_ospfv3:
        config:
        state: gathered
    #
    #
    # Task Output:
    # ------------
    #
    # gathered:
    #
    # - areas:
    #     - area_id: 0.0.0.100
    #       interfaces:
    #       - metric: 5
    #         name: so-0/0/0.0
    #         priority: 3
    #       - metric: 6
    #         name: so-0/0/1.0
    #         priority: 2
    #       stub:
    #         default_metric: 200
    #         set: true
    #     router_id: 10.200.16.75

    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <protocols>
    #             <ospf3>
    #                 <area>
    #                     <name>0.0.0.100</name>
    #                     <stub>
    #                         <default-metric>200</default-metric>
    #                     </stub>
    #                     <interface>
    #                         <name>so-0/0/0.0</name>
    #                         <passive></passive>
    #                         <metric>5</metric>
    #                         <priority>3</priority>
    #                         <flood-reduction/>
    #                     </interface>
    #                 </area>
    #                 <area>
    #                     <name>0.0.0.200</name>
    #                     <interface>
    #                         <name>ge-1/1/0.0</name>
    #                     </interface>
    #                     <interface>
    #                         <name>ge-2/2/0.0</name>
    #                     </interface>
    #                 </area>
    #             </ospf3>
    #         </protocols>
    #         <routing-options>
    #             <router-id>10.200.16.75</router-id>
    #         </routing-options>
    #     </configuration>
    # </rpc-reply>


    - name: Parsed the ospfv3 config into structured ansible resource facts.
      junipernetworks.junos.junos_ospfv3:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed
    #
    # Task Output:
    # ------------
    #
    # parsed:
    # - router_id: 10.200.16.75
    #         areas:
    #           - area_id: 0.0.0.100
    #             stub:
    #               default_metric: 200
    #               set: true
    #             interfaces:
    #               - name: so-0/0/0.0
    #                 priority: 3
    #                 metric: 5
    #                 flood_reduction: true
    #                 passive: true
    #           - area_id: 0.0.0.200
    #             interfaces:
    #               - name: ge-1/1/0.0
    #               - name: ge-2/2/0.0

    # Using rendered
    #
    - name: Render the commands for provided  configuration
      junipernetworks.junos.junos_ospfv3:
        config:
          - router_id: 10.200.16.75
            areas:
              - area_id: 0.0.0.100
                interfaces:
                  - metric: 5
                    name: so-0/0/0.0
                    priority: 3
                  - metric: 6
                    name: so-0/0/1.0
                    priority: 2
                stub:
                  default_metric: 200
                  set: true
        state: rendered

    # Task Output:
    # ------------
    #
    # rendered: "<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # <nc:ospf3><nc:area><nc:name>0.0.0.100</nc:name><nc:interface>
    # <nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority>
    # <nc:metric>5</nc:metric></nc:interface><nc:interface><nc:name>so-0/0/1.0</nc:name>
    # <nc:priority>2</nc:priority><nc:metric>6</nc:metric></nc:interface><nc:stub>
    # <nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf3></nc:protocols>"



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
                            <div>The resulting configuration module invocation.</div>
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
                            <div>The configuration prior to the module invocation.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:protocols xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt;&lt; nc:ospf3&gt;&lt;nc:area&gt;&lt;nc:name&gt;0.0.0.100&lt;/nc:name&gt;&lt;nc:interface&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
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

- Rohit Thakur (@rohitthakur2590)
