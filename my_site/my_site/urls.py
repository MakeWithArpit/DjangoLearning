from django.contrib import admin
from django.urls import path
from authenticationn.views import *

urlpatterns = [
    path('', home, name='home'),
    path('/login', login, name='login'),
    path('/register', register, name='register'),
    path('/forgot', forgot, name='forgot'),
    path('/contact', contact, name='contact'),
    path('/about', about, name='about'),

    path('admin/', admin.site.urls),
]
