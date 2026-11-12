FROM ubuntu:26.04

LABEL net.juniper.image.maintainer="Juniper Networks <jnpr-community-netdev@juniper.net>" \
      net.juniper.image.description="Lightweight image with Ansible, Python 3.14, and the Junos roles"

WORKDIR /tmp

# Prevent interactive prompts during apt installation
ENV DEBIAN_FRONTEND=noninteractive

## Copy project inside the containers
ADD requirements.txt .
ADD entrypoint.sh /usr/local/bin/.

## Install system dependencies and Python 3.14 development packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-full \
    python3-pip \
    libxslt1-dev \
    libxml2-dev \
    libffi-dev \
    libssl-dev \
    curl \
    ca-certificates \
    bash \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment for Python 3.14 dependencies
RUN python3 -m venv /opt/venv

# Make sure all subsequent RUN commands use the virtual environment by default
ENV PATH="/opt/venv/bin:$PATH"

## Install Python dependencies, PyEZ, Ansible, and collections in the venv
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt ansible \
    && ansible-galaxy collection install juniper.device

## Clean up build dependencies and cache to keep the image lightweight
RUN apt-get purge -y --auto-remove build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache \
    && chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /project

VOLUME /project

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
