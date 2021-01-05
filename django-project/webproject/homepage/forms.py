from django import forms
from .models import Coffee

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Coffee
        fields = ("name", "price", "stock")
