=======================================
Juniper Device Collection Release Notes
=======================================

===========================
Changelog for Juniper Device Ansible Collection
===========================

Version 1.0.8 (2025-04-30)
---------------------------
Enhancements
------------
- Supported juniper.device.software: VMHost device software upgrade with version check to use the details of "show vmhost version" (#709).
- Supported ansible-test sanity unit test and pytest framework (#718).
- Supported ansible-test network-integration framework (#713).
- Supported pre-commit hook #743
- Enhanced file_copy modules to support SCP, FTP, checksum and transfer-file

Bugs Fixed
----------
- Fixed typo in juniper.device.config module with format: "json" (#711).
- Fixed ansible-lint and PyEZ exception issues #738
- Fix to handle RPC response in JSON format of type <class 'dict'> #730

Version 1.0.7 (2024-12-19)
---------------------------
Enhancements
------------
- None.

Bugs Fixed
----------
- Fixed galaxy.yml "documentation" link (#692).
- Code formatting (trailing-whitespace removal, end-of-file-fixer, sort the import namespaces, Black validation) (#699, #701).
- Fixed version extraction from image filename for EX2300 firmware (#695).
- Fixed JSON response handling (#690, #703).
- Updated Dockerfile to include latest junos-eznc, jsnapy, and ansible modules (#707).
- Added DOCKER-EXAMPLES.md file.

Version 1.0.6 (2024-08-27)
---------------------------
Enhancements
------------
- Introduced `dest_dir` parameter to save the failed JSNAPy tests (#678).

Bugs Fixed
----------
- Fixed handling of ping failures when traffic-loss values are of type float (#672).
- Fixed `SyntaxWarning: invalid escape sequence '*'` emitted during ansible-playbook execution (#674).
- Fixed RPC exception handling when RPC is not supported on the platform while using persistent connection (#677).

Version 1.0.5 (2024-05-22)
---------------------------
Enhancements
------------
- Introduced new module `file_copy` to support SCP put and get options.

Bugs Fixed
----------
- Added timeout argument for configuration commit RPC (#607).
- Fixed ansible playbook coding style issues using ansible-lint tool (#623, #553).
- Support for relative paths for source configuration file added for PyEZ persistent connection (#580).
- Fixed exception handling for software install (#662).
- Fixed config module to perform all commit options (#660).

Version 1.0.4 (2024-04-30)
---------------------------
Enhancements
------------
- None.

Bugs Fixed
----------
- Added inventory template file to run ansible functional test cases for local and PyEZ persistent connection (#645).
- Updated command and config playbook-related test cases (#645).
- Fixed PyEZ connection rollback configuration issue (#645).
- Normalized value not passed correctly in PyEZ connection `rpc.ping()` API (#646).
- Fixed JSON encoder error "TypeError: Object of type function is not JSON serializable" (#647).
- Fixed persistent connection reboot exception handler for `ConnectionError` (#649).
- Module `snapy.py`: Added code for persistent PyEZ connection check and called `invoke_jsnapy` with required arguments (#650).
- Module `pyez.py`: Updated snapcheck — replaced `file_name` with `pre_file` argument (#650).

Version 1.0.3 (2024-01-25)
---------------------------
Enhancements
------------
- Supported configuration mode options: private, batch, dynamic, exclusive, and ephemeral (#635).
- Supported power-off functionality on VM host devices (#636).
- Supported installation of JUNOS package on specific member of VC (#613, #397).
- The Read the Docs build system will now require a configuration file `v2 (.readthedocs.yaml)` (#621).

Bugs Fixed
----------
- Updated the documentation link in `jsnapy.rst` and `snapy.py` (#612).
- Fixed issue where passing through credentials on the command line using `-u`, `-k`, or `--private-key` wasn't working after ansible-core 2.13 (#592).
- Fixed `Sphinx` object has no attribute 'add_stylesheet' with Sphinx 7.2.6 (#630).
- Fixed executing RPC with filters returning AttributeError: `'JuniperJunosModule' object has no attribute '_check_type_dict'` (#620).
- Fixed ansible PEZ exception issue when committing the configuration (#638).

Version 1.0.2 (2022-11-16)
---------------------------
Enhancements
------------
- Added changelogs (#596).
- Introduced `commit_sync` and `commit_force_sync` under `juniper.device.config` module (#525).

Bugs Fixed
----------
- Updated functional test playbooks (#598, #600, #603).

Version 1.0.1 (2021-10-05)
---------------------------
Bugs Fixed
----------
- Added `allow_bool_value` flag to be passed for RPC to support boolean values (#538).
- Fixed etree import issue when `libxml2` not installed (#558).

Version 1.0.0 (2021-04-23)
---------------------------
Features Added
--------------
- First release to support Junos modules for Ansible collections.

