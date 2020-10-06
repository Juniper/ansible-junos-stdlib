FROM juniper/pyez:2.4.0

LABEL net.juniper.image.maintainer="Stephen Steiner <ssteiner@juniper.net>" \
      net.juniper.image.description="Lightweight image with Ansible and the Junos roles"

RUN apk add --no-cache build-base python3-dev py3-pip \
    openssl-dev curl ca-certificates bash openssh-client

WORKDIR /tmp
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

WORKDIR /project

VOLUME /project

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
