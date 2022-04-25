from django.urls import path
from .views import (HomeView, LoginFormView, ProjectCreatView, ProjectListView, UserCreateView, ProjectDetailView, ProjectUpdateView)

app_name = 'sleuthApp'

urlpatterns = [
    path('user_login/', LoginFormView.as_view(), name= 'login'),
    path('', HomeView.as_view(), name='home'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/', ProjectCreatView.as_view(), name='project'),
    path('project_detail/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('update_project/<int:pk>', ProjectUpdateView.as_view(), name='update_project'),
]
