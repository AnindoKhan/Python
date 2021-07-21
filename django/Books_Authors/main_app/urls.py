from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	  
    path('create', views.create),
    path ('authors', views.authors),
    path ('author_create', views.author_create),
    path ('books/<int:book_id>', views.show_book),
    path ('authors/<int:author_id>', views.show_author),
    path ('add_book_to_author', views.addBook),
    path ('add_author_to_book', views.addAuthor)
]