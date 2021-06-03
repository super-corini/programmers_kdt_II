from django import forms

from .models import Game

class GameForm(forms.ModelForm) :
    class Meta :
        model = Game
        fields = ('title', 'platform', 'genre', 'price', 'stock', 'reserved', 'extinct')
        widgets = {
            'platform' : forms.TextInput(attrs={'style':'width:70px'}),
            'genre' : forms.TextInput(attrs={'style':'width:90px'})
        }
        