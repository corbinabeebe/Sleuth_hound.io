from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class Tasks(models.Model):
    TASK_STATUS = (
        ('N', 'New'),
        ('I','In_Progress'),
        ('C','Completed'),
    )
    SEVERITY = (
        ('H', 'High'),
        ('L', 'Low'),
    )
    tasks_id = models.BigAutoField(primary_key=True)
    task_subject = models.CharField(max_length=30)
    details = models.TextField(max_length=500)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(blank=True)
    tasks_status = models.CharField(max_length=1, choices=TASK_STATUS)
    severity = models.CharField(max_length=1, choices=SEVERITY)

class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    completion = models.IntegerField()

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    body = models.TextField()