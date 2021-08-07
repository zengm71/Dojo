from django.urls import path     
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.new_form),
    path('shows/create', views.new),
    path('shows/<int:id>/update', views.update),
    path('shows/<int:id>', views.view, name = 'view'), 
    path('shows/<int:id>/edit', views.edit, name = 'edit'), 
    path('shows/<int:id>/delete', views.delete, name = 'delete')

]
