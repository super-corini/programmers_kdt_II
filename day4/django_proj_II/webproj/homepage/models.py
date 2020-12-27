from django.db import models

# Create your models here.
class Bakery(models.Model):
    def __str__(self):
        return self.name

    name=models.CharField(default="", max_length=40)
    price=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
