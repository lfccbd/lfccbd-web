from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.throttling import AnonRateThrottle, AuthRateThrottle


def staff_required_403(view_func):
	def _wrapped_view(request: HttpRequest, *args, **kwargs):
		# check if user is authenticated and is staff
		if not request.user.is_authenticated or not request.user.is_staff:
			raise PermissionDenied
		# user is authenticated, call the original documentation view
		return view_func(request, *args, **kwargs)

	return _wrapped_view


openapi_info = NinjaAPI(
	openapi_extra={
		'info': {
			'title': 'Living Faith Church (Winners Chapel) CBD API',
			'version': '1.0',
			'termsOfService': 'https://winnerschapelcbd.com',
			'contact': {
				'name': 'LFC Johannesburg CBD API Support',
				'url': 'https://winnerschapelcbd.com/contact/',
			},
			'license': {
				'name': 'MIT Licence',
				'url': 'https://github.com/lfccbd/lfccbd-web/blob/main/LICENSE',
			},
		}
	},
	title='Living Faith Church (Winners Chapel) CBD API',
	description='API with Swagger UI integration For LFC Johannesburg CBD',
	docs_decorator=staff_required_403,
	throttle=[
		AnonRateThrottle('5/s'),
		AuthRateThrottle('50/s'),
	],
	csrf=True,
)


router = openapi_info
