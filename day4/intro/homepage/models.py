from django.db import models

# Create your models here.
class Fruit(models.Model):
    def __str__(self):
        return self.name, self.price
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    stack = models.IntegerField(default=0)
    #img = models.ImageField(upload_to='fruit', null=True)
