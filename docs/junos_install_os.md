### `junos_install_os`

### Synopsis

Install a Junos OS image on one or more routing-engine (RE) components.  This module supports single CPU devices, EX virtual-chassis (not-mixed mode), and MX dual-RE products.

Check-Mode is supported to report whether or not the current version matched the desired version.

If the existing version matches, no action is performed, and the "changed" attribute reports False.
If the existing version does not match, then the following actions are performed:

1.  Compuste the MD5 checksum of the package located on the server
2.  Copy the package image to the Junos device
3.  Compute the MD5 checksum on the Junos device and compare the two
4.  Install the Junos package
5.  Reboot the device (default)

### Example Usage

````
tasks:
   junos_install_os:
      host={{ inventory_hostname }}
      version=12.1X46-D10.2
      package=/usr/local/junos/images/junos-vsrx-12.1X46-D10.2-domestic.tgz
````

### Options

| parameter   | required | default | choices | description                                                                   |
|-------------|----------|---------|---------|-------------------------------------------------------------------------------|
| host        | yes      |         |         | This should be set to {{ inventory_hostname }}                                |
| user        | no       | $USER   |         | The username used during the NETCONF login process                            |
| passwd      | no       | None    |         | If not supplied, assumes that ssh-keys are installed and active               |
| version     | yes      | None    |         | The Junos version string as it would be reported by the "show version"        |
|             |          |         |         | command                                                                       |
| package     | yes      | None    |         | The complete path to the Junos package file (*.tgz) located on the            |
|             |          |         |         | ansible server                                                                |
| reboot      | no       | Yes     | Yes, No | Controls if the device will be rebooted after the software has been installed |
| reboot_wait | no       | 10      |         | Controls the amount of time (seconds) to pause execution after                |
|             |          |         |         | the reboot command has been issues; allows time for the reboot process        |
|             |          |         |         | to take effect                                                                |
|             |          |         |         |                                                                               |
