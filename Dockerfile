FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN buildDeps='software-properties-common git libtool cmake python-dev python3-pip python-pip libseccomp-dev curl' && \
    apt-get update && apt-get -y install python3 $buildDeps && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update && apt-get install -y openjdk-11-jdk && \
    pip3 install pika pylint &&\
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    mkdir -p /code && \
    mkdir -p /log
COPY setting /setting
COPY src /src
WORKDIR /code