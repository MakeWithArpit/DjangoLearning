from django.contrib import admin
from django.urls import path
from authenticationn.views import *

urlpatterns = [
    path('', auth_home, name='auth_home'),
    path('login', auth_login, name='auth_login'),
    path('register', auth_register, name='auth_register'),
    path('forgot', auth_forgot, name='auth_forgot'),
    path('admin/', admin.site.urls),
]
