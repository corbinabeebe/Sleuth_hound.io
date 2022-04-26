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
    path('project/', ProjectCreatView.as_view(), name='project'),
    # need to update this path to the project_detail function
    path('project_detail/<int:id>',views.project_detail_view, name='project_detail'), 
    path('update_project/<int:pk>', ProjectUpdateView.as_view(), name='update_project'),
]
