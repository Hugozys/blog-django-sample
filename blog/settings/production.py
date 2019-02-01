from .base import *
SECRET_KEY = os.environ['SECRET_KEY']
SECURE_HSTS_SECONDS = 31536000
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_PRELOAD = True
DEBUG = False
ALLOWED_HOSTS = [os.environ['HOST_NAME'],os.environ['HOST_IP']]
DATABASES = {
    'default': {
        'ENGINE': os.environ['DB_ENGINE'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST':os.environ['DB_HOST'],
        'PORT':os.environ['DB_PORT'],
    }
}

MARTOR_IMGUR_CLIENT_ID = os.environ['CLIENT_ID']
MARTOR_IMGUR_API_KEY   = os.environ['API_KEY']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PWD']

STATIC_URL = '/staticfiles/'

