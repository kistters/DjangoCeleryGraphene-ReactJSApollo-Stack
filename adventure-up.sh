#!/bin/sh
# adventure-up.sh

if [[ $1 == '--build' ]]; then
    docker build -t adventure-backend:latest .
    docker build -t adventure-frontend:latest react-front
fi

# up services
docker-compose up -d postgres-service rabbitmq-service

until docker-compose exec postgres-service psql -U postgres -c "select 1" > /dev/null 2>&1; do
    printf '.' && sleep 0.3;
done; echo ' database up :)'

if [[ $1 == '--build' ]]; then
    docker-compose up -d celery-worker-back
    docker-compose exec celery-worker-back python manage.py migrate
    docker-compose exec celery-worker-back python manage.py celerycatchall
fi

docker-compose up

