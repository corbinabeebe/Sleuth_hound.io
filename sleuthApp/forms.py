from django import forms
from .models import Project
from bootstrap_modal_forms.generic import BSModalModelForm

class LoginForm(forms.Form):
    """login form"""
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class ProjectModelForm(BSModalModelForm):
    '''Project form'''
    
    class Meta:
        model = Project
        fields = ['title', 'description']