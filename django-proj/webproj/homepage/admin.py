from django.contrib import admin
from .models import Coffee
# Register your models here.

admin.site.register(Coffee) # 관리자 페이지에서 모델을 관리할 수 있다.