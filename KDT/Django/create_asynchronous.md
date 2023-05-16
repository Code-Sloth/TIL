# Create 비동기 구현

<br/>

### html
- ```html
    <h1 class='recomment-header'>
      답변 <span>{{ comment.recomments.count }}</span>
    </h1>

    <form class='recomment-section-create-form' action="{% url 'communities:recomment_create' comment.pk %}" method="POST" data-comment-id="{{ comment.pk }}">
      {% csrf_token %}
      {{ recomment_form.content }}
      <div class='d-flex flex-row-reverse'>
        <button class='recomment-submit' type='submit'>등록</button>
        <button class='recomment-cancle'>취소</button>
      </div>
    </form>

    <!-- 출력되는 곳 -->
    <div class='recomment-section'>
      {% for recomment in recomments reversed %}
        <div class='recomment-section-item'>
          ...
        </div>
      {% endfor %}
    </div>
  ```

<br/>

### JS
- ```javascript
    document.addEventListener('DOMContentLoaded', () => {
      const recommentForm = document.querySelector('.recomment-section-create-form')
      const recommentContainer = document.querySelector('.recomment-section')

      recommentForm.addEventListener('submit', (event) => {
        event.preventDefault()

        const commentId = recommentForm.dataset.commentId
        const formData = new FormData(recommentForm)

        axios({
          method: 'POST',
          url: `/communities/comments/${commentId}/recomments/create/`,
          headers: { 'X-CSRFToken': csrftoken },
          data: formData
        })
          .then((response) => {
            recommentContainer.innerHTML = response.data.recomment_section_html
            
            const recommentCount = document.querySelector('.recomment-header > span')
            console.log(recommentCount)
            recommentCount.textContent = response.data.recomment_count
          })
          .catch((error) => {
            console.log(error.response)
          })
      })
    })
  ```

<br/>

### views.py
- ```python
    @login_required
    def recomment_create(request, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)

        recomment_form = RecommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.comment = comment
            recomment.user = request.user
            recomment.save()

            recomments = comment.recomments.all()

            recomments_html = render_to_string('communities/comment_detail.html', {'comment': comment, 'recomments': recomments, 'request': request, 'csrf_token': get_token(request)})

            soup = BeautifulSoup(recomments_html, 'html.parser')
            recomment_section = soup.find('div', {'class': 'recomment-section'})
            recomment_section_html = str(recomment_section)

            return JsonResponse({'recomment_section_html': recomment_section_html, 'recomment_count': comment.recomments.count()})

        errors = recomment_form.errors.as_json()
        return JsonResponse({'errors': errors}, status=400)
  ```
