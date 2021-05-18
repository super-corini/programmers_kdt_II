from django.db import models

# Create your models here.
class Chicken(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=30)
    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)