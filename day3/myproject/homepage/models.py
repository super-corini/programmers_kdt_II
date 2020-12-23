from django.db import models


class Coffee(models.Model):
    name = models.CharField(default="", max_length=50)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
