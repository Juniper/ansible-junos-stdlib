---
name: Task
about: Suggest an improvement or task for a Juniper Ansible Collection module, plugin, or behaviour
title: "[TASK] "
labels: task
assignees: ''
---

## Category

<!-- Check the one that applies -->

- [ ] Bug
- [ ] Feature
- [x] Task

---

## Collection Namespace & Version

<!-- Run `ansible-galaxy collection list` to get the installed version -->

| Field | Value |
|-------|-------|
| Collection namespace | <!-- e.g. juniper.device or junipernetworks.junos --> |
| Collection version (current) | <!-- e.g. 3.1.0 --> |
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
| Module version (if shown in output) | <!-- from ANSIBLE_DEBUG=1 output or module metadata --> |
| Plugin type | <!-- module / connection / callback / terminal / netconf --> |

```bash
# Inspect current module documentation:
ansible-doc juniper.device.config
```

---

## Summary

<!-- A clear and concise description of the enhancement you'd like to see. -->

---

## Inventory File (sanitized)

<!-- Provide the inventory file or relevant section used when testing.
     Replace hostnames, IPs, usernames, and passwords with placeholders. -->

```ini
[junos_devices]
device1 ansible_host=<redacted-ip>

[junos_devices:vars]
ansible_connection=netconf            # or juniper.device, ansible.netcommon.netconf
ansible_network_os=junipernetworks.junos.junos
ansible_user=<redacted>
ansible_port=830
```

---

## Current Behaviour

<!-- Describe what the module/plugin currently does that you want to improve.
     Include the playbook snippet and actual output that demonstrates the limitation. -->

```yaml
---
- name: Current behaviour example
  hosts: junos_devices
  gather_facts: no
  collections:
    - juniper.device        # or junipernetworks.junos

  tasks:
    - name: Existing task showing the limitation
      juniper.device.config:   # replace with the actual module FQCN
        # current parameters
      register: result

    - name: Debug
      ansible.builtin.debug:
        var: result
```

```bash
# Command used:
ansible-playbook -i inventory playbook.yml -vvv
```

**Current output / limitation:**

```
<paste current output here>
```

---

## Steps to Reproduce the Current Limitation

1. 
2. 
3. 

---

## Expected Behavior (after enhancement)

<!-- What should the module/plugin do differently after the enhancement?
     Be specific — e.g. "Should return the diff as a structured dict instead of a raw string" -->

---

## Actual Behavior (current)

<!-- What does it do today that falls short? Include error messages or incomplete output. -->

```
<paste current output / error here>
```

---

## Proposed Improvement

<!-- Describe the change that would improve the existing behaviour.
     Include an updated playbook/task example showing the desired interface. -->

```yaml
---
- name: Improved behaviour example
  hosts: junos_devices
  gather_facts: no
  collections:
    - juniper.device        # or junipernetworks.junos

  tasks:
    - name: Enhanced task
      juniper.device.config:   # replace with the actual module FQCN
        # proposed improved / new parameters
      register: result
```

---

## Motivation

<!-- Explain why this enhancement is valuable. What problem does it solve?
     Who else would benefit from this change? -->

---

## Alternatives Considered

<!-- Describe any alternative approaches or workarounds and why they are insufficient. -->

---

## Junos Platform / RPC Details (if applicable)

| Field | Value |
|-------|-------|
| Platform(s) | <!-- e.g. MX, QFX, EX, SRX, vMX, cRPD --> |
| Junos version(s) | <!-- e.g. 21.4+, Junos Evolved --> |
| Relevant RPC / CLI command | <!-- e.g. get-interface-information --> |

---

## Environment

| Item | Version |
|------|---------|
| Collection namespace & version | <!-- e.g. juniper.device 3.1.0 --> |
| ansible-core | <!-- e.g. 2.15.3 — run: ansible --version --> |
| Python | <!-- e.g. 3.12.2 — run: python3 --version --> |
| OS | <!-- e.g. Ubuntu 22.04 --> |
| junos-eznc | <!-- run: pip show junos-eznc --> |
| ncclient | <!-- run: pip show ncclient --> |

---

## Additional Context

<!-- Any other context, references, or screenshots about the enhancement request. -->

---

## Support

As Red Hat Ansible Certified Content, this collection is entitled to support through the **Ansible Automation Platform (AAP)** using the **Create issue** button on the top right corner of the [AAP support portal](https://access.redhat.com/support/cases/#/case/new).

If a support case cannot be opened with Red Hat and the collection has been obtained either from Galaxy or GitHub, there may be community help available on the [Ansible Forum](https://forum.ansible.com/).
