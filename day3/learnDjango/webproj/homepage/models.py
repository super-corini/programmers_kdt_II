from django.db import models

# Create your models here.
class Lol(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default = "", max_length=30)
    position = models.CharField(default = "", max_length=30)
    role = models.CharField(default = "", max_length=30)
    price = models.IntegerField(default = 0)

