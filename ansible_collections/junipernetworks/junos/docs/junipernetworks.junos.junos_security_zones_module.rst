.. _junipernetworks.junos.junos_security_zones_module:


******************************************
junipernetworks.junos.junos_security_zones
******************************************

**Manage security zones on Juniper JUNOS devices**


Version added: 2.9.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of security zones on Juniper JUNOS devices



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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Dictionary of security zone parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>functional_zone_management</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Functional zone to configure host for out of band management interfaces</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Text description of zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host_inbound_traffic</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allowed system services &amp; protocols</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocols</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Protocol type of incoming traffic to accept</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>except</b>
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
                        <div>Disallow the specified protocol traffic</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Type of incoming protocol to accept</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_services</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Type of incoming system-service traffic to accept</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>except</b>
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
                        <div>Disallow the specified incoming system-service traffic</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Type of incoming system-service traffic to accept</div>
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
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interfaces that are part of this zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>screen</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of ids option object applied to the zone</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>zones</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Security zones</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_book</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Address book entries</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_sets</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Define security address sets</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_sets</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Define an address-set name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Addresses to be included in this set</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Text description of address set</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Name of address set</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Define security addresses</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Text description of address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dns_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DNS address name</div>
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
                    <b>ipv4_only</b>
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
                        <div>IPv4 dns address</div>
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
                    <b>ipv6_only</b>
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
                        <div>IPv6 dns address</div>
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
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Fully qualified hostname</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Numeric IPv4 or IPv6 address with prefix</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Name of address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>range_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Address range</div>
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
                    <b>from</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Start of address range</div>
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
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>End of address range</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wildcard_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Numeric IPv4 wildcard address with in the form of a.d.d.r/netmask</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advance_policy_based_routing_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable Advance Policy Based Routing on this zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advanced_connection_tracking</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable Advance Policy Based Routing on this zone</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>allow-any-host</li>
                                    <li>allow-target-host</li>
                                    <li>allow-target-host-port</li>
                        </ul>
                </td>
                <td>
                        <div>Set connection tracking mode</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Timeout value in seconds for advanced-connection-tracking table for this zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>track_all_policies_to_this_zone</b>
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
                        <div>Mandate all policies with to-zone set to this zone to do connection track table lookup</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>application_tracking</b>
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
                        <div>Enable Application tracking support for this zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Text description of zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable_reverse_reroute</b>
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
                        <div>Enable Reverse route lookup when there is change in ingress interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host_inbound_traffic</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allowed system services &amp; protocols</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocols</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Protocol type of incoming traffic to accept</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>except</b>
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
                        <div>Disallow the specified protocol traffic</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Type of incoming protocol to accept</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_services</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Type of incoming system-service traffic to accept</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>except</b>
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
                        <div>Disallow the specified incoming system-service traffic</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Type of incoming system-service traffic to accept</div>
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
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interfaces that are part of this zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Name of the security zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>screen</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of ids option object applied to the zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_identity_log</b>
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
                        <div>Show user and group info in session log for this zone</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tcp_rst</b>
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
                        <div>Send RST for NON-SYN packet not matching TCP session</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unidirectional_session_refreshing</b>
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
                        <div>Enable unidirectional session refreshing on this zone</div>
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
                        <div>The value of this option should be the output received from the JunOS device by executing the command <b>show security policies</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
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
                                    <li>rendered</li>
                                    <li>gathered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required. behaviour for this module.</div>
                        <div>The state <em>gathered</em> will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into JSON format as per the resource module parameters and the value is returned in the <em>parsed</em> key within the result. The value of <code>running_config</code> option should be the same format as the output of command <em>show security policies detail</em> executed on device. For state <em>parsed</em> active connection to remote host is not required.</div>
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
    # vagrant@vsrx# show security zones
    #
    # [edit]
    # vagrant@vsrx# show security zones
    #
    - name: Merge the provided configuration with the exisiting running configuration
      junipernetworks.junos.junos_security_zones: &merged
        config:
          functional_zone_management:
            description: test description
            host_inbound_traffic:
              protocols:
                - name: all
                - name: bgp
                  except: true
              system_services:
                - name: all
                - except: true
                  name: dhcp
            interfaces:
              - ge-0/0/1.0
              - ge-0/0/2.0
            screen: test_screen
          security_zones:
            - address_book:
                address_sets:
                  - addresses:
                      - test_adr1
                      - test_adr2
                    name: test_adrset1
                  - addresses:
                      - test_adr3
                      - test_adr4
                    name: test_adrset2
                  - address_sets:
                      - test_adrset1
                      - test_adrset2
                    addresses:
                      - test_adr5
                    description: test description
                    name: test_adrset3
                addresses:
                  - description: test desc
                    ip_prefix: 10.0.0.0/24
                    name: test_adr1
                  - dns_name:
                      ipv6_only: true
                      name: 1.1.1.1
                    name: test_adr2
                  - name: test_adr3
                    range_address:
                      from: 10.2.0.1
                      to: 10.2.0.2
                  - name: test_adr4
                    wildcard_address: 10.3.0.1/24
                  - description: test desc
                    ip_prefix: 10.1.0.0/24
                    name: test_adr5
              advance_policy_based_routing_profile: test_profile
              application_tracking: true
              description: test description
              enable_reverse_reroute: true
              host_inbound_traffic:
                protocols:
                  - name: all
                  - except: true
                    name: bgp
                system_services:
                  - name: all
                  - except: true
                    name: dhcp
              interfaces:
                - ge-0/0/3.0
                - ge-0/0/4.0
              name: test_sec_zone1
              screen: test_screen
              source_identity_log: true
              tcp_rst: true
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #   "after": {
    #     "functional_zone_management": {
    #         "description": "test description",
    #         "host_inbound_traffic": {
    #             "protocols": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "bgp"
    #                 }
    #             ],
    #             "system_services": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "dhcp"
    #                 }
    #             ]
    #         },
    #         "interfaces": [
    #             "ge-0/0/1.0",
    #             "ge-0/0/2.0"
    #         ],
    #         "screen": "test_screen"
    #     },
    #     "security_zones": [
    #         {
    #             "address_book": {
    #                 "address_sets": [
    #                     {
    #                         "addresses": [
    #                             "test_adr1",
    #                             "test_adr2"
    #                         ],
    #                         "name": "test_adrset1"
    #                     },
    #                     {
    #                         "addresses": [
    #                             "test_adr3",
    #                             "test_adr4"
    #                         ],
    #                         "name": "test_adrset2"
    #                     },
    #                     {
    #                         "address_sets": [
    #                             "test_adrset1",
    #                             "test_adrset2"
    #                         ],
    #                         "addresses": [
    #                             "test_adr5"
    #                         ],
    #                         "description": "test description",
    #                         "name": "test_adrset3"
    #                     }
    #                 ],
    #                 "addresses": [
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.0.0.0/24",
    #                         "name": "test_adr1"
    #                     },
    #                     {
    #                         "dns_name": {
    #                             "ipv6_only": true,
    #                             "name": "1.1.1.1"
    #                         },
    #                         "name": "test_adr2"
    #                     },
    #                     {
    #                         "name": "test_adr3",
    #                         "range_address": {
    #                             "from": "10.2.0.1",
    #                             "to": "10.2.0.2"
    #                         }
    #                     },
    #                     {
    #                         "name": "test_adr4",
    #                         "wildcard_address": "10.3.0.1/24"
    #                     },
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.1.0.0/24",
    #                         "name": "test_adr5"
    #                     }
    #                 ]
    #             },
    #             "advance_policy_based_routing_profile": "test_profile",
    #             "application_tracking": true,
    #             "description": "test description",
    #             "enable_reverse_reroute": true,
    #             "host_inbound_traffic": {
    #                 "protocols": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "bgp"
    #                     }
    #                 ],
    #                 "system_services": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "dhcp"
    #                     }
    #                 ]
    #             },
    #             "interfaces": [
    #                 "ge-0/0/3.0",
    #                 "ge-0/0/4.0"
    #             ],
    #             "name": "test_sec_zone1",
    #             "screen": "test_screen",
    #             "source_identity_log": true,
    #             "tcp_rst": true
    #         }
    #     ]
    # },
    # "before": {},
    # "changed": true,
    # "commands":
    # '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones><nc:functional-zone><nc:management><nc:description>t'
    # 'est description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:na'
    # 'me>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-services><nc:system-services><n'
    # 'c:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/1.0</nc:name></nc'
    # ':interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:screen></nc:management></nc:f'
    # 'unctional-zone><nc:security-zone><nc:name>test_sec_zone1</nc:name><nc:address-book><nc:address><nc:name>test_adr1</nc:name><nc:i'
    # 'p-prefix>10.0.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:address><nc:address><nc:name>test_adr2</nc:nam'
    # 'e><nc:dns-name><nc:name>1.1.1.1</nc:name><nc:ipv6-only/></nc:dns-name></nc:address><nc:address><nc:name>test_adr3</nc:name><nc:r'
    # 'ange-address><nc:name>10.2.0.1</nc:name><nc:to><nc:range-high>10.2.0.2</nc:range-high></nc:to></nc:range-address></nc:address><n'
    # 'c:address><nc:name>test_adr4</nc:name><nc:wildcard-address><nc:name>10.3.0.1/24</nc:name></nc:wildcard-address></nc:address><nc:'
    # 'address><nc:name>test_adr5</nc:name><nc:ip-prefix>10.1.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:addre'
    # 'ss><nc:address-set><nc:name>test_adrset1</nc:name><nc:address><nc:name>test_adr1</nc:name></nc:address><nc:address><nc:name>test'
    # '_adr2</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset2</nc:name><nc:address><nc:name>test_adr3</nc:n'
    # 'ame></nc:address><nc:address><nc:name>test_adr4</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset3</nc'
    # ':name><nc:address><nc:name>test_adr5</nc:name></nc:address><nc:address-set><nc:name>test_adrset1</nc:name></nc:address-set><nc:a'
    # 'ddress-set><nc:name>test_adrset2</nc:name></nc:address-set><nc:description>test description</nc:description></nc:address-set></n'
    # 'c:address-book><nc:advance-policy-based-routing-profile><nc:profile>test_profile</nc:profile></nc:advance-policy-based-routing-p'
    # 'rofile><nc:application-tracking/><nc:description>test description</nc:description><nc:enable-reverse-reroute/><nc:host-inbound-t'
    # 'raffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:sys'
    # 'tem-services><nc:name>all</nc:name></nc:system-services><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-servi'
    # 'ces></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/3.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/4.0</nc'
    # ':name></nc:interfaces><nc:screen>test_screen</nc:screen><nc:source-identity-log/><nc:tcp-rst/></nc:security-zone></nc:zones></nc'
    # ':security>'

    # After state
    # -----------
    #
    # vagrant@vsrx# show system ntp
    # functional-zone management {
    #     interfaces {
    #         ge-0/0/1.0;
    #         ge-0/0/2.0;
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     description "test description";
    # }
    # security-zone test_sec_zone1 {
    #     description "test description";
    #     tcp-rst;
    #     address-book {
    #         address test_adr1 {
    #             description "test desc";
    #             10.0.0.0/24;
    #         }
    #         address test_adr2 {
    #             dns-name 1.1.1.1 {
    #                 ipv6-only;
    #             }
    #         }
    #         address test_adr3 {
    #             range-address 10.2.0.1 {
    #                 to {
    #                     10.2.0.2;
    #                 }
    #             }
    #         }
    #         address test_adr4 {
    #             wildcard-address 10.3.0.1/24;
    #         }
    #         address test_adr5 {
    #             description "test desc";
    #             10.1.0.0/24;
    #         }
    #         address-set test_adrset1 {
    #             address test_adr1;
    #             address test_adr2;
    #         }
    #         address-set test_adrset2 {
    #             address test_adr3;
    #             address test_adr4;
    #         }
    #         address-set test_adrset3 {
    #             description "test description";
    #             address test_adr5;
    #             address-set test_adrset1;
    #             address-set test_adrset2;
    #         }
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     interfaces {
    #         ge-0/0/3.0;
    #         ge-0/0/4.0;
    #     }
    #     application-tracking;
    #     source-identity-log;
    #     advance-policy-based-routing-profile {
    #         test_profile;
    #     }
    #     enable-reverse-reroute;
    # }
    #
    #
    # Using Replaced
    # Before state
    # ------------
    #
    # vagrant@vsrx# show security zones
    # functional-zone management {
    #     interfaces {
    #         ge-0/0/1.0;
    #         ge-0/0/2.0;
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     description "test description";
    # }
    # security-zone test_sec_zone1 {
    #     description "test description";
    #     tcp-rst;
    #     address-book {
    #         address test_adr1 {
    #             description "test desc";
    #             10.0.0.0/24;
    #         }
    #         address test_adr2 {
    #             dns-name 1.1.1.1 {
    #                 ipv6-only;
    #             }
    #         }
    #         address test_adr3 {
    #             range-address 10.2.0.1 {
    #                 to {
    #                     10.2.0.2;
    #                 }
    #             }
    #         }
    #         address test_adr4 {
    #             wildcard-address 10.3.0.1/24;
    #         }
    #         address test_adr5 {
    #             description "test desc";
    #             10.1.0.0/24;
    #         }
    #         address-set test_adrset1 {
    #             address test_adr1;
    #             address test_adr2;
    #         }
    #         address-set test_adrset2 {
    #             address test_adr3;
    #             address test_adr4;
    #         }
    #         address-set test_adrset3 {
    #             description "test description";
    #             address test_adr5;
    #             address-set test_adrset1;
    #             address-set test_adrset2;
    #         }
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     interfaces {
    #         ge-0/0/3.0;
    #         ge-0/0/4.0;
    #     }
    #     application-tracking;
    #     source-identity-log;
    #     advance-policy-based-routing-profile {
    #         test_profile;
    #     }
    #     enable-reverse-reroute;
    # }
    #
    #

    - name: Replaced running security zones configuration with provided configuration
      junipernetworks.junos.junos_security_zones:
        config:
          functional_zone_management:
            description: test description
            host_inbound_traffic:
              protocols:
                - name: all
                - name: bgp
                  except: true
              system_services:
                - name: all
                - except: true
                  name: dhcp
              interfaces:
                - ge-0/0/1.0
                - ge-0/0/2.0
            screen: test_screen
        state: replaced
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "after": {
    #     "functional_zone_management": {
    #         "description": "test description",
    #         "host_inbound_traffic": {
    #             "protocols": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "bgp"
    #                 }
    #             ],
    #             "system_services": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "dhcp"
    #                 }
    #             ]
    #         },
    #         "interfaces": [
    #             "ge-0/0/1.0",
    #             "ge-0/0/2.0"
    #         ],
    #         "screen": "test_screen"
    #     }
    # },
    # "before": {
    #     "functional_zone_management": {
    #         "description": "test description",
    #         "host_inbound_traffic": {
    #             "protocols": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "bgp"
    #                 }
    #             ],
    #             "system_services": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "dhcp"
    #                 }
    #             ]
    #         },
    #         "interfaces": [
    #             "ge-0/0/1.0",
    #             "ge-0/0/2.0"
    #         ],
    #         "screen": "test_screen"
    #     },
    #     "security_zones": [
    #         {
    #             "address_book": {
    #                 "address_sets": [
    #                     {
    #                         "addresses": [
    #                             "test_adr1",
    #                             "test_adr2"
    #                         ],
    #                         "name": "test_adrset1"
    #                     },
    #                     {
    #                         "addresses": [
    #                             "test_adr3",
    #                             "test_adr4"
    #                         ],
    #                         "name": "test_adrset2"
    #                     },
    #                     {
    #                         "address_sets": [
    #                             "test_adrset1",
    #                             "test_adrset2"
    #                         ],
    #                         "addresses": [
    #                             "test_adr5"
    #                         ],
    #                         "description": "test description",
    #                         "name": "test_adrset3"
    #                     }
    #                 ],
    #                 "addresses": [
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.0.0.0/24",
    #                         "name": "test_adr1"
    #                     },
    #                     {
    #                         "dns_name": {
    #                             "ipv6_only": true,
    #                             "name": "1.1.1.1"
    #                         },
    #                         "name": "test_adr2"
    #                     },
    #                     {
    #                         "name": "test_adr3",
    #                         "range_address": {
    #                             "from": "10.2.0.1",
    #                             "to": "10.2.0.2"
    #                         }
    #                     },
    #                     {
    #                         "name": "test_adr4",
    #                         "wildcard_address": "10.3.0.1/24"
    #                     },
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.1.0.0/24",
    #                         "name": "test_adr5"
    #                     }
    #                 ]
    #             },
    #             "advance_policy_based_routing_profile": "test_profile",
    #             "application_tracking": true,
    #             "description": "test description",
    #             "enable_reverse_reroute": true,
    #             "host_inbound_traffic": {
    #                 "protocols": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "bgp"
    #                     }
    #                 ],
    #                 "system_services": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "dhcp"
    #                     }
    #                 ]
    #             },
    #             "interfaces": [
    #                 "ge-0/0/3.0",
    #                 "ge-0/0/4.0"
    #             ],
    #             "name": "test_sec_zone1",
    #             "screen": "test_screen",
    #             "source_identity_log": true,
    #             "tcp_rst": true
    #         }
    #     ]
    # },
    # "changed": true,
    # "commands":
    # '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones delete="delete"/><nc:zones><nc:functional-zone><nc'
    # ':management><nc:description>test description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:p'
    # 'rotocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-se'
    # 'rvices><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:'
    # 'name>ge-0/0/1.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:'
    # 'screen></nc:management></nc:functional-zone></nc:zones></nc:security>'
    #
    #
    # After state
    # -----------
    #
    # vagrant@vsrx# show system ntp
    # functional-zone management {
    #     interfaces {
    #         ge-0/0/1.0;
    #         ge-0/0/2.0;
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     description "test description";
    # }
    #
    #
    # Using overridden
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show security zones
    # functional-zone management {
    #     interfaces {
    #         ge-0/0/1.0;
    #         ge-0/0/2.0;
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     description "test description";
    # }
    # security-zone test_sec_zone1 {
    #     description "test description";
    #     tcp-rst;
    #     address-book {
    #         address test_adr1 {
    #             description "test desc";
    #             10.0.0.0/24;
    #         }
    #         address test_adr2 {
    #             dns-name 1.1.1.1 {
    #                 ipv6-only;
    #             }
    #         }
    #         address test_adr3 {
    #             range-address 10.2.0.1 {
    #                 to {
    #                     10.2.0.2;
    #                 }
    #             }
    #         }
    #         address test_adr4 {
    #             wildcard-address 10.3.0.1/24;
    #         }
    #         address test_adr5 {
    #             description "test desc";
    #             10.1.0.0/24;
    #         }
    #         address-set test_adrset1 {
    #             address test_adr1;
    #             address test_adr2;
    #         }
    #         address-set test_adrset2 {
    #             address test_adr3;
    #             address test_adr4;
    #         }
    #         address-set test_adrset3 {
    #             description "test description";
    #             address test_adr5;
    #             address-set test_adrset1;
    #             address-set test_adrset2;
    #         }
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     interfaces {
    #         ge-0/0/3.0;
    #         ge-0/0/4.0;
    #     }
    #     application-tracking;
    #     source-identity-log;
    #     advance-policy-based-routing-profile {
    #         test_profile;
    #     }
    #     enable-reverse-reroute;
    # }
    #
    #

    - name: Override running security zones configuration with provided configuration
      junipernetworks.junos.junos_security_zones:
        config:
          functional_zone_management:
            description: test description
            host_inbound_traffic:
              protocols:
                - name: all
                - name: bgp
                  except: true
              system_services:
                - name: all
                - except: true
                  name: dhcp
            interfaces:
              - ge-0/0/1.0
              - ge-0/0/2.0
            screen: test_screen
        state: overridden
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "after": {
    #     "functional_zone_management": {
    #         "description": "test description",
    #         "host_inbound_traffic": {
    #             "protocols": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "bgp"
    #                 }
    #             ],
    #             "system_services": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "dhcp"
    #                 }
    #             ]
    #         },
    #         "interfaces": [
    #             "ge-0/0/1.0",
    #             "ge-0/0/2.0"
    #         ],
    #         "screen": "test_screen"
    #     }
    # },
    # "before": {
    #     "functional_zone_management": {
    #         "description": "test description",
    #         "host_inbound_traffic": {
    #             "protocols": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "bgp"
    #                 }
    #             ],
    #             "system_services": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "dhcp"
    #                 }
    #             ]
    #         },
    #         "interfaces": [
    #             "ge-0/0/1.0",
    #             "ge-0/0/2.0"
    #         ],
    #         "screen": "test_screen"
    #     },
    #     "security_zones": [
    #         {
    #             "address_book": {
    #                 "address_sets": [
    #                     {
    #                         "addresses": [
    #                             "test_adr1",
    #                             "test_adr2"
    #                         ],
    #                         "name": "test_adrset1"
    #                     },
    #                     {
    #                         "addresses": [
    #                             "test_adr3",
    #                             "test_adr4"
    #                         ],
    #                         "name": "test_adrset2"
    #                     },
    #                     {
    #                         "address_sets": [
    #                             "test_adrset1",
    #                             "test_adrset2"
    #                         ],
    #                         "addresses": [
    #                             "test_adr5"
    #                         ],
    #                         "description": "test description",
    #                         "name": "test_adrset3"
    #                     }
    #                 ],
    #                 "addresses": [
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.0.0.0/24",
    #                         "name": "test_adr1"
    #                     },
    #                     {
    #                         "dns_name": {
    #                             "ipv6_only": true,
    #                             "name": "1.1.1.1"
    #                         },
    #                         "name": "test_adr2"
    #                     },
    #                     {
    #                         "name": "test_adr3",
    #                         "range_address": {
    #                             "from": "10.2.0.1",
    #                             "to": "10.2.0.2"
    #                         }
    #                     },
    #                     {
    #                         "name": "test_adr4",
    #                         "wildcard_address": "10.3.0.1/24"
    #                     },
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.1.0.0/24",
    #                         "name": "test_adr5"
    #                     }
    #                 ]
    #             },
    #             "advance_policy_based_routing_profile": "test_profile",
    #             "application_tracking": true,
    #             "description": "test description",
    #             "enable_reverse_reroute": true,
    #             "host_inbound_traffic": {
    #                 "protocols": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "bgp"
    #                     }
    #                 ],
    #                 "system_services": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "dhcp"
    #                     }
    #                 ]
    #             },
    #             "interfaces": [
    #                 "ge-0/0/3.0",
    #                 "ge-0/0/4.0"
    #             ],
    #             "name": "test_sec_zone1",
    #             "screen": "test_screen",
    #             "source_identity_log": true,
    #             "tcp_rst": true
    #         }
    #     ]
    # },
    # "changed": true,
    # "commands":
    # '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones delete="delete"/><nc:zones><nc:functional-zone><nc'
    # ':management><nc:description>test description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:p'
    # 'rotocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-se'
    # 'rvices><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:'
    # 'name>ge-0/0/1.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:'
    # 'screen></nc:management></nc:functional-zone></nc:zones></nc:security>'
    #
    #
    # After state
    # -----------
    #
    # vagrant@vsrx# show system ntp
    # functional-zone management {
    #     interfaces {
    #         ge-0/0/1.0;
    #         ge-0/0/2.0;
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     description "test description";
    # }
    #
    #
    # Using deleted
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show security zones
    # functional-zone management {
    #     interfaces {
    #         ge-0/0/1.0;
    #         ge-0/0/2.0;
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     description "test description";
    # }
    #
    #
    - name: Delete running security zones configuration
      junipernetworks.junos.junos_security_zones:
        config:
        state: deleted
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {},
    #     "before": {
    #     "functional_zone_management": {
    #         "description": "test description",
    #         "host_inbound_traffic": {
    #             "protocols": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "bgp"
    #                 }
    #             ],
    #             "system_services": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "dhcp"
    #                 }
    #             ]
    #         },
    #         "interfaces": [
    #             "ge-0/0/1.0",
    #             "ge-0/0/2.0"
    #         ],
    #         "screen": "test_screen"
    #     }
    # },
    # "changed": true,
    # "commands":
    #   "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #   "<nc:zones delete="delete"/></nc:security>"
    #
    #
    # After state
    # -----------
    #
    # vagrant@vsrx# show security zones
    #
    # [edit]
    # Using gathered
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system ntp
    # functional-zone management {
    #     interfaces {
    #         ge-0/0/1.0;
    #         ge-0/0/2.0;
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     description "test description";
    # }
    # security-zone test_sec_zone1 {
    #     description "test description";
    #     tcp-rst;
    #     address-book {
    #         address test_adr1 {
    #             description "test desc";
    #             10.0.0.0/24;
    #         }
    #         address test_adr2 {
    #             dns-name 1.1.1.1 {
    #                 ipv6-only;
    #             }
    #         }
    #         address test_adr3 {
    #             range-address 10.2.0.1 {
    #                 to {
    #                     10.2.0.2;
    #                 }
    #             }
    #         }
    #         address test_adr4 {
    #             wildcard-address 10.3.0.1/24;
    #         }
    #         address test_adr5 {
    #             description "test desc";
    #             10.1.0.0/24;
    #         }
    #         address-set test_adrset1 {
    #             address test_adr1;
    #             address test_adr2;
    #         }
    #         address-set test_adrset2 {
    #             address test_adr3;
    #             address test_adr4;
    #         }
    #         address-set test_adrset3 {
    #             description "test description";
    #             address test_adr5;
    #             address-set test_adrset1;
    #             address-set test_adrset2;
    #         }
    #     }
    #     screen test_screen;
    #     host-inbound-traffic {
    #         system-services {
    #             all;
    #             dhcp {
    #                 except;
    #             }
    #         }
    #         protocols {
    #             all;
    #             bgp {
    #                 except;
    #             }
    #         }
    #     }
    #     interfaces {
    #         ge-0/0/3.0;
    #         ge-0/0/4.0;
    #     }
    #     application-tracking;
    #     source-identity-log;
    #     advance-policy-based-routing-profile {
    #         test_profile;
    #     }
    #     enable-reverse-reroute;
    # }
    - name: Gather running security zones configuration
      junipernetworks.junos.junos_security_zones:
        state: gathered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "gathered": {
    #     "functional_zone_management": {
    #         "description": "test description",
    #         "host_inbound_traffic": {
    #             "protocols": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "bgp"
    #                 }
    #             ],
    #             "system_services": [
    #                 {
    #                     "name": "all"
    #                 },
    #                 {
    #                     "except": true,
    #                     "name": "dhcp"
    #                 }
    #             ]
    #         },
    #         "interfaces": [
    #             "ge-0/0/1.0",
    #             "ge-0/0/2.0"
    #         ],
    #         "screen": "test_screen"
    #     },
    #     "security_zones": [
    #         {
    #             "address_book": {
    #                 "address_sets": [
    #                     {
    #                         "addresses": [
    #                             "test_adr1",
    #                             "test_adr2"
    #                         ],
    #                         "name": "test_adrset1"
    #                     },
    #                     {
    #                         "addresses": [
    #                             "test_adr3",
    #                             "test_adr4"
    #                         ],
    #                         "name": "test_adrset2"
    #                     },
    #                     {
    #                         "address_sets": [
    #                             "test_adrset1",
    #                             "test_adrset2"
    #                         ],
    #                         "addresses": [
    #                             "test_adr5"
    #                         ],
    #                         "description": "test description",
    #                         "name": "test_adrset3"
    #                     }
    #                 ],
    #                 "addresses": [
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.0.0.0/24",
    #                         "name": "test_adr1"
    #                     },
    #                     {
    #                         "dns_name": {
    #                             "ipv6_only": true,
    #                             "name": "1.1.1.1"
    #                         },
    #                         "name": "test_adr2"
    #                     },
    #                     {
    #                         "name": "test_adr3",
    #                         "range_address": {
    #                             "from": "10.2.0.1",
    #                             "to": "10.2.0.2"
    #                         }
    #                     },
    #                     {
    #                         "name": "test_adr4",
    #                         "wildcard_address": "10.3.0.1/24"
    #                     },
    #                     {
    #                         "description": "test desc",
    #                         "ip_prefix": "10.1.0.0/24",
    #                         "name": "test_adr5"
    #                     }
    #                 ]
    #             },
    #             "advance_policy_based_routing_profile": "test_profile",
    #             "application_tracking": true,
    #             "description": "test description",
    #             "enable_reverse_reroute": true,
    #             "host_inbound_traffic": {
    #                 "protocols": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "bgp"
    #                     }
    #                 ],
    #                 "system_services": [
    #                     {
    #                         "name": "all"
    #                     },
    #                     {
    #                         "except": true,
    #                         "name": "dhcp"
    #                     }
    #                 ]
    #             },
    #             "interfaces": [
    #                 "ge-0/0/3.0",
    #                 "ge-0/0/4.0"
    #             ],
    #             "name": "test_sec_zone1",
    #             "screen": "test_screen",
    #             "source_identity_log": true,
    #             "tcp_rst": true
    #         }
    #     ]
    # }
    # "changed": false,
    #
    #
    # Using rendered
    #
    # Before state
    # ------------
    #
    - name: Render xml for provided facts.
      junipernetworks.junos.junos_security_zones:
        config:
          functional_zone_management:
            description: test description
            host_inbound_traffic:
              protocols:
                - name: all
                - name: bgp
                  except: true
              system_services:
                - name: all
                - except: true
                  name: dhcp
            interfaces:
              - ge-0/0/1.0
              - ge-0/0/2.0
            screen: test_screen
          security_zones:
            - address_book:
                address_sets:
                  - addresses:
                      - test_adr1
                      - test_adr2
                    name: test_adrset1
                  - addresses:
                      - test_adr3
                      - test_adr4
                    name: test_adrset2
                  - address_sets:
                      - test_adrset1
                      - test_adrset2
                  - addresses:
                      - test_adr5
                    description: test description
                    name: test_adrset3
                addresses:
                  - description: test desc
                    ip_prefix: 10.0.0.0/24
                    name: test_adr1
                  - dns_name:
                      ipv6_only: true
                      name: 1.1.1.1
                    name: test_adr2
                  - name: test_adr3
                    range_address:
                      from: 10.2.0.1
                      to: 10.2.0.2
                  - name: test_adr4
                    wildcard_address: 10.3.0.1/24
                  - description: test desc
                    ip_prefix: 10.1.0.0/24
                    name: test_adr5
              advance_policy_based_routing_profile: test_profile
              application_tracking: true
              description: test description
              enable_reverse_reroute: true
              host_inbound_traffic:
                protocols:
                  - name: all
                  - except: true
                    name: bgp
                system_services:
                  - name: all
                  - except: true
                    name: dhcp
              interfaces:
                - ge-0/0/3.0
                - ge-0/0/4.0
              name: test_sec_zone1
              screen: test_screen
              source_identity_log: true
              tcp_rst: true
        state: rendered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "rendered":
    # '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones><nc:functional-zone><nc:management><nc:description>t'
    # 'est description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:na'
    # 'me>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-services><nc:system-services><n'
    # 'c:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/1.0</nc:name></nc'
    # ':interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:screen></nc:management></nc:f'
    # 'unctional-zone><nc:security-zone><nc:name>test_sec_zone1</nc:name><nc:address-book><nc:address><nc:name>test_adr1</nc:name><nc:i'
    # 'p-prefix>10.0.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:address><nc:address><nc:name>test_adr2</nc:nam'
    # 'e><nc:dns-name><nc:name>1.1.1.1</nc:name><nc:ipv6-only/></nc:dns-name></nc:address><nc:address><nc:name>test_adr3</nc:name><nc:r'
    # 'ange-address><nc:name>10.2.0.1</nc:name><nc:to><nc:range-high>10.2.0.2</nc:range-high></nc:to></nc:range-address></nc:address><n'
    # 'c:address><nc:name>test_adr4</nc:name><nc:wildcard-address><nc:name>10.3.0.1/24</nc:name></nc:wildcard-address></nc:address><nc:'
    # 'address><nc:name>test_adr5</nc:name><nc:ip-prefix>10.1.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:addre'
    # 'ss><nc:address-set><nc:name>test_adrset1</nc:name><nc:address><nc:name>test_adr1</nc:name></nc:address><nc:address><nc:name>test'
    # '_adr2</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset2</nc:name><nc:address><nc:name>test_adr3</nc:n'
    # 'ame></nc:address><nc:address><nc:name>test_adr4</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset3</nc'
    # ':name><nc:address><nc:name>test_adr5</nc:name></nc:address><nc:address-set><nc:name>test_adrset1</nc:name></nc:address-set><nc:a'
    # 'ddress-set><nc:name>test_adrset2</nc:name></nc:address-set><nc:description>test description</nc:description></nc:address-set></n'
    # 'c:address-book><nc:advance-policy-based-routing-profile><nc:profile>test_profile</nc:profile></nc:advance-policy-based-routing-p'
    # 'rofile><nc:application-tracking/><nc:description>test description</nc:description><nc:enable-reverse-reroute/><nc:host-inbound-t'
    # 'raffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:sys'
    # 'tem-services><nc:name>all</nc:name></nc:system-services><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-servi'
    # 'ces></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/3.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/4.0</nc'
    # ':name></nc:interfaces><nc:screen>test_screen</nc:screen><nc:source-identity-log/><nc:tcp-rst/></nc:security-zone></nc:zones></nc'
    # ':security>'
    #
    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <security>
    #             <zones>
    #                 <functional-zone>
    #                     <management>
    #                         <description>test description</description>
    #                         <host-inbound-traffic>
    #                             <protocols>
    #                                 <name>all</name>
    #                             </protocols>
    #                             <protocols>
    #                                 <name>bgp</name>
    #                                 <except />
    #                             </protocols>
    #                             <system-services>
    #                                 <name>all</name>
    #                             </system-services>
    #                             <system-services>
    #                                 <name>dhcp</name>
    #                                 <except />
    #                             </system-services>
    #                         </host-inbound-traffic>
    #                         <interfaces>
    #                             <name>ge-0/0/1.0</name>
    #                         </interfaces>
    #                         <interfaces>
    #                             <name>ge-0/0/2.0</name>
    #                         </interfaces>
    #                         <screen>test_screen</screen>
    #                     </management>
    #                 </functional-zone>
    #                 <security-zone>
    #                     <name>test_sec_zone1</name>
    #                     <address-book>
    #                         <address>
    #                             <name>test_adr1</name>
    #                             <ip-prefix>10.0.0.0/24</ip-prefix>
    #                             <description>test desc</description>
    #                         </address>
    #                         <address>
    #                             <name>test_adr2</name>
    #                             <dns-name>
    #                                 <name>1.1.1.1</name>
    #                                 <ipv6-only />
    #                             </dns-name>
    #                         </address>
    #                         <address>
    #                             <name>test_adr3</name>
    #                             <range-address>
    #                                 <name>10.2.0.1</name>
    #                                 <to>
    #                                     <range-high>10.2.0.2</range-high>
    #                                 </to>
    #                             </range-address>
    #                         </address>
    #                         <address>
    #                             <name>test_adr4</name>
    #                             <wildcard-address>
    #                                 <name>10.3.0.1/24</name>
    #                             </wildcard-address>
    #                         </address>
    #                         <address>
    #                             <name>test_adr5</name>
    #                             <ip-prefix>10.1.0.0/24</ip-prefix>
    #                             <description>test desc</description>
    #                         </address>
    #                         <address-set>
    #                             <name>test_adrset1</name>
    #                             <address>
    #                                 <name>test_adr1</name>
    #                             </address>
    #                             <address>
    #                                 <name>test_adr2</name>
    #                             </address>
    #                         </address-set>
    #                         <address-set>
    #                             <name>test_adrset2</name>
    #                             <address>
    #                                 <name>test_adr3</name>
    #                             </address>
    #                             <address>
    #                                 <name>test_adr4</name>
    #                             </address>
    #                         </address-set>
    #                         <address-set>
    #                             <name>test_adrset3</name>
    #                             <address>
    #                                 <name>test_adr5</name>
    #                             </address>
    #                             <address-set>
    #                                 <name>test_adrset1</name>
    #                             </address-set>
    #                             <address-set>
    #                                 <name>test_adrset2</name>
    #                             </address-set>
    #                             <description>test description</description>
    #                         </address-set>
    #                     </address-book>
    #                     <advance-policy-based-routing-profile>
    #                         <profile>test_profile</profile>
    #                     </advance-policy-based-routing-profile>
    #                     <application-tracking />
    #                     <description>test description</description>
    #                     <enable-reverse-reroute />
    #                     <host-inbound-traffic>
    #                         <protocols>
    #                             <name>all</name>
    #                         </protocols>
    #                         <protocols>
    #                             <name>bgp</name>
    #                             <except />
    #                         </protocols>
    #                         <system-services>
    #                             <name>all</name>
    #                         </system-services>
    #                         <system-services>
    #                             <name>dhcp</name>
    #                             <except />
    #                         </system-services>
    #                     </host-inbound-traffic>
    #                     <interfaces>
    #                         <name>ge-0/0/3.0</name>
    #                     </interfaces>
    #                     <interfaces>
    #                         <name>ge-0/0/4.0</name>
    #                     </interfaces>
    #                     <screen>test_screen</screen>
    #                     <source-identity-log />
    #                     <tcp-rst />
    #                 </security-zone>
    #             </zones>
    #         </security>
    #     </configuration>
    # </rpc-reply>
    #
    - name: Parse security zones running config
      junipernetworks.junos.junos_security_zones:
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
    #     "functional_zone_management": {
    #         "description": "test description 2",
    #         "host_inbound_traffic": {
    #             "protocols": [{"name": "all"}, {"except": True, "name": "bgp"}, {"except": True, "name": "bfd"}],
    #             "system_services": [{"name": "all"}, {"except": True, "name": "dhcp"}, {"except": True, "name": "dhcpv6"}],
    #         },
    #         "interfaces": ["ge-0/0/1.0", "ge-0/0/2.0"],
    #         "screen": "test_screen",
    #     },
    #     "security_zones": [
    #         {
    #             "address_book": {
    #                 "address_sets": [
    #                     {"addresses": ["test_adr1", "test_adr2"], "name": "test_adrset1"},
    #                     {"addresses": ["test_adr3", "test_adr4"], "name": "test_adrset2"},
    #                     {
    #                         "address_sets": ["test_adrset1", "test_adrset2"],
    #                         "addresses": ["test_adr5"],
    #                         "description": "test description",
    #                         "name": "test_adrset3",
    #                     },
    #                 ],
    #                 "addresses": [
    #                     {"description": "test desc", "ip_prefix": "10.0.0.0/24", "name": "test_adr1"},
    #                     {"dns_name": {"ipv6_only": True, "name": "1.1.1.1"}, "name": "test_adr2"},
    #                     {"name": "test_adr3", "range_address": {"from": "10.2.0.1", "to": "10.2.0.2"}},
    #                     {"name": "test_adr4", "wildcard_address": "10.3.0.1/24"},
    #                     {"description": "test desc", "ip_prefix": "10.1.0.0/24", "name": "test_adr5"},
    #                 ],
    #             },
    #             "advance_policy_based_routing_profile": "test_profile",
    #             "application_tracking": True,
    #             "description": "test description",
    #             "enable_reverse_reroute": True,
    #             "host_inbound_traffic": {
    #                 "protocols": [{"name": "all"}, {"except": True, "name": "bgp"}],
    #                 "system_services": [{"name": "all"}, {"except": True, "name": "dhcp"}],
    #             },
    #             "interfaces": ["ge-0/0/3.0", "ge-0/0/4.0"],
    #             "name": "test_sec_zone1",
    #             "screen": "test_screen",
    #             "source_identity_log": True,
    #             "tcp_rst": True,
    #         },
    #         {"name": "test_sec_zone2", "source_identity_log": True, "tcp_rst": True},
    #     ],
    # }
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
                            <div>The resulting configuration after module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em>, <em>deleted</em> or <em>purged</em></td>
                <td>
                            <div>The configuration prior to the module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em>, <em>deleted</em> or <em>purged</em></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;rpc-reply&gt; &lt;configuration&gt; &lt;security&gt; &lt;policies&gt; &lt;global&gt; &lt;policy&gt; &lt;name&gt;test_glob_1&lt;/name&gt; &lt;match&gt; &lt;source-address&gt;any-ipv6&lt;/source-address&gt; &lt;destination-address&gt;any-ipv6&lt;/destination-address&gt; &lt;application&gt;any&lt;/application&gt; &lt;/match&gt; &lt;then&gt; &lt;deny /&gt; &lt;/then&gt; &lt;/policy&gt; &lt;/global&gt; &lt;/policies&gt; &lt;/security&gt; &lt;/configuration&gt; &lt;/rpc-reply&gt;&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when state is <em>gathered</em></td>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when state is <em>parsed</em></td>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when state is <em>rendered</em></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;rpc-reply&gt; &lt;configuration&gt; &lt;security&gt; &lt;policies&gt; &lt;global&gt; &lt;policy&gt; &lt;name&gt;test_glob_1&lt;/name&gt; &lt;match&gt; &lt;source-address&gt;any-ipv6&lt;/source-address&gt; &lt;destination-address&gt;any-ipv6&lt;/destination-address&gt; &lt;application&gt;any&lt;/application&gt; &lt;/match&gt; &lt;then&gt; &lt;deny /&gt; &lt;/then&gt; &lt;/policy&gt; &lt;/global&gt; &lt;/policies&gt; &lt;/security&gt; &lt;/configuration&gt; &lt;/rpc-reply&gt;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Pranav Bhatt (@pranav-bhatt)
