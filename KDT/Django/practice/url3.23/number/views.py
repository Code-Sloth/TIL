from django.shortcuts import render

# Create your views here.

def number_print(request, number):
    context = {
        'number' : number
    }
    return render(request, 'number/number.html', context)