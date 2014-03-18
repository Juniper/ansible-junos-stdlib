### `junos_noob_config`

*NOTE: do not use, under construction*

### Synopsis

Install a minimal New Out of Box (NOOB) configuration that should at least set the IP-address and enable the NETCONF service.  This action is performed over the device CONSOLE port using either a SERIAL-PORT or a TERMINAL-SERVER.  This action will also log the device "facts" and "inventory" to a local server directory, which then provdies you with specific details about the device located on that console.  Refer to [netconify](https://github.com/jeremyschulman/py-junos-netconify) for further details on this process.

### Example Usage

The following is a complete playbook illustrating the use of this action.  

````
  tasks:
    - name: Junos NOOB config
      junos_noob_config:
        name={{ inventory_hostname }}
        file=/usr/local/junos/noobconf/{{inventory_hostname}}/noob.conf
        port="-t={{TERMSERV}},{{TERMSERVPORT}}"

````
The `TERMSERV` and `TERMSERVPORT` variables would be taken from the host inventory specific for each device.

### Options

| parameter 	| required 	| default 	| choices 	| description                                                                                                                              	|
|-----------	|----------	|---------	|---------	|------------------------------------------------------------------------------------------------------------------------------------------	|
| name      	| yes      	|         	|         	| This should be set to {{ inventory_hostname }}                                                                                           	|
| port      	| yes      	|         	|         	| The port configuration per the `netconify` utility                                                                                       	|
| user      	| no       	| root    	|         	| Login user-name                                                                                                                          	|
| passwd    	| no       	| None    	|         	| Login password.  *MUST* be provided if this device has already been provisioned                                                          	|
| file      	| yes      	|         	|         	| Path to the Junos NOOB configuration file                                                                                                	|
| logfile   	| no       	|         	|         	| Path to the local server file where configuration change status is logged                                                                	|
| savedir   	| no       	| None    	|         	| Path to the local server directory where device facts and inventory files will be stored.  Refer to the `netconify` utility for details. 	|
