from django.urls import path

from .views import CheckupView, OutreachView

urlpatterns = [
    path('', CheckupView.as_view(), name='followup'),
    path('members/outreach/', OutreachView.as_view(), name='outreach'),
]
