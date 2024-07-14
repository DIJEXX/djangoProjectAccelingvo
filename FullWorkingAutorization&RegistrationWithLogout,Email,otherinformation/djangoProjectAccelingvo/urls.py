from django.urls import path
from django.shortcuts import redirect
from django.contrib import admin

from myapp.views import main, login_user, logout_user, registry_user

urlpatterns = [
    path('', lambda request: redirect('main')),
    path('admin/', admin.site.urls),
    path('main/', main, name="main"),
    path('login/', login_user, name="login_user"),
    path('logout', logout_user, name="logout_user"),
    path('registry/', registry_user, name="registry_user"),
]
