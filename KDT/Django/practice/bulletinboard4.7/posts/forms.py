from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    category = forms.ChoiceField(choices = [
        ('','카테고리를 선택해주세요.'),
        ('개발','개발'),
        ('CS','CS'),
        ('신기술','신기술'),
    ])
    class Meta:
        model = Post
        fields = ('category', 'title', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs['class'] = 'form-control'

        self.fields['category'].widget.attrs['class'] = 'form-select'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        
        self.fields['content'].widget.attrs['class'] = 'form-control'