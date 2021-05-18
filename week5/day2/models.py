from django.db import models
from datetime import date

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
    '''
    문자열: CharField
    숫자: IntegerField, SmallIntegerField, ...
    논리형: BooleanField
    시간/날짜: DateTimeField 
    '''

class BaskinRobbins(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=20)
    serving_size = models.IntegerField(default="115")
    calory = models.IntegerField(default=0)
    allergy = models.CharField(default="-", max_length=200)
