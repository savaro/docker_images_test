#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.utils.timezone import activate

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

"""
Django settings for mathilde project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '##1tm$+il0qrnzrf9+yv()#@ca+ls)bhh7o0^5eo667c^id=wa'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DOCKER_REGISTRIES = {
    'PROTOCOL': 'http',
    'PORT': 5000,
    'HOSTS': [
      'registry-1.mathildetech.net'
    ],
    'ALLOW_CREATE_USER': True,
    # Redis settings
    'REDIS_HOST': 'localhost',
    'REDIS_PORT': '6379',
}

# Application definition

INSTALLED_APPS = (  # Third-party apps
                    # Mathilde API
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'json_field',
    'django_fsm',
    'allauth',
    'allauth.account',
    'marathon',
    'influxdb',
    'pika',
    'pickle',
    'users',
    'apps',
    'repositories',
    'commons',
    'docker_index',
    'billings',
    'activity',
    'code_repo',
    'docker_build'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'allauth.account.context_processors.account',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)  # Needed to login by username in Django admin, regardless of `allauth`
# "guardian.backends.ObjectPermissionBackend",
# `allauth` specific authentication methods, such as login by e-mail

API_VERSION = 'v1'
APP_BASE_URI = '/api/' + API_VERSION + '/apps'
INSTANCE_BASE_URI = '/api/' + API_VERSION + '/instances'
ANONYMOUS_USER_ID = -1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_USERNAME_BLACKLIST = ['system']
LOGIN_REDIRECT_URL = APP_BASE_URI
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'),
    'PAGINATE_BY': 1000,               # Default to 10
    'PAGINATE_BY_PARAM': None,         # Allow client to override, using `?page_size=xxx`. 'page_size'
    'MAX_PAGINATE_BY': 100             # Maximum limit allowed when using `?page_size=xxx`.
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mathilde.urls_internal'

WSGI_APPLICATION = 'mathilde.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'tmp.db',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
}}

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../template')
    .replace('\\', '/'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

APP_URL_REGEX = '[A-Za-z0-9-_.]+'
DEFAULT_BUILD = 'mathilde/helloworld'
WEB_ENABLED = False
REGISTRATION_ENABLED = True

CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_IMPORTS = ('apps.tasks', )
BROKER_URL = 'redis://{}:{}/{}'.format(
    os.environ.get(
        'CACHE_HOST', '127.0.0.1'), os.environ.get(
            'CACHE_PORT', 6379), os.environ.get(
                'CACHE_NAME', 0))
CELERY_RESULT_BACKEND = BROKER_URL
CELERYD_CONCURRENCY = 1

DOCKERCFG_FILE = "file:///etc/.dockercfg"

# Cluster configuration for mesosphere
CLUSTER_SCHEDULER = {
    'type': 'mesosphere',
    'endpoint': 'http://master.mathildetech.net:8080/'
}

CLUSTER_DOMAIN = 'dev.mathildeapps.com'

# Cluster configuration for mock
# CLUSTER_TYPE = 'mock'
# CLUSTER_ENTRYPOINT = 'mock-entrypoint'
# CLUSTER_DOMAIN = 'mock.mathildeapps.com'


NETWORK_MANAGER = {'type': 'mirana', 'endpoint': 'http://54.191.192.124:8000', }

MEMORY_SETTINGS = {
    'XS': 25,
    'S': 25,
    'M': 25,
    'L': 25,
    'XL': 25,
}

CPU_SETTINGS = {
    'XS': 0.1,
    'S': 0.1,
    'M': 0.1,
    'L': 0.1,
    'XL': 0.1,
}

MONITORING_STORAGE = {'type': 'influxdb',
                      'host': '54.149.182.210',
                      'port': 8086,
                      'username': 'root',
                      'password': 'root'
                      }

# MONITORING_STORAGE_TYPE = 'influxdb'
# MONITORING_STORAGE_HOST = '54.148.94.202'
# MONITORING_STORAGE_PORT = 8086
# MONITORING_STORAGE_USERNAME = 'root'
# MONITORING_STORAGE_PASSWORD = 'root'


# MONITORING_STORAGE_TYPE = 'mock'
# MONITORING_STORAGE_HOST = 'mock-host'
# MONITORING_STORAGE_PORT = 'mock-port'
# MONITORING_STORAGE_USERNAME = 'mock-username'
# MONITORING_STORAGE_PASSWORD = 'mock-password'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s][%(threadName)s]' +
                      '[%(name)s:%(lineno)d] %(message)s'}
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'standard'
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'standard'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['debug', 'info', 'error'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug', 'info', 'error'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['debug', 'info', 'error'],
            'level': 'DEBUG',
            'propagate': False

        },
    }
}

INVITATION_REQUIRED = False
ACTIVATION_REQUIRED = False

REPO_ADMIN = {
    'username': 'repo_admin',
    'password': '07Apples',
}

SYS_ADMIN = {
    'username': 'sys_admin',
    'password': '07Apples',
}

SMTP = {
    'server_host': 'email-smtp.us-west-2.amazonaws.com',
    'server_port': 465,
    'username': 'AKIAJS2CIHVXJZ5CKAOQ',
    'password': 'Aqi8q75QLVpi8bhyoYzx4PHNGRcNT5XTd4Jver0KD3Yd',
    'debug_level': 0
}

EMAIL = {
    'template_path': 'email',
    'from_mailbox': 'info@mathildetech.com',
    'debug_cc_email': 'rancheng@mathildetech.com',
    'rubick_url': 'http://www.alauda.io'
}

LANGUAGE_LIST = (('zh', 'Chinese'),
                 ('en', 'English'))

INDEX_URL = 'index.alauda.io'

# for building image repo
DOCKER_BUILD = {
    'endpoint': '54.148.145.55',
    'queue_name': 'build_task_queue'
}
