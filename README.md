## ABOUT

Juniper Networks provides support for using Ansible to deploy devices running the Junos operating system (Junos OS). The Juniper Networks Ansible library, which is hosted on the Ansible Galaxy website under the role [junos](https://galaxy.ansible.com/list#/roles/1116), enables you to use Ansible to perform specific operational and configuration tasks on devices running Junos OS, including installing and upgrading Junos OS, deploying specific devices in the network, loading configuration changes, retrieving information, and resetting, rebooting, or shutting down managed devices.  Please refer to [INSTALLATION](#installation) section for setup.

In addition to these modules, Since 2.1, Ansible natively include some [core modules for Junos](http://docs.ansible.com/ansible/list_of_network_modules.html#junos). Both Core and Galaxy modules can cohexist on the same platform.

## OVERVIEW OF MODULES

- **junos_get_facts** — Retrieve device-specific information from the host.
- **junos_commit** — Commit candidate configuration on device.
- **junos_get_config** — Retrieve configuration of device.
- **junos_install_config** — Modify the configuration of a device running Junos OS.
- **junos_install_os** — Install a Junos OS software package.
- **junos_rollback** — Rollback configuration of device.
- **junos_shutdown** — Shut down or reboot a device running Junos OS.
- **junos_srx_cluster** — Enable/Disable cluster mode for SRX devices
- **junos_zeroize** — Remove all configuration information on the Routing Engines and reset all key values on a device.
- **junos_get_table** - Retrieve data from a Junos device using Tables/Views
- **junos_ping** - execute ping on junos devices
- **junos_pmtud** - execute path MTU discovery on junos devices
- **junos_jsnapy** - Integrate JSNAPy to ansible which helps audit network devices
- **junos_rpc** — To execute RPC on device and save output locally
- **junos_cli** — To execute CLI on device and save output locally

### OVERVIEW OF PLUGINS

In addition to the modules listed above, a callback_plugin `jsnapy` is available for the module `junos_jsnapy`.

The callback_plugin `jsnapy` helps to print on the screen additional information regarding
 jsnapy failed tests.
For each failed test, a log will be printed after the RECAP of the playbook.  

> The plugin `jsnapy` is currently in **Experimental** stage, please provide feedback.

```
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
```

Callback plugins are not activated by default and needs to be manually added to the
configuration file under `[defaults]` with the variable `callback_whitelist`
```
[defaults]
callback_whitelist = jsnapy
```
## DOCUMENTATION

[Official documentation](http://www.juniper.net/techpubs/en_US/release-independent/junos-ansible/information-products/pathway-pages/index.html) (detailed information, includes examples)

[Ansible style documentation](http://junos-ansible-modules.readthedocs.org)


## INSTALLATION

This repo assumes you have the [DEPENDENCIES](#dependencies) installed on your system.  

### Ansible Galaxy Role
To download the latest released version of the junos role to the Ansible
server, execute the ansible-galaxy install command, and specify **Juniper.junos**.

```
[root@ansible-cm]# ansible-galaxy install Juniper.junos
- downloading role 'junos', owned by Juniper
- downloading role from https://github.com/Juniper/ansible-junos-stdlib/archive/1.3.1.tar.gz
- extracting Juniper.junos to /usr/local/etc/ansible/roles/Juniper.junos
- Juniper.junos was installed successfully
```
You can also use the ansible-galaxy install command to install the latest
development version of the junos role directly from GitHub.
```
sudo ansible-galaxy install git+https://github.com/Juniper/ansible-junos-stdlib.git,,Juniper.junos
```

### Git clone
For testing you can `git clone` this repo and run the `env-setup` script in the repo directory:
```
user@ansible-junos-stdlib> source env-setup
```
This will set your `$ANSIBLE_LIBRARY` variable to the repo location and the installed Ansible library path.  For example:

```
[jeremy@ansible-junos-stdlib]$ echo $ANSIBLE_LIBRARY
/home/jeremy/Ansible/ansible-junos-stdlib/library:/usr/share/ansible
```
An alternative to the above is installing the role from GitHub using ansible-galaxy. The first step is creating a yaml file for
input data to ansible-galaxy. We'll use install_role.yml.

```yaml
---
- src: https://github.com/Juniper/ansible-junos-stdlib
  name: Juniper.junos
```

Now run `sudo ansible-galaxy install -r install_role.yml` to install the role.


### Docker
To run this as a Docker container, which includes JSNAPy and PyEZ, simply pull it from the Docker hub and run it. The following will pull the latest image and run it in an interactive ash shell.
```
$ docker run -it --rm juniper/pyez-ansible ash
```
Although, you'll probably want to bind mount a host directory (perhaps the directory containing your playbooks and associated files). The following will bind mount the current working directory and start the ash shell.
```
$ docker run -it --rm -v $PWD:/playbooks ash
```
You can also use the container as an executable to run your playbooks. Let's assume we have a typical playbook structure as below:
```
example
|playbook.yml
|hosts
|-vars
|-templates
|-scripts
```
We can move to the example directory and run the playbook with the following command:
```
$ docker run -it --rm -v $PWD:/playbooks juniper/pyez-ansible ansible-playbook -i hosts playbook.yml
```
You may have noticed that the base command is almost always the same. We can also use an alias to save some keystrokes.
```
$ alias pb-ansible="docker run -it --rm -v $PWD:/playbooks juniper/pyez-ansible ansible-playbook"
$ pb-ansible -i hosts playbook.yml
```

## Example Playbook
This example outlines how to use Ansible to install or upgrade the software image on a device running Junos OS.

```yaml
---
- name: Install Junos OS
  hosts: dc1
  roles:
    - Juniper.junos
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
      junos_install_os:
        host: "{{ inventory_hostname }}"
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

Thes modules require the following to be installed on the Ansible server:

* Python 2.6 or 2.7
* [Ansible](http://www.ansible.com) 1.5 or later
* Junos [py-junos-eznc](https://github.com/Juniper/py-junos-eznc) 2.0.1 or
later (2.1.1 is recommended and required for some features)

## LICENSE

Apache 2.0

## CONTRIBUTORS

Juniper Networks is actively contributing to and maintaining this repo. Please contact jnpr-community-netdev@juniper.net for any queries.

*Contributors:*

[Nitin Kumar](https://github.com/vnitinv), [Stacy W Smith](https://github.com/stacywsmith), [David Gethings](https://github.com/dgjnpr), [Damien Garros](https://github.com/dgarros)

*Former Contributors:*

[Jeremy Schulman](https://github.com/jeremyschulman), [Rick Sherman](https://github.com/shermdog)
