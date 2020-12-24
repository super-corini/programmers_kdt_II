from django import forms
from .models import Coffees # Model 호출

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeForm 생성
    class Meta:
        model = Coffees
        fields = ('name', 'is_ice', 'price', 'count')