FROM juniper/pyez:latest

LABEL net.juniper.image.maintainer="Stephen Steiner <ssteiner@juniper.net>"

WORKDIR /tmp

RUN apk add --no-cache ca-certificates openssh-client build-base gcc g++ make

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /etc/ansible/roles/Juniper.junos
COPY action_plugins action_plugins
COPY callback_plugins callback_plugins
COPY library library
COPY meta meta
COPY module_utils module_utils

WORKDIR /playbooks

VOLUME /playbooks
