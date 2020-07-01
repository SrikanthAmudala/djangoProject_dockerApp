from django.db import models


# Create your models here.

class Task(models.Model):

    userID = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    taskDueDate = models.DateField()

    def __str__(self):
        return self.title