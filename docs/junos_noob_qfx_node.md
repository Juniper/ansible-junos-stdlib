### `junos_noob_config`

### Synopsis

Install a minimal New Out of Box (NOOB) configuration that should at least set the IP-address and enable the NETCONF service.  This action is performed over the device CONSOLE port using either a SERIAL-PORT or a TERMINAL-SERVER.  This action will also log the device "facts" and "inventory" to a local server directory, which then provdies you with specific details about the device located on that console.  Refer to [netconify](https://github.com/jeremyschulman/py-junos-netconify) for further details on this process.

### Example Usage

The following is a complete playbook illustrating the use of this action.  The `TERMSERV` and `TERMSERVPORT` variables would be taken from the host inventory specific for each device.

````
---
- name: Junos QFX Node Device Configuration
  hosts: qfx_nodes
  connection: local
  gather_facts: no

    logfile: /usr/local/junos/log/qfx_nodes.log

  tasks:
    - name: QFX {{mode}}-mode
      junos_noob_qfx_node:
        name={{ inventory_hostname }}
        port='-t={{TERMSERV}},{{TERMSERVPORT}}'
        mode=node
        logfile=/usr/local/junos/noob.log
        savedir=/usr/local/junos/inventory
````

### Options

| parameter 	| required 	| default 	| choices     	| description                                                                                                                                	|
|-----------	|----------	|---------	|-------------	|--------------------------------------------------------------------------------------------------------------------------------------------	|
| host      	| yes      	|         	|             	| This should be set to {{ inventory_hostname }}                                                                                             	|
| user      	| no       	| $USER   	|             	| Login user-name                                                                                                                            	|
| passwd    	| no       	| None    	|             	| Login password.  If not supplied, assumes that ssh-keys are installed and active                                                           	|
| file      	| yes      	| None    	|             	| File on the local server that contains the configuration change.                                                                           	|
| overrite  	| no       	| False   	| True, False 	| Determines if the `file` contents will completely replace the existing configuration (True) or a merged change (False)                     	|
| timeout   	| no       	| 0       	|             	| Temporarily change the NETCONF RPC timeout value.  This should be set if you know the configuration change may take longer that 30 seconds 	|
| logfile   	| no       	|         	|             	| File on the local server when progress and status is stored                                                                                	|
