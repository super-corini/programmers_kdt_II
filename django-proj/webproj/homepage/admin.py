from django.contrib import admin
from .models import Coffee

# Register your models here.
# 어떤 모델을 admin과 연동을 하면 superuse에서 이 페이지를 관리할 수 있음

admin.site.register(Coffee)

