from django import forms
from . models import Expert
from django_summernote.fields import SummernoteTextField, SummernoteTextFormField
from django_summernote.widgets import SummernoteWidget

class ExpertForm(forms.ModelForm):
    CATEGORY = (
        ('레시피', '레시피'),
        ('밀키트', '밀키트'),
    )
    category = forms.CharField(
        label='',
        widget=forms.RadioSelect(
            choices=CATEGORY,
            attrs={
                'class':'category',
            }
            
        )

    )
    body = SummernoteTextFormField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder':'asdf',
            }
        )
    )
    
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class':'title',
                'placeholder':'제목'

            }
            
        )

    )

    image = forms.ImageField(
        label='',
    )

    
    class Meta:
        model = Expert
        fields=[
            'title',
            'category',
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