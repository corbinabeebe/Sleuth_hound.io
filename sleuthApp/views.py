"""views.py used for managing views within the django app"""
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Project, Task, Comment
from .forms import RegisterForm, TaskForm, CommentForm




@login_required
def index(request):
    """Index functionview"""
    context = {
        'sleuth':'sleuth'
    }
    return render(request, 'sleuthApp/home.html', context)

# def logout(request):
#     """view to logout"""
#     return render(request, '/sleuthApp/')

def register(request):
    """view to register users"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            #this loads the profile instance the is created
            user.save()
            raw_password = form.cleaned_data['password1']

            #send user to login after signup
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # send to projects page upon successful login
            return HttpResponseRedirect('/sleuthApp/projects')
    else:
        form = RegisterForm()
    return render(request, 'sleuthApp/register_form.html', {
        'form': form,
    })


class ProjectCreatView(LoginRequiredMixin,CreateView):
    """View to create projects"""
    model = Project
    fields = "__all__"
    success_url = reverse_lazy('sleuthApp:projects')


class ProjectListView(LoginRequiredMixin,ListView):
    """View class for projects"""
    model = Project
    queryset = Project.objects.order_by('id')
    context_object_name = "project_list"


@login_required
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


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    """Adds ability to update project information"""
    model = Project
    fields = "__all__"
    success_url = reverse_lazy('sleuthApp:projects')


# class LoginFormView(LoginRequiredMixin,FormView):
#     """FormView to grab user login information"""
#     form_class = LoginForm
#     template_name = 'registration/login.html'

#     success_url = reverse_lazy('sleuthApp:projects')

#     # what to do with the form
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)


@login_required
def create_task(request, id):
    """fucntion based view to create a task"""
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
        'form': form,
        'project_id': id
    })


@login_required
def update_task(request, project_id, task_id):
    """Function view to update a task"""
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'/sleuthApp/project/{project_id}')
    else:
        data = {
            'task_subject' : task.task_subject,
            'details' : task.details,
            'task_status' : task.task_status,
            'severity': task.severity,
        }
        form = TaskForm(data)
    return render(request, 'sleuthApp/task_form.html', {
        'form': form,
        'project_id': project_id,
        'task_id': task_id
    })


@login_required
def view_comments(request, project_id, task_id):
    """shows task detail and comments associated to the task"""
    project = Project.objects.filter(id=project_id)
    task = Task.objects.filter(id=task_id)
    comments = Comment.objects.filter(task_id=task[0])
    context = {
        'project':project,
        'task':task,
        'comments': comments
    }
    return render(request, 'sleuthApp/comments_view.html', context)


@login_required
def add_comment(request, project_id, task_id):
    """Function view to add a comment to a task"""
    comment = Comment()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            task = Task.objects.filter(id=task_id)
            comment.task_id = task[0]
            comment.body = form.cleaned_data['body']
            comment.save()
            return HttpResponseRedirect(f'/sleuthApp/project/{project_id}/task/{task_id}/comments')
    else:
        form = CommentForm()
    return render(request, 'sleuthApp/comment_form.html', {
        'form': form,
        'project_id': project_id,
        'task_id': task_id
    })

@login_required
def update_comment(request, project_id, task_id, comment_id):
    """Function view to update comments"""
    comment = get_object_or_404(Comment, id=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'/sleuthApp/project/{project_id}/task/{task_id}/comments')
    else:
        data = {
            'body': comment.body,
        }
        form = CommentForm(data)
    return render(request, 'sleuthApp/comment_form.html', {
        'form': form,
        'project_id': project_id,
        'task_id': task_id
    })
