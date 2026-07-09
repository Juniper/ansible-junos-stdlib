---
name: Bug Report
about: Report a bug or unexpected behavior in a Juniper Ansible Collection
title: "[BUG] "
labels: bug
assignees: ''
---

## Category

<!-- Check the one that applies -->

- [x] Bug
- [ ] Feature
- [ ] Task

---

## Collection Namespace & Version

<!-- Run `ansible-galaxy collection list` to get the installed version -->

| Field | Value |
|-------|-------|
| Collection namespace | <!-- e.g. juniper.device or junipernetworks.junos --> |
| Collection version | <!-- e.g. 3.1.0 --> |
| Collection install path | <!-- e.g. ~/.ansible/collections/ansible_collections/juniper/device --> |

```bash
# How to find it:
ansible-galaxy collection list | grep -E 'juniper|junipernetworks'
```

---

## Module / Plugin Details

| Field | Value |
|-------|-------|
| Module / plugin name | <!-- e.g. juniper.device.config, junipernetworks.junos.junos_command --> |
| Module version (if shown in output) | <!-- e.g. from `ANSIBLE_DEBUG=1` output or module metadata --> |
| Plugin type | <!-- module / connection / callback / terminal / netconf --> |

```bash
# How to inspect module documentation:
ansible-doc juniper.device.config
```

---

## Description

<!-- A clear and concise description of the bug. What went wrong? -->

---

## Inventory File (sanitized)

<!-- Provide the inventory file or relevant section used when triggering the bug.
     Replace hostnames, IPs, usernames, and passwords with placeholders. -->

```ini
[junos_devices]
device1 ansible_host=<redacted-ip>

[junos_devices:vars]
ansible_connection=netconf            # or juniper.device, ansible.netcommon.netconf
ansible_network_os=junipernetworks.junos.junos   # or juniper.device
ansible_user=<redacted>
ansible_ssh_pass=<redacted>
ansible_port=830
```

<!-- If using a YAML inventory, paste that instead: -->

```yaml
# vars/inventory.yml (sanitized)
all:
  children:
    junos_devices:
      hosts:
        device1:
          ansible_host: <redacted-ip>
          ansible_user: <redacted>
          ansible_connection: netconf
          ansible_network_os: junipernetworks.junos.junos
          ansible_port: 830
```

---

## Playbook Details

<!-- Provide the full playbook or the minimal task snippet that triggers the bug.
     Remove any sensitive data (credentials, IPs, hostnames). -->

```yaml
---
- name: Reproduce the bug
  hosts: junos_devices
  gather_facts: no
  collections:
    - juniper.device        # or junipernetworks.junos

  vars:
    # any relevant variables

  tasks:
    - name: Failing task
      juniper.device.config:   # replace with the actual module FQCN
        # --- paste all task parameters below ---
        # param1: value1
        # param2: value2
      register: result

    - name: Debug output
      ansible.builtin.debug:
        var: result
```

<!-- Ansible command used to run the playbook: -->

```bash
ansible-playbook -i inventory playbook.yml -vvv
```

---

## Steps to Reproduce

<!-- Provide numbered steps so the issue can be reproduced reliably. -->

1. Install the collection: `ansible-galaxy collection install juniper.device==<version>`
2. Set up the inventory file as shown above.
3. Run the playbook: `ansible-playbook -i <inventory> <playbook>.yml`
4. <!-- Describe any additional step -->
5. Observe the error / unexpected behaviour.

---

## Expected Behavior

<!-- What did you expect the module / playbook to do?
     Be specific — e.g. "The task should apply the config and return changed=true" -->

---

## Actual Behavior

<!-- What actually happened? Include the full Ansible error, traceback, or unexpected output.
     Run with `-vvv` or `ANSIBLE_DEBUG=1` for maximum verbosity before pasting. -->

```
<paste full error output / traceback here>
```

<!-- Abbreviated one-line summary of the error (for quick scanning): -->
**Error summary:** <!-- e.g. "RPC error: device returned malformed XML" -->

---

## Environment

### Ansible & Python

| Item | Version |
|------|---------|
| ansible-core | <!-- e.g. 2.15.3 — run: ansible --version --> |
| Python | <!-- e.g. 3.12.2 — run: python3 --version --> |
| OS | <!-- e.g. Ubuntu 22.04, RHEL 9.2 --> |

### Collection & Python Package Versions

<!-- Run the commands below and paste the output -->

```bash
ansible-galaxy collection list | grep -E 'juniper|junipernetworks'
pip show junos-eznc ncclient paramiko lxml
```

```
# ansible-galaxy collection list output:

# pip show output:
junos-eznc    : <!-- version -->
ncclient      : <!-- version -->
paramiko      : <!-- version -->
lxml          : <!-- version -->
```

### Junos Device

| Item | Value |
|------|-------|
| Junos version | <!-- e.g. 22.2R1.9 — run: show version on device --> |
| Junos platform / model | <!-- e.g. MX480, vMX, QFX5100, SRX300, EX4300 --> |
| Transport | <!-- NETCONF over SSH / Console / Outbound SSH --> |
| NETCONF port | <!-- default 830 --> |

---

## Junos RPC / XML (if applicable)

<!-- If the bug is related to a specific RPC or XML response, include the raw XML.
     Capture with: ANSIBLE_DEBUG=1 ansible-playbook ... 2>&1 | tee debug.log -->

```xml
<!-- RPC request -->

<!-- RPC response / error -->
```

---

## Additional Context

<!-- Any other context, logs, screenshots, related issues, or workarounds you have found. -->

---

## Support

As Red Hat Ansible Certified Content, this collection is entitled to support through the **Ansible Automation Platform (AAP)** using the **Create issue** button on the top right corner of the [AAP support portal](https://access.redhat.com/support/cases/#/case/new).

If a support case cannot be opened with Red Hat and the collection has been obtained either from Galaxy or GitHub, there may be community help available on the [Ansible Forum](https://forum.ansible.com/).
