from django import forms
from .models import Coffees

class CoffeesForm(forms.ModelForm):
    class Meta:
        model = Coffees
        fields = ('name', 'price', 'is_ice')