from django.db import models

class coffe(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(default="",max_length=30)
    price=models.IntegerField(default=0)
    is_ice=models.BooleanField(default=False)



    # Create your models here.
