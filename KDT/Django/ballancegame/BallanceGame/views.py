from django.shortcuts import render
from games.models import Post
import random

def index(request):
    posts = Post.objects.all().order_by('-pk')
    pk_list = list(posts.values_list('pk', flat=True))
    if pk_list:
        random_pk = random.choice(pk_list)
    else:
        random_pk = 0

    context = {
        'random_pk':random_pk,
    }
    return render(request, 'index.html', context)