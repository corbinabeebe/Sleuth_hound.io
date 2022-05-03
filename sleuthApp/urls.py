"""sleuthApp Urls"""

from django.urls import path
from .views import (HomeView, UserCreateView,)
from . import views


app_name = 'sleuthApp'

urlpatterns = [
    #path('user_login/', LoginFormView.as_view(), name= 'login'),
    path('', HomeView.as_view(), name='home'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('all_projects/', views.all_projects, name='projects'),
    path('project/add', views.add_project, name='add_project'),
    path('project/<int:id>', views.project_detail_view, name='view_project'),
    path('project/<int:pk>/edit', views.edit_project, name='edit_project'),
    # path('project/<int:pk>/task/add', views.add_task, name='add_task'),
    # path('project/<int:pk>/task/edit/<int:pk>',views.update_task, name='update_task'),
    # path('project/<int:pk>/task/<int:pk>/comment/add',
    #      views.add_comment, name='add_comment'),
    # path('project/<int:pk>/task/<int:pk>/comment/update/<int:pk>',
    #      views.update_comment, name='udpate_comment'),
]
