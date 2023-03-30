# ORM - DELETE, UPDATE

<br/>

## Method
- redirect()
  - 인자에 작성된 주소로 다시 요청을 보냄
  - ```python
      from django.shortcuts import render, redirect

      def create(request):
        title = request.GET.get('title')
        content = request.GET.get('content')
        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:detail', article.pk)
    ```
- HTTP
  - 네트워크 상에서 데이터를 주고 받기위한 약속

<br/>

### HTTP request methods
- 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
- GET
  - 특정 리소스를 조회하는 요청
  - GET으로 데이터를 전달하면 `Query String` 형식으로 보내짐
  - https://127.0.0.1:8000/articles/create/?title=제목&content=내용
- POST
  - 특정 리소스에 `변경사항`을 만드는 요청
  - POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐
- HTTP response status code
  - 특정 HTTP 요청이 성공적으로 완료되었는지 알려줌
  - 5개의 그룹으로 나뉨(1xx,2xx,3xx,4xx,5xx)
  - 403 Forbidden
    - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
    - `CSRF` (Cross-Site-Request-Forgery)
      - 사용자가 자신의 의지와 무관하게 사용자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 `공격 방법`
    - Security Token(`CSRF Token`)
      - 대표적인 CSRF 방어 방법
      - 서버는 사용자 입력 데이터에 임의의 `난수 값(token)`을 부여
      - 매 요청마다 해당 token을 포함시켜 전송시키도록 함
      - 이후 서버에서 요청을 받을 때마다 전달된 token이 `유효`한지 검증
      - POST Method는 데이터베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것
      - ```html
          <!-- templates/articles/new.html -->

          <h1>NEW</h1>
          <form action="{% url 'articles:create' %}" method='POST'>
            {% csrf_token %}
            ...
        ```

<br/>

## DELETE
- ```python
    # articles/urls.py

    urlpatterns = [
      path(<int:pk>/delete/, views.delete, name='delete'),
    ]

    # aritlces/views.py

    def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('articles:index')
  ```
  ```html
    <!-- articles/detail.html -->

    <body>
      <h2>DETAIL</h2>
      ...
      <hr>
      <form action="{% url 'articles:delete' article.pk%}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
      <a href="{% url 'articles:index' %}">[back]</a>
    </body>
  ```

<br/>

## UPDATE
- edit
    - 사용자의 입력을 받는 페이지를 렌더링
    - ```python
        # articles/urls.py

        urlpatterns = [
          path('<int:pk>/edit/', views.edit, name='edit')
        ]

        # articles/views.py

        def edit(request, pk):
          article = Article.objects.get(pk=pk)
          context = {
            'article' : article,
          }
          return render(request, 'articles/edit.html', context)
      ```
      ```html
        <!-- articles/edit.html -->

        <h1>EDIT</h1>
        <form action="#" method="POST">
          {% csrf_token %}
          <div>
            <label for="title">Title: </label>
            <input type="text" name="title" id="title" value="{{ article.title }}">
          </div>
          <div>
            <label for="content">Content: </label>
            <textarea name="content" id="content">{{ article.content }}</textarea>
          </div>
          <input type="submit">
        </form>
        <hr>
        <a href="{% url 'articles:index' %}">[back]</a>
      ```
    - edit 페이지로 이동하기 위한 하이퍼링크 작성
      - detail에 `'articles:edit' article.pk` 의 a링크 추가
- update
    - 사용자가 입력한 데이터를 받아 DB에 저장
    - ```python
        # articles/urls.py

        urlpatterns = [
          path('<int:pk>/update/', views.update, name='update')
        ]

        # articles/views.py

        def update(request, pk):
          article = Article.objects.get(pk=pk)
          article.title = request.POST.get('title')
          article.content = request.POST.get('content')
          article.save()
          return redirect('articles:detail', article.pk)
      ```
    - articles/edit.html에서 form의 action을 `'articles:update' article.pk` 로 설정

<br/>

## 참고
- HTTP request methods를 활용한 효율적인 URL 구조
  - (UPDATE) articles/1/ 게시글 수정
  - (DELETE) articles/1/ 게시글 삭제
