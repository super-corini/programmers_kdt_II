from django.contrib import admin
from .models import Coffee, Burger

# Register your models here.
# 관리자 page에서 database 관리
admin.site.register(Coffee)
admin.site.register(Burger)