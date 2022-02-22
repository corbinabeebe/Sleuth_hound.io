"""views.py used for managing views within the django app"""

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from .forms import RegisterForm


from .models import Project

# Create your views here.
class ProjectListView(ListView):
    """project list view class"""
    model = Project

def home(request):
    """
    Method for home page view
    """
    return render(request, 'sleuthApp/base.html')

def register(request):
    """
        Handles view for user registration
    """

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('sleuth:home'))

    else:
        form = RegisterForm()
    return render(request, 'registration/register_user.html', context={'form':form})

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
            return render(request, 'registration/login.html',
            {'error_message':'Username or password is incorrect, '  +
            'please try again or create an account!!!'})
    else:
        #if no post data is available, we should show the login screen again
        return render(request, 'registration/login.html')
