#!/bin/bash

# Set setting env, please exchange the comment out line to switch for the other env
export DJANGO_SETTINGS_MODULE="config.settings.dev"
# export DJANGO_SETTINGS_MODULE="config.settings.prod"

# Install packages for dev or prod, about which packages will be installed, please decide by changing above env value
if [ $DJANGO_SETTINGS_MODULE = "config.settings.dev" ]; then
    pip3 install -r requirements/dev.txt
else
    pip3 install -r requirements/prod.txt
    mkdir -p /var/log/app && touch /var/log/app/app.log
    chmod +w /var/log/app/app.log
fi

# Prepare database
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', 'admin@example.com', 'adminpass');"

# Collect Staticfiles
python3 manage.py collectstatic --noinput

# Set server(gunicorn)
# mkdir -p /var/run/gunicorn
# gunicorn config.wsgi --bind=unix:/var/run/gunicorn/gunicorn.sock

# Set server(Django)
python3 manage.py runserver 0.0.0.0:8000
