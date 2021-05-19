from django import forms
from .models import Coffee, Burger # Model 호출

class CoffeeForm(forms.ModelForm):  # ModelForm을 상속받는 CoffeeForm 생성
    class Meta: # 이 폼이 어떤 모델이 쓰이는지 지정
        model = Coffee
        fields = ('name', 'price', 'is_ice')

class BurgerForm(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ('name', 'price', 'is_set')