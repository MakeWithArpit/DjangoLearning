from django.contrib import admin
from django.urls import path
from a_home.views import *

urlpatterns = [
    path('', home, name='home'),
]
