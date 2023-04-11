from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Review,Comment
from .forms import ReviewForm,CommentForm

# Create your views here.

def index(request):
    reviews = Review.objects.all()[::-1]
    return render(request, 'reviews/index.html',{'reviews':reviews})

@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            fo = form.save(commit=False)
            fo.author = request.user
            fo.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create.html',{'form':form})

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review':review,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'reviews/detail.html',context)

@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('reviews:index')

@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.author = request.user
        comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review':review,
        'comment_form':comment_form
    }
    return render(request,'reviews/detail.html', context)

@login_required
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)
