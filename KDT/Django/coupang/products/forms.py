from django import forms
from .models import Product,Comment,ProductImage
from django.forms import inlineformset_factory
from django.forms.widgets import ClearableFileInput

class ProductForm(forms.ModelForm):
    image = forms.FileField(widget=ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Product
        fields = ('title', 'price', 'delivery_date', 'content', 'category','image',)

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
        fields = ('product_img',)

ProductImageFormSet = inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=5)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'content', 'star',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control my-3'

        self.fields['content'].widget.attrs['class'] = 'form-control my-3'

        self.fields['star'].widget.attrs['class'] = 'form-control my-3'

