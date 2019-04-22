#!/bin/sh
# adventure-up.sh

docker-compose up --build  #TODO a postgres up check
docker-compose run --rm back-service python manage.py migrate # back-service depends on postgres-service
docker-compose run --rm back-service python manage.py celerycatchall #run integration with pokeApi
