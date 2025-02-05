from django.utils.timezone import timedelta

Simple_JWT = {
	'ACCESS_TOKEN_LIFETIME': timedelta(minutes=35),
	'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
	'ALGORITHM': 'HS512',
}

SWAGGER_SETTINGS = {
	'USE_SESSION_AUTH': False,
	'SECURITY_DEFINITIONS': {'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}},
}
