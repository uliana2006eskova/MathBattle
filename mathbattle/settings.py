"""
Django settings for mathbattle project.

Generated by 'django-admin startproject' using Django 2.1.5.

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
SECRET_KEY = 'saoy*kd&8w*t$^qgwemy+ioz9x)2t4p0m+^z-*eg1vgd40jysf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'contest.apps.ContestConfig',
   'authorization.apps.AuthorizationConfig',
   'tasks.apps.TasksConfig',
   'archiv.apps.ArchivConfig',
   'userprofile.apps.UserprofileConfig',
   'checker.apps.CheckerConfig',
   'django_summernote',
   'django_user_agents',
]

MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.common.CommonMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
   'django.middleware.clickjacking.XFrameOptionsMiddleware',
   'django_user_agents.middleware.UserAgentMiddleware',
   'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mathbattle.urls'

TEMPLATES = [
   {
          "BACKEND": "django.template.backends.django.DjangoTemplates",
          "DIRS": [os.path.join(BASE_DIR, "templates")],
          "APP_DIRS": True,
          "OPTIONS": {
              "context_processors": [
                  "django.template.context_processors.debug",
                  "django.template.context_processors.request",
                  "django.contrib.auth.context_processors.auth",
                  "django.contrib.messages.context_processors.messages",
              ],
          },
      },
]

WSGI_APPLICATION = 'mathbattle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME' : 'mathbattleul',
       'USER' : 'postgres',
       'PASSWORD' : 'postgres',
       'HOST' : '176.99.173.63',
       'PORT' : '5432'

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
SUMMERNOTE_THEME = 'bs4'

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'empty': ('<p><br/></p>', '<p><br></p>'),

    'width': '100%',
    'height': 480,
    'toolbar': [
        ['style', ['style']],
        ['font', ['bold', 'italic', 'underline', 'superscript', 'subscript',
                  'strikethrough', 'clear']],
        ['fontname', ['fontname']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video', 'hr', 'equation']],
        ['view', ['fullscreen', 'codeview']],
        ['help', ['help']],
    ],
    'lang': None,
    'lang_matches': {
        'ar': 'ar-AR',
        'bg': 'bg-BG',
        'ca': 'ca-ES',
        'cs': 'cs-CZ',
        'da': 'da-DK',
        'de': 'de-DE',
        'el': 'el-GR',
        'es': 'es-ES',
        'fa': 'fa-IR',
        'fi': 'fi-FI',
        'fr': 'fr-FR',
        'gl': 'gl-ES',
        'he': 'he-IL',
        'hr': 'hr-HR',
        'hu': 'hu-HU',
        'id': 'id-ID',
        'it': 'it-IT',
        'ja': 'ja-JP',
        'ko': 'ko-KR',
        'lt': 'lt-LT',
        'mn': 'mn-MN',
        'nb': 'nb-NO',
        'nl': 'nl-NL',
        'pl': 'pl-PL',
        'pt': 'pt-BR',
        'ro': 'ro-RO',
        'ru': 'ru-RU',
        'sk': 'sk-SK',
        'sl': 'sl-SI',
        'sr': 'sr-RS',
        'sv': 'sv-SE',
        'ta': 'ta-IN',
        'th': 'th-TH',
        'tr': 'tr-TR',
        'uk': 'uk-UA',
        'vi': 'vi-VN',
        'zh': 'zh-CN',
    },
    'attachment_storage_class': None,
    'attachment_filesize_limit': 1024 * 1024,
    'attachment_require_authentication': False,
    'attachment_model': 'django_summernote.Attachment',

    'jquery': '$',

    'base_css': (
        '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
    ),
    'base_js': (
        '//code.jquery.com/jquery-3.2.1.min.js',
        '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js',
    ),

    'codemirror_css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/codemirror.min.css',
    ),
    'codemirror_js': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/codemirror.min.js',
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/mode/xml/xml.min.js',
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/mode/htmlmixed/htmlmixed.min.js',
    ),

    'default_css': (
        'summernote/summernote.css',
        'summernote/django_summernote.css',
    ),
    'default_js': (
        'summernote/jquery.ui.widget.js',
        'summernote/jquery.iframe-transport.js',
        'summernote/jquery.fileupload.js',
        'summernote/summernote.min.js',
        'summernote/ResizeSensor.js',
    ),
    'css': ('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css',),
    'js': (
        'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.js',
    ),

    'css_for_inplace': ('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css',),
    'js_for_inplace': ('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.js', ),

    # Disable upload
    'disable_upload': False,

    # For lazy loading (inplace widget only)
    'lazy': False,
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'
