from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('final_checkout', views.final),
]
