from pathlib import Path

# ==================================================
# Base Directory
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# Security
# ==================================================
SECRET_KEY = 'django-insecure-3)47pq&o$(xoj5ph9^^eytmamd73)emh4xf90@jyx0#5q55fc8'

DEBUG = True

ALLOWED_HOSTS = []


# ==================================================
# Applications
# ==================================================
INSTALLED_APPS = [
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'accounts.apps.AccountsConfig',
    'catalog.apps.CatalogConfig',
    'orders.apps.OrdersConfig',
]


# ==================================================
# Custom User Model
# ==================================================
AUTH_USER_MODEL = 'accounts.User'


# ==================================================
# Middleware
# ==================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==================================================
# URLs & WSGI
# ==================================================
ROOT_URLCONF = 'la88.urls'

WSGI_APPLICATION = 'la88.wsgi.application'


# ==================================================
# Templates
# ==================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # مجلد القوالب الرئيسي
        'DIRS': [
            BASE_DIR / 'templates',
        ],

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


# ==================================================
# Database
# ==================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==================================================
# Password Validation
# ==================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==================================================
# Internationalization
# ==================================================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# ==================================================
# Static Files
# ==================================================
STATIC_URL = '/static/'

# ملفات التطوير
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# ملفات الإنتاج (collectstatic)
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ==================================================
# Media Files
# ==================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==================================================
# Default Primary Key
# ==================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
