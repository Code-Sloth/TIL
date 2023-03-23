from django.shortcuts import render

# Create your views here.

def calculate(request, number1, number2):

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    if num1:
        number1 = int(num1)
    if num2:
        number2 = int(num2)

    context = {
        'pl' : number1 + number2,
        'mi' : number1 - number2,
        'mu' : number1 * number2,
        'di' : number1 // number2,
    }

    return render(request, 'calculate/calculate.html', context)


def throw(request):
    return render(request, 'calculate/throw.html')