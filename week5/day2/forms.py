from django import forms
from .models import Coffee, BaskinRobbins  # Model 호출

# Modelform을 상속받는 CoffeeForm 생성
class CoffeeForm(forms.ModelForm):
    class Meta:
        # Form을 만들기 위해 어떤 모델을 사용해야 하는지 지정
        model = Coffee
        fields = ('name', 'price', 'is_ice')

class BRForm(forms.ModelForm):
    class Meta:
        model = BaskinRobbins
        fields = ('name', 'serving_size', 'calory', 'allergy')