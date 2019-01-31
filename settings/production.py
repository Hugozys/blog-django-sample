from .base import *


DEBUG = False
ALLOWED_HOSTS = ['hugozh.com','157.230.56.216']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'nobody',
        'PASSWORD':'hugoblog2019',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

MARTOR_IMGUR_CLIENT_ID = '672f0172131a407'
MARTOR_IMGUR_API_KEY   = '876193878c58c665d7db81ddb5ebb49a8bd4c842'
