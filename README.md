___NOTICE___ - *Under Active Development*

## ABOUT

Ansible modules to support Junos network build automation use-cases.  Developed for Ansible 1.5.  This library is not currently part of the Ansible distribution.  Please refer to [INSTALLATION](#installation) section for setup.

For examples of using this module library, refer to the [Ansible + Junos FireFly](https://github.com/jeremyschulman/ansible-vsrx-demo) demo repository.

## OVERVIEW OF MODULES

This library contains the following Ansible modules.  For detailed usage on each module, refer to [docs](docs).

#### Build Automation modules

These are the primary modules used to install Junos OS softawre and deploy the initial configuration.  These modules require that the Junos device has NETCONF enabled.

* `junos_install_os` - Install the Junos OS image
* `junos_install_config` - Install the Junos configuraiton

#### Utility modules

* `junos_get_facts` - Retrieve the Junos "facts" from the device
* `junos_shutdown` - Perform a 'shutdown' or 'reboot' command
* `junos_zeroize` - Perform a 'zeroize' command factory reset the device

#### New Out of Box (NOOB) modules

These modules are used to programmatically control the Junos device via the XML/API over the CONSOLE port; i.e. using a serial port or a terminal server port.  The purpose of these modules are to "bootstrap" the Junos device with IP reachability and enable NETCONF.

* `junos_noob_config` - Install a noob config 
* `junos_noob_qfx_node` - Change the operating mode of a QFX switch to QFabric "node"

## INSTALLATION

This section, blah, blah, blah ....

## DEPENDENCIES

Thes modules require the following to be installed on the Ansible server:

* [Ansible](http://www.ansible.com) 1.5 or later
* Junos [py-junos-eznc](https://github.com/Juniper/py-junos-eznc) v0.0.5 or later
* Junos [netconify](https://github.com/jeremyschulman/py-junos-netconify) if you plan to use the 'noob' modules

