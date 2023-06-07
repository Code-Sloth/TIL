# 무한 댓글 구현

<br/>

### models.py
- ```python
    class Comment(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_moims_comments')
      post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
      parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='child_comments')
      content = models.TextField()

      created_at = models.DateTimeField(auto_now_add=True)

      depth = models.IntegerField(default=0, validators=[MinValueValidator(0)])
  ```

<br/>

### views.py
- ```python
    def detail(request, moim_pk):
          post = Post.objects.get(pk=moim_pk)
          comments = post.comments.filter(parent_comment=None)
          comment_form = CommentForm()

          comment_pk = request.session.pop('comment_pk', None)

          if comment_pk:
              comment = Comment.objects.get(pk=comment_pk)
              comment_section_id = f'comment-{comment.pk}'
          else:
              comment = None
              comment_section_id = None

          context = {
              'post': post,
              'comments': comments,
              'comment_form': comment_form,
              'KAKAO_JS_KEY': KAKAO_JS_KEY,
              'comment': comment,
              'comment_section_id': comment_section_id,
          }
          return render(request, 'moims/detail.html', context)

    def comment_create(request, moim_pk, parent_pk):
      post = Post.objects.get(pk=moim_pk)
      if request.method == 'POST':
          comment_form = CommentForm(request.POST)

          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.user = request.user
              comment.post = post
              if parent_pk != 0:
                  parent_comment = Comment.objects.get(pk=parent_pk)
                  comment.parent_comment = parent_comment
                  comment.depth = parent_comment.depth + 10
                  if comment.depth > 50:
                      comment.depth = 10
              comment.save()
              request.session['comment_pk'] = comment.pk

              return redirect('moims:detail', moim_pk=moim_pk)
  ```

<br/>

### html
- ```html
    <!-- detail.html -->

    {% for comment in comments %}
      <div class='moims--detail--section--commentitem' id='comment-{{ comment.pk }}'>
        <div class='moims--detail--section--commentlist'>
          <header>
            <header>
              {% if comment.user.image %}
                <img src="{{ comment.user.image.url }}" alt="{{ comment.user.username }}">
              {% else %}
                <img src="{% static 'image/noimage.png' %}" alt="noimage">
              {% endif %}
            </header>

            <section>
              {{ comment.user.first_name }}
            </section>

            <footer>
              {{ comment.created_time }}
            </footer>

            <div class='moims--detail--section--commentlist--headerend'>
              <div>
                <button class='recomment--create--button'>
                  <i class="bi bi-chat-fill"></i> 
                  댓글
                </button>
                
                {% if request.user == comment.user %}
                  <form action="{% url 'moims:comment_delete' post.pk comment.pk %}" method="POST">
                    {% csrf_token %}
                    <button type='submit'>삭제</button>
                  </form>

                  <button class='comment--update--button'>
                    수정
                  </button>
                {% endif %}
              </div>
            </div>
          </header>

          <section class='moims--detail--section--commentlist--content'>
            <span class='moims--detail--comment--content--text'>
              {{ comment.content|linebreaksbr }}
            </span>
          </section>

        </div>

        <div class='moims--detail--section--comment--updateform d-none' style='padding-left: calc(20px + 2 * {{ comment.depth }}px);'>
          <form data-post-id="{{ post.pk }}" data-comment-id="{{ comment.pk }}">
            {% csrf_token %}
            {{ comment|get_comment_update_form|safe }}
            <div class='d-flex flex-row-reverse'>
              <button class='comment-submit' type='submit'>등록</button>
              <button class='comment-cancle' type='button'>취소</button>
            </div>
          </form>
        </div>

        <div class='moims--detail--section--comment--createform d-none' style='padding-left: calc(20px + 2 * {{ comment.depth }}px);'>
          <form action="{% url 'moims:comment_create' post.pk comment.pk %}" method="POST">
            <div class='mb-2'>
              <i class="fa-sharp fa-solid fa-reply"></i>
              <span class='moims--detail--recomment--tag'>@{{ comment.user.first_name }}</span>
            </div>
            {% csrf_token %}
            {{ comment_form.content }}
            <div class='d-flex flex-row-reverse'>
              <button class='comment-submit' type='submit'>등록</button>
              <button class='comment-cancle' type='button'>취소</button>
            </div>
          </form>
        </div>
      </div>

      {% if comment.child_comments.all %}
        <div class='moims--detail--section--recomment'>
          {% for c in comment.child_comments.all %}
            {% include "moims/recursive_comment.html" with recursive_comment=c %}
          {% endfor %}
        </div>
      {% endif %}
        
    {% endfor %}

    <!-- recursive_comment.html -->

    {% load static %}
    {% load customtags %}

    <div class='moims--detail--section--commentitem' id='comment-{{ recursive_comment.pk }}'>
      <div class='moims--detail--section--commentlist' style='padding-left: calc(20px + 2 * {{ recursive_comment.depth }}px);'>
        <header>
          <header>
            {% if recursive_comment.user.image %}
              <img src="{{ recursive_comment.user.image.url }}" alt="{{ recursive_comment.user.username }}">
            {% else %}
              <img src="{% static 'image/noimage.png' %}" alt="noimage">
            {% endif %}
          </header>

          <section>
            {{ recursive_comment.user.first_name }}
          </section>

          <footer>
            {{ recursive_comment.created_time }}
          </footer>

          <div class='moims--detail--section--commentlist--headerend'>
            <div>
              <button class='recomment--create--button'>
                <i class="bi bi-chat-fill"></i> 
                댓글
              </button>
              
              {% if request.user == recursive_comment.user %}
                <form action="{% url 'moims:comment_delete' post.pk recursive_comment.pk %}" method="POST">
                  {% csrf_token %}
                  <button type='submit'>삭제</button>
                </form>

                <button class='comment--update--button'>
                  수정
                </button>
              {% endif %}
            </div>
          </div>
        </header>

        <section class='moims--detail--section--commentlist--content'>
          <i class="fa-sharp fa-solid fa-reply"></i> <span class='moims--detail--recomment--tag'>@{{ recursive_comment.parent_comment.user.first_name }}</span> <span class='moims--detail--comment--content--text'>{{ recursive_comment.content|linebreaksbr }}</span>
        </section>

      </div>

      <div class='moims--detail--section--comment--updateform d-none' style='padding-left: calc(20px + 2 * {{ recursive_comment.depth }}px);'>
        <form data-post-id="{{ post.pk }}" data-comment-id="{{ recursive_comment.pk }}">
          {% csrf_token %}
          {{ recursive_comment|get_comment_update_form|safe }}
          <div class='d-flex flex-row-reverse'>
            <button class='comment-submit' type='submit'>등록</button>
            <button class='comment-cancle' type='button'>취소</button>
          </div>
        </form>
      </div>

      <div class='moims--detail--section--comment--createform d-none' style='padding-left: calc(20px + 2 * {{ recursive_comment.depth }}px);'>
        <form action="{% url 'moims:comment_create' post.pk recursive_comment.pk %}" method="POST">
          <div class='mb-2'>
            <i class="fa-sharp fa-solid fa-reply"></i>
            <span class='moims--detail--recomment--tag'>@{{ recursive_comment.user.first_name }}</span>
          </div>
          {% csrf_token %}
          {{ comment_form.content }}
          <div class='d-flex flex-row-reverse'>
            <button class='comment-submit' type='submit'>등록</button>
            <button class='comment-cancle' type='button'>취소</button>
          </div>
        </form>
      </div>
    </div>


    {% if recursive_comment.child_comments.all %}
      <div class='moims--detail--section--recomment'>
        {% for reply in recursive_comment.child_comments.all %}
          {% include "moims/recursive_comment.html" with recursive_comment=reply %}
        {% endfor %}
      </div>
    {% endif %}
      
  ```

<br/>

### JS
- ```javascript
    document.addEventListener('DOMContentLoaded', function() {
      const CommentlistDiv = document.querySelectorAll('.moims--detail--section--commentitem')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

      CommentlistDiv.forEach((listDiv) => {
        const CommentUpdateForm = listDiv.querySelector('.moims--detail--section--comment--updateform')
        const CommentUpdateSubmitForm = CommentUpdateForm.querySelector('form')
        const CommentCancleBtn = CommentUpdateForm.querySelector('.comment-cancle')
        const RecommentCreateForm = listDiv.querySelector('.moims--detail--section--comment--createform')
        const RecommentCancleBtn = RecommentCreateForm.querySelector('.comment-cancle')

        const CommentUpdateBtn = listDiv.querySelector('.comment--update--button')
        if (CommentUpdateBtn) {
          CommentUpdateBtn.addEventListener('click', (event) => {
            if (CommentUpdateForm.classList.contains('d-none')) {
              CommentUpdateForm.classList.remove('d-none')
            } else {
              CommentUpdateForm.classList.add('d-none')
            }

            if (!RecommentCreateForm.classList.contains('d-none')) {
              RecommentCreateForm.classList.add('d-none')
            }
          })
        }

        if (CommentCancleBtn) {
          CommentCancleBtn.addEventListener('click', (event) => {
            CommentUpdateForm.classList.add('d-none')
          })
        }

        if (CommentUpdateSubmitForm) {
          CommentUpdateSubmitForm.addEventListener('submit', (event) => {
            event.preventDefault()
            const postId = event.target.dataset.postId
            const commentId = event.target.dataset.commentId
            const formData = new FormData(CommentUpdateSubmitForm)
            formData.append('comment-content', CommentUpdateSubmitForm.querySelector('textarea').value)

            axios({
              method: "POST",
              url: `/moims/${postId}/update/${commentId}/`,
              headers: {'X-CSRFToken': csrftoken},
              data: formData,
            })
              .then((response) => {
                const CommentContent = listDiv.querySelector('.moims--detail--comment--content--text')
                CommentContent.textContent = response.data.commentContent

                CommentUpdateForm.classList.add('d-none')
              })
              .catch((error) => {
                console.log(error.response)
              })
          })
        }

        const RecommentCreateBtn = listDiv.querySelector('.recomment--create--button')
        if (RecommentCreateBtn) {
          RecommentCreateBtn.addEventListener('click', (event) => {
            if (RecommentCreateForm.classList.contains('d-none')) {
              RecommentCreateForm.classList.remove('d-none')
            } else {
              RecommentCreateForm.classList.add('d-none')
            }

            if (!CommentUpdateForm.classList.contains('d-none')) {
              CommentUpdateForm.classList.add('d-none')
            }
          })
        }

        if (RecommentCancleBtn) {
          RecommentCancleBtn.addEventListener('click', (event) => {
            RecommentCreateForm.classList.add('d-none')
          })
        }
      })
    })
  ```
