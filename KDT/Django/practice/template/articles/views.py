from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = random.choice([
        ['치킨','https://cdn.pixabay.com/photo/2017/06/26/13/58/chicken-2443901__340.jpg'],

        ['삼겹살','https://cdn.pixabay.com/photo/2018/11/16/16/22/korean-3819740__340.jpg'],

        ['짜장면','https://media.istockphoto.com/id/1458655920/ko/%EC%82%AC%EC%A7%84/%EC%9E%90%EC%9E%A5%EB%AF%B8%EC%97%B0-%EC%9E%90%EC%9E%A5%EB%AF%B8%EC%97%B0%EC%9D%80-%EB%B8%94%EB%9E%99-%EC%86%8C%EC%8A%A4%EB%A5%BC-%EA%B3%81%EB%93%A4%EC%9D%B8-%ED%95%9C%EA%B5%AD%EA%B5%AD%EC%88%98-%ED%95%9C%EA%B5%AD%EC%8B%9D-%EC%8A%A4%ED%83%80%EC%9D%BC.jpg?b=1&s=170667a&w=0&k=20&c=8Ip3EwdfjmJzxNktJj1ATwSeArE0PH6b39_Iu8dLo-k=']])

    context = {
        'foods' : foods[0],
        'img_path' : foods[1],
    }
    return render(request, 'today_dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def lotto_create(request):
    return render(request, 'lotto_create.html')

def lotto(request):
    win_numbers = [request.GET.get('win_number'+str(i)) for i in range(1,7)]

    win_numbers = [int(i) for i in win_numbers]

    number = request.GET.get('number')

    lotto_numbers = [random.sample(range(1,46),6) for _ in range(int(number))]
    
    for i in lotto_numbers:
        num = len(set(win_numbers) & set(i))

        if num == 6: i.append('1등')
        elif num == 5: i.append('2등')
        elif num == 4: i.append('3등')
        elif num == 3: i.append('4등')
        elif num == 2: i.append('5등')
        else: i.append('꽝')

    context = {
        'lotto_numbers' : lotto_numbers,
        'win_numbers' : win_numbers,
    }
    return render(request, 'lotto.html', context)