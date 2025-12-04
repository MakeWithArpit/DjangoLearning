from django.contrib import admin
from django.urls import path
from authenticationn.views import *

urlpatterns = [
    path('', auth_home, name='auth_home'),
    path('login', auth_login, name='auth_login'),
    path('admin/', admin.site.urls),
]
