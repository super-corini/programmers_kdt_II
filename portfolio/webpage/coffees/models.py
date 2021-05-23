from django.db import models

# Create your models here.
class Coffees(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    avaiable = models.BooleanField(default="True")

    def __str__(self):
        return self.name