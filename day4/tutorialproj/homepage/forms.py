from django import forms
from .models import Coffee, Bread  # model 호출


class CoffeeForm(forms.ModelForm):  # ModelForm을 상속받는 CoffeForm 생성
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')


class BreadForm(forms.ModelForm):
    class Meta:
        model = Bread
        fields = ('name', 'count')
