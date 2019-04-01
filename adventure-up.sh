#!/bin/sh
# adventure-up.sh

docker-compose up --build -d db-postgres #TODO a postgres up check
docker-compose run --rm adventure python manage.py migrate # adventure depends on db-postgres
docker-compose run --rm adventure python manage.py asyncatchall #run integration with pokeApi
docker-compose up #all services
