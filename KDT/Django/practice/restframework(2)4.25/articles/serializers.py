from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','image',)

class ArticleSerializer(serializers.ModelSerializer):
    class MyCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)
    
    comments = MyCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    class Meta:
        model = Article
        fields = ('id','title','content','image','comments', 'comment_count',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','article','content',)
        read_only_fields = ('article',)
