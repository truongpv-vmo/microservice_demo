FROM python:3.7-slim

RUN mkdir -p /var/www/auth
COPY . /var/www/auth

WORKDIR /var/www/auth
RUN apt-get update 
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
