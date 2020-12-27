from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Macaron(models.Model):
    def __str__(self):
        return ' '.join([str(self.id), self.name, str(self.price), str(self.amount)])
    
    # id : PK
    name = models.CharField(default='', max_length=50)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)


class Stock(models.Model):
    def __str__(self):
        return str(self.macaron_id)

    # id : PK
    macaron = models.ForeignKey(Macaron, on_delete=models.CASCADE) # FK
    amount = models.IntegerField(default=1)
    warehouse_time = models.DateField(auto_now_add=True) # 입고 시간
    # expired = models.DateField() # 유통 기한
    # warehouse_time+timedelta(days=7) 이렇게 하고픈데..



