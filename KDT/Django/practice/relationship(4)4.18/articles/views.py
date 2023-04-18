from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator

def index(request):
    articles = Article.objects.order_by('-pk')

    """
        [int] page
        현재 주소의 페이지 번호를 할당받는 변수
        주소에 page(키)에 대한 값이 없으면 1 할당
    """
    page = request.GET.get('page', '1')

    """
        [int] per_page
        페이지를 나누는 기준
        e.g. 10 -> 데이터를 10개를 기준으로 나눔.
    """
    per_page = 5

    """
        [Paginator 인스턴스] paginator
        첫 번째 인자 : 페이지네이션을 적용할 데이터(queryset)
        두 번째 인자 : per_page
    """
    paginator = Paginator(articles, per_page)

    """
        [Page 인스턴스] page_obj
        출력할 데이터 및 페이지네이션을 구현을 위한 데이터가 저장된 변수
        반복문으로 순회하면 페이징 처리가 된 데이터가 요소가 됨.
    """
    page_obj = paginator.get_page(page)

    context = {
        'articles': page_obj,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


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
