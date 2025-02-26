from .views import PrayerRequestPage
from django.urls import path

urlpatterns = [
	path('request/form/', PrayerRequestPage.as_view(), name='prayer_request'),
]
