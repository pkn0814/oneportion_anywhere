from accounts.forms import SignupForm
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, SignupForm 

# Create your views here.
def signup_view(request):
    if request.POST == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main")
    else:
        form = SignupForm()
        return render(request, 'signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                return redirect("login")
    
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect("main")