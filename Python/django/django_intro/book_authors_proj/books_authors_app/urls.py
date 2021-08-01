from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('authors', views.authors),
    path('addAuthor', views.addAuthor),
    path('books/<book_id>', views.book), 
    path('books/addAuthor2Book/<book_id>', views.addAuthor2Book),
    path('authors/<author_id>', views.author), 
    path('authors/addBook2Author/<author_id>', views.addBook2Author)
]
