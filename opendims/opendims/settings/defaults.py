"""
Django settings for opendims project.
Generated by 'django-admin startproject' using Django 1.9.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

import raven

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as message_constants

from easy_thumbnails.conf import Settings as thumbnail_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b^v8b0^!b-3_1jxk2s96#9_v8^=!75n_56kq#%j0y406x*e30-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PRODUCTION = False # This value is True in production.py

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
    'django_crontab',
    'captcha',
    'categories',
    'categories.editor',
    'easy_thumbnails',
    'image_cropping',
    'screamshot',
    'actstream',
    'absoluteuri',
    'embed_video',
    'colorfield',
    'django_rq',
    'raven.contrib.django.raven_compat',
    'common',
    'reports.apps.ReportsConfig',
    'reporting.apps.ReportingConfig',
    'geolevels.apps.GeolevelsConfig',
    'waterlevel.apps.WaterlevelConfig',
    'maps',
    'jaksafe',
    'contact.apps.ContactConfig',
    'weatherforecast.apps.WeatherforecastConfig',
    'smsblast.apps.SmsblastConfig',
    'automaticweathersystem.apps.AutomaticweathersystemConfig',
    'earlywarning.apps.EarlywarningConfig',
    'website.apps.WebsiteConfig',
    'disasterrehabilitation.apps.DisasterrehabilitationConfig',
    'reportaggregator.apps.ReportaggregatorConfig',
    'sendsms',
]

MIDDLEWARE_CLASSES = [
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware', # Comment to disable sentry 404 logging
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'common.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'common.middleware.GlobalUserMiddleware',  # for getting current_user, should be put after auth.middleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

# Custom middleware for errors in debug mode
MIDDLEWARE_CLASSES += [
    'common.middleware.AdminOnly404Middleware',
    'common.middleware.AdminOnly500Middleware',
    'common.middleware.AdminOnly403Middleware',
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

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
RQ_SHOW_ADMIN_LINK = True

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

LANGUAGES = (
    ('id', 'Indonesian'),
    ('en', 'English'),
)

LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

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

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger'
}

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
    'plotly.js#1.10.0',
    'flag-icon-css#2.3.1',
    'jquery.marquee#1.4.0',
)

# App model reordering in /admin page
ADMIN_REORDER = (
    ('geolevels', ('Province', 'City', 'Subdistrict', 'Village', 'RW', 'RT')),
    ('reports', ('Event', 'Report', 'Source', 'Disaster')),
    ('waterlevel', ('WaterGate', 'WaterLevelReport')),
    ('earlywarning', ('EarlyWarningReport')),
    ('automaticweathersystem', ('AWSStation', 'AWSReport')),
    ('weatherforecast', ('WeatherForecastReport')),
    ('reporting', ('Report', 'Template', 'Attachment')),
    ('website', ('Post', 'Attachment', 'Welcome', 'SiteHeader', 'Partner', 'Link', 'Resource')),
    ('reportaggregator', ('Source', 'Keyword')),
    ('disasterrehabilitation', ('Activity', 'EventAssessment', 'Location', 'Reference', 'Agency')),
    ('contact', ('Contact')),
    ('smsblast', ('Message', 'Template', 'Group', 'Contact')),
    ('jaksafe', ('ReportAutoSummary')),
    ('categories', ('Category')),
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
    ('0 1,7,13,19 * * *', 'jaksafe.cron.jaksafe_scheduled_job', '>> /tmp/jaksafe_scheduled_job.log'),
    ('0 23 * * *', 'weatherforecast.cron.weatherforecast_scheduled_job', '>> /tmp/weatherforecast_scheduled_job.log'),
    ('0 * * * *', 'reportaggregator.cron.report_scheduled_job', '>> /tmp/report_scheduled_job.log'),
]

CAPTCHA_NOISE_FUNCTIONS = ('')

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

IMAGE_CROPPING_THUMB_SIZE = (300, 300)

# Site header maximum image dimensions
MAX_WIDTH_SITEHEADER_IMAGE = 600
MAX_HEIGHT_SITEHEADER_IMAGE = 120

# Twitter API
CONSUMER_KEY = 'blUYa3qxm2SwqvuErHsjJmi0t'
CONSUMER_SECRET = 'U0JTayjzpv7DspEREQ1uqKowj0CUgn2waYV7bteFnsBcrJlDr9'
ACCESS_TOKEN = '714659320047095808-I3YIUUq29mMHWZwlDOwpyKY43XkwxYV'
ACCESS_SECRET = 'TBjrusWZs7DeHoqTFclqqDLPNDcbcsY27NGTZXljn8Hws'
MAX_TWEETS = 100

# External URLs
URL_FACEBOOK = 'https://www.facebook.com/BPBD-DKI-Jakarta-331934126896908/'
URL_TWITTER = 'https://twitter.com/BPBDJakarta'

# Water level map settings
DEFAULT_CENTER_WATERLEVEL = (-6.359658, 106.827621)
DEFAULT_ZOOM_WATERLEVEL = 10

# Disaster categories to show in the disaster statistics block
DISASTER_STATISTICS = ('BJR', 'CEK', 'KBK', 'SOS', 'GNJ')

# Cities to show in the weather forecast block
WEATHERFORECAST_CITIES = ('Jakarta Selatan', 'Jakarta Timur', 'Jakarta Pusat', 'Jakarta Barat', 'Jakarta Utara', 'Kepulauan Seribu')

# sendsms
SENDSMS_BACKEND = 'smsblast.mysmsbackend.SmsBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'foo@gmail.com'
EMAIL_HOST_PASSWORD = 'bar'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # Set this to admin's contact email

# django activity stream
ACTSTREAM_SETTINGS = {
    'MANAGER': 'website.managers.MyActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': False,
    'GFK_FETCH_DEPTH': 1,
}

# Sentry settings
RAVEN_CONFIG = {
    'dsn': 'https://1a28538b213c4c6d8f4b7b8d95cdb5e7:87e396ad8e9c4ce69a4805288a5f86d7@sentry.io/109389',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
