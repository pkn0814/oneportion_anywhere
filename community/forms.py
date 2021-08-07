from django import forms
from django_summernote.fields import SummernoteTextFormField
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    content = SummernoteTextFormField(
        label='',
    )

    category_select = (
        ('일반','일반'),
        ('사업자','사업자'),
    )
    category = forms.CharField(
        label='',
        widget=forms.RadioSelect(
            choices=category_select,
            attrs={
                'class':'border1',
            }
            
        )
    )

    title = forms.CharField(
        label='',
        widget = forms.TextInput(
            attrs={
                'class':'title',
            }
        )
    )

    class Meta:
        model = Post
        fields = ['title', 'content','category']
        widgets = {
            'content': SummernoteWidget(),
        }