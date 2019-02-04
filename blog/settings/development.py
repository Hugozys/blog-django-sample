from .base import *
import socket
import getpass
SECRET_KEY = '47fn)_(6_r5h^$(_g%=4ft+%rvppnafr*6*aj=usqvokj6kv-m'
DEBUG = True

#socket.gethostname()
ALLOWED_HOSTS = ['vcm-7520.vm.duke.edu']


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
ADMIN_ENABLED = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.duke.edu'
DEFAULT_FROM_EMAIL = 'yz395@vcm-7520.vm.duke.edu'
#getpass.getuser() + "@" + socket.gethostname()
EMAIL_USE_TLS = True
EMAIL_PORT = 587


