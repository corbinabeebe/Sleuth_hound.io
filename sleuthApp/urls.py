"""sleuthApp Urls"""

from django.urls import path
from .views import (ProjectCreatView, ProjectListView, ProjectUpdateView)
from . import views

app_name = 'sleuthApp'

urlpatterns = [
    path('', views.index, name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/create', ProjectCreatView.as_view(), name='create_project'),
    path('project/<int:id>',views.project_view, name='project'),
    path('project/<int:pk>/edit', ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:id>/create_task/', views.create_task, name='create_task'),
    path('project/<int:project_id>/task/<int:task_id>/update_task', views.update_task, name='update_task'),
    path('project/<int:project_id>/task/<int:task_id>/comments', views.view_comments, name='view_comments'),
    path('project/<int:project_id>/task/<int:task_id>/add_comment', views.add_comment, name='add_comment'),
    path('project/<int:project_id>/task/<int:task_id>/update_comment/<int:comment_id>',views.update_comment, name='update_comment'),
    path('signup/', views.register, name='signup'),
]
