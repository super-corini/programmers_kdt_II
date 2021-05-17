from django import forms
from .models import Coffee, CoffeeBeen # Model 호출

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')

class CoffeeBeenForm(forms.ModelForm):
    class Meta:
        model = CoffeeBeen
        fields = ('name', 'stock')