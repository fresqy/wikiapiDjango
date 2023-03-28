from django.contrib.auth import views as auth_views
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
]

