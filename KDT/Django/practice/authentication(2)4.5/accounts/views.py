from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserAuthenticationForm, CustomUserPasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'accounts/index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = CustomUserAuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html', {'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomUserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            return redirect('accounts:index')
    else:
        form = CustomUserPasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form':form})