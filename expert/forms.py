from django import forms
from . models import Expert
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class ExpertForm(forms.ModelForm):
    body = SummernoteTextField()
    
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            
            
        )

    )

    
    class Meta:
        model = Expert
        fields=[
            'title',
            'body',
            'image',
        ]
        widgets = {
            'body':SummernoteWidget()
        }



# class ExpertForm(forms.ModelForm):
#     class Meta:
#         model = Expert
#         fields = ['title','body']

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['file']

# #추가
# ImageFormSet = forms.inlineformset_factory(Expert, Image, form=ImageForm, extra=10)