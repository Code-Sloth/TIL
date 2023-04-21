from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    '''어떤 필드가 Optional인지, 필수항목으로 바꾸려면 어떻게 해야되는지'''
    password1 = forms.CharField(
        label=_("비밀번호"),
        label_suffix='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("비밀번호 확인"),
        label_suffix='',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("비밀번호를 한번 더 입력하세요"),
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'image',
            'password1',
            'password2',
        )


class CustomUserChangeForm(UserChangeForm):
    '''how to override part of settings?'''
    first_name = forms.CharField(label=_("이름"), label_suffix='', required=False)
    last_name = forms.CharField(label=_("성"), label_suffix='', required=False)
    email = forms.EmailField(label=_("이메일"), label_suffix='', required=True)
    password = ReadOnlyPasswordHashField(
        label='',
        label_suffix='',
        help_text=_(
            '<a href="{}">비밀번호 변경하기</a>'
        ),
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'image',
            'email',
            'first_name',
            'last_name',
        )