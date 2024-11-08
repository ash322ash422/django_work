from .base import *
DEBUG = True
ALLOWED_HOSTS = []

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
    #'rest_framework.authentication.SessionAuthentication', # comment this out to avoid error: { "detail": "CSRF Failed: CSRF token missing."} 
    'rest_framework.authentication.BasicAuthentication',
]
}