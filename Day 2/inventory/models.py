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

# Create your models here.
class Bugger(models.Model) :
    name = models.CharField(default="", max_length=75)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)
    outofstock = models.BooleanField(default=False)

    def __str__(self) :
        return self.name

    @property
    def to_list_without_ext(self) :
        return [self.name, self.price, self.stock, self.reserved, self.outofstock]
    
    def get_all_fields(self) :
        return self.name, self.price, self.stock, self.reserved, self.outofstock