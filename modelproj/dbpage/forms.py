# template에서 model을 변동하는 방법
# DB를 받기 위한 양식
# Model과 입력받을 field 지정
from django import forms
from .models import Coffee


class CoffeeForm(forms.ModelForm):
    class Meta:
        # Model,Coffee 연동
        model = Coffee
        fields = ('name', 'price', 'is_ice')
