from .base import *
SECRET_KEY = '47fn)_(6_r5h^$(_g%=4ft+%rvppnafr*6*aj=usqvokj6kv-m'
DEBUG = True

ALLOWED_HOSTS = ['vcm-7520.vm.duke.edu','67.159.94.90']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'hugoblog',
        'PASSWORD': '123456',
        'HOST':'db',
        'PORT':'5432',
    }
}
STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.duke.edu'
DEFAULT_FROM_EMAIL = 'yz395@vcm-7520.vm.duke.edu'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


