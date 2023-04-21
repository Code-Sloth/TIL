from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Post, Comment
from .forms import PostForm, CommentForm

from django.core.paginator import Paginator

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')

    page = request.GET.get('page', '1')
    per_page = 5
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page)

    context = {
        'posts':page_obj,
    }
    return render(request, 'games/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('games:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'games/create.html', context)


# from django.core.cache import cache

def detail(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    comment_form = CommentForm()
    comments = post.first().comment_set.all()

    if not post.exists():
        return redirect('games:index')
    
    previous_pk = next_pk = post_pk
    previous_posts = Post.objects.filter(pk__lt=post_pk)
    if previous_posts.exists():
        previous_pk = previous_posts.values('id').last().get('id')

    next_posts = Post.objects.filter(pk__gt=post_pk)
    if next_posts.exists():
        next_pk = next_posts.values('id').first().get('id')
    
    # if post_pk not in cache:
    #     cache.set(f'{post_pk}', 1)
    #     request.session['visited'].append(post_pk)
    #     print(request.session['visited'])
    # else:
    #     print(request.session['visited'])
    #     visited_page = request.session['visited'].pop()
    #     while visited_page != post_pk:
    #         cache.delete(f'{visited_page}')
    #         visited_page = request.session['visited'].pop()

    context = {
        'post': post.first(),
        'comment_form': comment_form,
        'comments': comments,
        'previous_pk': previous_pk,
        'next_pk': next_pk,
    }
    return render(request, 'games/detail.html', context)


@login_required
def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)

    if post.select1_content == answer and not post.select1_users.filter(pk=request.user.pk).exists():
        post.select1_users.add(request.user)

    elif  post.select2_content == answer and not post.select2_users.filter(pk=request.user.pk).exists():
        post.select2_users.add(request.user)

    return redirect('games:detail', post_pk)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        
    return redirect('games:detail', post_pk)

@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()

    return redirect('games:detail', post_pk)


import json

# @login_required
def like(request, post_pk):
    if request.user.is_anonymous:
        return JsonResponse({'logged_in': request.user.is_authenticated})

    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        data = json.loads(request.body)
        like = data.get('like')

    if request.user != post.user:
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
            is_liked = False
        else:
            post.like_users.add(request.user)
            is_liked = True
        context = {
            'isLiked': is_liked,
        }
        return JsonResponse(context)
    if like == 'detail':
        return redirect('games:detail', post_pk)
    else:
        return redirect('games:index')
