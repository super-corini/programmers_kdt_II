# for the form(직접 만들어야함)

from django import forms
from .models import Coffee  # Model 호출

class CoffeeForm(forms.ModelForm):  # ModelForm을 상속받는 객체 생성
	class Meta:
		model = Coffee
		fields = ('name', 'price', 'is_ice')