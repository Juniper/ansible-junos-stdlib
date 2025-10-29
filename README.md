[![Documentation Status](https://readthedocs.org/projects/junos-ansible-modules/badge/?version=stable)](https://junos-ansible-modules.readthedocs.io/en/2.3.0/)

# Juniper Ansible collection for Junos

## Description

Juniper Networks supports Ansible for managing devices running the Junos operating system (Junos OS and Junos Evolved).
This collection is hosted on the Ansible Galaxy website under the collection
[juniper.device](https://galaxy.ansible.com/ui/repo/published/juniper/device/).

The `juniper.device` collection includes a set of Ansible modules that perform specific operational and configuration tasks on devices running Junos OS.
These tasks include: installing and upgrading Junos OS, provisioning new Junos devices in the network, loading configuration changes,
retrieving information, and resetting, rebooting, or shutting down managed devices.  Please refer to the
[INSTALLATION](https://github.com/Juniper/ansible-junos-stdlib/blob/master/README.md#installation) section for instructions on installing this collection.

This collection is compatible with [junipernetworks.junos](https://github.com/ansible-collections/junipernetworks.junos) certified collection.

## Overview of Modules

This `juniper.device` collection includes the following modules:

- **command** — Execute one or more CLI commands on a Junos device.
- **config** — Manipulate the configuration of a Junos device.
- **facts** — Retrieve facts from a Junos device.
- **file_copy** - Copy the files from and to a Junos device.
- **jsnapy** — Execute JSNAPy tests on a Junos device.
- **ping** — Execute ping from a Junos device.
- **pmtud** — Perform path MTU discovery from a Junos device to a destination.
- **rpc** — Execute one or more NETCONF RPCs on a Junos device.
- **software** — Install software on a Junos device.
- **srx_cluster** — Add or remove SRX chassis cluster configuration.
- **system** — Initiate operational actions on the Junos system.
- **table** — Retrieve data from a Junos device using a PyEZ table/view.

### Overview of Plugins

In addition to the modules listed above, a callback_plugin `jsnapy` is available for the module [jsnapy](https://github.com/Juniper/jsnapy).

The callback_plugin `jsnapy` helps to print on the screen additional information regarding jsnapy failed tests.
For each failed test, a log will be printed after the RECAP of the playbook as shown in this example:

    PLAY RECAP *********************************************************************
    qfx10002-01                : ok=3    changed=0    unreachable=0    failed=1
    qfx10002-02                : ok=3    changed=0    unreachable=0    failed=1
    qfx5100-01                 : ok=1    changed=0    unreachable=0    failed=1

    JSNAPy Results for: qfx10002-01 ************************************************
    Value of 'peer-state' not 'is-equal' at '//bgp-information/bgp-peer' with {"peer-as": "65200", "peer-state": "Active", "peer-address": "100.0.0.21"}
    Value of 'peer-state' not 'is-equal' at '//bgp-information/bgp-peer' with {"peer-as": "60021", "peer-state": "Idle", "peer-address": "192.168.0.1"}
    Value of 'oper-status' not 'is-equal' at '//interface-information/physical-interface[normalize-space(admin-status)='up' and logical-interface/address-family/address-family-name ]' with {"oper-status": "down", "name": "et-0/0/18"}

    JSNAPy Results for: qfx10002-02 ************************************************
    Value of 'peer-state' not 'is-equal' at '//bgp-information/bgp-peer' with {"peer-as": "65200", "peer-state": "Active", "peer-address": "100.0.0.21"}

Callback plugins are not activated by default. They must be manually added to the Ansible
configuration file under the `[defaults]` section using the variable `callbacks_enabled = juniper.device.jsnapy`. Specifically, these lines
should be added to the Ansible configuration file in order to allow the jsnapy callback plugin:

    [defaults]
    callbacks_enabled = juniper.device.jsnapy 

[Official Juniper documentation](http://www.juniper.net/techpubs/en_US/release-independent/junos-ansible/information-products/pathway-pages/index.html) (detailed information, including examples)

[Ansible style documentation](https://ansible-juniper-collection.readthedocs.io)

## Requirements

This modules requires the following to be installed on the Ansible control machine:

- Python >= 3.8
- [Ansible](https://pypi.org/project/ansible/) 2.9 or later
- Junos [py-junos-eznc](https://github.com/Juniper/py-junos-eznc) 2.6.0 or later
- [jxmlease](https://github.com/Juniper/jxmlease) 1.0.1 or later
- [xmltodict](https://pypi.org/project/xmltodict/) 0.13.0 or later
- [jsnapy](https://github.com/Juniper/jsnapy) 1.3.7 or later

## Installation

You must have the [DEPENDENCIES](https://github.com/Juniper/ansible-junos-stdlib/blob/master/README.md#dependencies) installed on your system.
Check requirements.txt for the dependencies.

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```bash
ansible-galaxy collection install juniper.device
```

You can also include it in a requirements.yml file and install it with ansible-galaxy collection install -r requirements.yml, using the format:


```yaml
collections:
  - name: juniper.device
```

To upgrade the collection to the latest available version, run the following command:

```bash
ansible-galaxy collection install juniper.devie --upgrade
```

You can also install a specific version of the collection. Use the following syntax to install version 1.0.0:

```bash
ansible-galaxy collection install juniper.device:==1.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.


### Notices

### MacOS Mojave and newer

In MacOS Mojave and newer (>=10.14), ssh keys created with the system `ssh-keygen` are created using the newer 'OPENSSH' key format, even when specifying `-t rsa` during creation. This directly affects the usage of ssh keys, particularly when using the `ssh_private_key_file`. To create/convert/check keys, follow these steps:

- Create a new RSA key: `ssh-keygen -m PEM -t rsa -b 4096`
- Check existing keys: `head -n1 ~/.ssh/some_private_key` RSA keys will be `-----BEGIN RSA PRIVATE KEY-----` and OPENSSH keys will be `-----BEGIN OPENSSH PRIVATE KEY-----`
- Convert an OPENSSH key to an RSA key: `ssh-keygen -p -m PEM -f ~/.ssh/some_key`

## Use Cases

This example outlines how to use Ansible to install or upgrade the software image on a device running Junos OS.

```yaml
---
- name: Install Junos OS
  hosts: dc1
  connection: local
  gather_facts: false
  vars:
    wait_time: 3600
    pkg_dir: /var/tmp/junos-install
    os_version: 14.1R1.10
    os_package: jinstall-14.1R1.10-domestic-signed.tgz
    log_dir: /var/log/ansible

  tasks:
    - name: Checking NETCONF connectivity
      ansible.builtin.wait_for:
        host: "{{ inventory_hostname }}"
        port: 830
        timeout: 5
    - name: Install Junos OS package
      juniper.device.software:
        reboot: true
        version: "{{ os_version }}"
        package: "{{ pkg_dir }}/{{ os_package }}"
        logfile: "{{ log_dir }}/software.log"
      register: sw
      notify:
        - Wait_reboot

  handlers:
    - name: Wait_reboot
      ansible.builtin.wait_for:
        host: "{{ inventory_hostname }}"
        port: 830
        timeout: "{{ wait_time }}"
      when: not sw.check_mode
```

## Testing

[Please refer Funcational Tests](https://github.com/Juniper/ansible-junos-stdlib/tree/master/tests#readme)

## SUPPORT

As Red Hat Ansible Certified Content, this collection is entitled to support through the Ansible Automation Platform (AAP) using the **Create issue** button on the top right corner. If a support case cannot be opened with Red Hat and the collection has been obtained either from Galaxy or GitHub, there may community help available on the [Ansible Forum](https://forum.ansible.com/).

## Release Notes and Roadmap

[Release Notes](https://github.com/Juniper/ansible-junos-stdlib/blob/master/ansible_collections/juniper/device/CHANGELOG.rst)

## Contributing

Juniper Networks is actively contributing to and maintaining this repo. Please contact
[jnpr-community-netdev@juniper.net](jnpr-community-netdev@juniper.net) for any queries.

*Contributors:*
[Dinesh Babu](https://github.com/dineshbaburam91), [Chidanand Pujar](https://github.com/chidanandpujar)

*Former Contributors:*

[Stacy W Smith](https://github.com/stacywsmith), [Jeremy Schulman](https://github.com/jeremyschulman), [Rick Sherman](https://github.com/shermdog), [Damien Garros](https://github.com/dgarros), [David Gethings](https://github.com/dgjnpr), [Nitin Kumar](https://github.com/vnitinv), [Rahul Kumar](https://github.com/rahkumar651991), [Stephen Steiner](https://github.com/ntwrkguru)


## Support

As Red Hat Ansible Certified Content, this collection is entitled to support through the Ansible Automation Platform (AAP) using the **Create issue** button on the top right corner. If a support case cannot be opened with Red Hat and the collection has been obtained either from Galaxy or GitHub, there may community help available on the [Ansible Forum](https://forum.ansible.com/).

## License Information

Apache 2.0
