from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Sneaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    is_limited_edition = models.BooleanField(default=False)
    brand = models.CharField(max_length=8, choices=[("Nike", "Nike"), ("Adidas", "Adidas")])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Sneaker Details', kwargs={'id': self.id})
    