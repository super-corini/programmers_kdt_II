from django.db import models

# Create your models here.
class Burger(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_set = models.BooleanField(default=False)