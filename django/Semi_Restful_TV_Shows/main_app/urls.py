from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path ('shows/new', views.addShow),
    path ('shows/<int:show_id>', views.showInfo),
    path ('shows/<int:shows_id>/edit', views.edit),
    path ('shows/<int:shows_id>/delete', views.delete)	   
]
