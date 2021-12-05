FROM python:3.8-bullseye

ENV DEBIAN_FRONTEND=noninteractive
COPY setting /setting
COPY src /src
RUN pip3 install pika pylint requests && \
    mkdir -p /code && \
    mkdir -p /log
WORKDIR /code
COPY service /code/service
COPY main.py /code/main.py
COPY test.py /code/test.py
