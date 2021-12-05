FROM python:3.8-bullseye

ENV DEBIAN_FRONTEND=noninteractive
COPY setting /setting
COPY src /src
COPY requirements.txt /requirements/requirements.txt
RUN pip3 install --no-cache-dir --requirement /requirements/requirements.txt && \
    apt-get update && \ 
    apt-get -y --no-install-recommends install openjdk-11-jre-headless=11.0.12+7-2 && \
    apt-get -y --no-install-recommends install cloc=1.86-1 && \ 
    apt-get clean && rm -rf /var/lib/apt/lists/* && \ 
    mkdir -p /code && \
    mkdir -p /log && \
    rm -r /requirements
WORKDIR /code
COPY service /code/service
COPY main.py /code/main.py
ENTRYPOINT ["python3", "main.py"]