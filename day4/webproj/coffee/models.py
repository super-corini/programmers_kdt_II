from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(default="", max_length=50)
    price = models.IntegerField(default=0,)

    def __str__(self):
        return self.name