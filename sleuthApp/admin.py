
"""
    Django admin file to register models in admin
"""
from django.contrib import admin
from .models import User, Task, Comment, Project


class TaskInLineAdmin(admin.TabularInline):
    model = Task

class CommentInLineAdmin(admin.TabularInline):
    model = Comment

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInLineAdmin]

class TaskAdmin(admin.ModelAdmin):
    inlines = [CommentInLineAdmin]
# Register your models here.
admin.site.register(User)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment)
admin.site.register(Project, ProjectAdmin)