# Functional Tests for Juniper Ansible collection for Junos

Following are the steps to execute Ansible Functional test playbooks

## Steps to execute Ansible Functional test playbooks

1. Git clone the functional tests 
```
git clone https://github.com/Juniper/ansible-junos-stdlib.git
```
2. Change directory to ansible-junos-stdlib/tests
```
cd ansible-junos-stdlib/tests/
```
3. Update the ansible.cfg under tests directory 
```
[defaults]
hash_behaviour=merge
inventory = inventory
host_key_checking = False
log_path = ./ansible.log

[persistent_connection]
command_timeout = 300
```
4. To execute test playbook with Local connection, you need to update the inventory file for local connection test cases by setting ansible_connection=local
```
[junos]
local_connection_testcases  ansible_host=xx.xx.xx.xx  ansible_user=xyz  ansible_pass=xyz ansible_port=22 ansible_connection=local ansible_command_timeout=300

[all:vars]
ansible_python_interpreter=<Python interpreter path>
```
5. To execute test playbook with PyEZ persistent connection, you need to update the inventory file for persistent connection test cases by setting ansible_connection=juniper.device.pyez
``` 
[junos]
pyez_connection_testcases  ansible_host=xx.xx.xx.xx  ansible_user=xyz  ansible_ssh_pass=xyz ansible_port=22 ansible_connection=juniper.device.pyez ansible_command_timeout=300

[all:vars]
ansible_python_interpreter=<Python interpreter path>
```
6. To execute Functional test playbooks
ansible-playbook <playbook name>
```
ansible-playbook pb.juniper_junos_system.yml
```
### NOTE: 

To execute pb.juniper_junos_software_member.yml playbook, you have to use the following devices

Virtual Chassis - EX-VC, MX-VC 

To execute pb.juniper_junos_srx_cluster.yml playbook, you have to use the following devices

SRX HA Cluster enabled devices

### Ansible Fixes :
For the PyEZ persistent connection support, you need to apply the following fix for Ansible issue 
```
https://github.com/Juniper/ansible-junos-stdlib/issues/606
```