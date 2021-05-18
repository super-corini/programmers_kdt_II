from django import forms

from .models import Coffee
from .model import BugerMaterial

class BugerForm(forms.ModelForm):
    class Meta :
        model = BugerMaterial
        fields = ('type', 'stock', 'is_set')#'brend_name', 'director_name', 'price'


class CoffeeForm(forms.ModelForm):
    class Meta :
        model = Coffee
        fields = ('name', 'price', 'is_ice')


