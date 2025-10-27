.. _junipernetworks.junos.junos_prefix_lists_module:


****************************************
junipernetworks.junos.junos_prefix_lists
****************************************

**Manage prefix-lists attributes of interfaces on Junos devices.**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage prefix-lists attributes of interfaces on Junos network devices.



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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The provided link BGP address family dictionary.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_prefixes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify address prefixes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dynamic_db</b>
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
                        <div>Enable object to exist in dynamic DB.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specify the name of the prefix-list.</div>
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
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show policy-options</b>.</div>
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
    # vagrant@vsrx# show policy-options
    #
    # [edit]

    - name: Merge Junos prefix  lists
      junipernetworks.junos.junos_prefix_lists:
        config:
          - name: Internal
            address_prefixes:
              - 172.16.1.32
              - 172.16.3.32
          - name: Test1
            dynamic_db: true
          - name: Test2
            address_prefixes:
              - 172.16.2.32
              - 172.16.7.32
              - 172.16.9.32
        state: merged

    # Task Output
    # -------------
    #
    # before: []
    # commands:
    # - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # - "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item><nc:name>172.16.1.32</nc:name>"
    # - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.3.32</nc:name>"
    # - "</nc:prefix-list-item></nc:prefix-list><nc:prefix-list><nc:name>Test1</nc:name>"
    # - "<nc:dynamic-db/></nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name>"
    # - "<nc:prefix-list-item><nc:name>172.16.2.32</nc:name></nc:prefix-list-item>"
    # - "<nc:prefix-list-item><nc:name>172.16.7.32</nc:name></nc:prefix-list-item>"
    # - "<nc:prefix-list-item><nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
    # - "</nc:prefix-list></nc:policy-options>"
    # after:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal
    # - dynamic_db: true
    #   name: Test1
    # - address_prefixes:
    #   - 172.16.2.32/32
    #   - 172.16.7.32/32
    #   - 172.16.9.32/32
    #   name: Test2


    # After state
    # -----------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    # prefix-list Test1 {
    #     dynamic-db;
    # }
    # prefix-list Test2 {
    #     172.16.2.32/32;
    #     172.16.7.32/32;
    #     172.16.9.32/32;
    # }


    # Using gathered
    #
    # Before state
    # ------------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    # prefix-list Test1 {
    #     dynamic-db;
    # }
    # prefix-list Test2 {
    #     172.16.2.32/32;
    #     172.16.7.32/32;
    #     172.16.9.32/32;
    # }

    - name: Gather Junos prefix-lists
      junipernetworks.junos.junos_prefix_lists:
        state: gathered


    # Task Output
    # -------------
    #
    # gathered:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal
    # - dynamic_db: true
    #   name: Test1
    # - address_prefixes:
    #   - 172.16.2.32/32
    #   - 172.16.7.32/32
    #   - 172.16.9.32/32
    #   name: Test2


    # Using replaced


    # Before state
    # ------------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    # prefix-list Test1 {
    #     dynamic-db;
    # }
    # prefix-list Test2 {
    #     172.16.2.32/32;
    #     172.16.7.32/32;
    #     172.16.9.32/32;
    # }


    - name: Replace existing Junos prefix-lists configuration with provided config
      junipernetworks.junos.junos_prefix_lists:
        config:
          - name: Test2
            address_prefixes:
              - 172.16.4.32
              - 172.16.8.32
              - 172.16.9.32"
        state: replaced


    # Task Output
    # -------------
    #
    # before:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal
    # - dynamic_db: true
    #   name: Test1
    # - address_prefixes:
    #   - 172.16.2.32/32
    #   - 172.16.7.32/32
    #   - 172.16.9.32/32
    #   name: Test2
    # commands:
    # - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # - <nc:prefix-list delete="delete"><nc:name>Test2</nc:name></nc:prefix-list>
    # - "<nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item><nc:name>172.16.4.32</nc:name>"
    # - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.8.32</nc:name>"
    # - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.9.32</nc:name>"
    # - "</nc:prefix-list-item></nc:prefix-list></nc:policy-options>"
    # after:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal
    # - dynamic_db: true
    #   name: Test1
    # - address_prefixes:
    #   - 172.16.4.32/32
    #   - 172.16.8.32/32
    #   - 172.16.9.32/32
    #   name: Test2

    # After state
    # -----------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    # prefix-list Test1 {
    #     dynamic-db;
    # }
    # prefix-list Test2 {
    #     172.16.4.32/32;
    #     172.16.8.32/32;
    #     172.16.9.32/32;
    # }


    # Using overridden

    # Before state
    # ------------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    # prefix-list Test1 {
    #     dynamic-db;
    # }
    # prefix-list Test2 {
    #     172.16.4.32/32;
    #     172.16.8.32/32;
    #     172.16.9.32/32;
    # }


    - name: Override Junos prefix-lists configuration with provided configuration
      junipernetworks.junos.junos_prefix_lists:
        config:
          - name: Test2
            address_prefixes:
              - 172.16.4.32/28
              - 172.16.8.32/28
              - 172.16.9.32/28
        state: overridden


    # Task Output
    # -------------
    #
    # before:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal
    # - dynamic_db: true
    #   name: Test1
    # - address_prefixes:
    #   - 172.16.4.32/32
    #   - 172.16.8.32/32
    #   - 172.16.9.32/32
    #   name: Test2
    # commands:
    # - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # - <nc:prefix-list delete="delete"><nc:name>Internal</nc:name>
    # - </nc:prefix-list><nc:prefix-list delete="delete"><nc:name>Test1</nc:name>
    # - </nc:prefix-list><nc:prefix-list delete="delete"><nc:name>Test2</nc:name>
    # - "</nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item>"
    # - "<nc:name>172.16.4.32/28</nc:name></nc:prefix-list-item><nc:prefix-list-item>"
    # - "<nc:name>172.16.8.32/28</nc:name></nc:prefix-list-item><nc:prefix-list-item>"
    # - "<nc:name>172.16.9.32/28</nc:name></nc:prefix-list-item></nc:prefix-list></nc:policy-options>"
    # after:
    # - address_prefixes:
    #   - 172.16.4.32/28
    #   - 172.16.8.32/28
    #   - 172.16.9.32/28
    #   name: Test2

    # After state
    # -----------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Test2 {
    #     172.16.4.32/28;
    #     172.16.8.32/28;
    #     172.16.9.32/28;
    # }


    # Using deleted


    # Before state
    # ------------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    # prefix-list Test1 {
    #     dynamic-db;
    # }
    # prefix-list Test2 {
    #     172.16.2.32/32;
    #     172.16.7.32/32;
    #     172.16.9.32/32;
    # }


    - name: Delete provided prefix-lists
      junipernetworks.junos.junos_prefix_lists:
        config:
          - name: "Test1"
          - name: "Test2"
        state: deleted


    # Task Output
    # -------------
    #
    # before:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal
    # - dynamic_db: true
    #   name: Test1
    # - address_prefixes:
    #   - 172.16.2.32/32
    #   - 172.16.7.32/32
    #   - 172.16.9.32/32
    #   name: Test2
    # commands:
    # - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # - <nc:prefix-list delete="delete"><nc:name>Test1</nc:name></nc:prefix-list>
    # - <nc:prefix-list delete="delete"><nc:name>Test2</nc:name></nc:prefix-list></nc:policy-options>
    # after:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal


    # After state
    # -----------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    #


    # Using deleted without specifying config


    # Before state
    # ------------
    #
    # vagrant@vsrx# show policy-options
    # prefix-list Internal {
    #     172.16.1.32/32;
    #     172.16.3.32/32;
    # }
    # prefix-list Test1 {
    #     dynamic-db;
    # }
    # prefix-list Test2 {
    #     172.16.2.32/32;
    #     172.16.7.32/32;
    #     172.16.9.32/32;
    # }


    - name: Delete complete Junos prefix-lists configuration
      junipernetworks.junos.junos_prefix_lists:
        state: deleted


    # Task Output
    # -------------
    #
    # before:
    # - address_prefixes:
    #   - 172.16.1.32/32
    #   - 172.16.3.32/32
    #   name: Internal
    # - dynamic_db: true
    #   name: Test1
    # - address_prefixes:
    #   - 172.16.2.32/32
    #   - 172.16.7.32/32
    #   - 172.16.9.32/32
    #   name: Test2
    # commands:
    # - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # - <nc:prefix-list delete="delete"/></nc:policy-options>
    # after: []


    # After state
    # -----------
    #
    # vagrant@vsrx# show policy-options
    #
    # [edit]


    # Using parsed


    # parsed.cfg
    # ------------
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <version>18.4R1-S2.4</version>
    #         <policy-options>
    #         <prefix-list>
    #             <name>64510</name>
    #         </prefix-list>
    #         <prefix-list>
    #             <name>64500</name>
    #             <dynamic-db/>
    #             <prefix-list-item>
    #                 <name>172.16.1.16/28</name>
    #             </prefix-list-item>
    #             <prefix-list-item>
    #                 <name>172.16.1.32/28</name>
    #             </prefix-list-item>
    #         </prefix-list>
    #     </policy-options>
    #     </configuration>
    # </rpc-reply>


    - name: Parse running prefix-lists configuration
      junipernetworks.junos.junos_prefix_lists:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed


    # Task Output
    # -------------
    # parsed:
    # - name: '64510'
    # - address_prefixes:
    #   - 172.16.1.16/28
    #   - 172.16.1.32/28
    #   dynamic_db: true
    #   name: '64500'


    # Using rendered


    - name: Render the xml for provided  configuration
      junipernetworks.junos.junos_prefix_lists:
        config:
          - name: Internal
            address_prefixes:
              - 172.16.1.32
              - 172.16.3.32
          - name: Test1
            dynamic_db: true
          - name: Test2
            address_prefixes:
              - 172.16.2.32
              - 172.16.7.32
              - 172.16.9.32
        state: rendered


    # Task Output
    # -------------
    # rendered:
    # - <nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    # - "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item><nc:name>172.16.1.32</nc:name>"
    # - "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.3.32</nc:name>"
    # - "</nc:prefix-list-item></nc:prefix-list><nc:prefix-list><nc:name>Test1</nc:name>"
    # - "<nc:dynamic-db/></nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name>"
    # - "<nc:prefix-list-item><nc:name>172.16.2.32</nc:name></nc:prefix-list-item>"
    # - "<nc:prefix-list-item><nc:name>172.16.7.32</nc:name></nc:prefix-list-item>"
    # - "<nc:prefix-list-item><nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
    # - "</nc:prefix-list></nc:policy-options>"




Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
