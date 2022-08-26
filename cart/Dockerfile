FROM python:3.7-slim

RUN mkdir -p /var/www/cart
COPY . /var/www/cart

WORKDIR /var/www/cart
RUN apt-get update 
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
