FROM python:3
RUN apt-get update && apt-get install -y \
    python3-pip \
    make

RUN /usr/bin/pip3 install --no-cache-dir Django==2.2.1
