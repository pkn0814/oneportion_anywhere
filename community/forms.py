from django import forms
from django_summernote.fields import SummernoteTextFormField
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    content = SummernoteTextFormField(
        label='',
    )

    category_select = (
        ('일상공유','일상공유'),
        ('레시피공유','레시피공유'),
    )
    category = forms.ChoiceField(
        choices=category_select,
        
    )

    title = forms.CharField(
        label='',
        widget = forms.TextInput(
            attrs={
                'class':'title',
                'placeholder':'제목'
            }
        )
    )

    tag = forms.CharField(
        required=False, label="태그 "
    )

    class Meta:
        model = Post
        fields = ['title','category', 'content', 'tag',]
        widgets = {
            'content': SummernoteWidget(),
        }