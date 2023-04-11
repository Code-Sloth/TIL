# Django - Many to one relationships 1'

<br/>

## Foreign Key
- 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
- 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용

<br/>

## 모델 관계 설정
- Many to one relationships
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- Comment(N) - Article(1)
  - |Coment|Article|
    |--|--|
    |id|id|
    |content|title|
    |created_at|content|
    |updated_at|created_at|
    |Article의 id|updated_at|
- ForeignKey()
  - django에서 N:1관계 설정 모델 필드
- Comment 모델 정의
  - ```python
      # articles/models.py

      class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        content = models.CharField(max_length=200)
        author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

      # ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
      # ForeignKey 클래스를 작성하는 위치와 관계없이 필드 마지막에 생성됨
      # ForeignKey(to, on_delete)
      # to : 참조하는 모델 class 이름
      # on_delete : 참조하는 모델 class가 삭제될 때 연결된 하위 객체의 동작을 결정
      # CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
    ```

<br/>

### 댓글 생성
- `$ python manage.py shell_plus`

<br/>

## 관계 모델 참조
- 역참조
  - 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
  - N:1관계에서는 1이 N을 참조하는 상황
  - 하지만 Article에는 Comment를 참조할 어떠한 필드도 없음
- `article.comment_set.all()`
  - 모델 인스턴스.related manager.QuerySet API
- related manager
  - N:1혹은 M:N관계에서 역참조 시에 사용하는 manager
  - `objects`라는 api와 비슷하게 생각
  - 필요한 이유
    - article.comment 형식으로는 댓글 객체를 참조할 수 없음
    - 실제 Article 클래스에슨 Comment와의 어떠한 관계도 작성되어 있지 않기 때문
    - 대신 Django가 역참조할 수 있는 `'comment_set'` manager를 자동으로 생성해 댓글 객체를 참조 가능
    - N:1관계에서 생성되는 Related manager의 이름은 참조하는 '모델명_set'이름 규칙으로 만들어짐

<br/>

## 댓글 기능 구현
- 사용자로부터 댓글 데이터를 받기 위한 CommentForm 작성
  - ```python
      # articles/forms.py

      from .models import Article, Comment

      class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('content',)
    ```
- detail 페이지에서 CommentForm 출력 / `view`
  - ```python
      # articles/viwes.py

      from .forms import ArticleForm, CommentForm

      def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = article.comment_set.all() # article에 연결되어있는 모든 댓글을 가져옴
        context = {
            'article': article,
            'comment_form': comment_form,
            'comments': comments
        }
        return render(request, 'articles/detail.html', context)
    ```
- detail 페이지에서 CommentForm 출력 / `template`
  - ```html
      <!-- articles/detail.html -->

      {% for comment in comments %}
        <li>
        {{ comment.author }}
        {{ comment.content }}
        <!-- 아래 delete부분의 form도 작성 -->
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
        </li>
      {% endfor %}
    ```
- create
  - ```python
      # articles/views.py

      def comment_create(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # DB에 저장하지 않고 인스턴스만 반환
            comment.article = article # 단일 객체를 저장
            comment.author = request.user # user 데이터를 저장
            comment.save() # 최종 저장
            return redirect('articles:detail', article.pk)
        context = {
            'article':article,
            'comment_form':comment_form,
        }
        return render(request, 'articles/detail.html', context)
    ```
- delete
    - ```python
        # articles/urls.py

        app_name = 'articles'
        urlpatterns = [
            ...,
            path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
        ]
      ```
    - ```python
        # articles/views.py

        def comment_delete(request, article_pk, comment_pk):
          comment = Comment.objects.get(pk=comment_pk) # comment_pk로 댓글의 pk 연결
          comment.delete()
          return redirect('articles:detail', article_pk) # article_pk의 detail로 이동
      ```

<br/>

## 참고
- 댓글 개수 출력
  - DTL filter / length 사용
    - ```html
        {{ comments|length }}
      ```
    - ```html
        {{ article.comment_set.all|length}}
      ```
  - Queryset API / count() 사용
    - ```html
        {{ article.comment_set.count }}
      ```
- 댓글이 없는 경우 대체 컨텐츠 출력
  - ```html
      <!-- articles/detail.html -->

      {% for comment in comments %}
        <li>
        {{ comment.author }}
        {{ comment.content }}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
        </li>
      {% empty %}
        <p>댓글이 없습니다.</p>
      {% endfor %}
    ```
- 댓글 수정을 구현하지 않는 이유
  - 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form부분만 변경되어 수정 할 수 있도록 함
  - 이처럼 페이지의 일부 내용만 업데이트 하는 것은 `JavaScript`의 영역
- admin site 등록
  - 새로 작성한 Comment 모델을 admin site에 등록하고 싶으면
    - ```python
        # articles/admin.py

        from .models import Article, Comment

        admin.site.register(Article)
        admin.site.register(Comment)
      ```
