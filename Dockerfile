FROM juniper/pyez:latest
MAINTAINER Stephen Steiner <ssteiner@juniper.net>

ARG ver_ansible=2.3.0.0
ARG ver_jsnapy=1.1.0

WORKDIR /tmp
RUN mkdir /tmp/ansible-junos-stdlib &&\
    mkdir /tmp/ansible-junos-stdlib/library &&\
    mkdir /tmp/ansible-junos-stdlib/meta &&\
    mkdir /project

ADD library /tmp/ansible-junos-stdlib/library
ADD meta /tmp/ansible-junos-stdlib/meta

RUN tar -czf Juniper.junos ansible-junos-stdlib &&\
    apk update && apk add ca-certificates &&\
    apk add build-base gcc g++ make python-dev &&\
    pip install junos-netconify &&\
    pip install jxmlease &&\
    pip install -q ansible==$ver_ansible &&\
    pip install -q jsnapy==$ver_jsnapy &&\
    ansible-galaxy install Juniper.junos &&\
    apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /project
