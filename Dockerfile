FROM python:3.9.12

WORKDIR /app
ENV FLASK_APP=app

COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt
