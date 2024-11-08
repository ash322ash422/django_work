from .base import *
import os

DEBUG = False #NOTE: when DEBUG = False in production, django will not serve static files from STATIC_ROOT
#ALLOWED_HOSTS = ['13.126.177.3', 'radheshgypsum.com']
ALLOWED_HOSTS = ['*']

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
#print("STATICFILES_DIRS=",STATICFILES_DIRS)
"""