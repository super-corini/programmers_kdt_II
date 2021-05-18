from django.db import models

# Create your models here.
class Coffees(models.Model):
    name   = models.CharField(default='', max_length=30, unique=True)
    price  = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name