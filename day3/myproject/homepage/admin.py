from django.contrib import admin
from .models import Coffee


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "is_ice", "stock"]
