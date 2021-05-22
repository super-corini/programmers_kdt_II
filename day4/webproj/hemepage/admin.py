from django.contrib import admin
from .models import Coffee
from .model import Coffees

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Coffees)