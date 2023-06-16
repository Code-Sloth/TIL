# 장고 TIP

<br/>

### Select 필드
- ```html
    <!-- 보이는 데이터를 출력 -->
    {{ comment.get_category_display }}
  ```

<br/>

### Intcomma(가격 나타낼 때 사용)
- ```html
    <!-- settings.py에 humanize추가 후 -->

    {% load humanize %}

    {{ course.price|intcomma }}
  ```

<br/>

### model created_time
- ```python
    @property
    def created_time(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return self.created_at.strftime('%Y-%m-%d')
  ```

<br/>

### 세션을 이용한 조회수 구현
- ```python
    def detail(request, market_pk):
      post = Post.objects.get(pk=market_pk)

      if not request.session.get("post_viewed_{}".format(market_pk)):
          post.views += 1
          post.save()
          request.session["post_viewed_{}".format(market_pk)] = True

      context = {'post': post}
      return render(request, 'markets/detail.html', context)
  ```

<br/>

### 자연스러운 d-none 처리
- ```javascript
    setTimeout(() => {
      likeAlert.style.opacity = '0.9'
      setTimeout(() => {
        likeAlert.style.opacity = '0.8'
        setTimeout(() => {
          likeAlert.style.opacity = '0.7'
          setTimeout(() => {
            likeAlert.style.display = 'none'
          }, 50)
        }, 50)
      }, 50)
    }, 2500)
  ```

<br/>

### 공유 URL 복사
- ```javascript
    document.addEventListener('DOMContentLoaded', function() {

      document.getElementById('moims--detail--share').addEventListener('click', function() {
          var currentUrl = window.location.href
          var tempInput = document.createElement('input')

          tempInput.value = currentUrl
          document.body.appendChild(tempInput)

          tempInput.select()

          document.execCommand('copy')
    
          document.body.removeChild(tempInput)

          alert('URL이 복사되었습니다!')
      })
    })
  ```

<br/>

### Collapse Mouse Hover Event
- ```javascript
    const navbarImageBtn = document.querySelector('.nav--bar--right--image')
    const navbarCollapse = document.querySelector('#nav--bar--right--collapse')

    navbarImageBtn.addEventListener('mouseenter', (event) => {
      navbarCollapse.classList.remove('d-none')
    })

    navbarImageBtn.addEventListener('mouseleave', function(event) {
      if (!event.relatedTarget || !navbarCollapse.contains(event.relatedTarget)) {
        if (!navbarCollapse.classList.contains('d-none')) {
          navbarCollapse.classList.add('d-none')
        }
      }
    })

    navbarCollapse.addEventListener('mouseleave', function(event) {
      if (!event.relatedTarget || !navbarImageBtn.contains(event.relatedTarget)) {
        if (!navbarCollapse.classList.contains('d-none')) {
          navbarCollapse.classList.add('d-none')
        }
      }
    })
  ```

<br/>

### 템플릿에서 반복문 횟수 확인
- ```html
    {% for join_user in post.join_users.all %}
      <a class='moims--detail--section--member--item' href="??">
        {% if join_user.image %}
          <img src="{{ join_user.image.url }}" alt="{{ join_user }}">
        {% else %}
          <img src="{% static 'image/noimage.png' %}" alt="noimage">
        {% endif %}
        {% if forloop.counter == 1 %}
          <div class='moims--detail--section--member--crown'>
            <img src="{% static 'image/crown.png' %}" alt="crown">
          </div>
        {% endif %}
      </a>
    {% endfor %}
  ```

<br/>

### ckeditor 여러 개 사용
- ```javascript
    var editorContainers = document.querySelectorAll('.communities--detail--section--commentitem .comment-ckeditor');

    editorContainers.forEach(function(container) {
      ClassicEditor
        .create(container)
        .catch(error => {
          console.error(error);
        });
    });
  ```

<br/>

### sort
- ```python
    def index_sort(o, queryset):
      if o == '최신순':
          return queryset.order_by('-pk')
      elif o == '추천순':
          return queryset.annotate(likes_diff=Count('like_users') - Count('dislike_users')).order_by('-likes_diff')
      elif o == '댓글순':
          return queryset.annotate(comment_count=Count('comments')).order_by('-comment_count')
      elif o == '스크랩순':
          return queryset.annotate(scrape_count=Count('scrape_users')).order_by('-scrape_count')
      elif o == '조회순':
          return queryset.order_by('-views')
  ```

<br/>

### 비동기 메세지
- ```javascript
    const bodyElement  = document.querySelector('body');
    const sideElement = document.querySelector('#side-alarm')
    const newAlarm = document.createElement('a');

    if (window.innerWidth < 800) {
      // 겹치게 쌓이기

      newAlarm.href = `/chats/${sendername}`;
      newAlarm.classList.add('livealarm')
      newAlarm.innerHTML = `<span><i class="bi bi-chat-fill"></i> ${sendername}</span>님이 메세지를 보냈어요.`;
      
      bodyElement.insertBefore(newAlarm, bodyElement.lastChild);

      setTimeout(() => {
        bodyElement.removeChild(newAlarm);
      }, 3000);
    } else {
      // 위로 쌓이기
      newAlarm.href = `/chats/${sendername}`;
      newAlarm.classList.add('sidelivealarm')
      newAlarm.innerHTML = `<div><s><i class="bi bi-chat-fill"></i> ${sendername}</s>님이 메세지를 보냈어요.</div><section>${message}</section>`;
      
      sideElement.insertBefore(newAlarm, sideElement.firstChild);

      setTimeout(() => {
        sideElement.removeChild(newAlarm);
      }, 3000);
    }
  ```

<br/>

### 댓글 생성 후 스크롤 이동
- ```python
    def detail(request, post_pk):
      post = Post.objects.get(pk=post_pk)
      comments = post.comments.filter(parent_comment=None)
      comment_form = CommentForm()

      comment_pk = request.session.pop('comment_pk', None)

      if comment_pk:
          comment = Comment.objects.get(pk=comment_pk)
          comment_section_id = f'comment-{comment.pk}'
      else:
          comment = None
          comment_section_id = None

      if not request.session.get("post_viewed_{}".format(post_pk)):
          post.views += 1
          post.save()
          request.session["post_viewed_{}".format(post_pk)] = True
      
      context = {
          'post': post,
          'comments': comments,
          'comment_form': comment_form,
          'comment': comment,
          'comment_section_id': comment_section_id,
          'likes_count': post.like_users.count()-post.dislike_users.count(),
          'KAKAO_JS_KEY': KAKAO_JS_KEY,
      }
      return render(request, 'communities/detail.html', context)
  ```
- ```html
    {% for comment in comments %}
      <div class='communities--detail--section--commentitem' id='comment-{{ comment.pk }}'>
        {{ comment.content }}
      </div>
    <% endfor %>
  ```
- ```javascript
    {% if comment %}
      $(document).ready(function() {
        var targetScrollPosition = $('#{{ comment_section_id }}').offset().top - 100;

        $('html, body').animate({
          scrollTop: targetScrollPosition
        }, 500);
      });
    {% endif %}
  ```
