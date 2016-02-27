from defaults import *

# Development environment settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'opendims',
        'USER': 'vagrant',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from local_settings import *
except ImportError:
    pass
