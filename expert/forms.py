from django import forms
from . models import Expert

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ['title','user','pub_date','body']