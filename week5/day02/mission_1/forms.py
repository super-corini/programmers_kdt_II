from django import forms
from .models import Buger

class BugerForm(forms.ModelForm):
    class Meta:
        model = Buger
        fields = ('name', 'price', 'coke')