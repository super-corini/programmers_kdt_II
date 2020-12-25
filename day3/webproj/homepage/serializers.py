from homepage.models import Coffee
from rest_framework import serializers


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')