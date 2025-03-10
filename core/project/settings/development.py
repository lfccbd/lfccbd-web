from core.project.settings import BASE_DIR, DEBUG, ENV, INSTALLED_APPS, MIDDLEWARE, SECRET_KEY  # type: ignore

# Secrete key
SECRET_KEY = SECRET_KEY

# Allowed Host
ALLOWED_HOSTS = ENV.config('ALLOWED_HOSTS', default='127.0.0.1', cast=ENV.Csv())

# Debug
DEBUG = DEBUG

# Database
DATABASES = {
    'default': {
        'ENGINE': ENV.config('ENGINE'),
        'NAME': ENV.config('NAME'),
        'HOST': ENV.config('HOST'),
        'USER': ENV.config('USER'),
        'PASSWORD': ENV.config('PASSWORD'),
        'PORT': ENV.config('PORT'),
    }
}

# Add django extension and debug toolbar to installed apps
if 'django_extensions' not in INSTALLED_APPS and 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS.insert(len(INSTALLED_APPS) - 2, 'django_extensions')
    INSTALLED_APPS.insert(len(INSTALLED_APPS) - 3, 'debug_toolbar')

# Django debug middleware
if 'debug_toolbar.middleware.DebugToolbarMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(
        len(MIDDLEWARE) - 1, 'debug_toolbar.middleware.DebugToolbarMiddleware'
    )

# set internal ips
INTERNAL_IPS = ['127.0.0.1']

# Cors settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
]


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = f'{BASE_DIR}/core/media'

# Captcha settings
RECAPTCHA_PUBLIC_KEY = ENV.config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = ENV.config('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_REQUIRED_SCORE = ENV.config('RECAPTCHA_REQUIRED_SCORE', cast=float)
