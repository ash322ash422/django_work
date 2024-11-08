
from pathlib import Path
#from decouple import config #store parameters in .ini or .env files;

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e8f9f0tsxcpub0lbk=m_7!a*553refg%##&(g*y-vp%q5$#)xm'
#SECRET_KEY = config('SECRET_KEY',default=None, cast=str) #USE THIS LOGIC IN PRODUCTION

DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'rest_framework',
    
    #1)After adding below, have to run migrate command. Then 'python manage.py drf_create_token admin' would be able to
    # create token for admin. Also you can create token for user by logging to 'admin' page -> click 'Token' model
    #  -> 'Add user' and then read the token for the created user  
    'rest_framework.authtoken', 
    
    'api',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'VMS.urls'
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
WSGI_APPLICATION = 'VMS.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
#STATIC_ROOT=os.path.join(BASE_DIR, 'static_root')# dir is formed when user runs 'collectstatic' command
STATIC_ROOT = BASE_DIR / 'static_root'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#DO NOT NEED JWT here
REST_FRAMEWORK = {
    #"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination", #commented it out to receive certain response structure 
    #"PAGE_SIZE": 20, #env("PAGE_SIZE"),
    'DEFAULT_AUTHENTICATION_CLASSES': [
    #'rest_framework.authentication.SessionAuthentication', # comment this out to avoid error: { "detail": "CSRF Failed: CSRF token missing."} 
    #'rest_framework.authentication.BasicAuthentication',
    #TODO: set expiration time for below token
    'rest_framework.authentication.TokenAuthentication', 
    ]
}
