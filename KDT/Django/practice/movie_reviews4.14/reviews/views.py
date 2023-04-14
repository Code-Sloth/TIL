from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    reviews = Review.objects.all().order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'reviews/create.html', context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('reviews:index')

@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', review_pk)
        else:
            form = ReviewForm(instance=review)
        context = {
            'form':form
        }
        return render(request, 'reviews/update.html', context)
    else:
        return redirect('reviews:detail', review.pk)

@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('reviews:detail', review_pk)
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:detail', review_pk)