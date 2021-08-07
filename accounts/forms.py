from typing import AbstractSet
from accounts.models import CustomerUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from . models import CustomerUser
from django import forms
from argon2 import PasswordHasher, exceptions


class CustomerUserChangeForm(forms.ModelForm):
    upload = forms.FileField(
        label = '사업자 인증',
        required = False,
        widget=forms.FileInput(
            attrs={
            }
        )
    )
    profile = forms.ImageField(
        label = '프로필 사진',
        required = False,
        )

    username = forms.CharField(
        label='ID'
    )
    class Meta:
        model = CustomerUser
        fields = ['position','upload','profile','username','nickname','email']


class SignupForm(UserCreationForm):
    POSITION = (
        ('일반','일반'),
        ('사업자','사업자'),
        
    )
    position = forms.CharField(
        label='',
        widget=forms.RadioSelect(
            choices=POSITION,
            attrs={
                'class':'border1',
            }
            
        )

    )
    upload = forms.FileField(
        label = '사업자 인증',
        required = False,
        widget=forms.FileInput(
            attrs={
                'class':'business'
            }
        )
    )
    profile = forms.ImageField(
        label = '프로필 사진',
        required = False,
        
        )
    username = forms.CharField(
        label = '',
        widget=forms.TextInput(
                attrs={
                    'placeholder':'ID',
                    'class':'box',
                }
        ),
        error_messages={
            'unique':'중복된 아이디입니다.'
        }
    )
    nickname = forms.CharField(
        label = '',
        widget=forms.TextInput(
                attrs={
                    'placeholder':'닉네임',
                    'class':'box',
                }
        ),
        error_messages={
            'unique':'중복된 닉네임입니다.'
        }
    )
    password1 = forms.CharField(
        label = '',

        widget= forms.PasswordInput(
            
                attrs={
                    'placeholder':'비밀번호',
                    'class':'box',
                }

            )
        )
    
    password2 = forms.CharField(
        label = '',
        widget= forms.PasswordInput(
           
                attrs={
                    'placeholder':'비밀번호 확인',
                    'class':'box',
                }
        )
    )
    
    email = forms.EmailField(
        label = '',
        widget=forms.EmailInput(
                attrs={
                    'placeholder':'이메일',
                    'class':'box',
                }
    )
    )
    class Meta:
        model = CustomerUser
        fields = ['position','upload','profile','username','nickname','password1','password2','email']
    
    def clean(self):
        cleaned_data = super().clean()
        position = cleaned_data.get('position','')
        upload = cleaned_data.get('upload','')
        username = cleaned_data.get('username','')
        nickname = cleaned_data.get('nickname','')
        password1 = cleaned_data.get('password1','')
        password2 = cleaned_data.get('password2','')
        email = cleaned_data.get('email','')

        if CustomerUser.objects.filter(nickname=nickname):
            return self.add_error('nickname','중복된 닉네임입니다.')
        
    


class LoginForm(AuthenticationForm):
    username = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={
                    'placeholder':'ID',
                }
            ),
            error_messages={'':'안녕'}
        )
    password = forms.CharField(
            label = '',
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':'PASSWORD',
                }
                
            )
        )
    class Meta:
        model = CustomerUser
        fields = ['username','password']
    
    
