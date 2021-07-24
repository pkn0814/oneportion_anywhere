from django import forms
from .models import Fridge

class Ingredients(forms.ModelForm):
    class Meta:
        model = Fridge
    

