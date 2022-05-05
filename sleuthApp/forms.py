from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from sleuthApp.models import Task, Comment

class RegisterForm(UserCreationForm):
    """form class used to register a new user"""
    class Meta:
        """Meta user registration form class"""
        model = User
        fields = ('username', 'password1', 'password2')

class TaskForm(ModelForm):
    """Task Form"""
    class Meta:
        '''Meta task class'''
        model = Task
        fields = ['task_subject', 'details', 'task_status', 'severity']

class CommentForm(ModelForm):
    """Comment Form"""
    body = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Enter comment here:'}))
    class Meta:
        '''Meta class for comments'''
        model = Comment
        fields = ['body']
