from django import forms
from .models import Review,Comment
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class ReviewForm(forms.ModelForm):
    image = ProcessedImageField(
        spec_id='albums:image',
        processors=[ResizeToFill(100,150)],
        format='JPEG',
        options={'quality' : 90},
        required=False,
    )

    class Meta:
        model = Review
        fields = ('title','content','movie','image','author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control my-3'
        self.fields['title'].widget.attrs['placeholder'] = '리뷰 제목'

        self.fields['content'].widget.attrs['class'] = 'form-control my-3' 
        self.fields['content'].widget.attrs['placeholder'] = '리뷰 내용' 

        self.fields['movie'].widget.attrs['class'] = 'form-control my-3'
        self.fields['movie'].widget.attrs['placeholder'] = '영화 제목'

        self.fields['image'].widget.attrs['class'] = 'form-control my-3' 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = '댓글 작성'