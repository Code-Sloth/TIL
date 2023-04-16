from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth import get_user_model
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-3'
        self.fields['username'].widget.attrs['placeholder'] = '아이디'

        self.fields['password1'].widget.attrs['class'] = 'form-control my-3'
        self.fields['password1'].widget.attrs['placeholder'] = '비밀번호'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control my-3'
        self.fields['password2'].widget.attrs['placeholder'] = '비밀번호 확인'
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control my-3'
        self.fields['last_name'].widget.attrs['placeholder'] = '이름'

class CustomUserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-3'
        self.fields['username'].widget.attrs['placeholder'] = '아이디'

        self.fields['password'].widget.attrs['class'] = 'form-control my-3'
        self.fields['password'].widget.attrs['placeholder'] = '비밀번호'

class CustomUserChangeForm(UserChangeForm):
    image = ProcessedImageField(
        spec_id='profiles:image',
        processors=[ResizeToFill(100,150)],
        format='JPEG',
        options={'quality' : 90},
        required=False,
    )

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email','last_name','profile_image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control my-3'

        self.fields['last_name'].widget.attrs['class'] = 'form-control my-3'

        self.fields['profile_image'].widget.attrs['class'] = 'form-control my-3'

class CustomUserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control my-3'
        
        self.fields['new_password2'].widget.attrs['class'] = 'form-control my-3'
