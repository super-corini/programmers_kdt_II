from django import forms
from .models import Coffee, Burger  # Model 호출


class CoffeForm(forms.ModelForm):  # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')


class BurgerForm(forms.ModelForm):  # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Burger
        fields = ('name', 'price', 'is_set')
