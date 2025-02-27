from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.urls import include, path
from django.views.generic import RedirectView
from project.settings.utils.otp import CustomAdminLoginView  # type: ignore

from core.project.settings import ADMIN_PATH, DEBUG, MEDIA_ROOT, MEDIA_URL  # type: ignore

User = get_user_model()


urlpatterns = [
	path(f'{ADMIN_PATH}/login/', CustomAdminLoginView.as_view(), name='admin_login'),
	path(f'{ADMIN_PATH}/', admin.site.urls),
	path('api/', include('core.api.urls')),
	path('contact/', include('core.contacts.urls')),
	path('resources/', include('core.resources.urls')),
	path('testimonies/', include('core.testimonies.urls')),
	path('prayer/', include('core.prayers.urls')),
	path('', include('core.pages.urls')),
	path('favicon.ico', RedirectView.as_view(url='/static/assets/favicons/favicon.ico')),
]


# Add paths in debug mode
if DEBUG:
	import debug_toolbar

	urlpatterns += [
		path('__debug__/', include(debug_toolbar.urls)),
	] + static(MEDIA_URL, document_root=MEDIA_ROOT)


# Inherit from the existing admin site class
class OTPAdminSite(admin.site.__class__):
	def get_log_entries(self, request):
		return LogEntry.objects.all().order_by('-action_time')


# Enforce 2FA.
admin.site.__class__ = OTPAdminSite

# Overrides the default 400 handler django.views.defaults.bad_request
handler400 = 'core.project.settings.utils.views.bad_request'
# Overrides the default 403 handler django.views.defaults.permission_denied
handler403 = 'core.project.settings.utils.views.permission_denied'
# Overrides the default 404 handler django.views.defaults.page_not_found
handler404 = 'core.project.settings.utils.views.page_not_found'
# Overrides the default 500 handler django.views.defaults.server_error
handler500 = 'core.project.settings.utils.views.server_error'
