# Use this for production

from .base import *

DEBUG = False
# ALLOWED_HOSTS += ['*']

# WSGI_APPLICATION = 'app.wsgi.prod.application'
ASGI_APPLICATION = 'app.asgi.prod.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


