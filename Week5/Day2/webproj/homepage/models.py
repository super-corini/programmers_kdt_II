from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    is_ground = models.BooleanField(default=False)

    def __str__(self):
        return self.title