.. _junipernetworks.junos.junos_lacp_module:


********************************
junipernetworks.junos.junos_lacp
********************************

**Global Link Aggregation Control Protocol (LACP) Junos resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of global LACP on Juniper Junos network devices.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
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
                        <div>A dictionary of LACP global options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_protection</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>revertive</li>
                                    <li>non-revertive</li>
                        </ul>
                </td>
                <td>
                        <div>Enable LACP link-protection for the system. If the value is set to <code>non-revertive</code> it will not revert links when a better priority link comes up. By default the link will be reverted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>LACP priority for the system.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show chassis aggregated-devices ethernet lacp</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
   - Tested against vSRX JUNOS version 18.1R1.
   - This module works with connection ``netconf``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.



Examples
--------

.. code-block:: yaml

    # Using deleted

    # Before state:
    # -------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection {
    #    non-revertive;
    # }

    - name: Delete global LACP attributes
      junipernetworks.junos.junos_lacp:
        state: deleted

    # After state:
    # ------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    #


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    #

    - name: Merge global LACP attributes
      junipernetworks.junos.junos_lacp:
        config:
          system_priority: 63
          link_protection: revertive
        state: merged

    # After state:
    # ------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection {
    #    non-revertive;
    # }


    # Using replaced

    # Before state:
    # -------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection {
    #    non-revertive;
    # }

    - name: Replace global LACP attributes
      junipernetworks.junos.junos_lacp:
        config:
          system_priority: 30
          link_protection: non-revertive
        state: replaced

    # After state:
    # ------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 30;
    # link-protection;
    #
    # Using gathered
    # Before state:
    # ------------
    #
    # ansible@cm123456tr21# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection;

    - name: Gather junos lacp as in given arguments
      junipernetworks.junos.junos_lacp:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": {
    #         "link_protection": "revertive",
    #         "system_priority": 63
    #     }
    # After state:
    # ------------
    #
    # ansible@cm123456tr21# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection;
    # Using rendered
    - name: Render platform specific xml from task input using rendered state
      junipernetworks.junos.junos_lacp:
        config:
          system_priority: 63
          link_protection: revertive
        state: rendered
    # Task Output (redacted)
    # -----------------------
    # "rendered": "<nc:chassis
    #     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #     <nc:aggregated-devices>
    #         <nc:ethernet>
    #             <nc:lacp>
    #                 <nc:system-priority>63</nc:system-priority>
    #                 <nc:link-protection>
    #                     <nc:non-revertive delete="delete"/>
    #                 </nc:link-protection>
    #             </nc:lacp>
    #         </nc:ethernet>
    #     </nc:aggregated-devices>
    # </nc:chassis>
    #
    # Using parsed
    # parsed.cfg
    # ------------
    #
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #     <chassis>
    #         <aggregated-devices>
    #             <ethernet>
    #                 <lacp>
    #                     <system-priority>63</system-priority>
    #                     <link-protection>
    #                     </link-protection>
    #                 </lacp>
    #             </ethernet>
    #         </aggregated-devices>
    #     </chassis>
    #     </configuration>
    # </rpc-reply>
    # - name: Convert lacp config to argspec without connecting to the appliance
    #   junipernetworks.junos.junos_lacp:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": {
    #         "link_protection": "revertive",
    #         "system_priority": 63
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
                      <span style="color: purple">dictionary</span>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:chassis xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:aggregated-devices&gt; &lt;nc:ethernet&gt; &lt;nc:lacp&gt; &lt;nc:system-priority&gt;63&lt;/nc:system-priority&gt; &lt;nc:link-protection&gt; &lt;nc:non-revertive delete=&quot;delete&quot;/&gt; &lt;/nc:link-protection&gt; &lt;/nc:lacp&gt; &lt;/nc:ethernet&gt; &lt;/nc:aggregated-devices&gt; &lt;/nc:chassis&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
