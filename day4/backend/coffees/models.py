from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)