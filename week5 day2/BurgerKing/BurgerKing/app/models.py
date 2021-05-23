"""
Definition of models.
"""

from django.db import models

# Create your models here.

class burgers(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="",null=False, max_length=30)
    price = models.IntegerField(default=3000)
    stock = models.IntegerField(default=0)