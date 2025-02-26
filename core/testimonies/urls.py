from django.urls import path
from .views import TestimonyPage

urlpatterns = [
	path('', TestimonyPage.as_view(), name='testimonies'),
]
