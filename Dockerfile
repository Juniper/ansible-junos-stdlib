FROM juniper/pyez:2.0.1
MAINTAINER ntwrkguru@gmail.com

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
    pip install ansible &&\
    pip install jsnapy &&\
    ansible-galaxy install Juniper.junos &&\
    apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /project
