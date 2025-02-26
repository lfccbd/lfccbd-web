from django.urls import path

from .views import ContactPage

urlpatterns = [
	path('', ContactPage.as_view(), name='contact'),
]
