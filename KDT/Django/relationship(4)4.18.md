# Django - Many to many relationships 2

<br/>

## 개요
- Profile 구현
  - 자연스러운 follow 흐름을 위한 프로필 페이지 작성
    - ```python
        # accounts/urls.py

        urlpatterns = [
          ...
          path('profile/<username>/', views.profile, name='profile'),
          # 앞에 profile을 붙이지 않으면 path들의 순서를 고려해줘야 함
        ]

        # accounts/views.py

        from django.contrib.auth import get_user_model

        def profile(request, username):
            User = get_user_model()
            person = User.objects.get(username=username)
            context = {
                'person': person,
            }
            return render(request, 'accounts/profile.html', context)
      ```
  - profile 템플릿 작성
    - ```html
        <!-- accounts/profile.html -->

        <h1>{{ person.username }}님의 프로필</h1>

        <hr>

        <h2>{{ person.username }}'s 게시글</h2>
        {% for article in person.article_set.all %}
          <div>{{ article.title }}</div>
        {% endfor %}

        <hr>

        <h2>{{ person.username }}'s 댓글</h2>
        {% for comment in person.comment_set.all %}
          <div>{{ comment.content }}</div>
        {% endfor %}

        <hr>

        <h2>{{ person.username }}'s 좋아요한 게시글</h2>
        {% for article in person.like_articles.all %}
          <div>{{ article.title }}</div>
        {% endfor %}

        <h2>{{ person.username }}'s 좋아요한 게시글</h2>
        {% for article in person.like_comments.all %}
          <div>{{ article.title }}</div>
        {% endfor %}
      ```
  - profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성
    - ```html
        <!-- articles/index.html -->

        <!-- 잘못된 주소 <a href="{% url 'accounts:profile' user.username %}">내 프로필</a> -->
        <p>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></p>
      ```

<br/>

## User & User / Follow 구현
- User(M) - User(N)
  - 유저는 0명 이상의 다른 유저와 관련됨
  - 유저는 다른 유저로부터 0개 이상의 팔로우를 받을 수 있고, 유저는 0명 이상의 다른 유저들에게 팔로잉 할 수 있음
- Follow 구현
  - models 설계
    - ```python
        # accounts/models.py

        class User(AbstractUser):
          followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

        # self : 같은 모델의 다른 유저들과 연결 / related_name 자동 설정
        # symmetrical : 대칭 관계를 설정
      ```
  - url 및 view 함수 작성
    - ```python
        # accounts/urls.py

        urlpatterns = [
          ...
          path('<int:user_pk>/follow/', views.follow, name='follow'),
        ]

        # accounts/views.py

        @login_required
        def follow(request, user_pk):
            User = get_user_model()
            person = User.objects.get(pk=user_pk)
            # 헷갈리면 me와 you로 변수지정해서 사용
            if person != request.user: # 해당 프로필의 유저 정보와 현재 내 정보와 다를 때
                if person.followers.filter(pk=request.user.pk).exists():
                    person.followers.remove(request.user)
                else:
                    person.followers.add(request.user)
            return redirect('accounts:profile', person.username)
      ```
  - 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성
    - ```html
        <!-- accounts/profile.html -->

        <div>
          <div>
            팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
          </div>

          {% if request.user != person %}
            <div>
              <form action="{% url 'accounts:follow' person.pk %}" method="POST">
                {% csrf_token %}
                {% if request.user in person.followers.all %}
                  <input type="submit" value="Unfollow">
                {% else %}
                  <input type="submit" value="Follow">
                {% endif %}
              </form>
            </div>
          {% endif %}
        </div>
      ```

