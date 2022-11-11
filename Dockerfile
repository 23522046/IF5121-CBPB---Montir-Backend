# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .
