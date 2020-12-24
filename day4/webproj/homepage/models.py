from django.db import models

# Create your models here.
class Coffees(models.Model):
    def __str__(self):  # 대표 이름
        return self.name
    name = models.CharField(default = "none", max_length=30)
    is_ice = models.BooleanField(default = False)
    price = models.IntegerField(default = 0)
    count = models.IntegerField(default = 1)
