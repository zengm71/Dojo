from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('survey', views.fillSurvey),
    path('result', views.displaySurvey)
]
