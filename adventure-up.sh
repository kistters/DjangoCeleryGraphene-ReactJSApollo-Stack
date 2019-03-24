#!/bin/sh
# adventure-up.sh

docker-compose build db-postgres #TODO a postgres up check
docker-compose run --rm adventure migrate # adventure depends on db-postgres
docker-compose run --rm adventure asyncatchall #run integration with pokeApi
docker-compose up #all services
