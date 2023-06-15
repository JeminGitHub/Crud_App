from django.db import models
from django.urls import reverse


# Create your models here.
class Crud(models.Model):
    sl_no = models.IntegerField()
    item_name = models.CharField(max_length=250)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.item_name


    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])