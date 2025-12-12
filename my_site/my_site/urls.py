from django.contrib import admin
from django.urls import path
from authenticationn.views import *

urlpatterns = [
    path('', home, name='home'),
    path('', login, name='login'),
    path('', register, name='register'),
    path('', forgot, name='forgot'),
    path('', contact, name='contact'),
    path('', about, name='about'),

    path('admin/', admin.site.urls),
]
