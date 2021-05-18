from django import forms
from .models import Coffee, Fruit # Model 호출

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        # 폼을 만들기 위해 어떤 모델을 써야하는지 지정
        model = Coffee
        fields = ('name', 'price', 'is_ice')

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'stock')