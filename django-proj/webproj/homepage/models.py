from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    # Field 1,2,3 : (이 클래스를 통해 만들어진 객채들(row)이 가지게 될 속성(column))
    name = models.CharField(default="", null=False, max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
    '''
    FieldType 종류
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ...
    논리형 : BooleanField
    시간/날짜 : DateTimeField
    ...
    '''

class CoffeeBeen(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=30)
    stock = models.IntegerField(default=0)
    # last_purchased = models.DateTimeField(auto_now=True)


