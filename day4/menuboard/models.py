from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to='menuboard/static/')
    stock = models.IntegerField()