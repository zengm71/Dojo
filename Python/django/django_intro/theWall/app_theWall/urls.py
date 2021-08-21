from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login), 
    path("logout", views.logout),
    path("wall", views.wall), 
    path("wall/createPost", views.createPost), 
    path("wall/delete/<int:post_id>", views.deletePost), 
    path("wall/<int:post_id>/createComment", views.createComment)
]