from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        label = '생년 월일:',
        widget=forms.DateInput(attrs={'type':'date'})
        )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2','birthday')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = '아이디' 
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = '이메일' 

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = '성' 

        self.fields['last_name'].widget.attrs['class'] = 'form-control' 
        self.fields['last_name'].widget.attrs['placeholder'] = '이름'

        self.fields['password1'].widget.attrs['class'] = 'form-control' 
        self.fields['password1'].widget.attrs['placeholder'] = '비밀번호' 

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = '비밀번호확인' 

        self.fields['birthday'].widget.attrs['class'] = 'form-control' 
        self.fields['birthday'].widget.attrs['placeholder'] = '생년월일'

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control' 
        self.fields['last_name'].widget.attrs['class'] = 'form-control' 


class CustomUserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = '아이디' 

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = '비밀번호' 

class CustomUserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = '기존 비밀번호' 

        self.fields['new_password1'].widget.attrs['class'] = 'form-control' 
        self.fields['new_password1'].widget.attrs['placeholder'] = '새 비밀번호' 

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = '새 비밀번호 확인' 
 

        # self.fields['password'].widget.attrs['class'] = 'form-control'
        # self.fields['password'].widget.attrs['placeholder'] = '비밀번호' 