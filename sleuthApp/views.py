"""views.py used for managing views within the django app"""
from http.client import HTTPResponse
from django.views.generic import ListView
from .models import Project


# Create your views here.
class ProjectListView(ListView):
    """project list view class"""
    model = Project

def test_view(request):
    return HTTPResponse("Docker is working")