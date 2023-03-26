from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
