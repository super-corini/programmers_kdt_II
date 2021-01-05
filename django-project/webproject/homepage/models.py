from django.db import models

# Create your models here.
class Introduction(models.Model):
    def __str__(self):
        return "Who am I?"

class Eda(models.Model):
    def __str__(self):
        return "EDA!"

class Coffee(models.Model):
    def __str__(self): # Coffee 객체를 대표하는 이름이 self.name이 된다
        return self.name
    name = models.CharField(primary_key = True, default = "", null = False, max_length = 30)
    price = models.IntegerField(default = 0)
    stock = models.IntegerField(default = 0)
    """
    method에 대해...
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ...
    논리형 : BooleanField
    시간/날짜 : DateTimeField
    
    param에 대해...
    default : 기본값 설정
    null : null val 허용을 Boolean으로 지정
    max_length = 최대길이
    ,,,
    """
