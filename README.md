[![Documentation Status](https://readthedocs.org/projects/junos-ansible-modules/badge/?version=stable)](https://junos-ansible-modules.readthedocs.io/en/2.3.0/)

# Juniper Ansible collection for Junos

The repo is under active development.  If you take a clone, you are getting the latest, and perhaps not entirely stable code.  

## About

Juniper Networks supports Ansible for managing devices running the Junos operating system (Junos OS). 
This collection is hosted on the Ansible Galaxy website under the collection 
[Juniper.junos_collection](https://galaxy.ansible.com/Juniper/junos/). The Juniper.junos_collection collection includes 
a set of Ansible modules that perform specific operational and configuration tasks on devices running Junos OS. 
These tasks include:
installing and upgrading Junos OS, provisioning new Junos devices in the network, loading configuration changes,
retrieving information, and resetting, rebooting, or shutting down managed devices.  Please refer to the
[INSTALLATION](#installation) section for instructions on installing this collection.

## Juniper.junos roles by Juniper Networks

Ansible galaxy is upgrading to collections and plans to deprecate roles in future. The master branch will now have Juniper.junos_collection support. Juniper.junos roles have been moved to roles branch. Roles will be supported for now. For more information for roles, check: [https://github.com/Juniper/ansible-junos-stdlib/tree/roles](https://github.com/Juniper/ansible-junos-stdlib/tree/roles)

## Two Sets of Ansible Modules for Junos devices

Since Ansible version >= 2.1, Ansible also natively includes
[core modules for Junos](http://docs.ansible.com/ansible/list_of_network_modules.html#junos). The Junos modules included
in Ansible core have names which begin with the prefix `junos_`. The Junos modules included in this Juniper.junos_collection
collection have names which begin with the prefix `juniper_junos_`. These two sets of Junos modules can coexist on the same
Ansible control machine, and an Ansible play may invoke a module from either (or both) sets. Juniper Networks recommends
using the modules in this collection when writing new playbooks that manage Junos devices.

## Overview of Modules

This Juniper.junos_collection collection includes the following modules:

- **juniper_junos_command** — Execute one or more CLI commands on a Junos device.
- **juniper_junos_config** — Manipulate the configuration of a Junos device.
- **juniper_junos_facts** — Retrieve facts from a Junos device.
- **juniper_junos_jsnapy** — Execute JSNAPy tests on a Junos device.
- **juniper_junos_ping** — Execute ping from a Junos device.
- **juniper_junos_pmtud** — Perform path MTU discovery from a Junos device to a destination.
- **juniper_junos_rpc** — Execute one or more NETCONF RPCs on a Junos device.
- **juniper_junos_software** — Install software on a Junos device.
- **juniper_junos_srx_cluster** — Add or remove SRX chassis cluster configuration.
- **juniper_junos_system** — Initiate operational actions on the Junos system.
- **juniper_junos_table** — Retrieve data from a Junos device using a PyEZ table/view.

### PyEZ Version Requirement

For ansible collection junos_collection we will need to install junos-eznc(PyEZ) version 2.5.0 or higher. 

### Overview of Plugins

In addition to the modules listed above, a callback_plugin `jsnapy` is available for the module `juniper_junos_jsnapy`.

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

The `jsnapy` plugin is currently in **Experimental** stage, please provide feedback.

Callback plugins are not activated by default. They must be manually added to the Ansible
configuration file under the `[defaults]` section using the variable `callback_whitelist`. Specifically, these lines
should be added to the Ansible configuration file in order to allow the jsnapy callback plugin:

    [defaults]
    callback_whitelist = jsnapy

## DOCUMENTATION

[Official Juniper documentation](http://www.juniper.net/techpubs/en_US/release-independent/junos-ansible/information-products/pathway-pages/index.html) (detailed information, including examples)

[Ansible style documentation](http://junos-ansible-modules.readthedocs.org)

## INSTALLATION

You must have the [DEPENDENCIES](#dependencies) installed on your system.  

### NOTICES

### MacOS Mojave and newer

In MacOS Mojave and newer (>=10.14), ssh keys created with the system `ssh-keygen` are created using the newer 'OPENSSH' key format, even when specifying `-t rsa` during creation. This directly affects the usage of ssh keys, particularly when using the `ssh_private_key_file`. To create/convert/check keys, follow these steps:

- Create a new RSA key: `ssh-keygen -m PEM -t rsa -b 4096`
- Check existing keys: `head -n1 ~/.ssh/some_private_key` RSA keys will be `-----BEGIN RSA PRIVATE KEY-----` and OPENSSH keys will be `-----BEGIN OPENSSH PRIVATE KEY-----`
- Convert an OPENSSH key to an RSA key: `ssh-keygen -p -m PEM -f ~/.ssh/some_key`

### Ansible Galaxy collection

You can use the ansible-galaxy install command to install the latest
development version of the junos collection directly from GitHub.

  sudo ansible-galaxy collection install git+https://github.com/Juniper/ansible-junos-stdlib.git,,Juniper.junos_collection

### Git clone

For testing you can `git clone` this repo and run the `env-setup` script in the repo directory:

  user@ansible-junos-stdlib> source env-setup

This will set your `$ANSIBLE_LIBRARY` variable to the repo location and the installed Ansible library path.  For example:

  $ echo $ANSIBLE_LIBRARY
  /home/jeremy/Ansible/ansible-junos-stdlib/library:/usr/share/ansible

### Docker

To run this as a Docker container, which includes JSNAPy and PyEZ, simply pull it from the Docker hub and run it. The following will pull the latest image and run it in an interactive ash shell.

  docker run -it --rm juniper/pyez-ansible

Although, you'll probably want to bind mount a host directory (perhaps the directory containing your playbooks and associated files). The following will bind mount the current working directory and start the ash shell.

  docker run -it --rm -v $PWD:/project juniper/pyez-ansible

You can also use the container as an executable to run your playbooks. Let's assume we have a typical playbook structure as below:

    example
    |playbook.yml
    |hosts
    |-vars
    |-templates
    |-scripts

We can move to the example directory and run the playbook with the following command:

  cd example/
  docker run -it --rm -v $PWD:/playbooks juniper/pyez-ansible ansible-playbook -i hosts playbook.yml

You can pass any valid command string after the container name and it will be passed to Bash for execution.

You may have noticed that the base command is almost always the same. We can also use an alias to save some keystrokes.

  alias pb-ansible="docker run -it --rm -v $PWD:/project juniper/pyez-ansible ansible-playbook"
  pb-ansible -i hosts playbook.yml

### Extending the container with additional packages

It's possible to install additional OS (Alpine) packages, Python packages (via pip), and Ansible roles or collections at container instantiation. This can be done by passing in environment variables or bind mounting files.

#### OS Packages

Environment Variable: `$APK`
Bind Mount: `/extras/apk.txt`
File Format: list of valid Alpine packages, one per line
Examples:

As an environment variable, where the file containing a list of packages is in the current directory.

 docker run -it --rm -v $PWD:/project -e APK="apk.txt" juniper/pyez-ansible

As a bind mount.

  docker run -it --rm -v $PWD/apk.txt:/extras/apk.txt juniper/pyez-ansible

#### Python Packages

Environment Variable: `$REQ`
Bind Mount: `/extras/requirements.txt`
File Format: pip [requirements](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format) file

Examples:

  docker run -it --rm -v $PWD:/project -e REQ="requirements.txt" juniper/pyez-ansible

As a bind mount.

  docker run -it --rm -v $PWD/requirements.txt:/extras/requirements.txt juniper/pyez-ansible

#### Ansible Packages

Environment Variable: `$ROLES`
Bind Mount: `/extras/requirements.yml`
File Format: Ansible [requirements](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html#install-multiple-collections-with-a-requirements-file) file

_NOTE:_ This works for collections as well as roles.

Examples:

  docker run -it --rm -v $PWD:/project -e REQ="requirements.yml" juniper/pyez-ansible

As a bind mount.

  docker run -it --rm -v $PWD/requirements.txt:/extras/requirements.yml juniper/pyez-ansible

## Example Playbook

This example outlines how to use Ansible to install or upgrade the software image on a device running Junos OS.

```yaml
---
- name: Install Junos OS
  hosts: dc1
  collections:
    - Juniper.junos_collection
  connection: local
  gather_facts: no
  vars:
    wait_time: 3600
    pkg_dir: /var/tmp/junos-install
    OS_version: 14.1R1.10
    OS_package: jinstall-14.1R1.10-domestic-signed.tgz
    log_dir: /var/log/ansible

  tasks:
    - name: Checking NETCONF connectivity
      wait_for: host={{ inventory_hostname }} port=830 timeout=5
    - name: Install Junos OS package
      juniper_junos_software:
        reboot: yes
        version: "{{ OS_version }}"
        package: "{{ pkg_dir }}/{{ OS_package }}"
        logfile: "{{ log_dir }}/software.log"
      register: sw
      notify:
        - wait_reboot

  handlers:
    - name: wait_reboot
      wait_for: host={{ inventory_hostname }} port=830 timeout={{ wait_time }}
      when: not sw.check_mode
```

## DEPENDENCIES

This modules requires the following to be installed on the Ansible control machine:

- Python >= 2.7
- [Ansible](http://www.ansible.com) 2.3 or later
- Junos [py-junos-eznc](https://github.com/Juniper/py-junos-eznc) 2.1.7 or later
- [jxmlease](https://github.com/Juniper/jxmlease) 1.0.1 or later

## LICENSE

Apache 2.0

## SUPPORT

Support for this Juniper.junos_collection collection is provided by the community and Juniper Networks. If you have an
issue with a module in the Juniper.junos_collection collection, you may:

- Open a [GitHub issue](https://github.com/Juniper/ansible-junos-stdlib/issues).
- Post a question on our [Google Group](https://groups.google.com/forum/#!forum/junos-python-ez)
- Email [jnpr-community-netdev@juniper.net](jnpr-community-netdev@juniper.net)
- Open a [JTAC Case](https://www.juniper.net/casemanager/#/create)

Support for the Junos modules included in Ansible core is provided by Ansible. If you have an issue with an Ansible
core module you should open a [Github issue against the Ansible project](https://github.com/ansible/ansible/issues).

## CONTRIBUTORS

Juniper Networks is actively contributing to and maintaining this repo. Please contact
[jnpr-community-netdev@juniper.net](jnpr-community-netdev@juniper.net) for any queries.

*Contributors:*
[Nitin Kumar](https://github.com/vnitinv), [Rahul Kumar](https://github.com/rahkumar651991), [Stephen Steiner](https://github.com/ntwrkguru)

*Former Contributors:*

[Stacy W Smith](https://github.com/stacywsmith), [Jeremy Schulman](https://github.com/jeremyschulman), [Rick Sherman](https://github.com/shermdog), [Damien Garros](https://github.com/dgarros), [David Gethings](https://github.com/dgjnpr)
