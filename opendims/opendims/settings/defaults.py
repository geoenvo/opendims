"""
Django settings for opendims project.
Generated by 'django-admin startproject' using Django 1.9.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b^v8b0^!b-3_1jxk2s96#9_v8^=!75n_56kq#%j0y406x*e30-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'ckeditor',
    'ckeditor_uploader',
    'djangobower',
    'import_export',
    'leaflet',
    'crispy_forms',
    'registration',
    'rest_framework',
    'rest_framework_gis',
    'common',
    'reports',
    'reporting',
    'geolevels',
    'waterlevel',
    'maps',
    'jaksafe',
    'django_crontab',
    'contact',
    'weatherforecast',
    'smsblast',
    'automaticweathersystem',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

# Sites framework
SITE_ID = 1

ROOT_URLCONF = 'opendims.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'opendims.context_processors.resource_urls',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'opendims.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATETIME_FORMAT = 'iso-8601'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded')

MEDIA_URL = '/uploaded/'

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

BOWER_INSTALLED_APPS = (
    'jquery#2.2.1',
    'bootstrap#3.3.6',
    'font-awesome#4.5.0',
    'typeahead.js#0.10.5',
    'handlebars#3.0.3',
    'list.js#1.1.1',
    'leaflet.markercluster#0.4.0',
    'leaflet.locatecontrol#0.43.0',
    'leaflet-groupedlayercontrol#0.3.0',
    'eonasdan-bootstrap-datetimepicker#4.17.37',
    'animate.css#3.1.0',
    'jquery-migrate#1.2.1',
    'modernizr#2.0.6',
    'weather-icons#2.0.10',
)

# App model reordering in /admin page
ADMIN_REORDER = (
    ('geolevels', ('Province', 'City', 'Subdistrict', 'Village', 'RW', 'RT')),
    ('reports', ('Event', 'Report', 'Source', 'Disaster')),
    ('waterlevel', ('WaterGate', 'WaterLevelReport')),
    ('reporting', ('Report', 'Template', 'Attachment')),
)

SITE_NAME = 'Open-DiMS'

LOGIN_URL = reverse_lazy('login')

LOGIN_REDIRECT_URL = reverse_lazy('home')

LOGOUT_URL = reverse_lazy('logout')

CRISPY_TEMPLATE_PACK = 'bootstrap3'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'format_tags': 'p;h1;h2;h3;h4;h5;h6;pre;address;div',
    },
}

CKEDITOR_JQUERY_URL = STATIC_URL + 'jquery/dist/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'editor'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

MAPBOX_ACCESSTOKEN = 'pk.eyJ1IjoiZ2VvZW52byIsImEiOiJjaWxjNDBseWQyN29udHlseHJueGFjNTcxIn0.UHG-jg9OS12rmSwIHIyscg'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-6.208973, 106.846933),
    'DEFAULT_ZOOM': 11,
    'TILES': [
        (
            'OpenStreetMap',
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            {
                'maxZoom': 19,
                'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }
        ),
        (
            'MapBox Satellite',
            'http://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}',
            {
                'id': 'mapbox.satellite',
                'accessToken': MAPBOX_ACCESSTOKEN,
                'subdomains': 'abcd',
                'attribution': 'Imagery from <a href="http://mapbox.com/about/maps/">MapBox</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }
        ),
        (
            'Aerial Imagery',
            'http://otile{s}.mqcdn.com/tiles/1.0.0/{type}/{z}/{x}/{y}.{ext}',
            {
                'type': 'sat',
                'ext': 'jpg',
                'subdomains': '1234',
                'attribution': 'Tiles Courtesy of <a href="http://www.mapquest.com/">MapQuest</a> &mdash; Portions Courtesy NASA/JPL-Caltech and U.S. Depart. of Agriculture, Farm Service Agency'
            }
        ),
    ],
}

ACCOUNT_ACTIVATION_DAYS = 7

ITEMS_PER_PAGE = 20

CRONJOBS = [
    ('* 1,7,13,19 * * *', 'jaksafe.cron.jaksafe_scheduled_job')
]
