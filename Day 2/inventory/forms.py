from django import forms

from .models import Bugger

class BuggerForm(forms.ModelForm) :
    class Meta :
        model = Bugger
        fields = ('name', 'price', 'stock', 'reserved', 'outofstock')
        widgets = {
            'name' : forms.TextInput(attrs={'style':'width:100px'})
        }