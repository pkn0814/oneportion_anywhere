from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Ingredients
from django.forms.widgets import CheckboxSelectMultiple


class IngreForm(forms.ModelForm): 
    class Meta:
        model = Ingredients
        fields = ['main_ingre']
        widgets = {
            'main_ingre' : forms.CheckboxSelectMultiple(
                attrs={
                    'class' : 'form-check-input',
                    'name': 'ingredients[]',
                }
            ),
            
        }


        