from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import neighbourhood
from .forms import accounts, businessaccount
from django.contrib.auth.decorators import login_required


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password
            return redirect(loginpage)

    return render(request,'accounts/signup.html',{"form":form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('profile')

    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect(loginpage)