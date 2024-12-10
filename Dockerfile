FROM python:3.12-alpine

LABEL net.juniper.image.maintainer="Juniper Networks <jnpr-community-netdev@juniper.net>" \
      net.juniper.image.description="Lightweight image with Ansible and the Junos roles"

WORKDIR /source

## Copy project inside the containers
ADD setup.* ./
ADD requirements.txt .
ADD entrypoint.sh /usr/local/bin/.

## Install dependencies and PyEZ
RUN apk add --no-cache build-base python3-dev py3-pip \
    libxslt-dev libxml2-dev libffi-dev openssl-dev curl \
    ca-certificates py3-pip bash openssh-client

RUN pip install --upgrade pip \
    && pip install pipdeptree \
    && python3 -m pip install -r requirements.txt

# Also install the collections junipernetworks.junos and juniper.device
# Install Ansible modules in one layer
RUN ansible-galaxy collection install junipernetworks.junos && \
    ansible-galaxy collection install juniper.device

## Clean up and start init
RUN apk del -r --purge gcc make g++ \
    && rm -rf /source/* \
    && chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /project

VOLUME /project

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
