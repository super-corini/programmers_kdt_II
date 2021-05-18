from django import forms

from .models import coffe

class coffeForm (forms.ModelForm):
    class Meta:
        model=coffe
        fields=('name','price','is_ice')

