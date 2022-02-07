from .settings import *


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env.get("SECRET_KEY")


ALLOWED_HOSTS = env.get("ALLOWED_HOSTS").split(" ")

LOCAL_APPS = [
    'testData',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'djoser',
    'rest_framework_simplejwt',
    'drf_yasg'
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.get('POSTGRES_NAME'),
        'USER': env.get('POSTGRES_USER'),
        'PASSWORD': env.get('POSTGRES_PASSWORD'),
        'HOST': env.get('POSTGRES_HOST')
    }
}