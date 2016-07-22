from defaults import *

# Vagrant development environment settings

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

# Try looking for local settings...
try:
    from local_settings import *
except ImportError:
    pass

# Then look for production settings
try:
    from production import *
except ImportError:
    pass
