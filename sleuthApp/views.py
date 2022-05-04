"""views.py used for managing views within the django app"""
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, FormView
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


def project_view(request, id):
    """shows project detail and tasks"""
    ## need to write code to make context accessible in html
    project = Project.objects.filter(id=id)
    tasks = Task.objects.filter(project_id=id).all()
    context = {
        'project':project,
        'tasks':tasks
    }
    return render(request, 'sleuthApp/project_view.html', context)

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

def create_task(request, id):
    task = Task()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            projects = Project.objects.filter(id=id)
            task.project_id = projects[0]
            task.task_subject = form.cleaned_data['task_subject']
            task.details = form.cleaned_data['details']
            task.task_status = form.cleaned_data['task_status']
            task.severity = form.cleaned_data['severity']
            task.save()
            return HttpResponseRedirect(f'/sleuthApp/project/{id}')
    else:
        form = TaskForm()
    return render(request, 'sleuthApp/task_form.html', {
        'form': form
    })

def update_task(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'/sleuthApp/project/{project_id}')
    else:
        form = TaskForm()
    return render(request, 'sleuthApp/task_form.html', {
        'form': form
    })