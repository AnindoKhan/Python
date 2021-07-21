from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('user_guess', views.guess),
    path('low', views.index),
    path('correct', views.index),
    path('high', views.index),
]
