from django.db import models

# Create your models here.
class Coffee(models.Model):
    class CupSize(models.TextChoices):
        Tall = '355ml'
        Grande = '473ml'
        Venti = '591ml'

    class CupSelction(models.TextChoices):
        In_Store_Cup = "IC"
        Personal_Cup = "PC"
        Disposable_Cup = "DC"

    def __str__(self) -> str:
        return " | ".join([str(self.order_date), self.product_name, self.size, ])


    product_name = models.CharField(null=False, max_length=100)
    size = models.CharField(max_length=10, choices=CupSize.choices, default=CupSize.Tall)
    cup_select = models.CharField(max_length=30, choices=CupSelction.choices, default=CupSelction.In_Store_Cup)
    prodcut_description = models.CharField(default="", max_length=500)
    ice_only = models.BooleanField(default=False)

    quantity = models.IntegerField(default=0)
    order_date = models.DateField()









