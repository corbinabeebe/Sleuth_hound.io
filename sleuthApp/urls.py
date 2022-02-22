from atexit import register
from django.urls import path
from . import views

app_name = 'sleuth'

urlpatterns = [
    path('user_login/', views.user_login, name= 'login'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
]
