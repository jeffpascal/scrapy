
FROM ubuntu:18.04

WORKDIR /app

RUN apt-get update && apt-get install -y  curl software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.10 python3.10-distutils python3-apt
RUN apt-get -y install libxml2-dev libxslt-dev python3-dev
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
RUN pip3.10 install Scrapy
ADD jeffTests /app
ENTRYPOINT [ "bash" ]