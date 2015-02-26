"""
Django settings for the project.
"""

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # This makes Django OK with apps being in the apps directory
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

if(os.environ["DJANGO_ENV"] != "production"):
    DEBUG = True
    TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home',
    'apps.people',
    'pipeline',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
            'home/css/style.scss',
        ),
        'output_filename': 'css/style.css',
    },
}
PIPELINE_JS = {
    'global': {
        'source_filenames': (
            'home/js/global.js',
        ),
        'output_filename': 'js/global.js',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USERNAME'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.environ['MYSQL_HOSTNAME'],
        'PORT': os.environ['MYSQL_PORT'],
    }
}

# S3 configurations With pipeline cached storage for static files on development.
# collectstatic should never be needed on the development server with this set up...
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]

MEDIAFILES_LOCATION = "media"
DEFAULT_FILE_STORAGE = "project.custom_storages.MediaStorage"
MEDIA_URL = "https://%s.s3.amazonaws.com/%s/" % (AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION)

STATICFILES_LOCATION = "static"
if(os.environ["DJANGO_ENV"] == "development"):
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = ()
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
else:
    STATICFILES_STORAGE = "project.custom_storages.StaticStorage"
    STATIC_URL = "https://%s.s3.amazonaws.com/%s/" % (AWS_STORAGE_BUCKET_NAME, STATICFILES_LOCATION)


# Purely Local configurations
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = ()
# STATICFILES_FINDERS = (
#   'django.contrib.staticfiles.finders.FileSystemFinder',
#   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )
