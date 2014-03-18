### `junos_noob_qfx_node`

*NOTE: do not use, under construction*

### Synopsis

New Out of Box (NOOB) configuration that will change the "device mode" for a QFX switch.  For QFabric deployments, the QFX switch must be configured into 'node' mode.  This action is performed over the device CONSOLE port using either a SERIAL-PORT or a TERMINAL-SERVER.  This action will also log the device "facts" and "inventory" to a local server directory, which then provdies you with specific details about the device located on that console.  Refer to [netconify](https://github.com/jeremyschulman/py-junos-netconify) for further details on this process.

### Example Usage
````
  tasks:
    - name: QFX {{mode}}-mode
      junos_noob_qfx_node:
        name={{ inventory_hostname }}
        port='-t={{TERMSERV}},{{TERMSERVPORT}}'
        logfile=/usr/local/junos/noob.log
        savedir=/usr/local/junos/inventory
````

The `TERMSERV` and `TERMSERVPORT` variables would be taken from the host inventory specific for each device.

### Options

| parameter 	| required 	| default 	| choices      	| description                                                                                                                              	|
|-----------	|----------	|---------	|--------------	|------------------------------------------------------------------------------------------------------------------------------------------	|
| name      	| yes      	|         	|              	| This should be set to {{ inventory_hostname }}                                                                                           	|
| port      	| yes      	|         	|              	| The port configuration per the `netconify` utility                                                                                       	|
| user      	| no       	| root    	|              	| Login user-name                                                                                                                          	|
| passwd    	| no       	| None    	|              	| Login password.  *MUST* be provided if this device has already been provisioned                                                          	|
| mode      	| no       	| node    	| node, switch 	| Determines the device mode                                                                                                               	|
| logfile   	| no       	|         	|              	| Path to the local server file where configuration change status is logged                                                                	|
| savedir   	| no       	| None    	|              	| Path to the local server directory where device facts and inventory files will be stored.  Refer to the `netconify` utility for details. 	|
