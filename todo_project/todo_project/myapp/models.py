from django.db import models


# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=250)
    priority = models.CharField(max_length=10, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])
    date = models.DateField()

    def __str__(self):
        return self.name
