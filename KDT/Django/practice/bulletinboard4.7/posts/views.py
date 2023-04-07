from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    if request.method == 'POST':
        posts = catego(request.POST.get('cate'))
        posts = sort_time(posts,request.POST.get('sort'))

    return render(request, 'posts/index.html',{'posts':posts})

def catego(po):
    if po == '신기술':
        return Post.objects.filter(category='신기술')
    elif po == '개발':
        return Post.objects.filter(category='개발')
    elif po == 'CS':
        return Post.objects.filter(category='CS')
    else:
        return Post.objects.all()

def sort_time(queryset, so):
    if so == '':
        return queryset
    elif so == '최신순':
        return queryset.order_by('-pk')
    else:
        return queryset.order_by('pk')
    

def detail(request, pk):
    post = Post.objects.get(pk=pk)
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
