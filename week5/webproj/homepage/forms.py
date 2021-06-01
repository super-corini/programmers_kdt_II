from django import forms
from .models import Coffee

# ModelForm을 상속받는 CoffeeForm 생성
class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')