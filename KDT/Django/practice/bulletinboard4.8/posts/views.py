from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    sor = request.GET.get('sort','')
    posts = sort_func(Post.objects.all(),sor)

    return render(request, 'posts/index.html',{'posts':posts,'sor':sor})

def development(request):
    posts = Post.objects.filter(category='개발')
    sor = request.GET.get('sort','')
    posts = sort_func(posts,sor)
    return render(request, 'posts/development.html',{'posts':posts,'sor':sor})

def cs(request):
    posts = Post.objects.filter(category='CS')
    sor = request.GET.get('sort','')
    posts = sort_func(posts,sor)
    return render(request, 'posts/cs.html',{'posts':posts,'sor':sor})

def newtech(request):
    posts = Post.objects.filter(category='신기술')
    sor = request.GET.get('sort','')
    posts = sort_func(posts,sor)
    return render(request, 'posts/newtech.html',{'posts':posts,'sor':sor})

def sort_func(queryset, so):
    if so == '최신순':
        return queryset.order_by('-pk')
    elif so == '오래된순':
        return queryset.order_by('pk')
    elif so == '조회순':
        return queryset.order_by('-count_hit')
    elif so == '추천순':
        return queryset.order_by('-count_like')
    else:
        return queryset[::-1]
    

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST.get('like') == 'like':
            post.count_like += 1
        elif request.POST.get('like') == 'unlike':
            post.count_like -= 1
        else: pass
    else:
        post.count_hit += 1
    post.save()
    return render(request, 'posts/detail.html', {'post':post})

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form':form})

@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')

@login_required
def update(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update.html',{'form':form, 'post':post})
