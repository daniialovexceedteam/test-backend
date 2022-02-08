from .settings import *

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

NAME = env.get('POSTGRES_DB')
USER = env.get('POSTGRES_USER')
PASSWORD = env.get('POSTGRES_PASSWORD')
HOST = env.get('POSTGRES_HOST')
SECRET_KEY = env.get('SECRET_KEY')
ALLOWED_HOSTS = env.get('ALLOWED_HOSTS', ['localhost'])

if ALLOWED_HOSTS:
    ALLOWED_HOSTS = ALLOWED_HOSTS.split(' ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST
    }
}
