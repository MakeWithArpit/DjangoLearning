from django.contrib import admin
from django.urls import path
from mySite import views    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('about/', views.about_us),
    path('about/<int:num>', views.in_about_us), #dynamic url pattern. access via about/1 or about/2. in place of <int:num you can use <str:name> or <slug:slugname> etc based on your requirement
]
