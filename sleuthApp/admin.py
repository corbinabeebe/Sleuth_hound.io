
"""
    Django admin file to register models in admin
"""
from django.contrib import admin
from .models import User, Task, Comment, Project

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Project)
