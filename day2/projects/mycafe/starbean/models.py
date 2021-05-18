from django.db import models


class Coffees(models.Model):
    drink = models.CharField(max_length=100)  # 음료 종류(이름)
    stock = models.IntegerField()             # 재고

    def __str__(self):
        return self.drink
