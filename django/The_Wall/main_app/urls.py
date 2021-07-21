from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.register),
    path('wall', views.wall),
    path('logout', views.logout),
    path('login', views.login),
    path('wall_message', views.message),
    path('wall_comment/<int:message_id>', views.comment),
    path('wall_message/<int:message_id>/delete', views.delete)	   
]