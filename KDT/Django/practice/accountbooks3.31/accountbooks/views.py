from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.
def index(request):
    books = AccountBook.objects.all()[::-1]
    if request.method == 'POST':
        if request.POST['category2'] == '식비':
            books = AccountBook.objects.filter(category='식비')[::-1]
        elif request.POST['category2'] == '고정비':
            books = AccountBook.objects.filter(category='고정비')[::-1]
        elif request.POST['category2'] == '여가비':
            books = AccountBook.objects.filter(category='여가비')[::-1]
        elif request.POST['category2'] == '교통비':
            books = AccountBook.objects.filter(category='교통비')[::-1]
        elif request.POST['category2'] == '의료비':
            books = AccountBook.objects.filter(category='의료비')[::-1]
        else:
            books = AccountBook.objects.all()[::-1]
    context = {
        'books': books
    }
    return render(request, 'accountbooks/index.html', context)

def detail(request, books_pk):
    book = AccountBook.objects.get(pk=books_pk)
    context = {
        'book': book
    }
    return render(request, 'accountbooks/detail.html', context)

def new(request):
    return render(request, 'accountbooks/new.html')

def create(request):
    if request.method == 'POST':
        book = AccountBook(
                note = request.POST['note'],
                category = request.POST['category'],
                amount = request.POST['amount'],
                date = request.POST.get('date'),
                description = request.POST['description']
            )
        book.save()
        return redirect('accountbooks:detail', book.pk)
    return redirect('accountbooks:index')


def edit(request, books_pk):
    book = AccountBook.objects.get(pk=books_pk)

    context = {
        'book': book
    }

    return render(request, 'accountbooks/edit.html', context)


def update(request, books_pk):
    book = AccountBook.objects.get(pk=books_pk)

    book.note = request.POST.get('note')
    book.category = request.POST.get('category')
    book.amount = request.POST.get('amount')
    book.date = request.POST.get('date')
    book.description = request.POST.get('description')

    book.save()
    return redirect('accountbooks:detail', book.pk)


def delete(request, books_pk):
    book = AccountBook.objects.get(pk=books_pk)
    book.delete()
    
    return redirect('accountbooks:index')

def copy(request, books_pk):
    book = AccountBook.objects.get(pk=books_pk)

    note = book.note
    category = book.category
    amount = book.amount
    date = book.date
    description = book.description

    save_book = AccountBook(note = note, category = category, amount = amount, date = date, description = description)
    save_book.save()
    return redirect('accountbooks:index')


