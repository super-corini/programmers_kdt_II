from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name

    # field1 = models.FieldType(default="", null=True)...
    """
    문자열: CharField
    숫자: IntegerField, SmallIntegerField, ...
    논리형: BooleanField
    시간/날짜: DateTimeField
    """
    name = models.CharField(default="", max_length=30) # max_length=~(important)
    price = models.IntegerField(default=0) # null: False(default)
    is_ice = models.BooleanField(default=False)
    