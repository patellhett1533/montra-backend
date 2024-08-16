FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONOTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update

RUN pip install --upgrade pip

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt