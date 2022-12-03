# Image
FROM python:3.11.0-alpine3.16

# Default config
ENV PUBLIC_IP=127.0.0.1 \
    PUBLIC_PORT=8000 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

#Set exposed port
EXPOSE ${PUBLIC_PORT}

# Container basic set-up
# RUN apk update \
#     && apk add --virtual build-deps gcc python3-dev musl-dev \
#     && apk add --no-cache mariadb-dev \
#     && pip install mysqlclient  \
#     && apk del build-deps

# Project set-up
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt

# Container default run
ENTRYPOINT ["sh", "-c", "python manage.py runserver $PUBLIC_IP:$PUBLIC_PORT"]
