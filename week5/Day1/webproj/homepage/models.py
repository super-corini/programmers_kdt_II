from django.db import models

# Create your models here.
class Frog(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_salted = models.BooleanField(default=False)