from django.urls import path     
from . import views
urlpatterns = [
    path('users', views.index),
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register)

]