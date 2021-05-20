from django.db import models

# Create your models here

class Burger(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(default='', max_length=30)
    price = models.IntegerField(default=0)