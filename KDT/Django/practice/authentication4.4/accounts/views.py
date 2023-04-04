from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
