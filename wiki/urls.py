from django.urls import path
from . import views


urlpatterns = [
    path('', views.wiki, name="wiki"),
    path('save_search/', views.save_search, name='save_search'),
    path('archives/', views.archives, name='archives'),


]
