from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.register),
    path('home', views.home),
    path('logout', views.logout),
    path('login', views.login) ,	   
]