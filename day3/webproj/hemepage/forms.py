from django import forms
from .models import Coffee  # Model 호출
from .model import Coffees

class CoffeeForm(forms.ModelForm):  # ModelForm을 상속받는 CoffeeForm 상속
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')

class CoffeesForm(forms.ModelForm):
    class Meta:
        model = Coffees
        fields = ('name', 'price', 'is_ice')