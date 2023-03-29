from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Todo
        fields = ['title', 'content', 'completed', 'priority', 'deadline', 'image']