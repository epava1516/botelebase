#!/bin/bash
docker compose down
docker compose up -d
docker exec -ti rrhh-back sed -i "s/ungettext_lazy/gettext_lazy/g" /usr/local/lib/python3.11/site-packages/url_filter/validators.py
docker restart rrhh-back
docker exec -ti rrhh-back python manage.py makemigrations
docker exec -ti rrhh-back python manage.py migrate
sleep 10
python pushdb.py