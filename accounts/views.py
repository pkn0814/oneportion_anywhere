from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignupForm, CustomerUserChangeForm
from django.shortcuts import redirect, render
from . models import CustomerUser
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, SignupForm 
from django.contrib import auth, messages
from argon2 import PasswordHasher
from expert.models import Expert, Scrap
from community.models import Post, Scrap_commu
from django.contrib.auth.forms import UserChangeForm


# Create your views here.

def userInfoChange(request):
    if request.method == 'POST':
        user_change_form = CustomerUserChangeForm(request.POST,request.FILES, instance = request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'mypage.html')
    else:
        user_change_form = CustomerUserChangeForm(instance = request.user)
        return render(request, 'userInfoChange.html', {'user_change_form':user_change_form})

    

def signup_view(request):
    if request.method=='POST':
        
        forms = SignupForm(request.POST,request.FILES)
        context = {'forms':forms}
        if forms.is_valid():
            user = forms.save(commit=True)
            login(request, user)
            return redirect('main')
        else:
            context['forms']=forms
        return render(request, 'signup.html', context)
    else:
        forms = SignupForm()
        return render(request, 'signup.html',{'forms':forms})

    
def mypage(request):
    user = request.user
    expert_post = Expert.objects.filter(writer=user)
    expert_scrap = Scrap.objects.filter(user=user)

    com_post = Post.objects.filter(writer=user)
    com_scrap = Scrap_commu.objects.filter(user=user)

    best_post = Post.objects.filter(like__gt=4)
    best_scrap = Scrap_commu.objects.filter(user=user,post__like__gt=1)
    context = {
        'expert_posts':expert_post,
        'expert_scraps':expert_scrap,
        'com_posts':com_post,
        'com_scraps':com_scrap,
        'best_posts':best_post,
        'best_scraps':best_scrap,
    }
    return render(request, 'mypage.html', context)

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
            messages.info(request,'아이디 혹은 비밀번호를 확인해주세요.')
        return render(request,'login.html', context)

def logout_view(request):
    logout(request)
    return redirect("main")