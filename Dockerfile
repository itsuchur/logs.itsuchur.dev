# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /usr/src/www

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn"  , "-b", "0.0.0.0:8080", "app:app"]