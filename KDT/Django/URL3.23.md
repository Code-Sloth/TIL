# django URLs

<br/>

## 변수와 URL
- 템플릿의 많은 부분이 중복되고 URL의 일부만 변경되는 상황
  - ```python
      path('articles/1/', ...),
      path('articles/2/', ...),
      path('articles/3/', ...),
      path('articles/4/', ...),
      path('articles/5/', ...),
    ```
- Variable Routing
  - URL 일부에 변수를 포함시키는 것
  - 변수는 view함수의 인자로 전달 할 수 있음
  - ```python
      # urls.py
      path('articles/<int:num>', views.detail)
      path('hello/<str:name>', views.greeting)

      # views.py
      def detail(request, num):
        context = {
          'num' = num,
        }
        return render(request, 'articles/detail.html', context)
    ```
- Path Converters
  - URL 변수의 타입을 지정
  - str, int 등 5가지 타입 지원

<br/>

## App의 URL

<br/>

### App URL mapping
- 각 앱에 URL을 정의하는 것
- 프로젝트와 각각의 앱이 URL을 나누어 관리하여 주소 관리를 편하게 하기 위함
- 2번째 앱 생성 후 URL 주소가 겹친다면
- include()
  - 다른 URL들을 참조할 수 있도록 돕는 함수
  - URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URL로 전달
  - ```python
      # 별로 좋지 않은 방법

      from articles import views as articles_views
      from pages import views as pages_views

      urlpatterns = [
        ...,
        path('pages-index', pages_views.index),
      ]

      # 더 좋은 방법 / 각각의 앱 자체에서 URL을 관리

      from django.urls import path, include

      urlpatterns = [
        path('articles/', include('articles.urls')),
        path('pages/', include('pages.urls')),
      ]

      # articles/urls.py

      from django.urls import path
      from . import views # from . => 명시적 상대 경로

      urlpatterns = [
        ...,
      ]

      # pages/urls.py

      from django.urls import path
      from . import views

      urlpatterns = [
        ...,
      ]
    ```

<br/>

## URL 이름 지정
- 기존 articles/ 주소가 articles/index/로 변경됐기 때문에 모든 주소를 변경해야 하는 문제가 발생
- url tag
  - 주어진 URL패턴의 이름과 일치하는 절대 경로 주소를 반환
  - {% `url` 'url-name' arg1 arg2 %}
- ```python
    # articles/urls.py
    urlpatterns = [
      path('index/', views.index, name = 'index')
    ]
  ```
  ```html
    <!-- articles/index.html -->
    <a href = "{% url 'dinner' %}">dinner</a>
  ```

<br/>

## URL Namespace
- 서로 다른 앱 안에서 url name이 같으면 문제가 발생
- NoReverseMatch 에러 : 무조건 URL 관련 문제
- app_name 속성 지정
    - ```python
        # articles/urls.py

        app_name = 'articles'
        urlpatterns = [
          ...,
        ]

        # pages/urls.py

        app_name = 'pages'
        urlpatterns = [
          ...,
        ]
      ```  
  -   ```html
        <!-- articles/index.html -->
        <a href = "{% url 'articles:dinner' %}">dinner</a>
      ```

<br/>

## 참고
- app_name 지정 후 주의사항
  - app_name을 지정한 후에는 url태그에서 반드시 app_name:url_name형태로만 사용 가능
  - 그렇지 않으면 NoReverseMatch에러가 발생
- Trailing Slashes
  - django는 URL 끝에 '/'가 없다면 자동으로 붙임
  - django는 url설계 철학
    - 기술적인 측면에서, foo.com/bar 와 foo.com/bar/는 서로 다른 URL
  - 검색 엔진 로봇이나 웹 트래핑 분석 도구에서는 이 두 주소를 서로 다른 페이지로 봄
  - 그래서 django는 검색 엔진이 혼동하지 않게 하기 위해 사용
  - 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님
