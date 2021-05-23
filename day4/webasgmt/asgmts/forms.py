from django import forms
from django.forms import fields
from .models import Sneaker


class SneakerForm(forms.ModelForm):
    class Meta:
        model = Sneaker
        fields = ('name', 'price', 'is_limited_edition', 'brand')
        