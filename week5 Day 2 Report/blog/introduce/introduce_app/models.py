from django.db import models

# Create your models here.
class Burger(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default="",max_length=30, null=False)
    price = models.IntegerField(default=0, null=False)
    is_set = models.BooleanField(default=False)

    def __str__(self):
        return self.name