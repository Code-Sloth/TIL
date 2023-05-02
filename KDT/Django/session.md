# 세션

</br>

## 세션을 이용한 데이터 저장
- ```python
    def quiz(request):
        responses = {}
        request.session['survey_data'] = {'responses': responses}

        return render(request, 'products/quiz.html', {'index': 1})

    def quiz_response(request):
        survey_data = request.session.get('survey_data')
        responses = survey_data['responses']
        index = int(request.POST['index'])
        response = request.POST['response']

        responses[index] = response
        request.session['survey_data'] = survey_data

        if index < 6:
            next_index = index + 1
        else:

            if responses['1'] == 'all':
                products = Product.objects.all()
            else:
                products = Product.objects.filter(category = responses['1'])

            products = products.filter(
                alcohol_percentage__gte = int(responses['2'].split(',')[0]),
                alcohol_percentage__lte = int(responses['2'].split(',')[1]),
                sweetness__in = [responses['3'], 'middle'],
                sourness__in = [responses['4'], 'middle'],
                bitterness__in = [responses['5'], 'middle'],
                carbonated = bool(responses[6]),
            )

            if products:
                products = products.annotate(num_likes=Count('like_users')).order_by('-num_likes')[:3]

            return render(request, 'products/quiz.html', {'products':products, 'index':7})

        return render(request, 'products/quiz.html', {'index': next_index})
  ```
  ```html
    {% if index == 1 %}

        <div class='question-title'>
          원하는 주종을 <br>
          선택해주세요.
        </div>

        <form action="{% url 'products:quiz_response' %}" method="POST">
          {% csrf_token %}
          <input type="hidden" name='index' value='{{ index }}'>

          <div class='quiz1'>
            <button name='response' value='all' type='submit'>
              <div style='width:30px; margin-right: 20px;'>
                <img class='w-100' src="{% static 'image/전체.svg' %}" alt="전체">
              </div>
              <p>전체</p>
            </button>

            <button name='response' value='traditional' type='submit'>
              <div>
                <img class='w-100' src="{% static 'image/전통주.png' %}" alt="전통주">
              </div>
              <p>전통주</p>
            </button>

            <button name='response' value='beer' type='submit'>
              <div>
                <img style='opacity: 0.8;' class='w-100' src="{% static 'image/맥주.png' %}" alt="맥주">
              </div>
              <p>맥주</p>
            </button>

            <button name='response' value='whiskey' type='submit'>
              <div>
                <img class='w-100' src="{% static 'image/위스키.svg' %}" alt="위스키">
              </div>
              <p>위스키</p>
            </button>

            <button name='response' value='wine' type='submit'>
              <div>
                <img class='w-100' src="{% static 'image/와인.svg' %}" alt="와인">
              </div>
              <p>와인</p>
            </button>
          </div>
        </form>

      {% elif index == 2 %}
      ...
  ```