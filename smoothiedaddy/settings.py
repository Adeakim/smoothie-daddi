"""
Django settings for smoothiedaddy project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oyp=@#*7hz^i$5e9kbpp6v6w!_3-+wt=0astz48j99ouqx0k3q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['smoothiedaddi.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'smoothie.apps.SmoothieConfig',
    'cloudinary_storage',
    'cloudinary',
    'users.apps.UsersConfig',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'crispy_forms',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smoothiedaddy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'smoothiedaddy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# STATIC_URL = '/static/'
# MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# MEDIA_URL='/media/'
# static_dir = os.environ.get('STATIC_DIR', 'local')
# static_pth = os.path.join(BASE_DIR,"static")
# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# # MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,"staticfiles")
# ]
STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR,"static")
MEDIA_URL = '/smoothie/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK='bootstrap4'

LOGIN_REDIRECT_URL= 'smoothie-home'

LOGIN_URL='login'

CLOUDINARY_STORAGE ={
    'CLOUD_NAME': 'dje0qtxrs',
    'API_KEY': '347166829819152',
    'API_SECRET' : '8js9vybLTSvEMElZmPxT2UEwbA0'
}

