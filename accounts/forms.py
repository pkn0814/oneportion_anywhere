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
        label='등급',
        widget=forms.RadioSelect(
            choices=POSITION,
        )

    )
    upload = forms.FileField(
        label = '파일 업로드',
        required = False,
    )
    username = forms.CharField(
        label = '아이디',
    )
    nickname = forms.CharField(
        label = '닉네임',
    )
    password1 = forms.CharField(
        label = '비밀번호',
        widget= forms.PasswordInput(

        )
    )
    password2 = forms.CharField(
        label = '비밀번호 확인',
        widget= forms.PasswordInput(

        )
    )
    email = forms.EmailField(
        label = '이메일',
    )
    class Meta:
        model = CustomerUser
        fields = ['position','upload','username','nickname','password1','password2','email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
            label = '아이디',
        )
    password1 = forms.CharField(
            label = '비밀번호',
            widget=forms.PasswordInput(
                
            )
        )
    class Meta:
        model = CustomerUser
        fields = ['username']