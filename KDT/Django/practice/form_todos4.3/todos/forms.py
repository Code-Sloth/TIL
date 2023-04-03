from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(
    label = '할 일 제목',
    widget=forms.TextInput(
        attrs={'placeholder': '제목 입력'},
    ),
    )
    content = forms.CharField(
        label='할 일 내용',
        widget=forms.Textarea(
            attrs={'class': 'my-content'},
        ),
    )
    priority = forms.IntegerField(
        label='우선 순위',
        widget=forms.NumberInput(
            attrs={'min': 1, 'max': 5, 'value': 3},
        )
    )
    deadline = forms.DateField(
        label='마감 기한',
        widget=forms.DateInput(
            attrs={'type': 'date'},
        ),
    )
    class Meta:
        model = Todo
        exclude = ('completed',)