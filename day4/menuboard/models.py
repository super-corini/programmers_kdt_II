from django.db import models

# Create your models here.
class Fruit(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    imgsrc = models.TextField()
    stock = models.IntegerField()