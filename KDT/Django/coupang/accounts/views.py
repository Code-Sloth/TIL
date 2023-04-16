from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserAuthenticationForm, CustomUserPasswordChangeForm
from .models import User
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('products:index')
    
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('products:index')
    else:
        form = CustomUserAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('products:index')

def join(request):
    if request.user.is_authenticated:
        return redirect('products:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/join.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('products:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        password_form = CustomUserPasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
        if password_form.is_valid():
            password_form.save()

        return redirect('accounts:mypage')

    else:
        form = CustomUserChangeForm(instance=request.user)
        password_form = CustomUserPasswordChangeForm(request.user, request.POST)
    context = {
        'form': form,
        'password_form' : password_form,
    }
    return render(request, 'accounts/update.html', context)

# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = CustomUserPasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:login')
#     else:
#         form = CustomUserPasswordChangeForm(request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'change_password.html', context)

@login_required
def mypage(request):
    return render(request, 'accounts/mypage.html')

