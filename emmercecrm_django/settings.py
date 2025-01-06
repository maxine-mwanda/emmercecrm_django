from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis broker
CELERY_ACCEPT_CONTENT = ['json']               # Accepted content formats
CELERY_TASK_SERIALIZER = 'json'                # Serialize tasks in JSON format
CELERY_RESULT_BACKEND = 'django-db'            # Store results in the database
CELERY_TIMEZONE = 'UTC'

# Celery Beat settings (optional, for periodic tasks)
INSTALLED_APPS += [
    'django_celery_beat',
    'django_celery_results',
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y!vbxgjq)i7@3m^dlf!@9)r8y(ledyb&#wqz$2uvnhs*$i6dxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'leads',
    'django_celery_results',
]

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'