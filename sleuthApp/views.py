"""views.py used for managing views within the django app"""


from distutils.log import error
import re
from django.shortcuts import render
from django.views.generic import ListView
from  django.contrib.auth import authenticate, login
from .models import Project


# Create your views here.
class ProjectListView(ListView):
    """project list view class"""
    model = Project

def user_login(request):
    """
    Method to allows users to login to the system
    """
    if request.method == 'POST':

        #grab data from post request
        username = request.POST['username']
        password = request.POST['password']

        #check if username and password are correct compared to the db
        user = authenticate(username=username, password=password)
        if user is not None:
            # logs user in using session cookies
            login(request, user)
            return render(request, 'projects.html')
        else:
            return render(request, 'sleuthApp/login.html', {'error_message':'Username or password is incorrect, please try again or create an account!!!'})
    else:
        #if no post data is available, we should show the login screen again
        return render(request, 'sleuthApp/login.html')
