from django.urls import path

from .views import MediaContent, ResourcesListView

urlpatterns = [
    path('', ResourcesListView.as_view(), name='resources'),
    path('media/content/<str:id>/', MediaContent.as_view(), name='media_content'),
]
