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
      host=red_vsrx
      version=12.1X46-D10.2
      package=/usr/local/junos/images/junos-vsrx-12.1X46-D10.2-domestic.tgz
````

