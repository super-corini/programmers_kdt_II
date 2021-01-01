from django.db import models

# Create your models here.
# class <모델이름> (models.Model)


class Coffee(models.Model):
    def __str__(self):
        return self.name
    # field = models.타입
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)


class Bread(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=30)
    count = models.IntegerField(default=0)
