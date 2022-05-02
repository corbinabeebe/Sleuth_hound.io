"""views.py used for managing views within the django app"""

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, FormView
from django.urls import reverse_lazy
import sleuthApp
from .models import Project, Task, User, Comment
from .forms import LoginForm, TaskForm


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

def project_detail_view(request, id):
    """shows project detail and tasks"""
    ## need to write code to make context accessible in html
    project = Project.objects.filter(id=id).all()
    all_tasks = Task.objects.filter(project_id=id).all()
    context_list = {'tasks': all_tasks, 'project': project}
    return render(request, 'sleuthApp/project_view.html', context=context_list)

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

class TaskCreateView(FormView):
    '''creates a new task to be added to the project'''
    form_class = TaskForm
    template_name = 'task_form.html'
    if form_valid:
        success_url = reverse_lazy(f'sleuthApp:project_detail/{project_id}')

    def form_valid(self, form):
        print(form.cleaned_data)
        project_id = form.cleaned_data['project_id']

        return super().form_valid(form)
