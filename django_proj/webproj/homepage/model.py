from django.db import models

# Create your models here.

#class <모델이름>(models.Model):
class BugerMaterial(models.Model):
    def __str__(self):
        return self.type

    type = models.CharField(default="", max_length=30)
    #brend_name = models.CharField(default="",null=True, max_length=30)
    #director_name = models.CharField(default="",null=True, max_length=30)
    #price = models.IntegerField(default=0,null=True,)
    stock = models.IntegerField(default=0)
    is_set = models.BooleanField(default=False)

