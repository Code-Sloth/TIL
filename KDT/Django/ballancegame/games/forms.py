from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'select1_content',
            'image1',
            'select2_content',
            'image2',
        )
        labels = {
            'title': '제목',
            'select1_content': '첫 번째 픽',
            'select2_content': '두 번째 픽',
            'image1': '첫 번째 이미지',
            'image2': '두 번째 이미지',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )
        labels = {
            'content': '댓글',
        }
