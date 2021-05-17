from django.contrib import admin
from .models import Coffee
from .models import Burger

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Burger)