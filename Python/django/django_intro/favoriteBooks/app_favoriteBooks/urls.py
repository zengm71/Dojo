from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('logout', views.logout),
    path('add_book', views.add_book), 
    path('books/<int:user_id>/<int:book_id>', views.user_book), 
    path('books/<int:book_id>', views.book), 
    path('books/add/<int:user_id>/<int:book_id>', views.add_favorite),
    path('books/update_description', views.update_description), 
    path('books/delete_book', views.delete_book)
]