FROM python:3.6.4

ENV PYTHONUNBUFFERED 1

WORKDIR /srv

COPY requirements.txt /srv

RUN pip install -r requirements.txt

EXPOSE 8000

STOPSIGNAL SIGINT

ENTRYPOINT ["python", "manage.py"]
