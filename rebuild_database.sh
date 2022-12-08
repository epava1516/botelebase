#!/bin/bash
docker exec -ti rrhh-back python manage.py flush --no-input
docker exec -ti rrhh-back python manage.py makemigrations
docker exec -ti rrhh-back python manage.py migrate
python pushdb.py