from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(default="", max_length=30, unique=True)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)

    def __str__(self):
        return self.name
