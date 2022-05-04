"""
    Contains data models for sleuth_hound.io application
"""
from django.db import models

# Create your models here.
class User(models.Model):
    """
        User model class that maps objects to users in the user table
    """
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=25, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    """
        Task model class that maps objects to task
    """
    TASK_STATUS = (
        ('N', 'New'),
        ('I','In_Progress'),
        ('C','Completed'),
    )
    SEVERITY = (
        ('H', 'High'),
        ('L', 'Low'),
    )
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True)
    project_id = models.ForeignKey(
        'Project', default=None, on_delete=models.CASCADE)
    task_subject = models.CharField(max_length=30)
    details = models.TextField(max_length=500)
    date_opened = models.DateTimeField(auto_now_add=True)
    # close_date = models.DateTimeField(blank=True)
    task_status = models.CharField(max_length=1, choices=TASK_STATUS)
    severity = models.CharField(max_length=1, choices=SEVERITY)
    # assigned_user = models.ForeignKey(
    #     'User', default=None, on_delete=models.CASCADE)

class Project(models.Model):
    """
        Project model class that maps objects to projects
    """
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    """
        Comment model class that maps objects to comments in the db
    """
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=True)
    task_id = models.ForeignKey(
        'Task', default=None, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
