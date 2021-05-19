from django.db import models

# Create your models here.
class Buger(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(default='', max_length=30)
    price = models.IntegerField(default=0)
    coke = models.IntegerField(default=2000)
    set_menu = models.BooleanField(default=False)