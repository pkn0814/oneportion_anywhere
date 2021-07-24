from accounts.forms import SignupForm
from django.shortcuts import redirect, render
from . models import CustomerUser
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, SignupForm 
from django.contrib import auth
from argon2 import PasswordHasher

# Create your views here.
def signup_view(request):
    signup_form = SignupForm()
    context = {'forms':signup_form}

    if request.method == 'GET':
        return render(request, 'signup.html', context)

    elif request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = CustomerUser(
                position = signup_form.position,
                upload = signup_form.upload,
                nickname = signup_form.nickname,
                username = signup_form.username,
                password = signup_form.password1,
                email = signup_form.email,
                
            )
            user.save()
            auth.login(request,user)
            return redirect('main')
        else:
            context['forms']=signup_form
        return render(request, 'signup.html', context)


def login_view(request):
    loginform = LoginForm()
    context = {'forms':loginform}

    if request.method=='GET':
        return render(request, 'login.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            return redirect('main')
        else:
            context['forms']=loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error']=value
        return render(request,'login.html', context)

def logout_view(request):
    logout(request)
    return redirect("main")