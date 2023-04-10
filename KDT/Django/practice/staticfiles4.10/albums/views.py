from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.

def index(request):
    albums = Album.objects.all()
    form = AlbumForm()
    return render(request, 'albums/index.html',{'albums':albums,'form':form})

def create(request):
    form = AlbumForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('albums:index')

def delete(request, pk):
    album = Album.objects.get(pk=pk)
    album.delete()
    return redirect('albums:index')
