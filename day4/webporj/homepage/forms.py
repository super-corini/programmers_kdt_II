from .models import Burger
from django import forms
from django.forms import fields



class BugerForm(forms.ModelForm):
    
    class Meta:
        model = Burger
        fields = ("name",'price')
