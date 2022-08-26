FROM python:3.7-slim

RUN mkdir -p /var/www/main_api
COPY . /var/www/main_api

WORKDIR /var/www/main_api
RUN apt-get update 

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install -r requirements.txt

