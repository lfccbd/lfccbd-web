from core.project.settings import ADMIN_PATH  # type: ignore

# Allowed Host
ALLOWED_HOSTS = ['127.0.0.1:8000']

# Admin path
ADMIN_PATH = ADMIN_PATH

# Application definition
INSTALLED_APPS = [
	'jazzmin',
	# core apps
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'django.contrib.humanize',
	# third party apps
	'defender',
	'maintenance_mode',
	'corsheaders',
	# app
	'core.user.apps.UserConfig',
	# third party apps by position
	'django_filters',
	'simple_history',
	'drf_yasg',
	'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	# Corsheaders
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	# Auto logout
	'django_auto_logout.middleware.auto_logout',
	# CSP
	'csp.middleware.CSPMiddleware',
	# Custom csp for error pages
	'core.project.settings.middleware.custom_csp.CustomCSPMiddleware',
	# Remote address middleware, useful for security
	'core.project.settings.middleware.remoteAddr.RemoteAddrMiddleware',
	# Current request middleware
	'core.project.settings.middleware.current_request.RequestMiddleware',
	# Simple history middleware
	'simple_history.middleware.HistoryRequestMiddleware',
	# Defender for security
	'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'core.project.urls'

WSGI_APPLICATION = 'core.project.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_TZ = True

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth Backend
AUTHENTICATION_BACKENDS = [
	# Django ModelBackend is the default authentication backend.
	'django.contrib.auth.backends.ModelBackend',
]

# Site settings
SITE_ID = 1

# Custom User
AUTH_USER_MODEL = 'user.Users'
