from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now=False, auto_now_add=True)
    modification_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now=False, auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
    execution_status = models.BooleanField(default=False)
    description = models.TextField()
    board = models.ForeignKey('Board', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
