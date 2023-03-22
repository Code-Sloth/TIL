# Django Template

<br/>

## django template system
- 데이터 표현을 제어하면서, 표현과 관련된 로직을 담당
- HTML 컨텐츠를 변수 값에 따라 바꾸려면
  - ```html
    <body>
      <h1>Hello, {{ name }}</h1>
    </body>
    ```
  - ```python
      def index(request):
        context = {
          'name' : 'Sophia',
        }
        return render(request, 'articles/index.html', context)
      
    ```

<br/>

## DTL (Django Template Language)
- Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템
- Syntax(Variable, Filters, Tags, Comments)
- Variable
  - view함수에서 render함수의 세번째 인자로 딕셔너리 타입으로 넘겨 받을 수 있음
  - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
  - dot(.)를 사용하여 변수 속성에 접근 가능
  - ```html 
      {{variable}} 
    ```
- Filters
  - 표시할 변수를 수정할 때 사용
  - chained가 가능하며 일부 필터는 인자를 받기도 함
  - 약 60개의 built-in template filters를 제공
  - ```html
      {{ variable|filter }}
    ```
- Tags
  - 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
  - 일부 태그는 시작과 종료 태그가 필요
  - 약 24개의 built-in template tags를 제공
  - ```html
      {% tag %}
    ```
- Comments
  - DTL에서의 주석 표현
  - ```html
      {# name #}
    ```

<br/>

## 템플릿 상속
- 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
- ```html
    <!-- skeleton 템플릿 -->

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
      <style>
        {% block style %}
        {% endblock style %}
      </style>
    </head>
    <body>
      {% block content %}
      {% endblock content %}

      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    </body>
    </html>
  ```
- ```html
    <!-- 하위 템플릿 -->
    {% extends 'base.html' %}

    {% block style %}

        span {color: crimson}
        h1 {text-align: center}

    {% endblock style %}

    {% block content %}

      <h1>오늘의 추천 저녁 메뉴는 <span>{{ foods }}</span>입니다.</h1>
      
    {% endblock content %}
  ```
- extends : 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
- block : 하위 템플릿에서 재정의(overridden)할 수 있는 블록을 정의

<br/>

## 요청과 응답
- 데이터를 보내고 가져오기
  - HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기
  - ```html
      <form action="/catch/" method="GET">
        <input type="text" name="message">
        <input type="submit">
      </form>
    ```
- form element
  - 사용자로부터 할당된 데이터를 서버로 전송
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 제공
- action & method
  - 데이터를 어디(action)로 어떤 방식(method)으로 보낼지 정함
  - action
    - 입력 데이터가 전송될 URL을 지정
    - 만약 이 속성을 지정하지 않으면 현재 form이 있는 페이지의 URL로 보내짐
  - method
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP request methods(GET, POST)를 지정
- input element
  - 사용자의 데이터를 입력 받을 수 있는 요소
  - type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
- name
  - input의 핵심 속성
  - 데이터를 제출했을 때, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근할 수 있음
- Query String Parameters
  - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 넘기는 방법
  - 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성, 기본 URL과 ?로 구분됨
  - ex
    - https://host:port/path?`key=value`&`key=value`


<br/>

## 요청과 응답 활용
- 모든 요청 데이터는 HTTP request 객체에 들어있음
```python
# views.py

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(type(request))
    # print(dir(request))
    # print(request.GET.get('message'))

    data = request.GET.get('message')
    
    context = {
        'data' : data,
    }
    return render(request, 'articles/catch.html', context)
```
```html
<!-- throw.html -->
{% extends 'articles/base.html' %}

{% block content %}
  <h1>Throw</h1>
  <form action="/catch/" method="GET">
    <input type="text" name="message">
    <input type="submit">
  </form>
{% endblock content %}

<!-- catch.html -->
{% extends 'articles/base.html' %}

{% block content %}
  <h1>Catch</h1>
  <h1>{{ data }}를 받았습니다!</h1>
{% endblock content %}
```


<br/>

## 참고
- 추가 템플릿 경로 지정
  - settings.py => 'DIRS': [BASE_DIR / '추가 경로 입력']
- DTL 주의 사항
  - Python처럼 일부 프로그래밍 구조(if, for등)을 사용할 수 있지만 명칭을 그렇게 설계했을 뿐이지 Python 코드로 실행되는 것이 아니며 Python과 아무 관련이 없음
  - 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심
  - 되도록 view.py에서 로직을 처리