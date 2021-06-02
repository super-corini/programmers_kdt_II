from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    # Field
    name = models.CharField(default='', max_length=30)  # Field 옵션의 null= 은 디폴트가 False이다 
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
   
    '''
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ...
    논리형 : BooleanField
    시간/날짜 : DateTimeField
    ...
    '''

class Burger(models.Model):
    def __str__(self):
        return self.name
    
    # id = models.IntegerField(primary_key=True)    # 자동생성
    name = models.CharField(default='',max_length=30)
    price = models.IntegerField(default=0)
    is_set = models.BooleanField(default=False)
