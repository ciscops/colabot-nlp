FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
RUN apt-get install wget -y
RUN apt-get install unzip -y

RUN apt-get install curl -y
RUN apt-get install python3.8-venv
RUN python3.8 -m venv venv

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


