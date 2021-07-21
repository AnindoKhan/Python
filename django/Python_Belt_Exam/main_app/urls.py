from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.register),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('login', views.login),	 
    path('create', views.create),
    path('trips/new',views.newTrip),
    path('edit/<int:trip_id>', views.edit),
    path('update/<int:trip_id>', views.update),
    path('trips/<int:trip_id>', views.info),
    path('delete/<int:trip_id>', views.delete),
]