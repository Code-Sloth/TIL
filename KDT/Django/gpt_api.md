# OPEN AI Chat GPT API

<br/>

### settings.py
- ```python
    import os

    OPEN_API_KEY = os.getenv('OPEN_API_KEY')
  ```

<br/>

### urls.py
- ```python
    from django.urls import path
    from . import views


    app_name = 'products'
    urlpatterns = [
        ...,
        path('new_chat/', views.new_chat, name='new_chat'),
    ]

  ```

<br/>

### views.py
- ```python
    import openai
    import os

    OPEN_API_KEY = os.getenv('OPEN_API_KEY')
    openai.api_key = OPEN_API_KEY

    def new_chat(request):
        messages = []

        user_content = request.POST.get('gpt-q','')

        messages.append({
            "role": "user",
            "content": f"{user_content}",
        })

        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
        )
        gptresponse = completion.choices[0].message['content'].replace('\n', '<br>')
        return JsonResponse({'gptresponse': gptresponse})

  ```

<br/>

### base.html
- ```html
    <div class='gpt-collapse-btn'>
      <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapse-gpt" role="button" aria-expanded="false" aria-controls="collapse-gpt">
        <div style='width: 50px;'>
          <img class='w-100' src="{% static 'image/gpt.png' %}" alt="gpt">
        </div>
      </a>
    </div>

    <div class='gpt collapse' id='collapse-gpt'>
      <div class='gpt-response'></div>
      <form id='gpt-form'>
        {% csrf_token %}
        <input class='gpt-input' type="text" name="gpt-q">
        <button class='gpt-input-btn' type='submit'>
          <img class='w-100' src="{% static 'image/send.svg' %}" alt="send">
        </button>
      </form>
    </div>
  ```

<br/>

### base.js
- ```javascript
    const gptForm = document.querySelector('#gpt-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    gptForm.addEventListener('submit', (event) => {
      event.preventDefault()
      
      const qValue = document.querySelector('.gpt-input').value
      const formData = new FormData(gptForm)
      formData.append('gpt-q', qValue)

      axios({
        method: 'POST',
        url: `/products/new_chat/`,
        headers: {'X-CSRFToken': csrftoken},
        data: formData,
      })
        .then((response) => {
          const gptText = document.querySelector('.gpt-response')
          const gptResponse = response.data.gptresponse

          gptText.innerHTML = gptResponse
        })
    })
  ```