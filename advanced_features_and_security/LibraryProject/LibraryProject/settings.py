"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'apkuy62m%^vb68w+^qgjp-2a1pb508+ag*mbq)@$jsw6=z3k(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf'
    'csp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Ensure CSRF cookie is only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Ensure session cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Enable HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True

# Enable the browser's XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Enable HTTP Strict Transport Security (HSTS) for 1 year (in seconds)
SECURE_HSTS_SECONDS = 31536000  # 1 year

# Include all subdomains in the HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow preloading of the HSTS policy
SECURE_HSTS_PRELOAD = True

# Ensure cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Optionally, set the same-site attribute for cookies
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# Enable the browser’s XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True
# settings.py

# Ensure that session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure that CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Optionally, set the same-site attribute for cookies to enhance security
CSRF_COOKIE_SAMESITE = 'Lax'  # Use 'Strict' if you want more restrictive protection
SESSION_COOKIE_SAMESITE = 'Lax'  # Use 'Strict' if you want more restrictive protection

# Prevent the site from being framed and protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser’s XSS filtering to help prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
