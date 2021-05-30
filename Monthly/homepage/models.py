from django.db import models

# Create your models here.
class Coffee(models.Model):
    """
    문자열 field1 = models.ChartField()
    숫자 field1 = models.IntegerField()
    숫자 field1 = models.SmallIntegerField()
    논리형 field1 = models.BooleanField()
    날짜시간 field1 = models.DateTimeField()
    """
    def __str__(self):
        return self.name
    name = models.ChartField(default = "", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)