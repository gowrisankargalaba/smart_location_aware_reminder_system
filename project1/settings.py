from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------- ENV SAFETY ----------------
def get_env(key, default=''):
    return os.environ.get(key, default)


# ---------------- SECURITY ----------------
SECRET_KEY = get_env(
    'DJANGO_SECRET_KEY',
    'django-insecure-local-dev-key-change-in-production'
)

DEBUG = get_env('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.pythonanywhere.com',
]


# ---------------- APPS ----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App',
]


# ---------------- MIDDLEWARE ----------------
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


ROOT_URLCONF = 'project1.urls'


# ---------------- TEMPLATES ----------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'project1.context_processors.google_maps_api',
            ],
        },
    },
]


WSGI_APPLICATION = 'project1.wsgi.application'


# ---------------- DATABASE ----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ---------------- PASSWORD VALIDATION ----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ---------------- INTERNATIONALIZATION ----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# ---------------- STATIC FILES ----------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ---------------- EMAIL ----------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = get_env('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = get_env('DJANGO_EMAIL_PASS')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ---------------- TWILIO ----------------
TWILIO_ACCOUNT_SID = get_env('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = get_env('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = get_env('TWILIO_PHONE_NUMBER', '+917997182627')


# ---------------- GOOGLE MAPS ----------------
GOOGLE_MAPS_API_KEY = get_env('GOOGLE_MAPS_API_KEY')


# ---------------- DEFAULT ----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'