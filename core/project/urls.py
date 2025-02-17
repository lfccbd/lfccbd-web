from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from core.project.settings import DEBUG  # type: ignore
from core.project.settings import MEDIA_ROOT, MEDIA_URL  # type: ignore

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('core.api.urls')),
	path('favicon.ico', RedirectView.as_view(url='/static/assets/favicon/favicon.ico')),
]

# Add paths in debug mode
if DEBUG:
	import debug_toolbar

	urlpatterns += [
		path('__debug__/', include(debug_toolbar.urls)),
	] + static(MEDIA_URL, document_root=MEDIA_ROOT)
