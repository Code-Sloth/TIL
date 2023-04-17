from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='emote_articles', through='Emote')
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='emote_comments', through='CommentEmote')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(null=False)

class Emote(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=20)

class CommentEmote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=20)