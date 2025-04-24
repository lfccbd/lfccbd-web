from django.urls import path

from .views import AccountLogout, AccountSignIn, AccountSuspended

urlpatterns = [
    path('login/', AccountSignIn.as_view(), name='account_login'),
    path('logout/', AccountLogout.as_view(), name='account_logout'),
    path('user/suspended/', AccountSuspended.as_view(), name='account_suspended'),
]
