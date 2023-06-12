# 좋아요 & 싫어요 ajax 구현

<br/>

### html
- ```html
    <form class='detail-left-section-form' data-comment-id="{{ comment.pk }}">

      <button name='like_value' value='like' type='submit'>
        {% if request.user in comment.like_users.all %}
          <i class='fas fa-thumbs-up comment-like-icon like_green'></i>
        {% else %}
          <i class='fas fa-thumbs-up comment-like-icon like_gray'></i>
        {% endif %}
      </button>
    
      <div class='comment-detail-left-section-count'>
        <span>{{ comment.like_users.count }}</span>
      </div>

      <button name='like_value' value='unlike' type='submit'>
        {% if request.user in comment.like_users.all %}
          <i class='fas fa-thumbs-up comment-unlike-icon like_green'></i>
        {% else %}
          <i class='fas fa-thumbs-up comment-unlike-icon like_gray'></i>
        {% endif %}
      </button>

    </form>
  ```

<br/>

### JS
- ```javascript
    const likeForm = document.querySelector('.detail-left-section-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    likeForm.addEventListener('submit', (event) => {
      event.preventDefault()

      const commentId = event.target.dataset.commentId
      const likeBtn = event.submitter
      const likeValue = likeBtn.value

      const formData = new FormData(likeForm)
      formData.append('like_value', likeValue)

      axios({
        method: "POST",
        url: `/communities/comments/${commentId}/likes/`,
        headers: {'X-CSRFToken': csrftoken},
        data: formData
      })

        .then((response) => {
          const isLiked = response.data.is_liked
          const isUnLiked = response.data.is_unliked
          const likeIcon = likeForm.querySelector('.comment-like-icon')
          const UnLikeIcon = likeForm.querySelector('.comment-unlike-icon')

          const likeCount = likeForm.querySelector('.comment-detail-left-section-count')

          likeCount.textContent = response.data.comment_like

          if (isLiked === true) {
            likeIcon.classList.remove('like_gray')
            likeIcon.classList.add('like_green')
          } else if (isLiked == false) {
            likeIcon.classList.add('like_gray')
            likeIcon.classList.remove('like_green')
          }

          if (isUnLiked === true) {
            UnLikeIcon.classList.remove('like_gray')
            UnLikeIcon.classList.add('like_green')
          } else if (isUnLiked == false) {
            UnLikeIcon.classList.add('like_gray')
            UnLikeIcon.classList.remove('like_green')
          }

        })

        .catch((error) => {
          console.log(error.response)
        })
    })
  ```

<br/>

### views.py
- ```python
    def comment_like(request, comment_pk):
      comment = Comment.objects.get(pk=comment_pk)
      like_value = request.POST.get('like_value')

      if like_value == 'like':
          if comment.like_users.filter(pk=request.user.pk).exists():
              comment.like -= 1
              comment.like_users.remove(request.user)
              is_liked = False
              is_unliked = False

          elif comment.unlike_users.filter(pk=request.user.pk).exists():
              comment.like += 2
              comment.unlike_users.remove(request.user)
              comment.like_users.add(request.user)
              is_liked = True
              is_unliked = False

          else:
              comment.like += 1
              comment.like_users.add(request.user)
              is_liked = True
              is_unliked = False

      else:
          if comment.unlike_users.filter(pk=request.user.pk).exists():
              comment.like += 1
              comment.unlike_users.remove(request.user)
              is_liked = False
              is_unliked = False

          elif comment.like_users.filter(pk=request.user.pk).exists():
              comment.like -= 2
              comment.like_users.remove(request.user)
              comment.unlike_users.add(request.user)
              is_liked = False
              is_unliked = True

          else:
              comment.like -= 1
              comment.unlike_users.add(request.user)
              is_liked = False
              is_unliked = True

      comment.save()

      context = {
          'is_liked': is_liked,
          'is_unliked': is_unliked,
          'comment_like': comment.like,
      }

      return JsonResponse(context)
  ```

<br/>

### 참고
- ```python
    # 이 함수를 사용하 model field로 like integer field없이 가능
    @property
    def likes_count(self):
        return self.like_users.count()-self.dislike_users.count()
  ```