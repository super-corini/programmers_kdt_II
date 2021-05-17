from django.db import models

# Create your models here.
class Coffee(models.Model):
    ## 각 Attribute가 Columns가 된다.
    def __str__(self):
        return self.name

    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
    """
    default를 기본적으로 잡자, null 정하지 않으면, 기본값 False
    문자 : CharField   max_length 필수
    숫자 : IntegerField
    논리형 : BooleanField
    시간/날짜 : DateTimeField
    """