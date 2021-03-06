import os.path
from pathlib import Path
from datetime import timedelta
import dj_database_url
import django_heroku
# from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-mvxkk)xax5e#$c4l7nzk6z7*584ml+c$)rrjdh!t^4&8gssm$d'


DEBUG = False

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainAPI',
    'register',
    'ckeditor',
    'rest_framework',
    'rest_framework.authtoken',
    'baton.autodiscover',

]
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # cors headers
    'corsheaders.middleware.CorsMiddleware',
]



CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'geologiya.urls'

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

WSGI_APPLICATION = 'geologiya.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        "HOST": "127.0.0.1",
        "USER": "shaxbozaka",
        "PASSWORD": "1"

    }
}




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'register.CustomUser'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_root/'
STATIC_ROOT = BASE_DIR / "/static_root/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


BATON = {
    'SITE_HEADER': '?????????? ????????????????',
    'SITE_TITLE': '???????????????? ?????????????? ?????????????? ???????????? ??????????????????',
    'INDEX_TITLE': '???????????????? ?????????? ??????????????????????????????',
    'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': 'copyright ?? 2017 <a href="https://napaautomotive.uz/ru"> Napa Automotive</a>', # noqa
    'POWERED_BY': '<a href="https://www.instagram.com/d__abdunazarov/"> D_Abdunazarov</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'COLLAPSABLE_USER_AREA': False,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': '404',
    'LOGIN_SPLASH': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fsitara.com%2Ftours%2Felement%2Fuzbekistan-geology-tour%2F&psig=AOvVaw3rq30RSO3WhXu2SPPjeUxw&ust=1637321165868000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIDqqunmofQCFQAAAAAdAAAAABAD',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/api/',
    },
    'MENU': (
        { 'type': 'title', 'label': 'main', 'apps': ('auth', 'register') },
        {'type': 'free', 'icon': 'fa fa-lock', 'label': 'Authentication', 'default_open': True, 'children': [
            {'type': 'model', 'label': 'Tadbirkorlar', 'name': 'customuser', 'app': 'register'},
            {'type': 'model', 'label': 'Groups', 'name': 'group', 'app': 'auth'},
            {'type': 'model', 'label': 'Permissions', 'name': 'permission', 'app': 'auth'},
        ]},
        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'User ?????????????????? (1-??????????)',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'carouselnews',
                    'label': '???????????????????? (????????????????)'
                },
                {
                    'name': 'twomaps',
                    'label': '?????????? ??????????'
                },
                {
                    'name': 'mineralresources',
                    'label': '?????????????? ??????????????????'
                },
                {
                    'name': 'office',
                    'label': '???????????? ???? ??????????????'
                },
                {
                    'name': 'companypurpose',
                    'label': '???????????? ????????????????????'
                },
                {
                    'name': 'companytasks',
                    'label': '???????????? ??????????????????'
                },
                {
                    'name': 'companytasksitems',
                    'label': '???????????? ?????????????????? (????)'
                },
                {
                    'name': 'auditory',
                    'label': '???????????????? ??????????????????'
                },
                {
                    'name': 'navbar',
                    'label': '????????????'
                },
                {
                    'name': 'navbaritem',
                    'label': '???????????? (????)'
                },
                {
                    'name': 'footer',
                    'label': '?????????? (????)'
                },

            )
        },
        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'User ?????????????????? (2-??????????)',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'staff',
                    'label': '????????????????'
                },
                {
                    'name': 'youthunion',
                    'label': '?????????? ????????????????'
                },
                {
                    'name': 'laws',
                    'label': '????????????????'
                },
                {
                    'name': 'profconnections',
                    'label': '?????????????? ???????? ???????? ?????????????????????????? ??????????????????'
                },
                {
                    'name': 'reportacceptance',
                    'label': '?????????????????? ?????????? ??????????'
                }

            )
        },
        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'User ?????????????????? (3-??????????)',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'university',
                    'label': '?????????????????????? ????????????????????????'
                },
                {
                    'name': 'news',
                    'label': '???????? ?????????????????????? ??????????'
                },
            )
        },

        {'type': 'model', 'label': '?????????????? ?????????????????? ????????????', 'name': 'excelform', 'app': 'mainapi', 'icon': 'fas fa-file-excel'},
        { 'type': 'model', 'label': '???????????????????? ??????????????????????', 'name': 'bookkeepingreport', 'app': 'mainapi', 'icon': 'fa fa-table' },

        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'Page ??????????????????',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'applicationloc',
                    'label': '?????????? ?????????????????? ?????? ?????????????????? ????????????????'
                },
                {
                    'name': 'businessman',
                    'label': '??????????????????'
                },
                {
                    'name': 'bankinfo',
                    'label': '???????????? ???????????????????? ???????? ???????????? ??????????????????????'
                },
                {
                    'name': 'mineinfo',
                    'label': '?????? ????????????'
                },
            )
        },


        {'type': 'title', 'label': 'Contents', 'apps': ('flatpages', )},
        {'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages'},
    ),
}
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
CORS_ORIGIN_ALLOW_ALL = True


db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())