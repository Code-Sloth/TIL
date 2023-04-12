from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

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

class CustomUserChangeForm(UserChangeForm):
    image = ProcessedImageField(
        spec_id='profiles:image',
        processors=[ResizeToFill(100,100)],
        format='JPEG',
        options={'quality' : 90},
        required=False,
    )

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['class'] = 'form-control my-3'