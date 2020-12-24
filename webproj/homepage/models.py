from django.db import models


# Create your models here.
class Coffee(models.Model):
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PhoneCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    company = models.ManyToManyField(PhoneCompany)

    def __str__(self):
        return self.name
