from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)

    
class Icecream(models.Model):
    def __str__(self):
        return self.name

    flavor = models.CharField(default="", max_length=30)
    size = models.CharField(default="", max_length=20)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    

