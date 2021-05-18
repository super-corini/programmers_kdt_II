from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=50, unique = True)
    price = models.IntegerField(default=0, unique = False)

    