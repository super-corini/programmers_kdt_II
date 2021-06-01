from django import forms
from .models import Coffee


class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = [
            'product_name',
            'size',
            'cup_select',
            'prodcut_description',
            'ice_only',
            'quantity',
            'order_date',]
