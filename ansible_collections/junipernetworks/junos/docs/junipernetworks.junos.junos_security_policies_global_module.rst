.. _junipernetworks.junos.junos_security_policies_global_module:


****************************************************
junipernetworks.junos.junos_security_policies_global
****************************************************

**Manage global security policy settings on Juniper JUNOS devices**


Version added: 2.9.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of global security policy settings on Juniper JUNOS devices



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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of security policies</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>deny-all</li>
                                    <li>permit-all</li>
                        </ul>
                </td>
                <td>
                        <div>Configure the default security policy that defines the actions the device takes on a packet that does not match any user-defined policy.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>policy_rematch</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable the device to reevaluate an active session when its associated security policy is modified. The session remains open if it still matches the policy that allowed the session initially.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
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
                        <div>Enable the device to reevaluate an active session when its associated security policy is modified. The session remains open if it still matches the policy that allowed the session initially.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extensive</b>
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
                        <div>When a policy is modified or deleted, extensive option checks if any suitable policy permit to keep these sessions alive.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>policy_stats</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure policies statistics.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
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
                        <div>Enable policies statistics.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_wide</b>
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
                        <div>Configure systemwide policies statistics.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pre_id_default_policy_action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures default policy actions that occur prior to dynamic application identification (AppID) when the packet matches the criteria.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the log details at session close time and session initialization time.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>session_close</b>
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
                        <div>Enable logging on session close time</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>session_init</b>
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
                        <div>Enable logging on session initialization time</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>session_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When you update a session, the session timeout is configured, which specifies the session timeout details in seconds.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timeout value for ICMP sessions (seconds)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timeout value for ICMP6 sessions (seconds)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ospf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timeout value for OSPF sessions (seconds)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>others</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timeout value for other sessions (seconds)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tcp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timeout value for TCP sessions (seconds)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>udp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timeout value for UDP sessions (seconds)</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>traceoptions</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of security policies</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary to configure the trace file options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>files</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum number of trace files</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Refine the output to include lines that contain the regular expression.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_world_readable</b>
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
                        <div>Log files can be accessed only by the user who configures the tracing operation.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The maximum tracefile size</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>world_readable</b>
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
                        <div>The world_readable option enables any user to read the file.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>flag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>configuration</li>
                                    <li>compilation</li>
                                    <li>ipc</li>
                                    <li>lookup</li>
                                    <li>routing-socket</li>
                                    <li>rules</li>
                        </ul>
                </td>
                <td>
                        <div>Trace operation to perform.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_remote_trace</b>
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
                        <div>Disable remote tracing.</div>
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
                        <div>The value of this option should be the output received from the JunOS device by executing the command <b>show security policies</b>.</div>
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
                                    <li>rendered</li>
                                    <li>gathered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required. behaviour for this module.</div>
                        <div>The state <em>replaced</em> will replace the running configuration with the provided configuration</div>
                        <div>The state <em>replaced</em> and state <em>overridden</em> have the same behaviour</div>
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
    # vagrant@vsrx# show security policies
    # default-policy {
    #   permit-all;
    # }
    #
    - name: Update the running configuration with provided configuration
      junipernetworks.junos.junos_security_policies_global:
        config:
          policy_rematch:
            enable: true
          policy_stats:
            enable: true
          pre_id_default_policy_action:
            log:
              session_init: true
            session_timeout:
              icmp: 10
              others: 10
          traceoptions:
            file:
              files: 4
              match: /[A-Z]*/gm
              size: 10k
              no_world_readable: true
            flag: all
            no_remote_trace: true
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "after": {
    #     "default_policy": "permit-all",
    #     "policy_rematch": {
    #         "enable": true,
    #         "extensive": true
    #     },
    #     "policy_stats": {
    #         "enable": true,
    #         "system_wide": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 3,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
    # },
    # "before": {},
    # "changed": true,
    # "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:policies>
    #   <nc:policy-rematch> <nc:extensive/></nc:policy-rematch><nc:policy-stats>
    #   <nc:system-wide>enable</nc:system-wide></nc:policy-stats><nc:pre-id-default-policy>
    #   <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp>
    #   <nc:others>10</nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy>
    #   <nc:traceoptions><nc:file><nc:files>3</nc:files><nc:match>/[A-Z]*/gm</nc:match>
    #   <nc:size>10k</nc:size><nc:no-world-readable/></nc:file><nc:flag><nc:name>all
    #   </nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies></nc:security>"
    # After state
    # -----------
    #
    # vagrant@vsrx# show security policies
    # traceoptions {
    #   no-remote-trace;
    #   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
    #   flag all;
    # }
    # default-policy {
    #   permit-all;
    # }
    # policy-rematch extensive;
    # policy-stats;
    # pre-id-default-policy {
    #   then {
    #     log {
    #       session-init;
    #     }
    #     session-timeout {
    #       icmp 10;
    #       others 10;
    #     }
    #   }
    # }
    #
    #
    # Using Replaced
    # Before state
    # ------------
    #
    # vagrant@vsrx# show security policies
    # traceoptions {
    #   no-remote-trace;
    #   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
    #   flag all;
    # }
    # default-policy {
    #   permit-all;
    # }
    # policy-rematch extensive;
    # policy-stats;
    # pre-id-default-policy {
    #   then {
    #     log {
    #       session-init;
    #     }
    #     session-timeout {
    #       icmp 10;
    #       others 10;
    #     }
    #   }
    # }

    - name: Replace the running configuration with provided configuration
      junipernetworks.junos.junos_security_policies_global:
        config:
          default_policy: deny-all
          policy_rematch:
            enable: true
          policy_stats:
            enable: true
          pre_id_default_policy_action:
            log:
              session_init: true
            session_timeout:
              icmp: 10
              others: 10
          traceoptions:
            file:
              files: 4
              match: /[A-Z]*/gm
              size: 10k
              no_world_readable: true
            flag: all
            no_remote_trace: true
        state: replaced
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "after": {
    #     "default_policy": "deny-all",
    #     "policy_rematch": {
    #         "enable": true
    #     },
    #     "policy_stats": {
    #         "enable": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 4,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
    # },
    # "before": {
    #     "default_policy": "permit-all",
    #     "policy_rematch": {
    #         "enable": true,
    #         "extensive": true
    #     },
    #     "policy_stats": {
    #         "enable": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 4,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
    # },
    # "changed": true,
    # "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # <nc:policies delete="delete"/><nc:policies><nc:default-policy><nc:deny-all/></nc:default-policy>
    # <nc:policy-rematch> </nc:policy-rematch><nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy>
    # <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10
    # </nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file>
    # <nc:files>4</nc:files><nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/>
    # </nc:file><nc:flag><nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
    # </nc:security>"
    #
    # After state
    # -----------
    #
    # vagrant@vsrx# show security policies
    # traceoptions {
    #     no-remote-trace;
    #     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
    #     flag all;
    # }
    # default-policy {
    #     deny-all;
    # }
    # policy-rematch;
    # policy-stats;
    # pre-id-default-policy {
    #     then {
    #         log {
    #             session-init;
    #         }
    #         session-timeout {
    #             icmp 10;
    #             others 10;
    #         }
    #     }
    # }

    # Using overridden
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show security policies
    # traceoptions {
    #   no-remote-trace;
    #   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
    #   flag all;
    # }
    # default-policy {
    #   permit-all;
    # }
    # policy-rematch extensive;
    # policy-stats;
    # pre-id-default-policy {
    #   then {
    #     log {
    #       session-init;
    #     }
    #     session-timeout {
    #       icmp 10;
    #       others 10;
    #     }
    #   }
    # }

    - name: Replace the running configuration with provided configuration
      junipernetworks.junos.junos_security_policies_global:
        config:
          default_policy: deny-all
          policy_rematch:
            enable: true
          policy_stats:
            enable: true
          pre_id_default_policy_action:
            log:
              session_init: true
            session_timeout:
              icmp: 10
              others: 10
          traceoptions:
            file:
              files: 4
              match: /[A-Z]*/gm
              size: 10k
              no_world_readable: true
            flag: all
            no_remote_trace: true
        state: overridden
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "after": {
    #     "default_policy": "deny-all",
    #     "policy_rematch": {
    #         "enable": true
    #     },
    #     "policy_stats": {
    #         "enable": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 4,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
    # },
    # "before": {
    #     "default_policy": "permit-all",
    #     "policy_rematch": {
    #         "enable": true,
    #         "extensive": true
    #     },
    #     "policy_stats": {
    #         "enable": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 4,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
    # },
    # "changed": true,
    # "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # <nc:policies delete="delete"/><nc:policies><nc:default-policy><nc:deny-all/></nc:default-policy>
    # <nc:policy-rematch> </nc:policy-rematch><nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy>
    # <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10
    # </nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file>
    # <nc:files>4</nc:files><nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/>
    # </nc:file><nc:flag><nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
    # </nc:security>"
    #
    # After state
    # -----------
    #
    # vagrant@vsrx# show security policies
    # traceoptions {
    #     no-remote-trace;
    #     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
    #     flag all;
    # }
    # default-policy {
    #     deny-all;
    # }
    # policy-rematch;
    # policy-stats;
    # pre-id-default-policy {
    #     then {
    #         log {
    #             session-init;
    #         }
    #         session-timeout {
    #             icmp 10;
    #             others 10;
    #         }
    #     }
    # }
    #
    # Using deleted
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show security policies
    # traceoptions {
    #     no-remote-trace;
    #     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
    #     flag all;
    # }
    # default-policy {
    #     deny-all;
    # }
    # policy-rematch;
    # policy-stats;
    # pre-id-default-policy {
    #     then {
    #         log {
    #             session-init;
    #         }
    #         session-timeout {
    #             icmp 10;
    #             others 10;
    #         }
    #     }
    # }
    #
    - name: Delete the running configuration
      junipernetworks.junos.junos_security_policies_global:
        config:
        state: deleted
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "after": {},
    # "before": {
    #     "default_policy": "deny-all",
    #     "policy_rematch": {
    #         "enable": true
    #     },
    #     "policy_stats": {
    #         "enable": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 4,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
    # },
    # "changed": true,
    # "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #               <nc:policies delete="delete"/></nc:security>"
    #
    # After state
    # -----------
    #
    # vagrant@vsrx# show security policies
    #
    #
    # Using gathered
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show security policies
    # traceoptions {
    #     no-remote-trace;
    #     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
    #     flag all;
    # }
    # default-policy {
    #     deny-all;
    # }
    # policy-rematch;
    # policy-stats;
    # pre-id-default-policy {
    #     then {
    #         log {
    #             session-init;
    #         }
    #         session-timeout {
    #             icmp 10;
    #             others 10;
    #         }
    #     }
    # }
    #
    - name: Gather the running configuration
      junipernetworks.junos.junos_security_policies_global:
        config:
        state: gathered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    # "gathered": {
    #     "default_policy": "deny-all",
    #     "policy_rematch": {
    #         "enable": true
    #     },
    #     "policy_stats": {
    #         "enable": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 4,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
    # }
    #
    # Using rendered
    #
    # Before state
    # ------------
    #
    - name: Render the provided configuration
      junipernetworks.junos.junos_security_policies_global:
        config:
          default_policy: deny-all
          policy_rematch:
            enable: true
          policy_stats:
            enable: true
          pre_id_default_policy_action:
            log:
              session_init: true
            session_timeout:
              icmp: 10
              others: 10
          traceoptions:
            file:
              files: 4
              match: /[A-Z]*/gm
              size: 10k
              no_world_readable: true
            flag: all
            no_remote_trace: true
        state: replaced
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "rendered": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:policies>
    #     <nc:default-policy><nc:deny-all/></nc:default-policy><nc:policy-rematch> </nc:policy-rematch>
    #     <nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy><nc:then><nc:log><nc:session-init/>
    #     </nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10</nc:others></nc:session-timeout>
    #     </nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file><nc:files>4</nc:files>
    #     <nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/></nc:file><nc:flag>
    #     <nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
    #     </nc:security>"
    #
    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #    <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #       <version>18.4R1-S2.4</version>
    #         <security>
    #             <policies>
    #                 <traceoptions>
    #                     <no-remote-trace />
    #                     <file>
    #                         <size>10k</size>
    #                         <files>3</files>
    #                         <no-world-readable />
    #                         <match>/[A-Z]*/gm</match>
    #                     </file>
    #                     <flag>
    #                         <name>all</name>
    #                     </flag>
    #                 </traceoptions>
    #                 <default-policy>
    #                     <permit-all />
    #                 </default-policy>
    #                 <policy-rematch>
    #                     <extensive />
    #                 </policy-rematch>
    #                 <policy-stats>
    #                     <system-wide>enable</system-wide>
    #                 </policy-stats>
    #                 <pre-id-default-policy>
    #                     <then>
    #                         <log>
    #                             <session-init />
    #                         </log>
    #                         <session-timeout>
    #                             <icmp>10</icmp>
    #                             <others>10</others>
    #                         </session-timeout>
    #                     </then>
    #                 </pre-id-default-policy>
    #             </policies>
    #         </security>
    #     </configuration>
    # </rpc-reply>
    #
    #
    - name: Parse security policies global running config
      junipernetworks.junos.junos_security_policies_global:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "parsed": {
    #     "default_policy": "permit-all",
    #     "policy_rematch": {
    #         "enable": true,
    #         "extensive": true
    #     },
    #     "policy_stats": {
    #         "enable": true,
    #         "system_wide": true
    #     },
    #     "pre_id_default_policy_action": {
    #         "log": {
    #             "session_init": true
    #         },
    #         "session_timeout": {
    #             "icmp": 10,
    #             "others": 10
    #         }
    #     },
    #     "traceoptions": {
    #         "file": {
    #             "files": 3,
    #             "match": "/[A-Z]*/gm",
    #             "no_world_readable": true,
    #             "size": "10k"
    #         },
    #         "flag": "all",
    #         "no_remote_trace": true
    #     }
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em>, <em>deleted</em></td>
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em> or <em>deleted</em></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;rpc-reply&gt; &lt;configuration&gt; &lt;security&gt; &lt;policies&gt; &lt;default-policy&gt; &lt;permit-all /&gt; &lt;/default-policy&gt; &lt;/policies&gt; &lt;/security&gt; &lt;/configuration&gt; &lt;/rpc-reply&gt;&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;rpc-reply&gt; &lt;configuration&gt; &lt;security&gt; &lt;policies&gt; &lt;default-policy&gt; &lt;permit-all /&gt; &lt;/default-policy&gt; &lt;/policies&gt; &lt;/security&gt; &lt;/configuration&gt; &lt;/rpc-reply&gt;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Pranav Bhatt (@pranav-bhatt)
