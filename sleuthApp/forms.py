from django import forms

class LoginForm(forms.Form):
    """login form"""
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
