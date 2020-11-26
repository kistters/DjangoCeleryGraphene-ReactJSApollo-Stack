FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
# dependence to psycopg2-binary, Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
 build-essential gcc postgresql-client postgresql-client-common

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
