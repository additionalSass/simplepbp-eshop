release: python manage.py migrate
web: python manage.py collectstatic --noinput && gunicorn simplepbpshop.wsgi