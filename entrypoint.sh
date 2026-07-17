#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); u,created=U.objects.get_or_create(username='$DJANGO_SUPERUSER_USERNAME', defaults={'email':'$DJANGO_SUPERUSER_EMAIL','is_staff':True,'is_superuser':True}); u.set_password('$DJANGO_SUPERUSER_PASSWORD'); u.is_staff=True; u.is_superuser=True; u.save()"
python manage.py seed_demo
python manage.py collectstatic --noinput

exec python manage.py runserver 0.0.0.0:8000
