from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('project/<str:pk>/', views.project, name = 'project'),
    path('createproject/', views.createProject, name = 'createProject'),
    path('editproject/<str:pk>/', views.editProject, name = 'editProject'),
    path('deleteproject/<str:pk>/', views.deleteProject, name = 'deleteProject'),

]