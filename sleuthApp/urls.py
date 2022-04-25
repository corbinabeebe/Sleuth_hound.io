from django.urls import path
from .views import (HomeView, LoginFormView, ProjectListView, UserCreateView)

app_name = 'sleuthApp'

urlpatterns = [
    path('user_login/', LoginFormView.as_view(), name= 'login'),
    path('', HomeView.as_view(), name='home'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('projects/', ProjectListView.as_view(), name='projects'),
]
