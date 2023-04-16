from django import forms
from .models import Product,Comment,ProductImage,CommentImage

class ProductForm(forms.ModelForm):
    delivery_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'},
        ),
    )
    class Meta:
        model = Product
        fields = ('title', 'price', 'delivery_date', 'content', 'category',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control my-3'

        self.fields['price'].widget.attrs['class'] = 'form-control my-3' 

        self.fields['delivery_date'].widget.attrs['class'] = 'form-control my-3'

        self.fields['content'].widget.attrs['class'] = 'form-control my-3'

        self.fields['category'].widget.attrs['class'] = 'form-control my-3'

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['multiple'] = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'content', 'star',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control my-3'

        self.fields['content'].widget.attrs['class'] = 'form-control my-3'

        self.fields['star'].widget.attrs['class'] = 'form-control my-3'


class CommentImageForm(forms.ModelForm):
    class Meta:
        model = CommentImage
        fields = ('comment_image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment_image'].widget.attrs['multiple'] = True