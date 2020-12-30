from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", null=False, max_length=30)    # default : 기본적으로 행에 담겨있는 값
    price = models.IntegerField(default=0)       # null : 비어있어도 되는지의 여부 (default : False)
    is_ice = models.BooleanField(default=False)     # max_length : 최대 길이
    '''
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField
    논리형 : BooleanField
    시간/날짜 : DateTimeField
    '''