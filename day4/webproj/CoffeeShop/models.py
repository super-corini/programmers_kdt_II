from django.db import models

# Create your models here.
class Coffee(models.Model):
    
    def __str__(self):
        return "name: {} ".format(self.name) + "price: {}".format(self.price)
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="",max_length=30)
    price = models.IntegerField(default=0)
