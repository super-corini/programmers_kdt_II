from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="Unknow", max_length=30)
    price = models.IntegerField(default=0)
    is_caffein = models.BooleanField(default=True)
    is_ice = models.BooleanField(default=False)
    img_url = models.CharField(default="", max_length=100, null=True, blank=True)