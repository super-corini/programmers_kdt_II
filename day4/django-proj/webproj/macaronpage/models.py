from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Macaron(models.Model):
    def __str__(self):
        return self.name
    
    # id : PK
    name = models.CharField(default='', max_length=50)
    price = models.IntegerField(default=0)


# class Stock(models.Model):
#     # id : PK
#     # Macaron_id : FK
#     amount = models.IntegerField(default=1)
#     warehouse_time = models.DateTimeField(auto_now_add=True) # 입고 시간
#     expired = models.DateTimeField(default=(warehouse_time+timedelta(days=7))) # 유통 기한
    


