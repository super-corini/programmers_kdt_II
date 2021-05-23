"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import burgers

class BurgerForm(forms.ModelForm):
    class Meta:
        model = burgers
        fields = {'name', 'price', 'stock'}
