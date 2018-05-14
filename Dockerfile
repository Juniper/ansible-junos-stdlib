FROM juniper/pyez:latest
MAINTAINER Stephen Steiner <ssteiner@juniper.net>

ARG ver_ansible=2.4.0.0
ARG ver_jsnapy=1.2.1

WORKDIR /tmp
RUN mkdir /tmp/ansible-junos-stdlib &&\
    mkdir /tmp/ansible-junos-stdlib/library &&\
    mkdir /tmp/ansible-junos-stdlib/meta &&\
    mkdir /project

ADD action_plugins /tmp/ansible-junos-stdlib/action_plugins
ADD callback_plugins /tmp/ansible-junos-stdlib/callback_plugins
ADD library /tmp/ansible-junos-stdlib/library
ADD LICENSE /tmp/ansible-junos-stdlib/LICENSE
ADD meta /tmp/ansible-junos-stdlib/meta
ADD module_utils /tmp/ansible-junos-stdlib/module_utils
ADD version.py /tmp/ansible-junos-stdlib/version.py



RUN tar -czf Juniper.junos ansible-junos-stdlib &&\
    apk update && apk add ca-certificates &&\
    apk add openssh-client &&\
    apk add build-base gcc g++ make python-dev &&\
    apk update && apk add py-pip &&\
    pip install --upgrade pip setuptools &&\
    pip install jxmlease &&\
    pip install ansible==$ver_ansible &&\
    pip install jsnapy==$ver_jsnapy &&\
    ansible-galaxy install --roles-path=/etc/ansible/roles Juniper.junos &&\
    apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /project
