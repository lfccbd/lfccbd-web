from django.urls import path

from .views import PrayerRequestPage

urlpatterns = [
	path('request/form/', PrayerRequestPage.as_view(), name='prayer_request'),
]
