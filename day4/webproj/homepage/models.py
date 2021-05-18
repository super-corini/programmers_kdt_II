from django.db import models


# Create your models here.
class Coffee(models.Model):
    """
    문자열: CharField
    숫자: IntegerField, SmallIntegerField, ...
    논리형: BooleanField
    시간/날짜: DateTimeField
    """
    def __str__(self) -> str:
        return self.name
    name = models.CharField(default="", max_length=30)  # null은 디폴트 false
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)


class Burger(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(default="", max_length=30)  # null은 디폴트 false
    price = models.IntegerField(default=0)
    is_set = models.BooleanField(default=False)

