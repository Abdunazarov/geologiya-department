import os.path
from pathlib import Path

import dj_database_url
import django_heroku
# from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-mvxkk)xax5e#$c4l7nzk6z7*584ml+c$)rrjdh!t^4&8gssm$d'


DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainAPI',
    'ckeditor',
    'rest_framework',
    'baton.autodiscover',

]

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


STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "static_root"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


BATON = {
    'SITE_HEADER': 'ЎЗРЕС Геология',
    'SITE_TITLE': 'Геология ахборот маркази Давлат корхонаси',
    'INDEX_TITLE': 'Геология сайти администрацияси',
    'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': 'copyright © 2017 <a href="https://napaautomotive.uz/ru"> Napa Automotive</a>', # noqa
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
    'GRAVATAR_DEFAULT_IMG': 'mp',
    'LOGIN_SPLASH': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fsitara.com%2Ftours%2Felement%2Fuzbekistan-geology-tour%2F&psig=AOvVaw3rq30RSO3WhXu2SPPjeUxw&ust=1637321165868000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIDqqunmofQCFQAAAAAdAAAAABAD',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/api/',
    },
    'MENU': (
        { 'type': 'title', 'label': 'main', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-address-card',
            'default_open': False,
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'User моделлари (1-қисим)',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'carouselnews',
                    'label': 'Янгиликлар (карусель)'
                },
                {
                    'name': 'twomaps',
                    'label': 'Иккта Карта'
                },
                {
                    'name': 'mineralresources',
                    'label': 'Минерал Ресурслар'
                },
                {
                    'name': 'office',
                    'label': 'Манзил ва телефон'
                },
                {
                    'name': 'companypurpose',
                    'label': 'Асосий мақсадлари'
                },
                {
                    'name': 'companytasks',
                    'label': 'Асосий вазифалар'
                },
                {
                    'name': 'companytasksitems',
                    'label': 'Асосий вазифалар (эл)'
                },
                {
                    'name': 'auditory',
                    'label': 'Мақсадли аудитория'
                },
                {
                    'name': 'navbar',
                    'label': 'Навбар'
                },
                {
                    'name': 'navbaritem',
                    'label': 'Навбар (эл)'
                },
                {
                    'name': 'footer',
                    'label': 'Футер (эл)'
                },

            )
        },
        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'User моделлари (2-қисим)',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'staff',
                    'label': 'Ходимлар'
                },
                {
                    'name': 'youthunion',
                    'label': 'Ёшлар иттифоқи'
                },
                {
                    'name': 'laws',
                    'label': 'Қарорлар'
                },
                {
                    'name': 'profconnections',
                    'label': 'Хисобот олиш учун масъулларнинг алоқалари'
                },
                {
                    'name': 'reportacceptance',
                    'label': 'Хисоботни қабул қилиш'
                }

            )
        },
        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'User моделлари (3-қисим)',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'university',
                    'label': 'Университет тадқиқотлари'
                },
                {
                    'name': 'news',
                    'label': 'Олиб борилаётган ишлар'
                },
            )
        },

        {'type': 'model', 'label': 'Минерал ресурслар базаси', 'name': 'excelform', 'app': 'mainapi', 'icon': 'fas fa-file-excel'},
        { 'type': 'model', 'label': 'Буғалтерия хисоботлари', 'name': 'bookkeepingreport', 'app': 'mainapi', 'icon': 'fa fa-table' },

        {
            'type': 'app',
            'name': 'mainapi',
            'label': 'Page Тадбиркор',
            'icon': 'fa fa-lock',
            'default_open': False,
            'models': (
                {
                    'name': 'applicationloc',
                    'label': 'Ариза берадиган жой тўғрисида маълумот'
                },
                {
                    'name': 'businessman',
                    'label': 'Тадбиркор'
                },
                {
                    'name': 'bankinfo',
                    'label': 'Хизмат кўрсатувчи банк бўйича маълумотлар'
                },
                {
                    'name': 'mineinfo',
                    'label': 'Кон ҳақида'
                },
            )
        },


        {'type': 'title', 'label': 'Contents', 'apps': ('flatpages', )},
        {'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages'},
        # {'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
    ),
}
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())