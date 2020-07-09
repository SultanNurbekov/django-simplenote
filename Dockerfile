FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /simple
WORKDIR /simple
COPY requirements.txt /simple/

RUN pip install -r requirements.txt
COPY . /simple/