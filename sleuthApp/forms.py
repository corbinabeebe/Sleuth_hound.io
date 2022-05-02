from django import forms
from django.forms import ModelForm

from sleuthApp.models import Task

class LoginForm(forms.Form):
    """login form"""
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class TaskForm(ModelForm):
    """Task Form"""
    class Meta:
        '''Meta task class'''
        model = Task
        fields = ['task_subject', 'details', 'task_status', 'severity']
        