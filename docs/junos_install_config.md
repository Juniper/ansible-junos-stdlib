### `junos_install_config`

### Synopsis

Install a Junos OS configuration.  This could either be a complete configuration (overrite) or a "snippet" of change.  The format of the file can either be Junos "set" commands, "curly-text" format, or XML format.  This module uses the file extention to determine the format:

* `.xml` = XML
* `.conf` = text
* `.set` = set

Check-Mode is supported.

If the configuration does not result in a change, then the "changed" flag will be `False`.


### Example Usage

````
  tasks:
    - name: Pushing banner config
      junos_install_config:
        host={{ inventory_hostname }}
        file=/var/tmp/banner.conf
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
