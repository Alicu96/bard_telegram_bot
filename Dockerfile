FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    locales \
    python3 python3-pip python3-yaml python3-numpy && \
    rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

LABEL app="telebard"
LABEL maintainer="Alicu96"

WORKDIR /opt

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY bot/ /opt/bot/

COPY scripts/run_app.sh run_app.sh

ENTRYPOINT ./run_app.sh

