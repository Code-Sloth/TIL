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
