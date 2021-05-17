from django import forms
from .models import Coffee # Model 호출
from .models import Burger # Model 호출

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')


class BurgerForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Burger
        fields = ('id', 'name', 'price')