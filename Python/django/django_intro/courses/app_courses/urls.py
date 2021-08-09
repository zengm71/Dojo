from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('courses/destroy/<int:id>', views.destroy, name = 'destroy'), 
    path('courses/delete/<int:id>', views.delete, name = 'delete'),
    path('courses/comment/<int:id>', views.showComment, name = 'comment'), 
    path('courses/comment/addComment', views.addComment, name = 'addComment')

]
