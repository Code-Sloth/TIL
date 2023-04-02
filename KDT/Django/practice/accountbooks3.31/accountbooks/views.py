from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.
def index(request):
    books = AccountBook.objects.all()[::-1]
    cate = request.POST.get('category2')
    sort = request.POST.get('sort')
    
    if request.method == 'POST':
        if request.POST.get('category2') == '식비':
            books = AccountBook.objects.filter(category='식비')
        elif request.POST.get('category2') == '고정비':
            books = AccountBook.objects.filter(category='고정비')
        elif request.POST.get('category2') == '여가비':
            books = AccountBook.objects.filter(category='여가비')
        elif request.POST.get('category2') == '교통비':
            books = AccountBook.objects.filter(category='교통비')
        elif request.POST.get('category2') == '의료비':
            books = AccountBook.objects.filter(category='의료비')
        else:
            books = AccountBook.objects.all()
        
        if request.POST.get('sort') == 'amount':
            books = books.order_by('amount')
        elif request.POST.get('sort') == 'amount_desc':
            books = books.order_by('-amount')
        elif request.POST.get('sort') == 'date':
            books = books.order_by('date')
        elif request.POST.get('sort') == 'date_desc':
            books = books.order_by('-date')
        elif request.POST.get('sort') == 'pk':
            books = books.order_by('pk')
        elif request.POST.get('sort') == 'pk_desc':
            books = books.order_by('-pk')
        else:
            books = books[::-1]
        
    context = {
        'books': books,
        'cate' : cate,
        'sort' : sort
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


