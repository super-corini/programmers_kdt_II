from django.contrib import admin

# Register your models here.
from .models import Coffee
from .model import BugerMaterial

admin.site.register(Coffee)
admin.site.register(BugerMaterial)