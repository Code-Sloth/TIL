from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email','first_name','last_name','password1','password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-4'
        self.fields['username'].widget.attrs['placeholder'] = 'ID'
        self.fields['username'].label = False
        self.fields['username'].help_text = False

        self.fields['password1'].widget.attrs['class'] = 'form-control my-4'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = False
        self.fields['password1'].help_text = False

        self.fields['password2'].widget.attrs['class'] = 'form-control my-4'
        self.fields['password2'].widget.attrs['placeholder'] = 'RePassword'
        self.fields['password2'].label = False
        self.fields['password2'].help_text = False

        self.fields['email'].widget.attrs['class'] = 'form-control my-4'
        self.fields['email'].widget.attrs['placeholder'] = 'e-mail'
        self.fields['email'].label = False

        self.fields['first_name'].widget.attrs['class'] = 'form-control my-4'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['first_name'].label = False

        self.fields['last_name'].widget.attrs['class'] = 'form-control my-4'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['last_name'].label = False
        

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control my-4'
        self.fields['email'].widget.attrs['placeholder'] = 'e-mail'
        self.fields['email'].label = False

        self.fields['first_name'].widget.attrs['class'] = 'form-control my-4'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['first_name'].label = False

        self.fields['last_name'].widget.attrs['class'] = 'form-control my-4'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['last_name'].label = False

        self.fields['password'].label = False
        self.fields['password'].help_text = False

class CustomUserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-4'
        self.fields['username'].widget.attrs['placeholder'] = 'ID'
        self.fields['username'].label = False

        self.fields['password'].widget.attrs['class'] = 'form-control my-4'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = False

class CustomUserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control my-4'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].label = False
        self.fields['old_password'].help_text = False

        self.fields['new_password1'].widget.attrs['class'] = 'form-control my-4'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].label = False
        self.fields['new_password1'].help_text = False

        self.fields['new_password2'].widget.attrs['class'] = 'form-control my-4'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'New RePassword'
        self.fields['new_password2'].label = False
        self.fields['new_password2'].help_text = False