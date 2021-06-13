release: python3 manage.py migrate
web: gunicorn raspberry.wsgi --preload --log-file-
