from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(default="", null=False, max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)

class Fruit(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(default="", null=False, max_length=50)
    stock = models.IntegerField(default=0)