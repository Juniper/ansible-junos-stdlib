FROM juniper/pyez:latest

LABEL net.juniper.image.maintainer="Stephen Steiner <ssteiner@juniper.net>"

WORKDIR /tmp

RUN apk add --no-cache ca-certificates openssh-client build-base gcc g++ make \
    bash

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /usr/share/ansible/collections/
COPY ansible_collections/ .

WORKDIR /usr/bin
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Also install the roles, until collections is ready for prime-time
RUN ansible-galaxy role install Juniper.junos

WORKDIR /playbooks

VOLUME /playbooks

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
