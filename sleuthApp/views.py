"""views.py used for managing views within the django app"""

from concurrent.futures.process import _threads_wakeups
import django
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Project, User, Task
from .forms import LoginForm


class HomeView(TemplateView):
    """Homepage for sleuthhound.io"""
    template_name = 'sleuthApp/home.html'

class ProjectCreatView(CreateView):
    """View to create projects"""
    model = Project
    fields = "__all__"
    success_url = reverse_lazy('sleuthApp:projects')

class ProjectListView(ListView):
    """View class for projects"""
    model = Project
    queryset = Project.objects.order_by('id')
    context_object_name = "project_list"

class ProjectDetailView(DetailView):
    """View that allows one project to be seen on the screen"""
    model = Project

def project_detail(request):
    """shows project detail and tasks"""
    project = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, 'project_detail.html',{project=project, tasks=tasks})


class ProjectUpdateView(UpdateView):
    """Adds ability to update project information"""
    model = Project
    fields = "__all__"
    success_url = reverse_lazy('sleuthApp:projects')

class UserCreateView(CreateView):
    """Model to create a user"""
    model = User
    fields = "__all__"
    success_url = reverse_lazy('sleuthApp:login')

class LoginFormView(FormView):
    """FormView to grab user login information"""
    form_class = LoginForm
    template_name = 'registration/login.html'

    success_url = reverse_lazy('sleuthApp:projects')

    # what to do with the form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)