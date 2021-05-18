from django import forms
from .models import Burger

class BurgerForm(forms.ModelForm) : #{
    class Meta :
        model  = Burger
        fields = ('name', 'price', 'stock')    
#}