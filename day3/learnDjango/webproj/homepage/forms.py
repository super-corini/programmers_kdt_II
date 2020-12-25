from django import forms
from .models import Lol

class LolForm(forms.ModelForm):
    class Meta:
        model = Lol
        fields = ('name', 'position', 'role', 'price')