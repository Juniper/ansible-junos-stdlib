### `junos_shutdown`

### Synopsis

Performs either a 'shutdown' or 'reboot' of the Junos device.

### Example Usage

````
  tasks:
    - name: Shutting down Junos
      junos_shutdown:
        host={{ inventory_hostname }}
        shutdown="shutdown"
````

### Options

| parameter 	| required 	| default 	| choices 	| description                                                                      	|
|-----------	|----------	|---------	|---------	|----------------------------------------------------------------------------------	|
| host      	| yes      	|         	|         	| This should be set to {{ inventory_hostname }}                                   	|
| user      	| no       	| $USER   	|         	| Login user-name                                                                  	|
| passwd    	| no       	| None    	|         	| Login password.  If not supplied, assumes that ssh-keys are installed and active 	|
| shutdown  	| yes      	| None    	|         	| You **MUST** set this to "shutdown" as a safe-guard                                	|
| reboot    	| no       	| no      	| yes, no 	| If `yes` then this action will cause a reboot, rather than a shutdown            	|
