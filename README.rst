.. figure:: https://winnerschapelcbd.com/static/assets/img/logo.png
    :align: center


=============
Winners CBD
=============

Winners Chapel JHB CBD is part of the Living Faith Church Worldwide, a mandate By God 
Through his Servant Bishop David Oyedepo for the Liberation of mankind. As a Commission, 
we have experienced amazing testimonies ever since this commission was handed down - 
that is over thirty years now, To God be the glory.




==========
Setup
==========

Set environment variable for Django Secret Key, Debug, Allowed Host, Admin Path andIdle lockout time(s). 
Also add configuration for Database, Django Defender and Email with SMTP Host.

.. code-block:: bash

    # Security
    SECRET_KEY = '...'
    DEBUG = '...'
    ALLOWED_HOSTS = '...'
    DJANGO_ENV = '...' # Production or Development
    ADMIN_PATH = '...'
    AUTO_LOGOUT_IDLE_TIME = '...' 


    # Database
    ENGINE = '...'
    NAME = '...'
    HOST = '...'
    USER = '...'
    PASSWORD = '...'
    PORT = '...'

    # Defender Settings
    DEFENDER_LOGIN_FAILURE_LIMIT = '...'
    DEFENDER_LOCK_OUT_BY_IP_AND_USERNAME = '...'
    DEFENDER_COOLOFF_TIME = '...'
    DEFENDER_ATTEMPT_COOLOFF_TIME = '...'
    DEFENDER_LOCKOUT_TEMPLATE = '...'
    DEFENDER_LOCKOUT_URL = '...'
    DEFENDER_USERNAME_FORM_FIELD = '...'
    DEFENDER_STORE_ACCESS_ATTEMPTS = '...'
    DEFENDER_ACCESS_ATTEMPT_EXPIRATION = '...'
    DEFENDER_REDIS_URL = '...'
    DEFENDER_GET_USERNAME_FROM_REQUEST_PATH = '...'
    DEFENDER_REVERSE_PROXY_HEADER = '...'
    DEFENDER_BEHIND_REVERSE_PROXY = '...'

    # Email
    EMAIL_BACKEND = '...'
    EMAIL_PORT = '...'
    EMAIL_HOST = '...'
    EMAIL_HOST_USER = '...'
    EMAIL_HOST_PASSWORD = '...'
    DEFAULT_FROM_EMAIL = '...'
    SERVER_EMAIL = '...'
    EMAIL_SUBJECT_PREFIX = '...'
    EMAIL_USE_TSL = '...'


Additional Setup
-----------------

Set config for *Sentry*, *DigitalOcean Spaces*, project maintenance, *NH3*, *CSP* and *Import/Export*.

.. code-block:: bash

    # Sentry
    SENTRY_DNS = '...'
    SENTRY_REPORT_URL = '...'


    USE_SPACES = '..' # True or False
    AWS_REGION_NAME = '...'
    AWS_ACCESS_KEY_ID = '...'
    AWS_SECRET_ACCESS_KEY = '...'
    AWS_STORAGE_BUCKET_NAME = '...'
    AWS_S3_ENDPOINT_URL = '...'
    AWS_LOCATION = '...'
    AWS_S3_SIGNATURE_VERSION = '...'
    PUBLIC_MEDIA_LOCATION = '...'
    AWS_DEFAULT_ACL = '...'


    MAINTENANCE_MODE = '...' # True or False
    MAINTENANCE_MODE_STATE_BACKEND = '...'
    MAINTENANCE_MODE_STATE_FILE_PATH = '...'
    MAINTENANCE_MODE_IGNORE_ADMIN_SITE = '...'
    MAINTENANCE_MODE_IGNORE_ANONYMOUS_USER = '...'
    MAINTENANCE_MODE_IGNORE_AUTHENTICATED_USER = '...'
    MAINTENANCE_MODE_IGNORE_STAFF = '...'
    MAINTENANCE_MODE_IGNORE_SUPERUSER = '...'
    MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS = '...'
    MAINTENANCE_MODE_GET_CONTEXT = '...'
    MAINTENANCE_MODE_IGNORE_TESTS = '...'
    MAINTENANCE_MODE_LOGOUT_AUTHENTICATED_USER = '...'
    MAINTENANCE_MODE_RESPONSE_TYPE = '...'
    MAINTENANCE_MODE_TEMPLATE = '...'
    MAINTENANCE_MODE_STATUS_CODE = '...'
    MAINTENANCE_MODE_RETRY_AFTER = '...'
    MAINTENANCE_MODE_IGNORE_URLS = '...'


    # NH3 settings
    NH3_ALLOWED_TAGS = '...'
    NH3_ALLOWED_ATTRIBUTES = '...'

    # csp
    SECURE_SSL_HOST = '...'
    CSRF_TRUSTED_ORIGINS = '...'

    # django import/export
    IMPORT_EXPORT_IMPORT_IGNORE_BLANK_LINES = '...'
    IMPORT_EXPORT_ESCAPE_FORMULAE_ON_EXPORT = '...'
    IMPORT_EXPORT_IMPORT_PERMISSION_CODE = '...'
    IMPORT_EXPORT_EXPORT_PERMISSION_CODE = '...'




Recaptcha Setup
----------------

Set *Google Recaptcha* public and private key in environment variables. 
Public and private key can be gotten from *https://developers.google.com/recaptcha/*. 
Ensure you use :emphasis:`reCAPTCHA v3`.

.. code-block:: bash

    RECAPTCHA_PUBLIC_KEY = '...'
    RECAPTCHA_PRIVATE_KEY = '...'
    PRODUCTION_RECAPTCHA_PUBLIC_KEY = '...'
    PRODUCTION_RECAPTCHA_PRIVATE_KEY = '...'
    RECAPTCHA_REQUIRED_SCORE = '...'



Running Project
----------------

Setup
^^^^^^^^^^^

.. code-block:: bash

    make setup


create Superuser
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    make superuser


Run Server
^^^^^^^^^^^
.. code-block:: bash

    make runserver



Running Test 
^^^^^^^^^^^^^^

.. code-block:: bash

    make test
