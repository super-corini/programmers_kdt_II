from django import forms
from .models import Chicken

class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ('name', 'price', 'amount')

