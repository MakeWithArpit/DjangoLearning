from django.contrib import admin
from django.urls import path
from mySite import views    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about_us, name='about'),
]
