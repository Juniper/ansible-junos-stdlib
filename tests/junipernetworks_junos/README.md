Functional Tests for Juniper Ansible Collection (junipernetworks.junos)

This directory contains a complete suite of functional tests for the modules in the junipernetworks.junos Ansible collection.

These playbooks verify behavior for each supported module using real Junos devices or virtual environments, following official module documentation examples. This ensures compatibility, schema adherence, and correctness across configuration states like merged, replaced, overridden, deleted, rendered, gathered, and parsed.

í ½í´§ Directory Structure

All functional test playbooks are located under:

tests/junipernetworks.junos/

Each playbook corresponds to one Ansible module, for example:

pb.juniper_junos_system.yml

pb.juniper_junos_lag_interfaces.yml

pb.juniper_junos_bgp_global.yml

etc.

Any required configuration files (e.g., parsed_configs/*.cfg) are also included.

í ¾í·ª Steps to Execute Functional Test Playbooks

1. Clone the Repository

git clone https://github.com/Juniper/ansible-junos-stdlib.git
cd ansible-junos-stdlib/tests/junipernetworks.junos

2. Ensure ansible.cfg is configured correctly

[defaults]
hash_behaviour = merge
inventory = inventory
host_key_checking = False
log_path = ./ansible.log

[persistent_connection]
command_timeout = 300

3. Inventory Setup (inventory)

The inventory file defines three connection types:

a. NETCONF (default)

[all]
all ansible_host=xx.xx.xx.xx

b. Local connection

[local_connection_testcases]
all ansible_connection=local ansible_network_os=none

c. Network CLI

[all]
junos_netconf_device ansible_host=xx.xx.xx.xx ansible_connection=network_cli ansible_network_os=junipernetworks.junos.junos ansible_user=xx ansible_password=xx

Global variables:

[all:vars]
ansible_python_interpreter=/path/to/venv/bin/python
ansible_connection=netconf
ansible_network_os=junipernetworks.junos.junos
ansible_user=xx
ansible_password=xx


4. Run a Functional Test

ansible-playbook pb.juniper_junos_l3_interfaces.yml

You can use -v or -vvv for verbose output and troubleshooting.

5. Run All Tests Automatically

To run all 38 functional tests in sequence, use the provided script:

./run_all_tests.sh


This script will:

Execute every test playbook under junipernetworks.junos/

Log results to ansible.log

Ensure a complete functional regression pass

Make sure the script is executable:

chmod +x run_all_tests.sh


