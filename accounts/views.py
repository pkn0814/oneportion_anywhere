from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignupForm
from django.shortcuts import redirect, render
from . models import CustomerUser
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, SignupForm 
from django.contrib import auth
from argon2 import PasswordHasher
from expert.models import Expert, Scrap
from community.models import Post
# Create your views here.
def signup_view(request):
    if request.method=='POST':
        
        forms = SignupForm(request.POST)
        context = {'forms':forms}
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            return redirect('main')
        else:
            context['forms']=forms
        return render(request, 'signup.html', context)
    else:
        forms = SignupForm()
        return render(request, 'signup.html',{'forms':forms})

    


def login_view(request):
    loginform = LoginForm()
    context = {'forms':loginform}

    if request.method=='GET':
        return render(request, 'login.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request=request,data=request.POST)

        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password = password)
            auth.login(request,user)
            return redirect('main')
        else:
            context['forms']=loginform
        return render(request,'login.html', context)

def logout_view(request):
    logout(request)
    return redirect("main")

def mypage(request):
    user = request.user
    expert_post = Expert.objects.filter(writer=user)
    expert_scrap = Scrap.objects.filter(user=user)

    com_post = Post.objects.filter(writer=user)

   
    return render(request, 'mypage.html',{'expert_posts':expert_post,'expert_scraps':expert_scrap,'com_posts':com_post})