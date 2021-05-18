from django.db import models

# Create your models here.

#class <모델이름>(models.Model):
class Coffee(models.Model):
    def __str__(self):
        return self.name
    #Field 1 - 하나의 열
    #field1 = models.FieldType()...
    #field1 = models.CharField()
    #field1 = models.IntegerField()
    #field1 = models.Booleanfield()
    """
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ...
    논리형 : Booleanfield
    시간/날짜 : DateTimeField
    등등
    """
    name = models.CharField(default="",max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)