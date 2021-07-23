from typing import AbstractSet
from accounts.models import CustomerUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import CustomerUser
from django import forms

class SignupForm(UserCreationForm):
    POSITION = (
        ('일반사용자','일반사용자'),
        ('사업자','사업자')
    )
    position = forms.CharField(
        label='등급선택',
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
                'class':'border1',
            }
        )
    )
    username = forms.CharField(
        label = '',
        widget=forms.TextInput(
                attrs={
                    'placeholder':'ID',
                    'class':'box',
                }
        )
    )
    nickname = forms.CharField(
        label = '',
        widget=forms.TextInput(
                attrs={
                    'placeholder':'닉네임',
                    'class':'box',
                }
        )
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
        fields = ['position','upload','username','nickname','password1','password2','email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
            label = '',
            widget=forms.TextInput(
                attrs={
                    'placeholder':'ID',
                }
            )
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
        fields = ['username']