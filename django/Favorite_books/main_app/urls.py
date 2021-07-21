from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.register),
    path('books', views.books),
    path('logout', views.logout),
    path('login', views.login),
    path('add_book',views.addBook),
    path('books/<int:book_id>',views.bookInfo), 
    path('books/<int:books_id>/edit',views.edit),
    path('books/<int:books_id>/edit_book',views.editBook),
    path('books/<int:books_id>/delete',views.delete),
    path('books/<int:books_id>/user/<int:user_id>', views.favorite),
    path('books/<int:books_id>/user/<int:user_id>/unfavorite', views.unfavorite)
]
