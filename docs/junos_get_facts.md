### `junos_get_facts`

### Synopsis

Retrieves the Junos device "facts" JSON dictionary.  This dictionary contains information like serial-number, product model, software version, etc.

### Example Usage

````
  tasks:
    - name: Get Junos Facts
      junos_get_facts:
        host={{ inventory_hostname }}
      register: junos
    - name: version
      debug: msg="{{ junos.facts.version }}"
````

### Options

| parameter 	| required 	| default 	| choices 	| description                                                                      	|
|-----------	|----------	|---------	|---------	|----------------------------------------------------------------------------------	|
| host      	| yes      	|         	|         	| This should be set to {{ inventory_hostname }}                                   	|
| user      	| no       	| $USER   	|         	| Login user-name                                                                  	|
| passwd    	| no       	| None    	|         	| Login password.  If not supplied, assumes that ssh-keys are installed and active 	|
