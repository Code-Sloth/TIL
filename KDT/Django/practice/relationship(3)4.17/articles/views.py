from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Emote, CommentEmote
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

EMOTIONS = [
    {'label': '쓸쓸정보', 'value': 1},
    {'label': '흥미진진', 'value': 2},
    {'label': '공감백배', 'value': 3},
    {'label': '분석탁월', 'value': 4},
    {'label': '후속강추', 'value': 5},
]

COMMENT_EMOTIONS = [
    {'label': '좋아요', 'value': 1},
    {'label': '싫어요', 'value': 2},
]

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    emotions = []
    for emotion in EMOTIONS:
        label = emotion['label']
        value = emotion['value']
        count = Emote.objects.filter(article=article, emotion=value).count()
        if request.user.is_authenticated:
            exist = Emote.objects.filter(article=article, emotion=value, user=request.user)
        else: exist = None
        emotions.append(
            {
                'label': label,
                'value': value,
                'count': count,
                'exist': exist,
            }
        )
        
    comments = article.comment_set.all()
    comment_emotions = {}
    for comment in comments:
        comment_emotions[comment.pk] = []
        for comment_emotion in COMMENT_EMOTIONS:
            label = comment_emotion['label']
            value = comment_emotion['value']
            count = CommentEmote.objects.filter(comment=comment, emotion=value).count()
            if request.user.is_authenticated:
                exist = CommentEmote.objects.filter(comment=comment, emotion=value, user=request.user)
            else: exist = None
            comment_emotions[comment.pk].append(
                {
                    'label': label,
                    'value': value,
                    'count': count,
                    'exist': exist,
                }
            )

    comment_form = CommentForm()
    context = {
        'emotions': emotions,
        'comment_emotions': comment_emotions,
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def emotes(request, article_pk, emotion):
    article = Article.objects.get(pk=article_pk)
    filter_query = Emote.objects.filter(
        article=article,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(article=article, user=request.user, emotion=emotion)

    return redirect('articles:detail', article_pk)

@login_required
def comment_emotes(request, article_pk, comment_pk, comment_emotion):
    comment = Comment.objects.get(pk=comment_pk)
    filter_query = CommentEmote.objects.filter(
        comment=comment,
        user=request.user,
        emotion=comment_emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        CommentEmote.objects.create(comment=comment, user=request.user, emotion=comment_emotion)

    return redirect('articles:detail', article_pk)

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article_pk=article.pk)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()

    return redirect('articles:detail', article.pk)


@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()

    return redirect('articles:detail', article_pk)
