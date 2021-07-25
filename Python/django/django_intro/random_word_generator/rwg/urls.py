from django.urls import path     
from . import views
urlpatterns = [
    path('', views.init),
    path('random_word', views.display),
    path('generate', views.generate),
    path('reset', views.reset)
]
