from django.contrib import admin
from .models import Coffee, Phone, PhoneCompany

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Phone)
admin.site.register(PhoneCompany)