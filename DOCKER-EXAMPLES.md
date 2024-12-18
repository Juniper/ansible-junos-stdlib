# Examples of using the Docker image

To run this as a Docker container, which includes JSNAPy and PyEZ, simply pull it from the Docker hub and run it. The following will pull the latest image and run it in an interactive ash shell.

  docker run -it --rm juniper/pyez-ansible

Although, you'll probably want to bind mount a host directory (perhaps the directory containing your playbooks and associated files). The following will bind mount the current working directory and start the ash shell.

  docker run -it --rm -v $PWD:/project juniper/pyez-ansible

You can also use the container as an executable to run your playbooks. Let's assume we have a typical playbook structure as below:

    example
    |playbook.yml
    |hosts
    |-vars
    |-templates
    |-scripts

We can move to the example directory and run the playbook with the following command:

  cd example/
  docker run -it --rm -v $PWD:/playbooks juniper/pyez-ansible ansible-playbook -i hosts playbook.yml

You can pass any valid command string after the container name and it will be passed to Bash for execution.

You may have noticed that the base command is almost always the same. We can also use an alias to save some keystrokes.

  alias pb-ansible="docker run -it --rm -v $PWD:/project juniper/pyez-ansible ansible-playbook"
  pb-ansible -i hosts playbook.yml

### Extending the container with additional packages

It's possible to install additional OS (Alpine) packages, Python packages (via pip), and Ansible collections at container instantiation. This can be done by passing in environment variables or binding mount files.

#### OS Packages

Environment Variable: `$APK`
Bind Mount: `/extras/apk.txt`
File Format: list of valid Alpine packages, one per line
Examples:

As an environment variable, where the file containing a list of packages is in the current directory.

 docker run -it --rm -v $PWD:/project -e APK="apk.txt" juniper/pyez-ansible

As a bind mount.

  docker run -it --rm -v $PWD/apk.txt:/extras/apk.txt juniper/pyez-ansible

#### Python Packages

Environment Variable: `$REQ`
Bind Mount: `/extras/requirements.txt`
File Format: pip [requirements](https://pip.pypa.io/en/stable/reference/requirements-file-format/) file

Examples:

  docker run -it --rm -v $PWD:/project -e REQ="requirements.txt" juniper/pyez-ansible

As a bind mount.

  docker run -it --rm -v $PWD/requirements.txt:/extras/requirements.txt juniper/pyez-ansible

#### Ansible Packages

Environment Variable: `$COLLECTIONS`
Bind Mount: `/extras/requirements.yml`
File Format: Ansible [requirements](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html#install-multiple-collections-with-a-requirements-file) file


Examples:

  docker run -it --rm -v $PWD:/project -e REQ="requirements.yml" juniper/pyez-ansible

As a bind mount.

  docker run -it --rm -v $PWD/requirements.txt:/extras/requirements.yml juniper/pyez-ansible
