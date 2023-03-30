from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# Create your views here.

def index(request):
    todos = Todo.objects.all()[::-1]
    return render(request, 'todos/index.html', {'todos':todos})

def check(request, check_pk):
    todo = Todo.objects.get(pk=check_pk)
    todo.completed = request.POST.get('completed') == 'on'
    todo.save()
    return redirect('todos:index')

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    print(todo.deadline)
    if todo.deadline:
        day = str((todo.deadline-datetime.now().date()).days)
        context = {'todo':todo, 'day':day}
    else:
        context = {'todo':todo}
    return render(request, 'todos/detail.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    if request.method == 'POST':
        todo = Todo(
            title = request.POST['title'],
            content = request.POST['content'],
            priority = request.POST['priority'],
        )
        if request.POST['deadline']:
            todo.deadline = request.POST['deadline']
        if 'image' in request.FILES:
            todo.image = request.FILES['image']
        todo.save()
        return redirect('todos:detail', todo.pk)
    return redirect('todos:index')

def delete(request, delete_pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=delete_pk)
        todo.delete()
        return redirect('todos:index')
    return redirect('todos:detail', delete_pk)

def edit(request, edit_pk):
    todo = Todo.objects.get(pk=edit_pk)
    return render(request, 'todos/edit.html', {'todo':todo})

def update(request, update_pk):
    todo = Todo.objects.get(pk=update_pk)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.content = request.POST['content']
        todo.priority = request.POST['priority']
        if request.POST['deadline']:
            todo.deadline = request.POST['deadline']
        if 'image' in request.FILES:
            todo.image = request.FILES['image']
        todo.save()
        return redirect('todos:detail', todo.pk)
    return render('todos:detail', todo.pk)