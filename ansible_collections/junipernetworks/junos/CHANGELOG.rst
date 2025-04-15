==============================================
Junipernetworks Junos Collection Release Notes
==============================================

.. contents:: Topics

v9.1.0
======

Minor Changes
-------------

- Add implementation to gather ether-channels for gig-ether-options.
- Added support for virtual-switch instances.
- Based on ether-option-type create supported commands for config module.
- Implemented bridge-domains configuration management for routing instances.
- Implemented support for setting the Maximum Transmission Unit (MTU) in Layer 3 (L3) Internet Protocol (IP) interfaces.
- Tested successfully on Junos MX204.

Bugfixes
--------

- Fix the lag_interfaces facts for gigether supported model.

v9.0.0
======

Release Summary
---------------

Starting from this release, the minimum `ansible-core` version this collection requires is `2.15.0`. The last known version compatible with ansible-core<2.15 is v8.0.0.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

v8.0.0
======

Major Changes
-------------

- Update the netcommon base version 6.1.0 to support cli_restore plugin.

Minor Changes
-------------

- Add support for cli_restore functionality.
- Please refer the PR to know more about core changes (https://github.com/ansible-collections/ansible.netcommon/pull/618).
- cli_restore module is part of netcommon.

v7.0.0
======

Major Changes
-------------

- This release removes previously deprecated modules from this collection. Please refer to the **Removed Features** section for details.

Removed Features (previously deprecated)
----------------------------------------

- Remove deprected junos_logging module which is replaced by junos_logging_global resource module.

Bugfixes
--------

- Fix the empty facts list placement

v6.0.2
======

Bugfixes
--------

- acls
- initialize facts dictionary with empty containers for respective resources mentioned below
- lldp_global
- lldp_interfaces
- logging_global
- ntp_global
- ospf_interfaces
- ospfv2
- ospfv3
- prefix_lists
- routing_instances
- routing_options
- security_policies
- security_policies_global
- security_zones
- snmp_server
- static_routes
- vlans

Documentation Changes
---------------------

- Remove the part of the description which incorrectly describes the behavior and type of confirm attribute.
- Update example performing `confirm_commit`.
- Update with more examples using the `confirm` option to set a timer.

v6.0.1
======

Bugfixes
--------

- Prevents module_defaults from were being incorrectly applied to the platform action, instead of the concerned module.

v6.0.0
======

Release Summary
---------------

Starting from this release, the minimum `ansible-core` version this collection requires is `2.14.0`. That last known version compatible with ansible-core<2.14 is `v5.3.1`.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

v5.3.1
======

Bugfixes
--------

- fix to gather l2_interfaces facts with default port-mode access.

Documentation Changes
---------------------

- Improve docs of prefix-lists RM.
- ios_l2_interfaces - Fixed module documentation and examples.
- ios_l3_interfaces - Fixed module documentation and examples.

v5.3.0
======

Minor Changes
-------------

- add overridden state opperation support.

Bugfixes
--------

- fix `no_advertise_adjacency_segment` config implementation.
- fix `no_eligible_backup` config implementation.
- fix `no_eligible_remote_backup` config implementation.
- fix `no_interface_state_traps` config implementation.
- fix `no_neighbor_down_notification` config implementation.
- fix `node_link_protection` implementation.
- fix md5 authentication which allows list of keys to be configured.

v5.2.0
======

Minor Changes
-------------

- `junos_ospfv2` - Fix the authentication config when password is configured
- `junos_ospfv2` - Rename key ospf to ospfv2 in facts.
- `junos_ospfv2` - add area_ranges attribute which supports list of dict attributes.
- `junos_ospfv2` - add attributes `allow_route_leaking`, `stub_network` and `as-external` to overload dict.
- `junos_ospfv2` - add attributes `no_ignore_out_externals` to spf_options dict.
- `junos_ospfv2` - fix to gather reference_bandwidth and rfc1583compatibility.
- add acl_interfaces key for junos_facts output.

Deprecated Features
-------------------

- `junos_ospfv2` - add deprecate warning for area_range.
- add deprecate warning for junos_acl_interfaces key for junos facts results.

Documentation Changes
---------------------

- Update examples for junos_ospfv3

v5.1.0
======

Minor Changes
-------------

- Adding unlink option to junos package installation.

Bugfixes
--------

- Fix enabled attribute implementation.
- Fix lldp_global_assertion.
- Fix sanity issues.
- Fix the snmp view and traps configuration.
- fix the implementation of disabling interface.
- module should return with failure when rollback is 0 and device is not reachable.

Documentation Changes
---------------------

- Update bgp_address_family docs with examples.
- Update bgp_global docs with examples.
- junos_interfaces - Updated documentation with examples and task output.
- junos_static_routes - add task output to module documentation examples. (https://github.com/ansible-collections/junipernetworks.junos/pull/402).

v5.0.0
======

Major Changes
-------------

- change gathered key from junos_acls to acls

Bugfixes
--------

- enable provider support for junos_scp and junos_package.
- fix diff to result when prepared diff exists.
- fix junos_security_zones facts gathering when we have single interface configured.
- revert diff mode to default.

v4.1.0
======

Minor Changes
-------------

- Implement file_size as string.
- Used xmltodict to gather the sub-module chassis list and return it as a dictionary.

v4.0.0
======

Major Changes
-------------

- Use of connection: local and the provider option are no longer valid on any modules in this collection.

Removed Features (previously deprecated)
----------------------------------------

- Remove following deprecated Junos Modules.
- junos_interface
- junos_l2_interface
- junos_l3_interface
- junos_linkagg
- junos_lldp
- junos_lldp_interface
- junos_static_route
- junos_vlan

v3.1.0
======

Minor Changes
-------------

- Add mac-vrf instance type.

Bugfixes
--------

- fixes the nighbors list overwrite issue.

v3.0.1
======

Bugfixes
--------

- Fix incorrect param pass to to_text.

v3.0.0
======

Major Changes
-------------

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.
- `junos_facts` - change default gather_subset to `min` from `!config`.

Bugfixes
--------

- Fix junos_acl fact gathering when only destination port defined (https://github.com/ansible-collections/junipernetworks.junos/issues/268).

v2.10.0
=======

Minor Changes
-------------

- Added junos_security_policies module.
- Added junos_security_policies_global module.
- Added junos_security_zones module.

New Modules
-----------

- junos_security_policies - Create and manage security policies on Juniper JUNOS devices
- junos_security_policies_global - Manage global security policy settings on Juniper JUNOS devices
- junos_security_zones - Manage security zones on Juniper JUNOS devices

v2.9.0
======

Minor Changes
-------------

- Add junos_hostname resource module.
- Allow interfaces resource module to configure and gather logical interface description.

Bugfixes
--------

- Fix junos_command output when empty config response is received for show commands (https://github.com/ansible-collections/junipernetworks.junos/issues/249).

New Modules
-----------

- junos_hostname - Manage Hostname server configuration on Junos devices.
- junos_snmp_server - Manage SNMP server configuration on Junos devices.

v2.8.0
======

Minor Changes
-------------

- Add junos_routing_options resource module.
- Add junos_snmp_server resource module.

Deprecated Features
-------------------

- 'router_id' options is deprecated from junos_ospf_interfaces, junos_ospfv2 and junos_ospfv3 resuorce module.

New Modules
-----------

- junos_routing_options - Manage routing-options configuration on Junos devices.

v2.7.1
======

Bugfixes
--------

- Fix ospf router_id overlap issue.

v2.7.0
======

Documentation Changes
---------------------

- Add note for router_id deprecation from ospf-interfaces resource module.
- make sure router_id facts and config operation works fine for ospfv2 and ospfv3 RM

v2.6.0
======

Minor Changes
-------------

- Add junos_ntp_global resource module.

Deprecated Features
-------------------

- Deprecated router_id from ospfv2 resource module.

New Modules
-----------

- junos_ntp_global - Manage NTP configuration on Junos devices.

v2.5.0
======

Minor Changes
-------------

- Improve junos ospfv2 integration and unit tests coverage and router id assignment check implemented.
- Improve junos vlans integration and unit tests coverage and facts gathering logic modification.

Deprecated Features
-------------------

- Deprecated router_id from ospfv3 resource module.

v2.4.0
======

Minor Changes
-------------

- Add junos_logging_global Resource Module.
- Add support for backup_format option in junos_config
- support l3_interface in junos vlans

Deprecated Features
-------------------

- The junos_logging module has been deprecated in favor of the new junos_logging_global resource module and will be removed in a release after '2023-08-01'.

Bugfixes
--------

- fix lacp force-up without port-priority in junos_lacp_interfaces
- fix netconf test-case for lacp revert
- junos_acls failed to parse acl when multiple addresses defined within a single term (https://github.com/ansible-collections/junipernetworks.junos/issues/190)

New Modules
-----------

- junos_logging_global - Manage logging configuration on Junos devices.

v2.3.0
======

Minor Changes
-------------

- Add junos_prefix_lists Resource Module.

v2.2.0
======

Minor Changes
-------------

- Change src element from str to path for junos_scp.
- Improve junos_bgp_address_family unit test coverage.

v2.1.0
======

Minor Changes
-------------

- Add junos_routing_instances Resource Module.
- Add support for available_network_resources key, which allows to fetch the available resources for a platform (https://github.com/ansible-collections/junipernetworks.junos/issues/160).
- Replace unsupported parameter `vlan-id` in junipernetworks.junos.junos_vlans module with `vlan_id`

Security Fixes
--------------

- Mask values of sensitive keys in module result(https://github.com/ansible-collections/junipernetworks.junos/issues/165).

New Modules
-----------

- junos_routing_instances - Manage routing instances on Junos devices.

v2.0.1
======

Minor Changes
-------------

- Add support df_bit and size option for junos_ping (https://github.com/ansible-collections/junipernetworks.junos/pull/136).

v2.0.0
======

Major Changes
-------------

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

Minor Changes
-------------

- Add junos_bgp_address_family resource module.
- Add support for autonomous-system routing-options for bgp global and updating tests and documentation.
- Add support for bgp group and neighbors in bgp_global resource module.
- Add support for configuration caching (single_user_mode).
- Re-use device_info dictionary in cliconf.

New Modules
-----------

- junos_bgp_address_family - Manage BGP Address Family attributes of interfaces on Junos devices.

v1.3.0
======

Minor Changes
-------------

- Add junos bgp global resource module.
- Add ospf interfaces resource module.

Bugfixes
--------

- changing prefix list type to list and correcting facts gathering (https://github.com/ansible-collections/junipernetworks.junos/issues/131)
- constructing the facts based on the addresses per unit (https://github.com/ansible-collections/junipernetworks.junos/issues/111)
- release version added updated to 1.3.0 for junos_ospf_interfaces and junos_bgp_global module

New Modules
-----------

- junos_bgp_global - Manages BGP Global configuration on devices running Juniper JUNOS.
- junos_ospf_interfaces - OSPF Interfaces Resource Module.

v1.2.1
======

Bugfixes
--------

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Updating unit tests for resource modules (https://github.com/ansible-collections/junipernetworks.junos/pull/127)
- allowing partial config filter for junos commands (https://github.com/ansible-collections/junipernetworks.junos/issues/112)
- checking for units and family attributes in conf dictionary (https://github.com/ansible-collections/junipernetworks.junos/issues/121)

v1.2.0
======

Minor Changes
-------------

- Add ospfv3 resource module.

New Modules
-----------

- junos_ospfv3 - OSPFv3 resource module

v1.1.1
======

Minor Changes
-------------

- Use FQCN to M() references in modules documentation (https://github.com/ansible-collections/junipernetworks.junos/pull/79)

v1.1.0
======

Minor Changes
-------------

- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lacp.
- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lldp_global.
- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lldp_interfaces.
- Gathered state operation enabled, Parsed and rendered state operations implemented for ospfv2, acl_interfaces, vlans and static_routes RM.
- Gathered state operation enabled. Parsed and rendered state operations implemented.
- Gathered state operation enabledand Parsed and rendered state operations implemented.

Bugfixes
--------

- set_config called only when state is not gathered so that gathered opeartion works fine (https://github.com/ansible-collections/junipernetworks.junos/issues/89).
- set_config called only when state is not gathered so that gathered opeartion works fine (https://github.com/ansible-collections/junipernetworks.junos/issues/93).
- set_config called only when state is not gathered so that gathered opeartion works fine for l2_interfaces resource module (https://github.com/ansible-collections/junipernetworks.junos/issues/91).

v1.0.1
======

Bugfixes
--------

- Make `src`, `backup` and `backup_options` in junos_config work when module alias is used (https://github.com/ansible-collections/junipernetworks.junos/pull/83).
- Update docs after sanity fixes to modules.

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- junos - Use junos cliconf to run command on Juniper Junos OS platform

Netconf
~~~~~~~

- junos - Use junos netconf plugin to run netconf commands on Juniper JUNOS platform

New Modules
-----------

- junos_acl_interfaces - ACL interfaces resource module
- junos_acls - ACLs resource module
- junos_banner - Manage multiline banners on Juniper JUNOS devices
- junos_command - Run arbitrary commands on an Juniper JUNOS device
- junos_config - Manage configuration on devices running Juniper JUNOS
- junos_facts - Collect facts from remote devices running Juniper Junos
- junos_interfaces - Junos Interfaces resource module
- junos_l2_interfaces - L2 interfaces resource module
- junos_l3_interfaces - L3 interfaces resource module
- junos_lacp - Global Link Aggregation Control Protocol (LACP) Junos resource module
- junos_lacp_interfaces - LACP interfaces resource module
- junos_lag_interfaces - Link Aggregation Juniper JUNOS resource module
- junos_lldp_global - LLDP resource module
- junos_lldp_interfaces - LLDP interfaces resource module
- junos_logging - Manage logging on network devices
- junos_netconf - Configures the Junos Netconf system service
- junos_ospfv2 - OSPFv2 resource module
- junos_package - Installs packages on remote devices running Junos
- junos_ping - Tests reachability using ping from devices running Juniper JUNOS
- junos_rpc - Runs an arbitrary RPC over NetConf on an Juniper JUNOS device
- junos_scp - Transfer files from or to remote devices running Junos
- junos_static_routes - Static routes resource module
- junos_system - Manage the system attributes on Juniper JUNOS devices
- junos_user - Manage local user accounts on Juniper JUNOS devices
- junos_vlans - VLANs resource module
- junos_vrf - Manage the VRF definitions on Juniper JUNOS devices
