from django import forms
from .models import Bakery

class BakeryForm(forms.ModelForm):
    class Meta:
        model=Bakery
        fields=('name', 'price', 'stock')