from django import forms
from .models import Review, Comment
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class ReviewForm(forms.ModelForm):
    image = ProcessedImageField(
        spec_id='reviews:image',
        processors=[ResizeToFill(60,86)],
        format='JPEG',
        options={'quality' : 90},
        required=False,
    )
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['movie'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class'] = 'form-control'
