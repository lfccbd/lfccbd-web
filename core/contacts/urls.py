from .views import ContactPage
from django.urls import path

urlpatterns = [
	path('', ContactPage.as_view(), name='contact'),
]
