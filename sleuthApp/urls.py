"""sleuthApp Urls"""

from django.urls import path
from .views import (HomeView, LoginFormView, ProjectCreatView, ProjectListView,UserCreateView, ProjectUpdateView)
from . import views

app_name = 'sleuthApp'

urlpatterns = [
    path('user_login/', LoginFormView.as_view(), name= 'login'),
    path('', HomeView.as_view(), name='home'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/create', ProjectCreatView.as_view(), name='create_project'),
    # need to update this path to the project_detail function
    path('project/<int:id>',views.project_view, name='project'), 
    path('project/<int:pk>/edit', ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:id>/create_task/', views.create_task, name='create_task'),
    path('project/<int:project_id>/task/<int:task_id>/update_task', views.update_task, name='update_task')
]
