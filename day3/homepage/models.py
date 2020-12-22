from django.db import models


# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    price = models.IntegerField()
    is_ice = models.BooleanField(default=False)
