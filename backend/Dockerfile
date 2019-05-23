FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# dependence to psycopg2-binary, Pillow
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && apk add jpeg-dev zlib-dev

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

# remove weight ;)
RUN apk del build-deps

COPY . /code/
