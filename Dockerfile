FROM juniper/pyez:latest

ARG ver_ansible=2.7.9
ARG ver_jsnapy=1.3.2
ARG ver_ansible-stdlib=2.1.0

LABEL net.juniper.image.maintainer="Stephen Steiner <ssteiner@juniper.net>"
LABEL net.juniper.ansible.version=$ver_ansible
LABEL net.juniper.jsnapy.version=$ver_jsnapy
LABEL net.juniper.ansible.module.version=$ver_ansible-stdlib

RUN apk add --no-cache ca-certificates openssh-client build-base gcc g++ make python-dev py-pip &&\
    pip install --upgrade pip setuptools jxmlease ansible==$ver_ansible jsnapy==$ver_jsnapy &&\
    apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /root/.ansible/roles/Juniper.junos
COPY action_plugins action_plugins
COPY callback_plugins callback_plugins
COPY library library
COPY meta meta
COPY module_utils module_utils

WORKDIR /playbooks

VOLUME /playbooks