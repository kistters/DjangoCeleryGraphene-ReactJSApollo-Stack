#!/bin/sh
# adventure-up.sh

if [ "$1" == "--build" ]; then
    docker build -t adventure-backend:latest backend
    docker build -t adventure-frontend:latest frontend
fi


docker-compose up react-front django-back celery-worker-back #TODO a postgres up check

#docker-compose run --rm django-back sh
#docker-compose run --rm react-front sh
#docker-compose run --rm celery-worker-back sh
