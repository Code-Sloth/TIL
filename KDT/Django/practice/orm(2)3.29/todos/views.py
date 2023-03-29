from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    todos = Todo.objects.all()[::-1]
    return render(request, 'todos/index.html', {'todos' : todos})

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    return render(request, 'todos/detail.html', {'todo' : todo})

def new(request):
    form = TodoForm()
    return render(request, 'todos/new.html', {'form' : form})

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    return render(request, 'todos/create.html', {'form':form})

def remove(request, remove_pk):
    remove_todo = Todo.objects.get(pk=remove_pk)
    if request.method == 'POST':
        remove_todo.delete()
        return redirect('todos:index')
    return render(request, 'todos/remove.html')