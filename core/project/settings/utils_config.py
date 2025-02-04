import jinja2
import sentry_sdk

from core.project.settings import BASE_DIR, ENV, MAINTENANCE_MODE, PROJECT_DIR  # type: ignore

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [f'{BASE_DIR}/core/jinja2'],
        'APP_DIRS': True,
        'OPTIONS': {
            'autoescape': False,
            'undefined': jinja2.StrictUndefined,
            'environment': 'core.project.settings.jinja.env.JinjaEnvironment',
            'extensions': [
                'jinja2.ext.loopcontrols',
                'jinja2.ext.do',
                'core.project.settings.jinja.extensions.DjangoNow',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f'{BASE_DIR}/core/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = f'{BASE_DIR}/core/static'
STATICFILES_DIRS = [f'{PROJECT_DIR}/static']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = f'{BASE_DIR}/core/media'

# Email settings
EMAIL_BACKEND = ENV.config('EMAIL_BACKEND')
EMAIL_PORT = ENV.config('EMAIL_PORT')
EMAIL_HOST = ENV.config('EMAIL_HOST')
EMAIL_HOST_USER = ENV.config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = ENV.config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = ENV.config('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = ENV.config('SERVER_EMAIL')
EMAIL_SUBJECT_PREFIX = ENV.config('EMAIL_SUBJECT_PREFIX')
EMAIL_USE_TSL = ENV.config('EMAIL_USE_TSL')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Sentry config
sentry_sdk.init(
    dsn=ENV.config('SENTRY_DNS'),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# Maintenance mode
MAINTENANCE_MODE = MAINTENANCE_MODE
MAINTENANCE_MODE_STATE_BACKEND = ENV.config('MAINTENANCE_MODE_STATE_BACKEND')
MAINTENANCE_MODE_STATE_FILE_PATH = ENV.config('MAINTENANCE_MODE_STATE_FILE_PATH')
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = ENV.config('MAINTENANCE_MODE_IGNORE_ADMIN_SITE', cast=bool)
MAINTENANCE_MODE_IGNORE_ANONYMOUS_USER = ENV.config('MAINTENANCE_MODE_IGNORE_ANONYMOUS_USER', cast=bool)
MAINTENANCE_MODE_IGNORE_AUTHENTICATED_USER = ENV.config('MAINTENANCE_MODE_IGNORE_AUTHENTICATED_USER', cast=bool)
MAINTENANCE_MODE_IGNORE_STAFF = ENV.config('MAINTENANCE_MODE_IGNORE_STAFF', cast=bool)
MAINTENANCE_MODE_IGNORE_SUPERUSER = ENV.config('MAINTENANCE_MODE_IGNORE_SUPERUSER', cast=bool)
MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS = (
    None
    if ENV.config('MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS') == 'None'
    else ENV.config('MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS')
)  # noqa: E501
MAINTENANCE_MODE_GET_CONTEXT = (
    None if ENV.config('MAINTENANCE_MODE_GET_CONTEXT') == 'None' else ENV.config('MAINTENANCE_MODE_GET_CONTEXT')
)  # noqa: E501
MAINTENANCE_MODE_IGNORE_TESTS = ENV.config('MAINTENANCE_MODE_IGNORE_TESTS', cast=bool)
MAINTENANCE_MODE_LOGOUT_AUTHENTICATED_USER = ENV.config('MAINTENANCE_MODE_LOGOUT_AUTHENTICATED_USER', cast=bool)
MAINTENANCE_MODE_RESPONSE_TYPE = ENV.config('MAINTENANCE_MODE_RESPONSE_TYPE')
MAINTENANCE_MODE_STATUS_CODE = ENV.config('MAINTENANCE_MODE_STATUS_CODE', cast=int)
MAINTENANCE_MODE_RETRY_AFTER = ENV.config('MAINTENANCE_MODE_RETRY_AFTER', cast=int)
MAINTENANCE_MODE_IGNORE_URLS = ENV.config('MAINTENANCE_MODE_IGNORE_URLS', cast=ENV.Csv())
MAINTENANCE_MODE_TEMPLATE = ENV.config('MAINTENANCE_MODE_TEMPLATE')
