# ORM UPDATE, DELETE

<br>

## ORM UPDATE
- ```python
    # 수정할 인스턴스 조회
    article = Article.objects.get(pk=1)

    # 인스턴스 변수를 변경
    article.title = 'byebye'

    # 저장
    article.save()

    # 정상적으로 변겨오딘 것을 확인
    article.title
    'byebye'
  ```

<br/>

## ORM DELETE
- ```python
    # 삭제할 인스턴스 조회
    article = Article.objects.get(pk=1)

    # delete 메서드 호출 (삭제된 객체가 반환)
    article.delete()
    (1, {'article.Article' : 1})

    # 삭제한 데이터는 더이상 조회 불가능
    Article.objects.get(pk=1)
    DoesNotExist: Article matching query does not exist
  ```

<br/>

# Django - ORM with view

<br/>

## 사전 준비
- app URLs 분할 및 연결
    - ```python
        # articles/urls.py
        from django.urls import path

        app_name = 'articles'
        urlpatterns = [

        ]

        # crud/urls.py

        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
          path('admin/', admin.site.urls),
          path('articles/', include('articles.urls')),
        ]
      ```
- index 페이지 작성
    - ```python
        # articles/urls.py

        from django.urls import path
        from . import views

        app_name = 'articles'
        urlpatterns = [
          path('', views.index, name = 'index'),
        ]

        # articles/views.py

        def index(request):
          return render(request, 'articles/index.html')
      ```
      ```html
        <h1>Articles</h1>
      ```

## READ
- 전체 게시글 조회
    - ```python
        # articles/views.py

        from .models import Article

        def index(request):
          articles = Article.objects.all()
          context = {
            'articles' : articles,
          }
          return render(request, 'articles/index.html', context)
      ```
      ```html
        <h1>Articles</h1>
        <hr>
        {% for article in articles %}
          <p>{{ article.pk }}</p>
          <p>{{ article.title }}</p>
          <p>{{ article.content }}</p>
          <hr>
        {% endfor %}
      ```
- 단일 게시글 조회
    - ```python
        # articles/urls.py

        urlpatterns = [
          path('<int:pk>/', views.detail, name = 'detail'),
        ]

        # articles/views.py

        def detail(request, pk):
          article = Article.objects.get(pk=pk)
          context = {
            'article' : article,
          }
          return render(request, 'articles/detail.html', context)
      ```
      ```html
        <!-- templates/articles/detail.html -->

        <h2>DETAIL</h2>
        <h3>{{ article.pk }}</h3>
        <hr>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <p>{{ article.created_at }}</p>
        <p>{{ article.updated_at }}</p>
        <hr>
        <a href="{% url 'articles:index' %}">[back]</a>
      ```
- 제목을 누르면 해당 글의 상세 페이지로 이동
    - ```html
        <!-- templates/articles/detail.html -->

        <h1>Articles</h1>
        <hr>
        {% for article in articles %}
          <p>글 번호: {{ article.pk }}</p>
          <a href="{% url 'articles:detail' article.pk %}">
            <p>{{ article.title }}</p>
          </a>
          <p>{{ article.content }}</p>
          <hr>
        {% endfor %}
      ```

<br/>

## CREATE
- Create 로직을 구현하기 위해 필요한 view함수
- new : 사용자의 입력을 받는 페이지를 렌더링
- create : 사용자가 입력한 데이터를 받아 DB에 저장

<br/>

### new 로직
- ```python
    # articles/urls.py

    urlpatterns = [
      path('new/', views.new, name = 'new'),
    ]

    # articles/views.py
    
    def new(request):
      return render(request, 'articles/new.html')
  ```
  ```html
    <!-- templates/articles/new.html -->

    <h1>NEW</h1>
    <form action="#" method="GET">
      <div>
        <label for="title">Title: </label>
        <input type="text" name="title" id="title">
      </div>
      
      <div>
        <label for="content">Content: </label>
        <textarea name="content" id="content"></textarea>
      </div>

      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
  ```
- new페이지로 이동할 수 있는 하이퍼 링크 작성
    - ```html
        <!-- templates/articles/index.html -->

        <h1>Articles</h1>
        <a href="{% url 'articles:new' %}">NEW</a>
        <hr>
      ```

<br/>

### create 로직
- ```python
    # articles/urls.py

    urlpatterns = [
      path('create/', views.create, name='create'),
    ]

    # articles/views.py

    def create(request):
      title = request.GET.get('title')
      content = request.GET.get('content')

      article = Article(title=title, content=content)
      article.save()

      return render(request, 'articles/create.html')
  ```
  ```html
    <!-- templates/articles/create.html -->

    <h1>게시글이 문제없이 작성 되었습니다.</h1>
  ```
  ```html
    <!-- templates/articles/new.html -->

    form의 action을 {% url 'articles:create' %}로 설정
  ```

<br/>

### 참고
- 시간 설정
  - settings.py/ TIME_ZONE = 'Asia/Seoul'
