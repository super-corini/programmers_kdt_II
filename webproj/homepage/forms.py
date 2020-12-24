from django import forms
from .models import Coffee, Phone  # Model 호출


class CoffeeForm(forms.ModelForm):  # ModelForm을 상속받는 CoffeForm 생성
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ('name', 'price', 'company')
