from django import forms
from .models import Macaron

class MacaronForm(forms.ModelForm):
    class Meta:
        model = Macaron
        fields = ("name", "price", "amount")