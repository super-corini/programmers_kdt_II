from django import forms

from .models import Coffees


class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffees
        fields = ['drink', 'stock']
