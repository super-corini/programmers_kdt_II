from django import forms
from .models import Coffee


class CoffeeForm(forms.ModelForm):
    def __str__(self):
        return self.name

    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')
