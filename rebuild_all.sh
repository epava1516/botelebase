#!/bin/bash
docker compose down
docker stop $(docker ps -aq)
docker system prune -af
docker build . -t teleback:1.0.1
docker compose up -d
docker restart rrhh-back
rm -rf  api/migrations/0*.py
docker exec -ti rrhh-back python manage.py makemigrations
docker exec -ti rrhh-back python manage.py migrate
sleep 5
python pushdb.py