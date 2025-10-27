.. _junipernetworks.junos.junos_ospfv2_module:


**********************************
junipernetworks.junos.junos_ospfv2
**********************************

**OSPFv2 resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages OSPFv2 configuration on devices running Juniper JUNOS.



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
            <th colspan="6">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="6">
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
                        <div>A list of OSPFv2 process configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                        <div>A list of OSPFv2 areas&#x27; configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="4">
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
                        <div>Included for compatibility, remove/deprecate after 2025-07-01.</div>
                        <div>Alternate for this would be area_ranges which is a list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>area_ranges</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure IP address ranges for the area.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify ip address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>exact</b>
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
                        <div>Enforce exact match for advertisement of this area range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>override_metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Override the dynamic metric for this area-range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>restrict</b>
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
                        <div>Restrict advertisement of this area range.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="3">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>md5</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MD5 authentication keys</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify key value</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify the key identity</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>start_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Start time for key transmission (YYYY-MM-DD.HH:MM)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify authentication key.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Included for compatibility, remove/deprecate after 2025-07-01.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                <td colspan="2">
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
                        <div>Specify metric</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                <td colspan="3">
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
                <td colspan="3">
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
                <td colspan="3">
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
                <td colspan="3">
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
                <td colspan="3">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="4">
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
                <td colspan="3">
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
                <td colspan="3">
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
                <td colspan="5">
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
                <td colspan="5">
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
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_route_leaking</b>
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
                        <div>Allow routes to be leaked when overload is configured.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_external</b>
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
                        <div>Advertise As External with maximum usable metric.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stub_network</b>
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
                        <div>Advertise Stub Network with maximum metric.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="5">
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
                <td colspan="5">
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
                <td colspan="5">
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
                <td colspan="5">
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
                <td colspan="5">
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
                        <div>The OSPFv2 router id.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                <td colspan="4">
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
                <td colspan="4">
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
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_ignore_our_externals</b>
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
                        <div>Do not ignore self-generated external and NSSA LSAs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="6">
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
                <td colspan="6">
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
    # admin# show protocols ospf

    - name: Merge provided OSPFv2 configuration into running config.
      junipernetworks.junos.junos_ospfv2:
        config:
          - reference_bandwidth: 10g
            areas:
              - area_id: 0.0.0.100
                area_ranges:
                  - address: 10.200.17.0/24
                    exact: true
                    restrict: true
                    override_metric: 2000
                  - address: 10.200.15.0/24
                    exact: true
                    restrict: true
                    override_metric: 2000
                    stub:
                      default_metric: 100
                      set: true
                    interfaces:
                      - name: so-0/0/0.0
                        priority: 3
                        metric: 5
                        flood_reduction: false
                        passive: true
                        bandwidth_based_metrics:
                          - bandwidth: 1g
                            metric: 5
                          - bandwidth: 10g
                            metric: 40
                        timers:
                          dead_interval: 4
                          hello_interval: 2
                          poll_interval: 2
                          retransmit_interval: 2
            rfc1583compatibility: false
        state: merged

    # Task Output:
    # ------------
    #
    # before: []
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf><nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/>
    #   <nc:area><nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/>
    #   <nc:restrict/><nc:override-metric>2000</nc:override-metric></nc:area-range><nc:area-range>
    #   <nc:name>10.200.15.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
    #   </nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority>
    #   <nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name>
    #   <nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric>
    #   </nc:bandwidth></nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval>
    #   <nc:hello-interval>2</nc:hello-interval><nc:poll-interval>2</nc:poll-interval>
    #   <nc:retransmit-interval>2</nc:retransmit-interval></nc:interface><nc:stub>
    #   <nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
    #
    # after:
    # - areas:
    #   - area_id: 0.0.0.100
    #     area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
    #     area_ranges:
    #     - address: 10.200.17.0/24
    #       exact: true
    #       override_metric: 2000
    #       restrict: true
    #     - address: 10.200.15.0/24
    #       exact: true
    #       override_metric: 2000
    #       restrict: true
    #     interfaces:
    #     - bandwidth_based_metrics:
    #       - bandwidth: 1g
    #         metric: 5
    #       - bandwidth: 10g
    #         metric: 40
    #       metric: 5
    #       name: so-0/0/0.0
    #       passive: true
    #       priority: 3
    #       timers:
    #         dead_interval: 4
    #         hello_interval: 2
    #         poll_interval: 2
    #         retransmit_interval: 2
    #     stub:
    #       default_metric: 100
    #       set: true
    #   reference_bandwidth: 10g
    #   rfc1583compatibility: false

    # After state
    # -----------
    #
    # admin# show protocols ospf
    # reference-bandwidth 10g;
    # no-rfc-1583;
    # area 0.0.0.100 {
    #     stub default-metric 100;
    #     area-range 10.200.17.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     area-range 10.200.15.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     interface so-0/0/0.0 {
    #         passive;
    #         bandwidth-based-metrics {
    #             bandwidth 1g metric 5;
    #             bandwidth 10g metric 40;
    #         }
    #         metric 5;
    #         priority 3;
    #         retransmit-interval 2;
    #         hello-interval 2;
    #         dead-interval 4;
    #         poll-interval 2;
    #     }
    # }
    #
    # Using replaced
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf
    # reference-bandwidth 10g;
    # no-rfc-1583;
    # area 0.0.0.100 {
    #     stub default-metric 100;
    #     area-range 10.200.17.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     area-range 10.200.15.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     interface so-0/0/0.0 {
    #         passive;
    #         bandwidth-based-metrics {
    #             bandwidth 1g metric 5;
    #             bandwidth 10g metric 40;
    #         }
    #         metric 5;
    #         priority 3;
    #         retransmit-interval 2;
    #         hello-interval 2;
    #         dead-interval 4;
    #         poll-interval 2;
    #     }
    # }

    - name: Replace existing Junos OSPFv2 config with provided config
      junipernetworks.junos.junos_ospfv2:
        config:
          - reference_bandwidth: 10g
            areas:
              - area_id: 0.0.0.100
                area_ranges:
                  - address: 10.200.17.0/24
                    exact: true
                    restrict: true
                  - address: 10.200.16.0/24
                    exact: true
                    restrict: true
                    override_metric: 1000
                stub:
                  default_metric: 100
                  set: true
                interfaces:
                  - name: so-0/0/0.0
                    priority: 3
                    metric: 5
                    flood_reduction: false
                    passive: true
                    bandwidth_based_metrics:
                      - bandwidth: 1g
                        metric: 5
                      - bandwidth: 10g
                        metric: 40
                    timers:
                      dead_interval: 4
                      hello_interval: 2
                      poll_interval: 2
                      retransmit_interval: 2
            rfc1583compatibility: false
        state: replacedd

    # Task Output:
    # ------------
    #
    # before:
    #   - areas:
    #     - area_id: 0.0.0.100
    #       area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
    #       area_ranges:
    #       - address: 10.200.17.0/24
    #         exact: true
    #         override_metric: 2000
    #         restrict: true
    #       - address: 10.200.15.0/24
    #         exact: true
    #         override_metric: 2000
    #         restrict: true
    #       interfaces:
    #       - bandwidth_based_metrics:
    #         - bandwidth: 1g
    #           metric: 5
    #         - bandwidth: 10g
    #           metric: 40
    #         metric: 5
    #         name: so-0/0/0.0
    #         passive: true
    #         priority: 3
    #         timers:
    #           dead_interval: 4
    #           hello_interval: 2
    #           poll_interval: 2
    #           retransmit_interval: 2
    #       stub:
    #         default_metric: 100
    #         set: true
    #     reference_bandwidth: 10g
    #     rfc1583compatibility: false
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area></nc:ospf><nc:ospf>
    #   <nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/><nc:area>
    #   <nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/>
    #   <nc:restrict/></nc:area-range><nc:area-range><nc:name>10.200.16.0/24</nc:name><nc:exact/>
    #   <nc:restrict/><nc:override-metric>1000</nc:override-metric></nc:area-range><nc:interface>
    #   <nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/>
    #   <nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name><nc:metric>5</nc:metric>
    #   </nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric></nc:bandwidth>
    #   </nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval><nc:hello-interval>2</nc:hello-interval>
    #   <nc:poll-interval>2</nc:poll-interval><nc:retransmit-interval>2</nc:retransmit-interval></nc:interface>
    #   <nc:stub><nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
    #
    # after:
    #   - areas:
    #     - area_id: 0.0.0.100
    #       area_range: '[''10.200.17.0/24'', ''10.200.16.0/24'']'
    #       area_ranges:
    #       - address: 10.200.17.0/24
    #         exact: true
    #         restrict: true
    #       - address: 10.200.16.0/24
    #         exact: true
    #         override_metric: 1000
    #         restrict: true
    #       interfaces:
    #       - bandwidth_based_metrics:
    #         - bandwidth: 1g
    #           metric: 5
    #         - bandwidth: 10g
    #           metric: 40
    #         metric: 5
    #         name: so-0/0/0.0
    #         passive: true
    #         priority: 3
    #         timers:
    #           dead_interval: 4
    #           hello_interval: 2
    #           poll_interval: 2
    #           retransmit_interval: 2
    #       stub:
    #         default_metric: 100
    #         set: true
    #     reference_bandwidth: 10g
    #     rfc1583compatibility: false
    #
    # After state
    # -----------
    #
    # admin# show protocols ospf
    # reference-bandwidth 10g;
    # no-rfc-1583;
    # area 0.0.0.100 {
    #     stub default-metric 100;
    #     area-range 10.200.17.0/24 {
    #         restrict;
    #         exact;
    #     }
    #     area-range 10.200.16.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 1000;
    #     }
    #     interface so-0/0/0.0 {
    #         passive;
    #         bandwidth-based-metrics {
    #             bandwidth 1g metric 5;
    #             bandwidth 10g metric 40;
    #         }
    #         metric 5;
    #         priority 3;
    #         retransmit-interval 2;
    #         hello-interval 2;
    #         dead-interval 4;
    #         poll-interval 2;
    #     }
    # }
    #
    # Using overridden
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf
    # reference-bandwidth 10g;
    # no-rfc-1583;
    # area 0.0.0.100 {
    #     stub default-metric 100;
    #     area-range 10.200.17.0/24 {
    #         restrict;
    #         exact;
    #     }
    #     area-range 10.200.16.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 1000;
    #     }
    #     interface so-0/0/0.0 {
    #         passive;
    #         bandwidth-based-metrics {
    #             bandwidth 1g metric 5;
    #             bandwidth 10g metric 40;
    #         }
    #         metric 5;
    #         priority 3;
    #         retransmit-interval 2;
    #         hello-interval 2;
    #         dead-interval 4;
    #         poll-interval 2;
    #     }
    # }

    - name: Override runnig OSPFv2 config with provided config
      junipernetworks.junos.junos_ospfv2:
        config:
          - reference_bandwidth: 10g
            areas:
              - area_id: 0.0.0.110
                area_ranges:
                  - address: 20.200.17.0/24
                    exact: true
                    restrict: true
                    override_metric: 2000
                  - address: 20.200.15.0/24
                    exact: true
                    restrict: true
                    override_metric: 2000
                stub:
                  default_metric: 200
                  set: true
                interfaces:
                  - name: so-0/0/0.0
                    priority: 3
                    metric: 5
                    flood_reduction: false
                    passive: true
                    bandwidth_based_metrics:
                      - bandwidth: 1g
                        metric: 5
                      - bandwidth: 10g
                        metric: 40
        state: overridden

    # Task Output:
    # ------------
    #
    # before:
    # - areas:
    #   - area_id: 0.0.0.100
    #     area_range: '[''10.200.17.0/24'', ''10.200.16.0/24'']'
    #     area_ranges:
    #     - address: 10.200.17.0/24
    #       exact: true
    #       restrict: true
    #     - address: 10.200.16.0/24
    #       exact: true
    #       override_metric: 1000
    #       restrict: true
    #     interfaces:
    #     - bandwidth_based_metrics:
    #       - bandwidth: 1g
    #         metric: 5
    #       - bandwidth: 10g
    #         metric: 40
    #       metric: 5
    #       name: so-0/0/0.0
    #       passive: true
    #       priority: 3
    #       timers:
    #         dead_interval: 4
    #         hello_interval: 2
    #         poll_interval: 2
    #         retransmit_interval: 2
    #     stub:
    #       default_metric: 100
    #       set: true
    #   reference_bandwidth: 10g
    #   rfc1583compatibility: false
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area></nc:ospf><nc:ospf>
    #   <nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:area><nc:name>0.0.0.110</nc:name>
    #   <nc:area-range><nc:name>20.200.17.0/24</nc:name><nc:exact/><nc:restrict/>
    #   <nc:override-metric>2000</nc:override-metric></nc:area-range><nc:area-range>
    #   <nc:name>20.200.15.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
    #   </nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority>
    #   <nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name>
    #   <nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric>
    #   </nc:bandwidth></nc:bandwidth-based-metrics></nc:interface><nc:stub>
    #   <nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
    #
    # after:
    #   - areas:
    #     - area_id: 0.0.0.110
    #       area_range: '[''20.200.17.0/24'', ''20.200.15.0/24'']'
    #       area_ranges:
    #       - address: 20.200.17.0/24
    #         exact: true
    #         override_metric: 2000
    #         restrict: true
    #       - address: 20.200.15.0/24
    #         exact: true
    #         override_metric: 2000
    #         restrict: true
    #       interfaces:
    #       - bandwidth_based_metrics:
    #         - bandwidth: 1g
    #           metric: 5
    #         - bandwidth: 10g
    #           metric: 40
    #         metric: 5
    #         name: so-0/0/0.0
    #         passive: true
    #         priority: 3
    #       stub:
    #         default_metric: 200
    #         set: true
    #     reference_bandwidth: 10g
    #     rfc1583compatibility: false

    # After state
    # -----------
    #
    # admin# show protocols ospf
    # reference-bandwidth 10g;
    # no-rfc-1583;
    # area 0.0.0.110 {
    #     stub default-metric 200;
    #     area-range 20.200.17.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     area-range 20.200.15.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     interface so-0/0/0.0 {
    #         passive;
    #         bandwidth-based-metrics {
    #             bandwidth 1g metric 5;
    #             bandwidth 10g metric 40;
    #         }
    #         metric 5;
    #         priority 3;
    #     }
    # }
    # Using deleted
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf
    # reference-bandwidth 10g;
    # no-rfc-1583;
    # area 0.0.0.110 {
    #     stub default-metric 200;
    #     area-range 20.200.17.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     area-range 20.200.15.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     interface so-0/0/0.0 {
    #         passive;
    #         bandwidth-based-metrics {
    #             bandwidth 1g metric 5;
    #             bandwidth 10g metric 40;
    #         }
    #         metric 5;
    #         priority 3;
    #     }
    # }

    - name: Delete OSPFv2 running config.
      junipernetworks.junos.junos_ospfv2:
        config:
        state: deleted

    # Task Output:
    # ------------
    #
    # before:
    #   - areas:
    #     - area_id: 0.0.0.110
    #       area_range: '[''20.200.17.0/24'', ''20.200.15.0/24'']'
    #       area_ranges:
    #       - address: 20.200.17.0/24
    #         exact: true
    #         override_metric: 2000
    #         restrict: true
    #       - address: 20.200.15.0/24
    #         exact: true
    #         override_metric: 2000
    #         restrict: true
    #       interfaces:
    #       - bandwidth_based_metrics:
    #         - bandwidth: 1g
    #           metric: 5
    #         - bandwidth: 10g
    #           metric: 40
    #         metric: 5
    #         name: so-0/0/0.0
    #         passive: true
    #         priority: 3
    #       stub:
    #         default_metric: 200
    #         set: true
    #     reference_bandwidth: 10g
    #     rfc1583compatibility: false
    #
    # commands:
    # - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area><nc:reference-bandwidth delete="delete"/>
    #   <nc:no-rfc-1583 delete="delete"/></nc:ospf></nc:protocols>
    #
    # after: []
    #
    #
    # After state
    # -----------
    #
    # admin# show protocols ospf

    # Using gathered
    #
    # Before state
    # ------------
    #
    # admin# show protocols ospf
    # reference-bandwidth 10g;
    # no-rfc-1583;
    # area 0.0.0.100 {
    #     stub default-metric 100;
    #     area-range 10.200.17.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     area-range 10.200.15.0/24 {
    #         restrict;
    #         exact;
    #         override-metric 2000;
    #     }
    #     interface so-0/0/0.0 {
    #         passive;
    #         bandwidth-based-metrics {
    #             bandwidth 1g metric 5;
    #             bandwidth 10g metric 40;
    #         }
    #         metric 5;
    #         priority 3;
    #         retransmit-interval 2;
    #         hello-interval 2;
    #         dead-interval 4;
    #         poll-interval 2;
    #     }
    # }

    - name: Gather Junos OSPFv2 running-configuration
      junipernetworks.junos.junos_ospfv2:
        config:
        state: gathered
    #
    #
    # Task Output:
    # ------------
    #
    # gathered:
    #
    #  - areas:
    # - area_id: 0.0.0.100
    #   area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
    #   area_ranges:
    #   - address: 10.200.17.0/24
    #     exact: true
    #     override_metric: 2000
    #     restrict: true
    #   - address: 10.200.15.0/24
    #     exact: true
    #     override_metric: 2000
    #     restrict: true
    #   interfaces:
    #   - bandwidth_based_metrics:
    #     - bandwidth: 1g
    #       metric: 5
    #     - bandwidth: 10g
    #       metric: 40
    #     metric: 5
    #     name: so-0/0/0.0
    #     passive: true
    #     priority: 3
    #     timers:
    #       dead_interval: 4
    #       hello_interval: 2
    #       poll_interval: 2
    #       retransmit_interval: 2
    #   stub:
    #     default_metric: 100
    #     set: true
    # reference_bandwidth: 10g
    # rfc1583compatibility: false

    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <protocols>
    #             <ospf>
    #             <reference-bandwidth>10g</reference-bandwidth>
    #             <no-rfc-1583/>
    #             <area>
    #                 <name>0.0.0.100</name>
    #                 <stub>
    #                     <default-metric>100</default-metric>
    #                 </stub>
    #                 <area-range>
    #                     <name>10.200.16.0/24</name>
    #                     <exact/>
    #                     <override-metric>10000</override-metric>
    #                 </area-range>
    #                 <area-range>
    #                     <name>10.200.11.0/24</name>
    #                     <restrict/>
    #                     <exact/>
    #                 </area-range>
    #                 <interface>
    #                     <name>so-0/0/0.0</name>
    #                     <passive>
    #                     </passive>
    #                     <bandwidth-based-metrics>
    #                         <bandwidth>
    #                             <name>1g</name>
    #                             <metric>5</metric>
    #                         </bandwidth>
    #                         <bandwidth>
    #                             <name>10g</name>
    #                             <metric>40</metric>
    #                         </bandwidth>
    #                     </bandwidth-based-metrics>
    #                     <metric>5</metric>
    #                     <priority>3</priority>
    #                     <retransmit-interval>2</retransmit-interval>
    #                     <hello-interval>2</hello-interval>
    #                     <dead-interval>4</dead-interval>
    #                     <poll-interval>2</poll-interval>
    #                 </interface>
    #             </area>
    #         </ospf>
    #         </protocols>
    #         <routing-options>
    #             <static>
    #                 <route>
    #                     <name>172.16.17.0/24</name>
    #                     <discard />
    #                 </route>
    #             </static>
    #             <router-id>10.200.16.75</router-id>
    #             <autonomous-system>
    #                 <as-number>65432</as-number>
    #             </autonomous-system>
    #         </routing-options>
    #     </configuration>
    # </rpc-reply>


    - name: Parsed the ospfv2 config into structured ansible resource facts.
      junipernetworks.junos.junos_ospfv2:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed
    #
    # Task Output:
    # ------------
    #
    # parsed:
    # - areas:
    #     - area_id: 0.0.0.100
    #       area_range: '[''10.200.16.0/24'', ''10.200.11.0/24'']'
    #       area_ranges:
    #       - address: 10.200.16.0/24
    #         exact: true
    #         override_metric: 10000
    #       - address: 10.200.11.0/24
    #         exact: true
    #         restrict: true
    #       interfaces:
    #       - bandwidth_based_metrics:
    #         - bandwidth: 1g
    #           metric: 5
    #         - bandwidth: 10g
    #           metric: 40
    #         metric: 5
    #         name: so-0/0/0.0
    #         passive: true
    #         priority: 3
    #         timers:
    #           dead_interval: 4
    #           hello_interval: 2
    #           poll_interval: 2
    #           retransmit_interval: 2
    #       stub:
    #         default_metric: 100
    #         set: true
    #     reference_bandwidth: 10g
    #     rfc1583compatibility: false
    #     router_id: 10.200.16.75

    # Using rendered
    #
    - name: Render the commands for provided  configuration
      junipernetworks.junos.junos_ospfv2:
        config:
          - reference_bandwidth: 10g
            areas:
              - area_id: 0.0.0.100
                area_ranges:
                  - address: 10.200.17.0/24
                    exact: true
                    restrict: true
                    override_metric: 2000
                  - address: 10.200.15.0/24
                    exact: true
                    restrict: true
                    override_metric: 2000
                stub:
                  default_metric: 100
                  set: true
                interfaces:
                  - name: so-0/0/0.0
                    priority: 3
                    metric: 5
                    flood_reduction: false
                    passive: true
                    bandwidth_based_metrics:
                      - bandwidth: 1g
                        metric: 5
                      - bandwidth: 10g
                        metric: 40
                    timers:
                      dead_interval: 4
                      hello_interval: 2
                      poll_interval: 2
                      retransmit_interval: 2
            rfc1583compatibility: false
        state: rendered

    # Task Output:
    # ------------
    #
    # rendered: "<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # <nc:ospf><nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/><nc:area><nc:name>0.0.0.100</nc:name>
    # <nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
    # </nc:area-range><nc:area-range><nc:name>10.200.15.0/24</nc:name><nc:exact/><nc:restrict/>
    # <nc:override-metric>2000</nc:override-metric></nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name>
    # <nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth>
    # <nc:name>1g</nc:name><nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name>
    # <nc:metric>40</nc:metric></nc:bandwidth></nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval>
    # <nc:hello-interval>2</nc:hello-interval><nc:poll-interval>2</nc:poll-interval>
    # <nc:retransmit-interval>2</nc:retransmit-interval></nc:interface><nc:stub>
    # <nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>"



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:protocols xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt;&lt; nc:ospf&gt;&lt;nc:area delete=&quot;delete&quot;&gt;0.0.0.100&lt;/nc:area&gt;&lt;nc:reference-bandwidth delete=&quot;delete&quot;/&gt; &lt;nc:no-rfc-1583 delete=&quot;delete&quot;/&gt;&lt;/nc:ospf&gt;&lt;/nc:protocols&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
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

- Daniel Mellado (@dmellado)
- Rohit Thakur (@rohitthakur2590)
