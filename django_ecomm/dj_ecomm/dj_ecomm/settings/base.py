from decouple import config #store parameters in .ini or .env files;
import os
from pathlib import Path

#We invoke dirname 3 times to move up into directory by 3 levels 
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #changed
#print("BASE_DIR=",BASE_DIR)
BASE_DIR = Path(__file__).resolve().parent.parent.parent #move upto directory by 3 levels 
#print("BASE_DIR=",BASE_DIR)

#BASE_DIR1 = os.path.dirname(os.path.abspath(__file__))
#print("BASE_DIR1=",BASE_DIR1)



SECRET_KEY = config('SECRET_KEY',default=None, cast=str)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #I am commenting this to make .../admin/ page work.
    'django.contrib.sites', # you also have to SITE_ID = 1. Scroll below.
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'crispy_forms',
    
    #'django_countries',

    'store'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'dj_ecomm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #changed from default
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

WSGI_APPLICATION = 'dj_ecomm.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static_root/' #NOTE I had to change this from 'static/' that allowed debug_toolbar to display.

MEDIA_URL = '/media/'
#MEDIA_URL = os.path.join(BASE_DIR, '/media_root/')

#this is where bootstraps {font,img,js,scss,css} static dir are located
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_bootstrap')] 
#print("STATICFILES_DIRS=",STATICFILES_DIRS)

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')# dir is formed when user runs 'collectstatic' command
#print("STATIC_ROOT=",STATIC_ROOT)

#This is where images are saved when user creates new items
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Authenticate
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend', #his is default
    
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend' #TODO: where defined
)

SITE_ID = 1 ## We have to set this variable if we enable 'django.contrib.sites'
LOGIN_REDIRECT_URL = '/' #redirect after sign-in, sign-out, login.

# CRISPY FORMS
# other options: 'uni_form','foundation','tailwind','Bootstrap 5','Bulma'
CRISPY_TEMPLATE_PACK = 'bootstrap4' 
