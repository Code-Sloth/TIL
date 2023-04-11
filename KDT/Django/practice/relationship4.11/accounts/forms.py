from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-3'
        self.fields['username'].widget.attrs['placeholder'] = '아이디' 

        self.fields['password1'].widget.attrs['class'] = 'form-control my-3'
        self.fields['password1'].widget.attrs['placeholder'] = '비밀번호' 

        self.fields['password2'].widget.attrs['class'] = 'form-control my-3'
        self.fields['password2'].widget.attrs['placeholder'] = '비밀번호확인' 

class CustomUserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-3'
        self.fields['username'].widget.attrs['placeholder'] = '아이디'

        self.fields['password'].widget.attrs['class'] = 'form-control my-3'
        self.fields['password'].widget.attrs['placeholder'] = '비밀번호'
