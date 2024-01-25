from django.db import models


class TodoApp(models.Model):

    choice = (('In Progress','In Progress'),('Finished','Finished'))

    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=choice, default='In Progress')