---
name: Feature
about: Suggest a new feature for a Juniper Ansible Collection module or plugin
title: "[FEATURE] "
labels: feature
assignees: ''
---

## Category

<!-- Check the one that applies -->

- [ ] Bug
- [x] Feature
- [ ] Task

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
| Module / plugin this feature applies to | <!-- e.g. juniper.device.config — or "new module" if proposing a new one --> |
| Plugin type | <!-- module / connection / callback / terminal / netconf --> |

---

## Summary

<!-- A clear and concise description of the feature you'd like to see. -->

---

## Motivation

<!-- Describe the problem or use case this feature would solve.
     Why is this important? Who else might benefit? -->

---

## Proposed Playbook / Task Usage

<!-- Show how you would expect to use the new feature in a playbook.
     This helps clarify the desired interface. -->

```yaml
---
- name: Example using the proposed feature
  hosts: junos_devices
  gather_facts: no
  collections:
    - juniper.device        # or junipernetworks.junos

  vars:
    # any variables relevant to the proposed feature

  tasks:
    - name: Proposed new task
      juniper.device.config:   # replace with the actual / proposed module FQCN
        # --- proposed new parameters ---
        # new_param1: value1
        # new_param2: value2
      register: result
```

---

## Inventory File (if applicable)

<!-- Provide a sanitized inventory snippet if the feature is connection- or inventory-specific. -->

```ini
[junos_devices]
device1 ansible_host=<redacted-ip>

[junos_devices:vars]
ansible_connection=netconf
ansible_network_os=junipernetworks.junos.junos
ansible_user=<redacted>
ansible_port=830
```

---

## Steps to Trigger the Current Limitation

<!-- Show what happens today without this feature, to illustrate why it is needed. -->

1. 
2. 
3. 

---

## Expected Behavior (with the new feature)

<!-- What should happen once the feature is implemented? -->

---

## Current Behavior (without the feature)

<!-- What happens today? Include any error messages or missing functionality. -->

```
<paste current output / error if applicable>
```

---

## Alternatives Considered

<!-- Describe any alternative solutions or workarounds you've considered and why they are insufficient. -->

---

## Junos Platform / RPC Details (if applicable)

| Field | Value |
|-------|-------|
| Platform(s) | <!-- e.g. MX, QFX, EX, SRX, vMX, cRPD --> |
| Junos version(s) | <!-- e.g. 21.4+, Junos Evolved --> |
| Relevant RPC / CLI command | <!-- e.g. get-route-information, show bgp summary --> |

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

<!-- Any other context, references, prior art, or screenshots about the feature request. -->

---

## Support

As Red Hat Ansible Certified Content, this collection is entitled to support through the **Ansible Automation Platform (AAP)** using the **Create issue** button on the top right corner of the [AAP support portal](https://access.redhat.com/support/cases/#/case/new).

If a support case cannot be opened with Red Hat and the collection has been obtained either from Galaxy or GitHub, there may be community help available on the [Ansible Forum](https://forum.ansible.com/).
