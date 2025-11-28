from pathlib import Path
import os

from import_export.formats.base_formats import XLSX

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-y%j&z(8vzos7et_h10(_h3u$*hsgb@v+gg=!eww%1gn00hh4ro'
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'import_export',
    'apps.geo',
    'apps.auxiliares',
    'apps.produccion',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Asegúrate de incluir la carpeta de plantillas
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'unidades_productivas',
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_Gf4reHTD3iYM',
        'HOST': 'ep-raspy-union-a25dpbib-pooler.eu-central-1.aws.neon.tech',  
        'PORT': '5432',
        # 'OPTIONS': {
        #     'options': '-c search_path=auxiliares,geo,public'
        # }       
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS    = [os.path.join(BASE_DIR, 'static/'),]
STATIC_ROOT         = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'API del Sistema de Unidades Productivas',
    'DESCRIPTION': 'Documentación de la API',
    'VERSION': '1.0.0',
    'SWAGGER_UI_DIST': 'SIDECAR', 
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}

JAZZMIN_SETTINGS = {
    "site_logo": "img/logito_mejorado.png",  # Ruta al logo en tu carpeta static
    "login_logo": "img/logo_cuspal.png",
    "site_header": "Panel Administrativo",  # Encabezado del admin
    "site_title": "Admin del sistema",  # Título del sitio
    "site_brand" : "Administración",
    "welcome_sign": "Bienvenido al Sistema de Registro y Control de unidades productivas",  # Mensaje de bienvenida
    "custom_css": "css/custom_admin.css",  # Ruta al archivo CSS
    "related_modal_active": False,
    "order_with_respect_to": ["auth", "produccion","auxiliares" ],
    "hide_apps": ["auth"],
    "topmenu_links": [
        {"name": "Inicio",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "auth"},
    ],
    "icons": {
        "auth": "fas fa-users-cog",  # Ícono para la app de autenticación
        "auth.User": "fas fa-user",  # Ícono para el modelo User
        "auth.Group": "fas fa-users",  # Ícono para el modelo Group
        "produccion.SituacionJuridica": "fa-solid fa-scale-balanced",  # Ícono para un modelo personalizado
        "produccion.Almacenaje" : "fa-solid fa-boxes-stacked",
        "produccion.UnidadProduccion" : "fa-solid fa-warehouse",
        "produccion.Produccion" : "fa-solid fa-arrow-trend-up",
        "auxiliares.Responsable": "fa-solid fa-people-roof",
        "auxiliares.RazonSocial": "fa-solid fa-book",
    },
}

#JAZZMIN_SETTINGS["show_ui_builder"] = True

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

IMPORT_EXPORT_FORMATS = [XLSX]
