# Django - Many to one relationships 2

<br/>

## 개요
- Article(N) - User(1)
  - 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음
- Comment(N) - User(1)
  - 0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음

<br/>

## 모델 관계 설정 / Article & User
- User 외래 키 정의
  - ```python
      # articles/models.py

      from django.conf import settings

      class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        pass
    ```
- User 모델을 참조하는 2가지 방법
  - get_user_model()
    - 반환 값 `User Object(객체)`
    - models.py가 아닌 다른 모든 곳에서 참조할 때 사용
  - settings.AUTH_USER_MODEL
    - 반환 값 `accounts.User(문자열)`
    - models.py의 모델 필드에서 참조할 때 사용
- Migration 진행
  - 기본적으로 모든 컬럼은 NOT NULL 제약 조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
  - 기본값 설정 `1`을 입력하고 Enter진행
  - user_id에 어떤 데이터를 넣을 지 `1`을 입력하고 Enter진행
  - 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨
- Migrate 진행

<br/>

## CRUD 구현 / Article & User
- CREATE
  - 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit옵션 활용
  - ```python
      # articles/views.py

      @login_required
      def create(request):
          if request.method == 'POST':
              form = ArticleForm(request.POST)
              if form.is_valid():
                  article = form.save(commit=False)
                  article.user = request.user
                  return redirect('articles:detail', article.pk)
          else:
              form = ArticleForm()
          context = {
              'form': form,
          }
          return render(request, 'articles/create.html', context)
    ```
- READ
  - index 템플릿과 detail템플릿에서 각 게시글의 작성자 출력 및 확인
  - ```html
      <!-- articles/index.html -->

      {% for article in articles %}
        <p>
          작성자 : {{ article.user }}
        </p>
      {% endfor %}

      <!-- articles/detail.html -->

      작성자 : {{ article.user }}
    ```
- UPDATE
    - 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함
      - ```python
          # articles/views.py

          @login_required
          def update(request, article_pk):
              article = Article.objects.get(pk=article_pk)
              if request.user == article.user:
                  if request.method == 'POST':
                      form = ArticleForm(request.POST, instance=article)
                      if form.is_valid():
                          form.save()
                          return redirect('articles:detail', article.pk)
                  else:
                      form = ArticleForm(instance=article)
              else:
                  return redirect('articles:index')
              context = {
                  'article': article,
                  'form': form,
              }
              return render(request, 'articles/update.html', context)
      ```
    - 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 함
      - ```html
          <!-- articles/detail.html -->

          {% if request.user == article.user %}
            <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
            <form action="{% url 'articles:delete' article.pk  %}" method="POST">
              {% csrf_token %}
              <input type="submit" value="삭제">
            </form>
          {% endif %}
        ```
- DELETE
    - 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함
      - ```python
          # articles/views.py

          @login_required
          def delete(request, article_pk):
              article = Article.objects.get(pk=article_pk)
              if request.user == article.user:
                  article.delete()
              return redirect('articles:index')
        ```

<br/>

## 모델 관계 설정 / Comment & User
- User 외래 키 정의
  - ```python
      # articles/models.py

      class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ```
- Migration 진행
  - 위의 Article user생성과 동일하게 진행

<br/>

## CRD 구현 / Comment & User
- CREATE
  - 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit옵션 활용
    - ```python
        # articles/views.py

        def comment_create(request, article_pk):
          article = Article.objects.get(pk=article_pk)
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.article = article
              comment.user = request.user
              comment.save()
              return redirect('articles:detail', article.pk)
          context = {
              'article':article,
              'comment_form':comment_form,
          }
          return render(request, 'articles/detail.html', context)
      ```
- READ
  - detail 템플릿에서 각 댓글의 작성자 출력 및 확인
    - ```html
        <!-- articles/detail.html -->

        {% for comment in comments %}
          댓글 작성자 : {{ comment.author }}
        {% endfor %}
      ```
- DELETE
  - 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함
    - ```python
        # articles/views.py

        def comment_delete(request, article_pk, comment_pk):
          comment = Comment.objects.get(pk=comment_pk)
          if request.user == comment.user:
            comment.delete()
          return redirect('articles:detail', article_pk)
      ```
  - 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함
    - ```html
        <!-- articles/detail.html -->

        {% for comment in comments %}
          댓글 작성자 : {{ comment.author }}
          {{ comment.content }}
          {% if request.user == comment.user %}
            <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
              {% csrf_token %}
              <input type="submit" value="삭제">
            </form>
          {% endif %}
        {% endfor %}
      ```

<br/>

## 참고
- 인증된 사용자인 경우만 댓글 작성 및 삭제하기
  - ```python
      # articles/views.py

      @login_required
      def comments_create(request, article_pk):
        pass

      @login_required
      def comments_delete(request, article_pk, comment_pk):
        pass
    ```
