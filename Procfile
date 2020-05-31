web: gunicorn TraceUserActions.wsgi:application --log-file - --log-level debug
release: python manage.py migrate
release: python manage.py insertdata