from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    income_mean = models.IntegerField(null=True, blank=True)
    document_deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
