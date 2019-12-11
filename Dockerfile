FROM juniper/pyez:latest

LABEL net.juniper.image.maintainer="Stephen Steiner <ssteiner@juniper.net>"

WORKDIR /tmp

RUN echo -e "http://nl.alpinelinux.org/alpine/v3.5/main\nhttp://nl.alpinelinux.org/alpine/v3.5/community" \
    > /etc/apk/repositories
RUN apk add --no-cache ca-certificates openssh-client build-base gcc g++ make python-dev py-pip

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN ansible-galaxy install Juniper.junos

RUN apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /playbooks

VOLUME /playbooks
