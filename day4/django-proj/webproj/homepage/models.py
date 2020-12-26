from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    """
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ..
    논리형 : BooleanField
    시간/날짜 : DateTimeField
    """
    # Field 1
    name = models.CharField(default="", max_length=30)
    # Field 2
    price = models.IntegerField(default=0)
    # Field 3
    is_ice = models.BooleanField(default=False)


    