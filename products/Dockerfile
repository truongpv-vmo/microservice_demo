FROM python:3.7-slim

RUN mkdir -p /var/www/products
COPY . /var/www/products

WORKDIR /var/www/products
RUN apt-get update 

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
