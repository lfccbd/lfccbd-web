from django.urls import path

from .views import CheckupView

urlpatterns = [
	path('', CheckupView.as_view(), name='followup'),
]
