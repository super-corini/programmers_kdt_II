# form 이라는 모듈을 import
from django import forms
# Model 호출
from .models import Coffee, Burger, Id_s

# ModelForm 을 상속받는 CoffeeForm 생성
class CoffeeForm(forms.ModelForm):
    class Meta: # 이 form을 만들기 위해서 어떤 모델이 쓰여야하는지 안에있는 class 에서 지정이 된다.
        model = Coffee
        fields = ('name', 'price', 'is_ice')



class BurgerForm(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ('id', 'name', 'price', 'is_set')

class IdForm(forms.ModelForm):
    class Meta:
        model = Id_s
        fields = ('id_s',)
