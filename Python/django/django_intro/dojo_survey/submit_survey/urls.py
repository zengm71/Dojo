from django.urls import path     
from . import views
urlpatterns = [
    path('', views.fillSurvey),
    path('result', views.displaySurvey)
]
