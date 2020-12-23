from django import forms
from django.db.models import fields
from .models import Coffee


class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = [
            "name",
            "price",
            "is_ice",
            "stock",
        ]