# 댓글 수정 ajax

<br/>

### urls.py
- ```python
    from django.urls import path
    from . import views


    app_name = 'products'
    urlpatterns = [
        ...,
        path('<int:product_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    ]
  ```

<br/>

### views.py
- ```python
    def detail(request, product_pk):
        product = Product.objects.get(pk=product_pk)
        comments = product.comments.all().order_by('-pk')

        comment_comment_form = []
        for comment in comments:
            comment_form = CommentForm(instance=comment)
            comment_comment_form.append((comment, comment_form))

        sort = request.GET.get('sort','')
        if sort:
            comments = comment_sort(comments, sort)

            comment_comment_form = []
            for comment in comments:
                comment_form = CommentForm(instance=comment)
                comment_comment_form.append((comment, comment_form))

        context = {
            'product': product,
            'comment_comment_form': comment_comment_form,
        }
        return render(request, 'products/detail.html', context)

    def comment_update(request, product_pk, comment_pk):
        product = Product.objects.get(pk=product_pk)
        comment = Comment.objects.get(pk=comment_pk)
        comment_form = CommentForm(request.POST,request.FILES, instance=comment)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.star = int(request.POST.get('star-rating'))
            comment.save()
            
            context = {
                'commentContent': comment.content,
                'commentImageUrl': comment.image.url,
                'commentStar_count': comment.star,
            }
            return JsonResponse(context)
        else:
            print(comment_form.errors)
  ```

<br/>

### detail.html
- ```html
    {% for comment, comment_form in comment_comment_form %}
      <div class='detail-comment-allbox'>
        <div class='comment-header'>
          <div class='comment-header-title'>
            {{ comment.user.last_name }}
          </div>

          <div class='comment-header-right'>
            <div class='star-box comment-starbox'>
              <div class='star-gray'>
                <img class='w-100' src="{% static 'image/product_graystar.png' %}" alt="graystar">
              </div>
              <div class='star-star comment-star-star' style='width: {{ comment.star_multiple }}%;'>
                <img src="{% static 'image/product_star.png' %}" alt="star">
              </div>
            </div>

            <div class='comment-star-count'>
              {{ comment.star }}
            </div>

            <div class='comment-time'>
              {{ comment.created_time }}
            </div>

            {% if request.user == comment.user %}
              <button class='update-btn comment-delete ms-3' type='submit'>수정</button>

              <form action="{% url 'products:comment_delete' product.pk comment.pk %}" method="POST">
                {% csrf_token %}
                <button class='comment-delete' class='btn btn-outline-secondary' type='submit'>삭제</button>
              </form>
            {% endif %}
          </div>
        </div>

        <div class='comment-contentbox d-block'>
          <div class='comment-content'>
            {{ comment.content|linebreaks }}
          </div>

          {% if comment.image %}
            <div class='comment-img'>
              <img class='h-100' src="{{ comment.image.url }}" alt="commentImage">
            </div>
          {% endif %}
        </div>

        <form class='comment_form mb-5 d-none' data-user-id="{{ product.pk }}" enctype="multipart/form-data">
          <input type="hidden" class="comment_pk" value="{{ comment.pk }}">

          {{ comment_form.content }}

          {% if comment.image %}
            <div class='comment_form_image'>
              <img class='w-100' src="{{ comment.image.url }}" alt="#">
            </div>
          {% endif %}

          {{ comment_form.image }}

          <div class='d-flex comment-form-star'>
            <button type="button" class='comment_star' id="star1" data-value="1">
              <img src="{% static 'image/star1.svg' %}" id="img1" alt="star" data-value="1">
            </button>
            <button type="button" class='comment_star' id="star2" data-value="2">
              <img src="{% static 'image/star1.svg' %}" id="img2" alt="star" data-value="2">
            </button>
            <button type="button" class='comment_star' id="star3" data-value="3">
              <img src="{% static 'image/star1.svg' %}" id="img3" alt="star" data-value="3">
            </button>
            <button type="button" class='comment_star' id="star4" data-value="4">
              <img src="{% static 'image/star1.svg' %}" id="img4" alt="star" data-value="4">
            </button>
            <button type="button" class='comment_star' id="star5" data-value="5">
              <img src="{% static 'image/star1.svg' %}" id="img5" alt="star" data-value="5">
            </button>

            <div class='comment-star-content'>
              최고
            </div>
          </div>

          <button id='star_rating' name='star_rating' value='{{ comment.star }}' class='comment-submit-btn' type='submit'>등록</button>
        </form>
      </div>
    {% endfor %}
  ```

<br/>

### JS
- ```javascript
    const allBox = document.querySelectorAll('.detail-comment-allbox')

    allBox.forEach((box) => {
      const updateBtn = box.querySelector('.update-btn')
      const commentBox = box.querySelector('.comment-contentbox')
      const commentForm = box.querySelector('.comment_form')

      if (updateBtn) {

        updateBtn.addEventListener('click', (event) => {
      
          if (commentBox.classList.contains('d-block')) {
            commentBox.classList.remove('d-block')
            commentBox.classList.add('d-none')
            commentForm.classList.remove('d-none')
            commentForm.classList.add('d-block')
          } else {
            commentBox.classList.remove('d-none')
            commentBox.classList.add('d-block')
            commentForm.classList.remove('d-block')
            commentForm.classList.add('d-none')
          }
        })
      }

      const starBtns = box.querySelectorAll('.comment_star')
      const starRating = box.querySelector('#star_rating')
      const starContent = box.querySelector('.comment-star-content')

      starBtns.forEach((bt) => {
        const img = bt.querySelector('img')
        const attr = bt.getAttribute('data-value')

        if (attr <= starRating.value) {
          img.src = "/static/image/star1.svg"
          img.alt = "star1"
        } else {
          img.src = "/static/image/graystar1.svg"
          img.alt = "graystar1"
        }
      })

      starBtns.forEach((btn) => {
        btn.addEventListener('click', (event) => {
          const value = event.target.getAttribute('data-value')

          if (value == 1) {
            starContent.textContent = '나쁨'
          } else if (value == 2) {
            starContent.textContent = '별로'
          } else if (value == 3) {
            starContent.textContent = '보통'
          } else if (value == 4) {
            starContent.textContent = '좋음'
          } else if (value == 5) {
            starContent.textContent = '최고'
          }

          starRating.value = value
          starBtns.forEach((bt) => {
            const img = bt.querySelector('img')
            const attr = bt.getAttribute('data-value')

            if (attr <= value) {
              img.src = "/static/image/star1.svg"
              img.alt = "star1"
            } else {
              img.src = "/static/image/graystar1.svg"
              img.alt = "graystar1"
            }
          })
        })
      })

      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

      if (commentForm) {

        commentForm.addEventListener('submit', (event) => {
          event.preventDefault()
      
          const productId = event.target.dataset.userId
          const commentId = commentForm.querySelector('.comment_pk').value
          const formData = new FormData(commentForm)
          formData.append('csrfmiddlewaretoken', csrftoken)
          formData.append('star-rating', starRating.value)

          axios({
            method: 'POST',
            url: `/products/${productId}/comments/${commentId}/update/`,
            headers: {
              'Content-Type': 'multipart/form-data'
            },
            data: formData,
          })
            .then((response) => {

              if (commentBox.classList.contains('d-block')) {
                commentBox.classList.remove('d-block')
                commentBox.classList.add('d-none')
                commentForm.classList.remove('d-none')
                commentForm.classList.add('d-block')
              } else {
                commentBox.classList.remove('d-none')
                commentBox.classList.add('d-block')
                commentForm.classList.remove('d-block')
                commentForm.classList.add('d-none')
              }

              const commentContent = box.querySelector('.comment-content > p')
              const commentImg = box.querySelector('.comment-img > img')
              const responseContent = response.data.commentContent
              const responseImageUrl = response.data.commentImageUrl

              commentContent.textContent = responseContent
              commentImg.src = responseImageUrl
              commentImg.alt = responseContent

              const commentStarStar = box.querySelector('.comment-star-star')
              const commentStarCount = box.querySelector('.comment-star-count')
              const commentStar = response.data.commentStar_count

              commentStarStar.style['width'] = `${commentStar*20}%`
              commentStarCount.textContent = commentStar

            })

            .catch((error) => {
              console.log(error.response)
            })
        })
      }
    })



  ```
  ...
  ...