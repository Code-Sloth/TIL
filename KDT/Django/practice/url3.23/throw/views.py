from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'throw/throw.html')

def catch(request):
    context = {
        'content' : request.GET.get('content')

    }
    return render(request, 'throw/catch.html', context)