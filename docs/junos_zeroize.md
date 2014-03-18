### `junos_zeroize`

### Synopsis

Performs a Junos 'zeroize' command to wipe the system to factory state.  This action can be performed either over the NETCONF interface or over the CONSOLE interface (requires 'netconify').

*NOTE*: do not use at present.

### Example Usage

````
  tasks:
    - name: ZEROIZE Junos device, see-ya!
      junos_zeroize:
        host={{ inventory_hostname }}
        zeroize="zeroize"
````

### Options

| parameter 	| required 	| default 	| choices 	| description                                                                                                                                      	|
|-----------	|----------	|---------	|---------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| host      	| no       	|         	|         	| This should be set to {{ inventory_hostname }} when using NETCONF mode, not needed if using the `tty` parameter                                  	|
| user      	| no       	| $USER   	|         	| Login user-name                                                                                                                                  	|
| passwd    	| no       	| None    	|         	| Login password.  If not supplied, assumes that ssh-keys are installed and active                                                                 	|
| zeroize   	| yes      	| None    	|         	| You *MUST* set this to "zeroize" as a safe-guard                                                                                                 	|
| tty       	| no       	| None    	|         	| If set, this parameter is the same value passed to the `netconify` utility to issue the command over either the SERIAL port or a TERMINAL-SERVER 	|
