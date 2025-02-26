from ninja import NinjaAPI
from ninja.throttling import AnonRateThrottle, AuthRateThrottle

openapi_info = NinjaAPI(
    openapi_extra={
        'info': {
            'title': 'Living Faith Church (Winners Chapel) CBD API',
            'version': '1.0',
            'termsOfService': 'https://example.com/terms/',
            'contact': {
                'name': 'LFC Johannesburg CBD API Support',
                'url': "https://winnerschapelcbd.com'",
            },
            'license': {
                'name': 'MIT Licence',
                'url': "https://winnerschapelcbd.com'",
            },
        }
    },
    title='Living Faith Church (Winners Chapel) CBD API',
    description='API with Swagger UI integration For LFC Johannesburg CBD',
    throttle=[
        AnonRateThrottle('5/s'),
        AuthRateThrottle('50/s'),
    ],
    csrf=True,
)


router = openapi_info
