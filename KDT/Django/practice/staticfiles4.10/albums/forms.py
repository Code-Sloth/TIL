from django import forms
from .models import Album

from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class AlbumForm(forms.ModelForm):
    image = ProcessedImageField(
        spec_id='albums:image',
        processors=[ResizeToFill(100,100)],
        format='JPEG',
        options={'quality' : 80},
        required=False,
    )

    class Meta:
        model = Album
        fields = ('content','image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
