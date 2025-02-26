DAISY_SETTINGS = {
    'SITE_TITLE': 'LFC CBD Admin',
    'SITE_HEADER': 'LFC CBD Admin',
    'INDEX_TITLE': 'Hi, welcome to your dashboard',
    'SITE_LOGO': '/static/assets/img/logo.png',
    'EXTRA_STYLES': [
        '/static/assets/css/daisyui.css',
    ],
    'EXTRA_SCRIPTS': [],
    'LOAD_FULL_STYLES': True,
    'SHOW_CHANGELIST_FILTER': True,
    'DONT_SUPPORT_ME': True,
    'APPS_REORDER': {
        'auth': {
            'icon': 'fa-solid fas fa-users-cog',
            'name': 'Groups',
            'hide': False,
            'app': 'auth',
            'divider_title': 'Auth',
        },
        'sites': {
            'icon': 'fa-solid fas fa-link',
            'name': 'Sites',
            'hide': False,
            'app': 'auth',
        },
        'otp_totp': {
            'icon': 'fa-solid fas fa-mobile',
            'name': 'OTP Device',
            'hide': False,
            'app': 'otp_totp',
            'divider_title': 'OTP',
        },
        'otp_static': {
            'icon': 'fa-solid fas fa-tasks',
            'name': 'OTP Static',
            'hide': False,
            'app': 'otp_totp',
        },
        'defender': {
            'icon': 'fa-solid fas fa-users-cog',
            'name': 'Security',
            'hide': False,
            'app': 'defender',
            'divider_title': 'Security',
        },
    },
}
