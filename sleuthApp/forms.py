"""
    file containing forms for Sleuth_hound.io
"""

from django.forms import ModelForm

from .models import User

class RegisterForm(ModelForm):
    """"
    Builds user registration form from user model
    """
    class Meta:
        """
            Meta class for Register Model
        """
        model = User
        fields = "__all__" # passes in all model fields as form fields

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'username': 'Username',
            'password': 'Password'
        }
