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

# Project set-up
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt && \
    sed -i "s/ungettext_lazy/gettext_lazy/g" /usr/local/lib/python3.11/site-packages/url_filter/validators.py

# Container default run
ENTRYPOINT ["sh", "-c", "python manage.py runserver $PUBLIC_IP:$PUBLIC_PORT"]
