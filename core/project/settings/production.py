# Space check
from core.project.settings import DEBUG, ENV, SECRET_KEY  # type: ignore

# Secrete key
SECRET_KEY = SECRET_KEY

# Allowed Host
ALLOWED_HOSTS = ENV.config('ALLOWED_HOSTS', cast=ENV.Csv())

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
		'OPTIONS': {
			'sslmode': 'require',
		},
	}
}

# Cors
CORS_ORIGIN_ALLOW_ALL = True

# Security Settings In Production Environment
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
# Prefix session cookie with '__Host-'
SESSION_COOKIE_NAME = '__Host-sessionid'
# Prefix CSRF cookie with '__Host-'
CSRF_COOKIE_NAME = '__Host-csrftoken'
SECURE_SSL_HOST = ENV.config('SECURE_SSL_HOST')
CSRF_TRUSTED_ORIGINS = ENV.config('CSRF_TRUSTED_ORIGINS', cast=ENV.Csv())


# Cors settings
CORS_ALLOWED_ORIGINS = ['https://winnerschapelcbd.com']


# Media settings
AWS_ACCESS_KEY_ID = ENV.config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = ENV.config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = ENV.config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = ENV.config('AWS_S3_ENDPOINT_URL')
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = ENV.config('AWS_LOCATION')
AWS_DEFAULT_ACL = ENV.config('AWS_DEFAULT_ACL')
AWS_S3_SIGNATURE_VERSION = ENV.config('AWS_S3_SIGNATURE_VERSION')
DEFAULT_FILE_STORAGE = 'core.project.settings.utils.storage_backends.PublicMediaStorage'
PUBLIC_MEDIA_LOCATION = ENV.config('PUBLIC_MEDIA_LOCATION')
MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/'
