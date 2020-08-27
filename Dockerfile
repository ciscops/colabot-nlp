FROM ubuntu:18.04

COPY source.list /etc/apt/source.list
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get -y install software-properties-common curl vim wget unzip

RUN apt-get -y install python3-pip python-dev build-essential && \
    apt-get -y install software-properties-common

RUN apt-get -y install python3-venv
RUN python3 -m venv venv

COPY requirements.txt requirements.txt
RUN venv/bin/pip3 install -r requirements.txt
RUN venv/bin/pip3 install gunicorn

COPY app.py app.py
COPY build_model.py build_model.py
COPY colabot_commands.yaml colabot_commands.yaml
COPY config.py config.py

COPY docker_boot.sh docker_boot.sh
RUN chmod +x docker_boot.sh

EXPOSE 5005
ENTRYPOINT ["/docker_boot.sh"]


