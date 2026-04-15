from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('CLAVE_SECRETA') or os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-development')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG_ENV = os.getenv('DEPURAR') or os.getenv('DEBUG', 'False')
DEBUG = DEBUG_ENV.lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,*.onrender.com').split(',')

# Asegura importación de la app 'core' como módulo
import sys
sys.path.append(os.path.join(BASE_DIR, 'core'))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise antes de CommonMiddleware
    'core.middleware.MediaFilesMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'glamstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'core', 'Clientes', 'tienda'),
            os.path.join(BASE_DIR, 'core', 'Clientes', 'carrito'),
            os.path.join(BASE_DIR, 'core', 'Clientes', 'perfil'),
            os.path.join(BASE_DIR, 'core', 'Clientes', 'productos_categoria'),
            os.path.join(BASE_DIR, 'core', 'Clientes', 'seguimiento_pedidos'),
            os.path.join(BASE_DIR, 'core', 'Clientes', 'registrar_usuario'),
            os.path.join(BASE_DIR, 'core', 'Clientes', 'pedido_confirmado'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Panel_admin'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Panel_distribuidores'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Panel_pedidos'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Panel_repartidores'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Panel_cliente'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Panel_productos'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Panel_categorias'),
            os.path.join(BASE_DIR, 'core', 'Gestion_admin', 'Admin'),
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

LOGOUT_REDIRECT_URL = '/'

WSGI_APPLICATION = 'glamstore.wsgi.application'

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core', 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# -----------------------------------------------------------------------------
# Database (solo uso local con MySQL/MariaDB)
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'glamstoredb'),
        'USER': os.getenv('MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', '0000'),  # cambia si es necesario
        'HOST': os.getenv('MYSQL_HOST', '127.0.0.1'),
        'PORT': os.getenv('MYSQL_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email (Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'glamstore0303777@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # usa App Password si tienes 2FA
DEFAULT_FROM_EMAIL = 'Glam Store <glamstore0303777@gmail.com>'