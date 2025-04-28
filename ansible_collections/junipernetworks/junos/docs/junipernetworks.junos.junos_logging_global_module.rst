.. _junipernetworks.junos.junos_logging_global_module:


******************************************
junipernetworks.junos.junos_logging_global
******************************************

**Manage logging configuration on Junos devices.**


Version added: 2.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages logging configuration on devices running Junos.



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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of logging configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_duplicates</b>
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
                        <div>Do not suppress the repeated message for all targets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify archive file information.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>binary_data</b>
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
                        <div>Mark file as if it contains binary data.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Size of files to be archived (65536..1073741824 bytes).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify number of files to be archived (1..1000).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_binary_data</b>
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
                        <div>Don&#x27;t mark file as if it contains binary data.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Don&#x27;t allow any user to read the log file.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Set archive file information.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Allow any user to read the log file.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>console</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set console logging parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>any</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set All facilities.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authorization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify authorization system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>change_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration change log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>conflict_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration conflict log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>daemon</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify various system processes.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dfc</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify dynamic flow capture.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Local external applications.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>firewall</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Firewall filtering system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ftp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify FTP process.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interactive_commands</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify commands executed by the UI.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>kernel</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Kernel specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ntp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify NTP process specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfe</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Packet Forwarding Engine specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Security related logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify user specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>files</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify files logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_duplicates</b>
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
                        <div>Do not suppress the repeated message for all targets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>any</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set All facilities.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify archive file information.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive_sites</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Primary and failover URLs to receive archive facilities.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>binary_data</b>
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
                        <div>Mark file as if it contains binary data.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Size of files to be archived (65536..1073741824 bytes).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Specify number of files to be archived (1..1000).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_binary_data</b>
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
                        <div>Don&#x27;t mark file as if it contains binary data.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Don&#x27;t allow any user to read the log file.</div>
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
                        <div>Set archive file information.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Specify start time for file transmission (yyyy-mm-dd.hh:mm).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transfer_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify frequency at which to transfer files to archive sites (5..2880 minutes).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Allow any user to read the log file.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authorization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify authorization system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>change_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration change log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>conflict_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration conflict log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>daemon</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify various system processes.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dfc</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify dynamic flow capture.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>explicit_priority</b>
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
                        <div>Include priority and facility in messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Local external applications.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>firewall</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Firewall filtering system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ftp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify FTP process.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interactive_commands</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify commands executed by the UI.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>kernel</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Kernel specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify regular expression for lines to be logged.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_strings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify matching string(s) for lines to be logged.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify filename in which to log data.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ntp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify NTP process specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfe</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Packet Forwarding Engine specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Security related logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>structured_data</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Log system message in structured format.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>brief</b>
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
                        <div>Omit English-language text from end of logged messages.</div>
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
                        <div>Set Log system message in structured format.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify user specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify hosts  to be notified.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_duplicates</b>
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
                        <div>Do not suppress the repeated message for all targets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>any</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set All facilities.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authorization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify authorization system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>change_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration change log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>conflict_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration conflict log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>daemon</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify various system processes.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dfc</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify dynamic flow capture.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>exclude_hostname</b>
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
                        <div>Specify exclude hostname field in messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>explicit_priority</b>
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
                        <div>Include priority and facility in messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Local external applications.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility_override</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify alternate facility for logging to remote host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>firewall</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Firewall filtering system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ftp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify FTP process.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interactive_commands</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify commands executed by the UI.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>kernel</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Kernel specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Prefix for all logging to this host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify regular expression for lines to be logged.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_strings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify matching string(s) for lines to be logged.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify the host name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ntp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify NTP process specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfe</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Packet Forwarding Engine specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify port number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify routing-instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Security related logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify address as source address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>structured_data</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Log system message in structured format.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>brief</b>
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
                        <div>Omit English-language text from end of logged messages.</div>
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
                        <div>Set Log system message in structured format.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify user specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_rotate_frequency</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Rotate log frequency (1..59 minutes).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Specify Routing routing-instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify syslog server logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>routing_instance</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>nable/disable syslog server in routing-instances.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>all</b>
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
                        <div>Enable/disable all routing instances.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default</b>
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
                        <div>Enable/disable default routing instances.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>routing_instances</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify routing-instances.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable</b>
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
                        <div>Disable syslog server in this routing instances.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Specify routing-instance name.</div>
                </td>
            </tr>


            <tr>
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
                        <div>Enable syslog server.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Specify address as source address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>time_format</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify additional information to include in system log timestamp.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>millisecond</b>
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
                        <div>Include milliseconds in timestamp.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Set time-format</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>year</b>
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
                        <div>Include year in timestamp.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>users</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify user logging</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_duplicates</b>
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
                        <div>Do not suppress the repeated message for all targets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>any</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set All facilities.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authorization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify authorization system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>change_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration change log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>conflict_log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify configuration conflict log.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>daemon</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify various system processes.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dfc</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify dynamic flow capture.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Local external applications.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>firewall</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Firewall filtering system.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ftp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify FTP process.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interactive_commands</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify commands executed by the UI.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>kernel</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Kernel specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specify regular expression for lines to be logged.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_strings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify matching string(s) for lines to be logged.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify user name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ntp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify NTP process specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfe</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Packet Forwarding Engine specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify Security related logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify user specific logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alert</li>
                                    <li>any</li>
                                    <li>critical</li>
                                    <li>emergency</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>none</li>
                                    <li>notice</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Set severity logging level.</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show system syslog</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
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
                                    <li>deleted</li>
                                    <li>overridden</li>
                                    <li>parsed</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
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
    # vagrant@vsrx# show system syslog
    #
    # [edit]
    # vagrant@vsrx# show routing-instances
    # inst11 {
    #     description inst11;
    # }
    - name: Merge provided logging configuration into running configuration.
      junipernetworks.junos.junos_logging_global:
        config:
          allow_duplicates: true
          archive:
            set: true
            no_binary_data: true
            files: 10
            file_size: 65578
            no_world_readable: true
          console:
            any:
              level: "info"
            authorization:
              level: "any"
            change_log:
              level: "critical"
            ftp:
              level: "none"
          files:
            - name: "file101"
              allow_duplicates: true
            - name: "file102"
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
            - name: "file103"
              archive:
                set: true
                no_binary_data: true
                files: 10
                file_size: 65578
                no_world_readable: true
              explicit_priority: true
              match: "^set*"
              match_strings:
                - "^delete"
                - "^prompt"
          hosts:
            - name: host111
              exclude_hostname: true
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
                brief: true
              facility_override: "ftp"
              log_prefix: "field"
              match: "^set*"
              match_strings:
                - "^delete"
                - "^prompt"
              port: 1231
              routing_instance: "inst11"
              source_address: "11.1.1.11"
          routing_instance: "inst11"
          log_rotate_frequency: 45
          source_address: "33.33.33.33"
          time_format:
            millisecond: true
            year: true
          users:
            - name: "user1"
              allow_duplicates: true
            - name: "user2"
              allow_duplicates: true
              any:
                level: "any"
              user:
                level: info
        state: merged
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "allow_duplicates": true,
    #         "archive": {
    #             "file_size": 65578,
    #             "files": 10,
    #             "no_binary_data": true,
    #             "no_world_readable": true
    #         },
    #         "console": {
    #             "any": {
    #                 "level": "info"
    #             },
    #             "authorization": {
    #                 "level": "any"
    #             },
    #             "change_log": {
    #                 "level": "critical"
    #             },
    #             "ftp": {
    #                 "level": "none"
    #             }
    #         },
    #         "files": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "file101"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "file102",
    #                 "structured_data": {
    #                     "set": true
    #                 }
    #             },
    #             {
    #                 "archive": {
    #                     "file_size": 65578,
    #                     "files": 10,
    #                     "no_binary_data": true,
    #                     "no_world_readable": true
    #                 },
    #                 "explicit_priority": true,
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "file103"
    #             }
    #         ],
    #         "hosts": [
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "exclude_hostname": true,
    #                 "facility_override": "ftp",
    #                 "log_prefix": "field",
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "host111",
    #                 "port": 1231,
    #                 "routing_instance": "inst11",
    #                 "source_address": "11.1.1.11",
    #                 "structured_data": {
    #                     "brief": true
    #                 }
    #             }
    #         ],
    #         "log_rotate_frequency": 45,
    #         "routing_instance": "inst11",
    #         "source_address": "33.33.33.33",
    #         "time_format": {
    #             "millisecond": true,
    #             "year": true
    #         },
    #         "users": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "user1"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "user2",
    #                 "user": {
    #                     "level": "info"
    #                 }
    #             }
    #         ]
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #         "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #         "<nc:syslog><nc:allow-duplicates/><nc:archive><nc:files>10</nc:files>"
    #         "<nc:no-binary-data/><nc:size>65578</nc:size><nc:no-world-readable/></nc:archive>"
    #         "<nc:console><nc:name>change-log</nc:name><nc:critical/></nc:console><nc:console>"
    #         "<nc:name>any</nc:name><nc:info/></nc:console><nc:console><nc:name>authorization</nc:name>"
    #         "<nc:any/></nc:console><nc:console><nc:name>ftp</nc:name><nc:none/></nc:console><nc:file>"
    #         "<nc:name>file101</nc:name><nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name>"
    #         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/>"
    #         "</nc:file><nc:file><nc:name>file103</nc:name><nc:archive><nc:files>10</nc:files><nc:no-binary-data/>"
    #         "<nc:size>65578</nc:size><nc:no-world-readable/></nc:archive><nc:explicit-priority/>"
    #         "<nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
    #         "<nc:match-strings>^prompt</nc:match-strings></nc:file><nc:host><nc:name>host111</nc:name>"
    #         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents>"
    #         "<nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
    #         "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
    #         "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
    #         "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
    #         "<nc:structured-data><nc:brief/></nc:structured-data></nc:host>"
    #         "<nc:log-rotate-frequency>45</nc:log-rotate-frequency><nc:routing-instance>inst11</nc:routing-instance>"
    #         "<nc:source-address>33.33.33.33</nc:source-address><nc:time-format><nc:millisecond/>"
    #         "<nc:year/></nc:time-format><nc:user><nc:name>user1</nc:name><nc:allow-duplicates/></nc:user>"
    #         "<nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/>"
    #         "</nc:contents><nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system syslog
    # archive size 65578 files 10 no-world-readable no-binary-data;
    # user user1 {
    #     allow-duplicates;
    # }
    # user user2 {
    #     any any;
    #     user info;
    #     allow-duplicates;
    # }
    # host host111 {
    #     any any;
    #     match "^set*";
    #     allow-duplicates;
    #     port 1231;
    #     facility-override ftp;
    #     log-prefix field;
    #     source-address 11.1.1.11;
    #     routing-instance inst11;
    #     exclude-hostname;
    #     match-strings [ "^delete" "^prompt" ];
    #     structured-data {
    #         brief;
    #     }
    # }
    # allow-duplicates;
    # file file101 {
    #     allow-duplicates;
    # }
    # file file102 {
    #     any any;
    #     allow-duplicates;
    #     structured-data;
    # }
    # file file103 {
    #     match "^set*";
    #     archive size 65578 files 10 no-world-readable no-binary-data;
    #     explicit-priority;
    #     match-strings [ "^delete" "^prompt" ];
    # }
    # console {
    #     any info;
    #     authorization any;
    #     ftp none;
    #     change-log critical;
    # }
    # time-format year millisecond;
    # source-address 33.33.33.33;
    # routing-instance inst11;
    # log-rotate-frequency 45;
    # Using replaced
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system syslog
    # archive size 65578 files 10 no-world-readable no-binary-data;
    # user user1 {
    #     allow-duplicates;
    # }
    # user user2 {
    #     any any;
    #     user info;
    #     allow-duplicates;
    # }
    # host host111 {
    #     any any;
    #     match "^set*";
    #     allow-duplicates;
    #     port 1231;
    #     facility-override ftp;
    #     log-prefix field;
    #     source-address 11.1.1.11;
    #     routing-instance inst11;
    #     exclude-hostname;
    #     match-strings [ "^delete" "^prompt" ];
    #     structured-data {
    #         brief;
    #     }
    # }
    # allow-duplicates;
    # file file101 {
    #     allow-duplicates;
    # }
    # file file102 {
    #     any any;
    #     allow-duplicates;
    #     structured-data;
    # }
    # file file103 {
    #     match "^set*";
    #     archive size 65578 files 10 no-world-readable no-binary-data;
    #     explicit-priority;
    #     match-strings [ "^delete" "^prompt" ];
    # }
    # console {
    #     any info;
    #     authorization any;
    #     ftp none;
    #     change-log critical;
    # }
    # time-format year millisecond;
    # source-address 33.33.33.33;
    # routing-instance inst11;
    # log-rotate-frequency 45;
    - name: Replaced running logging global configuration with provided configuration
      junipernetworks.junos.junos_logging_global:
        config:
          files:
            - name: "file104"
              allow_duplicates: true
            - name: "file102"
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
          hosts:
            - name: host222
              exclude_hostname: true
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
                brief: true
              facility_override: "ftp"
              log_prefix: "field"
              match: "^set*"
              match_strings:
                - "^delete"
                - "^prompt"
              port: 1231
              routing_instance: "inst11"
              source_address: "11.1.1.11"
          users:
            - name: "user1"
              allow_duplicates: true
            - name: "user2"
              allow_duplicates: true
              any:
                level: "any"
              user:
                level: info
        state: replaced
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "files": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "file104"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "file102",
    #                 "structured_data": {
    #                     "set": true
    #                 }
    #             }
    #         ],
    #         "hosts": [
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "exclude_hostname": true,
    #                 "facility_override": "ftp",
    #                 "log_prefix": "field",
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "host222",
    #                 "port": 1231,
    #                 "routing_instance": "inst11",
    #                 "source_address": "11.1.1.11",
    #                 "structured_data": {
    #                     "brief": true
    #                 }
    #             }
    #         ],
    #         "users": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "user1"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "user2",
    #                 "user": {
    #                     "level": "info"
    #                 }
    #             }
    #         ]
    #     },
    #     "before": {
    #         "allow_duplicates": true,
    #         "archive": {
    #             "file_size": 65578,
    #             "files": 10,
    #             "no_binary_data": true,
    #             "no_world_readable": true
    #         },
    #         "console": {
    #             "any": {
    #                 "level": "info"
    #             },
    #             "authorization": {
    #                 "level": "any"
    #             },
    #             "change_log": {
    #                 "level": "critical"
    #             },
    #             "ftp": {
    #                 "level": "none"
    #             }
    #         },
    #         "files": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "file101"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "file102",
    #                 "structured_data": {
    #                     "set": true
    #                 }
    #             },
    #             {
    #                 "archive": {
    #                     "file_size": 65578,
    #                     "files": 10,
    #                     "no_binary_data": true,
    #                     "no_world_readable": true
    #                 },
    #                 "explicit_priority": true,
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "file103"
    #             }
    #         ],
    #         "hosts": [
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "exclude_hostname": true,
    #                 "facility_override": "ftp",
    #                 "log_prefix": "field",
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "host111",
    #                 "port": 1231,
    #                 "routing_instance": "inst11",
    #                 "source_address": "11.1.1.11",
    #                 "structured_data": {
    #                     "brief": true
    #                 }
    #             }
    #         ],
    #         "log_rotate_frequency": 45,
    #         "routing_instance": "inst11",
    #         "source_address": "33.33.33.33",
    #         "time_format": {
    #             "millisecond": true,
    #             "year": true
    #         },
    #         "users": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "user1"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "user2",
    #                 "user": {
    #                     "level": "info"
    #                 }
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #             "<nc:syslog delete="delete"/><nc:syslog><nc:file><nc:name>file104</nc:name>"
    #             "<nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name><nc:allow-duplicates/>"
    #             "<nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/></nc:file>"
    #             "<nc:host><nc:name>host222</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name>"
    #             "<nc:any/></nc:contents><nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
    #             "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match>"
    #             "<nc:match-strings>^delete</nc:match-strings>"
    #             "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
    #             "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
    #             "<nc:structured-data><nc:brief/></nc:structured-data></nc:host><nc:user><nc:name>user1</nc:name>"
    #             "<nc:allow-duplicates/></nc:user><nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents>"
    #             "<nc:name>any</nc:name><nc:any/></nc:contents>"
    #             "<nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system syslog
    # user user1 {
    #     allow-duplicates;
    # }
    # user user2 {
    #     any any;
    #     user info;
    #     allow-duplicates;
    # }
    # host host222 {
    #     any any;
    #     match "^set*";
    #     allow-duplicates;
    #     port 1231;
    #     facility-override ftp;
    #     log-prefix field;
    #     source-address 11.1.1.11;
    #     routing-instance inst11;
    #     exclude-hostname;
    #     match-strings [ "^delete" "^prompt" ];
    #     structured-data {
    #         brief;
    #     }
    # }
    # file file104 {
    #     allow-duplicates;
    # }
    # file file102 {
    #     any any;
    #     allow-duplicates;
    #     structured-data;
    # }
    # Using overridden
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system syslog
    # archive size 65578 files 10 no-world-readable no-binary-data;
    # user user1 {
    #     allow-duplicates;
    # }
    # user user2 {
    #     any any;
    #     user info;
    #     allow-duplicates;
    # }
    # host host111 {
    #     any any;
    #     match "^set*";
    #     allow-duplicates;
    #     port 1231;
    #     facility-override ftp;
    #     log-prefix field;
    #     source-address 11.1.1.11;
    #     routing-instance inst11;
    #     exclude-hostname;
    #     match-strings [ "^delete" "^prompt" ];
    #     structured-data {
    #         brief;
    #     }
    # }
    # allow-duplicates;
    # file file101 {
    #     allow-duplicates;
    # }
    # file file102 {
    #     any any;
    #     allow-duplicates;
    #     structured-data;
    # }
    # file file103 {
    #     match "^set*";
    #     archive size 65578 files 10 no-world-readable no-binary-data;
    #     explicit-priority;
    #     match-strings [ "^delete" "^prompt" ];
    # }
    # console {
    #     any info;
    #     authorization any;
    #     ftp none;
    #     change-log critical;
    # }
    # time-format year millisecond;
    # source-address 33.33.33.33;
    # routing-instance inst11;
    # log-rotate-frequency 45;
    - name: Override running logging global configuration with provided configuration
      junipernetworks.junos.junos_logging_global:
        config:
          files:
            - name: "file104"
              allow_duplicates: true
            - name: "file102"
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
          hosts:
            - name: host222
              exclude_hostname: true
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
                brief: true
              facility_override: "ftp"
              log_prefix: "field"
              match: "^set*"
              match_strings:
                - "^delete"
                - "^prompt"
              port: 1231
              routing_instance: "inst11"
              source_address: "11.1.1.11"
          users:
            - name: "user1"
              allow_duplicates: true
            - name: "user2"
              allow_duplicates: true
              any:
                level: "any"
              user:
                level: info
        state: overridden
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {
    #         "files": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "file104"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "file102",
    #                 "structured_data": {
    #                     "set": true
    #                 }
    #             }
    #         ],
    #         "hosts": [
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "exclude_hostname": true,
    #                 "facility_override": "ftp",
    #                 "log_prefix": "field",
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "host222",
    #                 "port": 1231,
    #                 "routing_instance": "inst11",
    #                 "source_address": "11.1.1.11",
    #                 "structured_data": {
    #                     "brief": true
    #                 }
    #             }
    #         ],
    #         "users": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "user1"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "user2",
    #                 "user": {
    #                     "level": "info"
    #                 }
    #             }
    #         ]
    #     },
    #     "before": {
    #         "allow_duplicates": true,
    #         "archive": {
    #             "file_size": 65578,
    #             "files": 10,
    #             "no_binary_data": true,
    #             "no_world_readable": true
    #         },
    #         "console": {
    #             "any": {
    #                 "level": "info"
    #             },
    #             "authorization": {
    #                 "level": "any"
    #             },
    #             "change_log": {
    #                 "level": "critical"
    #             },
    #             "ftp": {
    #                 "level": "none"
    #             }
    #         },
    #         "files": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "file101"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "file102",
    #                 "structured_data": {
    #                     "set": true
    #                 }
    #             },
    #             {
    #                 "archive": {
    #                     "file_size": 65578,
    #                     "files": 10,
    #                     "no_binary_data": true,
    #                     "no_world_readable": true
    #                 },
    #                 "explicit_priority": true,
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "file103"
    #             }
    #         ],
    #         "hosts": [
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "exclude_hostname": true,
    #                 "facility_override": "ftp",
    #                 "log_prefix": "field",
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "host111",
    #                 "port": 1231,
    #                 "routing_instance": "inst11",
    #                 "source_address": "11.1.1.11",
    #                 "structured_data": {
    #                     "brief": true
    #                 }
    #             }
    #         ],
    #         "log_rotate_frequency": 45,
    #         "routing_instance": "inst11",
    #         "source_address": "33.33.33.33",
    #         "time_format": {
    #             "millisecond": true,
    #             "year": true
    #         },
    #         "users": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "user1"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "user2",
    #                 "user": {
    #                     "level": "info"
    #                 }
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #             "<nc:syslog delete="delete"/><nc:syslog><nc:file><nc:name>file104</nc:name>"
    #             "<nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name><nc:allow-duplicates/>"
    #             "<nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/></nc:file>"
    #             "<nc:host><nc:name>host222</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name>"
    #             "<nc:any/></nc:contents><nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
    #             "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match>"
    #             "<nc:match-strings>^delete</nc:match-strings>"
    #             "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
    #             "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
    #             "<nc:structured-data><nc:brief/></nc:structured-data></nc:host><nc:user><nc:name>user1</nc:name>"
    #             "<nc:allow-duplicates/></nc:user><nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents>"
    #             "<nc:name>any</nc:name><nc:any/></nc:contents>"
    #             "<nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system syslog
    # user user1 {
    #     allow-duplicates;
    # }
    # user user2 {
    #     any any;
    #     user info;
    #     allow-duplicates;
    # }
    # host host222 {
    #     any any;
    #     match "^set*";
    #     allow-duplicates;
    #     port 1231;
    #     facility-override ftp;
    #     log-prefix field;
    #     source-address 11.1.1.11;
    #     routing-instance inst11;
    #     exclude-hostname;
    #     match-strings [ "^delete" "^prompt" ];
    #     structured-data {
    #         brief;
    #     }
    # }
    # file file104 {
    #     allow-duplicates;
    # }
    # file file102 {
    #     any any;
    #     allow-duplicates;
    #     structured-data;
    # }
    # Using deleted
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system syslog
    # user user1 {
    #     allow-duplicates;
    # }
    # user user2 {
    #     any any;
    #     user info;
    #     allow-duplicates;
    # }
    # host host222 {
    #     any any;
    #     match "^set*";
    #     allow-duplicates;
    #     port 1231;
    #     facility-override ftp;
    #     log-prefix field;
    #     source-address 11.1.1.11;
    #     routing-instance inst11;
    #     exclude-hostname;
    #     match-strings [ "^delete" "^prompt" ];
    #     structured-data {
    #         brief;
    #     }
    # }
    # file file104 {
    #     allow-duplicates;
    # }
    # file file102 {
    #     any any;
    #     allow-duplicates;
    #     structured-data;
    # }
    - name: Delete running logging global configuration
      junipernetworks.junos.junos_logging_global:
        config:
        state: deleted
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "after": {},
    #     "before": {
    #         "files": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "file104"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "file102",
    #                 "structured_data": {
    #                     "set": true
    #                 }
    #             }
    #         ],
    #         "hosts": [
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "exclude_hostname": true,
    #                 "facility_override": "ftp",
    #                 "log_prefix": "field",
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "host222",
    #                 "port": 1231,
    #                 "routing_instance": "inst11",
    #                 "source_address": "11.1.1.11",
    #                 "structured_data": {
    #                     "brief": true
    #                 }
    #             }
    #         ],
    #         "users": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "user1"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "user2",
    #                 "user": {
    #                     "level": "info"
    #                 }
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #               "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #               "<nc:syslog delete="delete"/></nc:system>"
    #     ]
    # After state
    # -----------
    #
    # vagrant@vsrx# show system syslog
    #
    # [edit]
    # Using gathered
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show system syslog
    # user user1 {
    #     allow-duplicates;
    # }
    # user user2 {
    #     any any;
    #     user info;
    #     allow-duplicates;
    # }
    # host host222 {
    #     any any;
    #     match "^set*";
    #     allow-duplicates;
    #     port 1231;
    #     facility-override ftp;
    #     log-prefix field;
    #     source-address 11.1.1.11;
    #     routing-instance inst11;
    #     exclude-hostname;
    #     match-strings [ "^delete" "^prompt" ];
    #     structured-data {
    #         brief;
    #     }
    # }
    # file file104 {
    #     allow-duplicates;
    # }
    # file file102 {
    #     any any;
    #     allow-duplicates;
    #     structured-data;
    # }
    - name: Gather running logging global configuration
      junipernetworks.junos.junos_logging_global:
        state: gathered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "gathered": {
    #         "files": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "file104"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "file102",
    #                 "structured_data": {
    #                     "set": true
    #                 }
    #             }
    #         ],
    #         "hosts": [
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "exclude_hostname": true,
    #                 "facility_override": "ftp",
    #                 "log_prefix": "field",
    #                 "match": "^set*",
    #                 "match_strings": [
    #                     "^delete",
    #                     "^prompt"
    #                 ],
    #                 "name": "host222",
    #                 "port": 1231,
    #                 "routing_instance": "inst11",
    #                 "source_address": "11.1.1.11",
    #                 "structured_data": {
    #                     "brief": true
    #                 }
    #             }
    #         ],
    #         "users": [
    #             {
    #                 "allow_duplicates": true,
    #                 "name": "user1"
    #             },
    #             {
    #                 "allow_duplicates": true,
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "name": "user2",
    #                 "user": {
    #                     "level": "info"
    #                 }
    #             }
    #         ]
    #     },
    #     "changed": false,
    # Using rendered
    #
    # Before state
    # ------------
    #
    - name: Render xml for provided facts.
      junipernetworks.junos.junos_logging_global:
        config:
          allow_duplicates: true
          archive:
            set: true
            no_binary_data: true
            files: 10
            file_size: 65578
            no_world_readable: true
          console:
            any:
              level: "info"
            authorization:
              level: "any"
            change_log:
              level: "critical"
            ftp:
              level: "none"
          files:
            - name: "file101"
              allow_duplicates: true
            - name: "file102"
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
            - name: "file103"
              archive:
                set: true
                no_binary_data: true
                files: 10
                file_size: 65578
                no_world_readable: true
              explicit_priority: true
              match: "^set*"
              match_strings:
                - "^delete"
                - "^prompt"
          hosts:
            - name: host111
              exclude_hostname: true
              allow_duplicates: true
              any:
                level: "any"
              structured_data:
                set: true
                brief: true
              facility_override: "ftp"
              log_prefix: "field"
              match: "^set*"
              match_strings:
                - "^delete"
                - "^prompt"
              port: 1231
              routing_instance: "inst11"
              source_address: "11.1.1.11"
          routing_instance: "inst11"
          log_rotate_frequency: 45
          source_address: "33.33.33.33"
          time_format:
            millisecond: true
            year: true
          users:
            - name: "user1"
              allow_duplicates: true
            - name: "user2"
              allow_duplicates: true
              any:
                level: "any"
              user:
                level: info
        state: rendered
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #     "rendered": [
    #         "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
    #         "<nc:syslog><nc:allow-duplicates/><nc:archive><nc:files>10</nc:files>"
    #         "<nc:no-binary-data/><nc:size>65578</nc:size><nc:no-world-readable/></nc:archive>"
    #         "<nc:console><nc:name>change-log</nc:name><nc:critical/></nc:console><nc:console>"
    #         "<nc:name>any</nc:name><nc:info/></nc:console><nc:console><nc:name>authorization</nc:name>"
    #         "<nc:any/></nc:console><nc:console><nc:name>ftp</nc:name><nc:none/></nc:console><nc:file>"
    #         "<nc:name>file101</nc:name><nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name>"
    #         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/>"
    #         "</nc:file><nc:file><nc:name>file103</nc:name><nc:archive><nc:files>10</nc:files><nc:no-binary-data/>"
    #         "<nc:size>65578</nc:size><nc:no-world-readable/></nc:archive><nc:explicit-priority/>"
    #         "<nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
    #         "<nc:match-strings>^prompt</nc:match-strings></nc:file><nc:host><nc:name>host111</nc:name>"
    #         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents>"
    #         "<nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
    #         "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
    #         "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
    #         "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
    #         "<nc:structured-data><nc:brief/></nc:structured-data></nc:host>"
    #         "<nc:log-rotate-frequency>45</nc:log-rotate-frequency><nc:routing-instance>inst11</nc:routing-instance>"
    #         "<nc:source-address>33.33.33.33</nc:source-address><nc:time-format><nc:millisecond/>"
    #         "<nc:year/></nc:time-format><nc:user><nc:name>user1</nc:name><nc:allow-duplicates/></nc:user>"
    #         "<nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/>"
    #         "</nc:contents><nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
    #     ]
    # Using parsed
    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <system xmlns="http://yang.juniper.net/junos-es/conf/system">
    #         <syslog>
    #             <user>
    #                 <name>*</name>
    #                 <contents>
    #                     <name>any</name>
    #                     <emergency/>
    #                 </contents>
    #             </user>
    #             <file>
    #                 <name>messages</name>
    #                 <contents>
    #                     <name>any</name>
    #                     <any/>
    #                 </contents>
    #                 <contents>
    #                     <name>authorization</name>
    #                     <info/>
    #                 </contents>
    #             </file>
    #             <file>
    #                 <name>interactive-commands</name>
    #                 <contents>
    #                     <name>interactive-commands</name>
    #                     <any/>
    #                 </contents>
    #             </file>
    #         </syslog>
    #     </system>
    #     </configuration>
    # </rpc-reply>
    - name: Parse logging global running config
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
    # "parsed":  {
    #         "files": [
    #             {
    #                 "any": {
    #                     "level": "any"
    #                 },
    #                 "authorization": {
    #                     "level": "info"
    #                 },
    #                 "name": "messages"
    #             },
    #             {
    #                 "interactive_commands": {
    #                     "level": "any"
    #                 },
    #                 "name": "interactive-commands"
    #             }
    #         ],
    #         "users": [
    #             {
    #                 "any": {
    #                     "level": "emergency"
    #                 },
    #                 "name": "*"
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:allow-duplicates/&gt;&lt;/nc:user&gt;&lt;nc:user&gt;&lt;nc:name&gt;user2&lt;/nc:name&gt; &lt;nc:allow-duplicates/&gt;&lt;nc:contents&gt;&lt;nc:name&gt;any&lt;/nc:name&gt;&lt;nc:any/&gt; &lt;/nc:contents&gt;&lt;nc:contents&gt;&lt;nc:name&gt;user&lt;/nc:name&gt;&lt;nc:info/&gt;&lt;/nc:contents&gt; &lt;/nc:user&gt;&lt;/nc:syslog&gt;&lt;/nc:system&gt;&quot;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
