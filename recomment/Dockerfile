FROM python:3.7-slim

RUN mkdir -p /var/www/recomment
COPY . /var/www/recomment

WORKDIR /var/www/recomment
RUN apt-get update 

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install -r requirements.txt
