from rest_framework import serializers
from .models import Coffee

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee #모델 설정
        fields = ('id','name','price','stock','is_ground') #필드 설정