from django.contrib import admin
from django.urls import path
from project_admin.views import views as project_admin_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project_admin_views.home, name='home'),
]
