from django import forms
from .models import Coffee # Model 호출

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta: # form을 만들기 위해서 어떤 클래스가 필요한지
        model = Coffee
        fields = ("name", "price", "is_ice")

        