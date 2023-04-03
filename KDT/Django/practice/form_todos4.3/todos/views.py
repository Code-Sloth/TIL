from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from datetime import datetime

# Create your views here.

def index(request):
    todos = Todo.objects.all()[::-1]
    for todo in todos:
        a = ''
        for i in range(todo.priority):
            a += 'a'
        todo.priority = a
    return render(request, 'todos/index.html', {'todos':todos})

def check(request,todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed == False:
        todo.completed = True
    else:
        todo.completed = False
    todo.save()
    return redirect('todos:index')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    return render(request, 'todos/detail.html', {'todo':todo})

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()    
    return render(request, 'todos/create.html', {'form':form})

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/update.html', {'form':form})