"""views.py used for managing views within the django app"""

from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from sleuthApp.models import Project, User
from sleuthApp.forms import TaskForm, ProjectForm


class HomeView(TemplateView):
    """Homepage for sleuthhound.io"""
    template_name = 'sleuthApp/home.html'

def all_projects(request):
    '''Shows all projects'''
    projects = Project.objects.all()
    context = {
        "project": projects
    }
    return render(request, "sleuthApp/project_list.html", context=context)

def add_project(request):
    '''add a project to the instance'''
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            success_url = reverse_lazy('sleuthApp:projects')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form':form,
    })

# class ProjectCreatView(CreateView):
#     """View to create projects"""
#     model = Project
#     fields = "__all__"
#     success_url = reverse_lazy('sleuthApp:projects')


# class ProjectListView(ListView):
#     """View class for projects"""
#     model = Project
#     queryset = Project.objects.order_by('id')
#     context_object_name = "project_list"


# class ProjectDetailView(DetailView):
#     """View that allows one project to be seen on the screen"""
#     model = Project

# def project_detail_view(request, id):
#     """shows project detail and tasks"""
#     ## need to write code to make context accessible in html
#     project = Project.objects.filter(id=id).all()
#     all_tasks = Task.objects.filter(project_id=id).all()
#     context_list = {'tasks': all_tasks, 'project': project}
#     return render(request, 'sleuthApp/project_view.html', context=context_list)

# class ProjectUpdateView(UpdateView):
#     """Adds ability to update project information"""
#     model = Project
#     fields = "__all__"
#     success_url = reverse_lazy('sleuthApp:projects')


class UserCreateView(CreateView):
    """Model to create a user"""
    model = User
    fields = "__all__"
    success_url = reverse_lazy('sleuthApp:login')

# class LoginFormView(FormView):
#     """FormView to grab user login information"""
#     form_class = LoginForm
#     template_name = 'registration/login.html'

#     success_url = reverse_lazy('sleuthApp:projects')

#     # what to do with the form
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

# class TaskCreateView(FormView):
#     '''creates a new task to be added to the project'''
#     form_class = TaskForm
#     template_name = 'task_form.html'
#     if form_valid:
#         success_url = reverse_lazy(f'sleuthApp:project_detail/{project_id}')

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         project_id = form.cleaned_data['project_id']

#         return super().form_valid(form)

def create_task_form(request):
    '''creates a form for a task'''

    context = {
        "form" : TaskForm()
    }
    return render(request, "partials/task_form.html", context=context)

def project_detail(request, pk):
    '''project detail view'''
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }

    return render(request, "sleuthApp/project_detail.html", context=context)

# def create_project(request, pk):
#     '''function to create projects in the system'''
#     task = task.objects.get(pk=pk)
#     formset = ProjectForm

#     if request.method == "POST":
#         pass
