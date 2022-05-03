from django import forms

from django.forms import ModelForm

from sleuthApp.models import Task, Comment, Project

class LoginForm(forms.Form):
    """login form"""
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class ProjectForm(ModelForm):
    """Project Form"""
    class Meta:
        '''Meta project class'''
        model = Project
        fields = ('title', 'description')

class TaskForm(ModelForm):
    """Task Form"""
    class Meta:
        '''Meta task class'''
        model = Task
        fields = ('task_subject', 'details', 'task_status', 'severity')

class CommentForm(ModelForm):
    """Comment Form"""
    class Meta:
        """Meta comment form"""
        model = Comment
        fields = (
            'body',
        )
