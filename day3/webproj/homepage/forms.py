from django import forms

from .models import Coffee, Chicken

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')

class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ('name', 'price', 'num')
        