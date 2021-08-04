from django import forms
from django_summernote.fields import SummernoteTextFormField
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    content = SummernoteTextFormField(
        label='',
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
        fields = [
        'title', 
        'content',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }