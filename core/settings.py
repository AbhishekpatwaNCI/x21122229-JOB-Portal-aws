from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = (
    "django-insecure-udin7n06jc&dy&j&y@psw5iic@p7ta+2d^-c+st2-mhdf^ook7"
)
DEBUG = True
ALLOWED_HOSTS = ['x21122229jobportalcppprojecteb-env.eba-5n67yeew.eu-west-1.elasticbeanstalk.com','127.0.0.1']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "project",
    'storages',
    'crispy_forms',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": BASE_DIR / "db.sqlite3",
#    }
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobportal',
        'USER': 'admin',
        'PASSWORD': '8806069513',
        'HOST': 'databasejobportal.csxqr3aaa1vb.eu-west-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

import os

STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'


AWS_STORAGE_BUCKET_NAME = 'x21122229-job-portal-cpp'
AWS_S3_REGION_NAME = 'eu-west-1'  # e.g. us-east-2
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = None
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStorage'

# s3 public media settings
#MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
#MEDIA_ROOT = MEDIA_URL
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 
#STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION) 
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#PUBLIC_MEDIA_LOCATION = 'media'
#MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'

#DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
