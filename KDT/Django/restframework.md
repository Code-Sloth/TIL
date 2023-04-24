# Django - Django rest framework

<br/>

## 개요
- HTTP Request Methods
  - 리소스(resource, 자원)에 대한 행위(수행하고자 하는 동작)를 정의
  - HTTP verbs라고도 함
  - 대표 HTTP request method
    - GET
      - 서버에 리소스의 표현을 요청
      - GET을 사용하는 요청은 데이터만 검색해야 함
    - POST
      - 데이터를 지정된 리소스에 제출
      - 서버의 상태를 변경
    - PUT
      - 요청한 주소의 리소스를 수정
    - DELETE
      - 지정된 리소스를 삭제
- HTTP response status codes
  - 특정 HTTP요청이 성공적으로 완료되었는지 여부를 나타냄
  - 응답은 5개의 그룹으로 나뉨
    - Informational responses`(100~199)`
    - Successful response`(200~299)`
    - Redirection messages`(300~399)`
    - Client error responses`(400~499)`
    - Server error responses`(500~599)`

<br/>

## REST API
- API (Application Programming Interface)
  - 애플리케이션과 프로그래밍으로 소통하는 방법
  - API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공
    - ex / 집의 가전 제품에 전기를 공급
    - 우리는 그저 가전 제품의 플러그를 소켓에 꽂으면 제품이 작동
    - 중요한 것은 우리가 가전 제품에 전기를 공급하기 위해 직접 배선을 하지 않음
    - 이는 매우 위험하면서도 비효율적인 일
- Web API
  - 웹 서버 또는 웹 브라우저를 위한 API
  - 현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 `Open API`를 활용하는 추세
  - 대표적인 Third Party Open API 서비스 목록
    - Youtube API
    - Naver Papago API
    - Kakao Map API
  - API는 다양한 타입의 데이터를 응답
    - HTML, JSON

<br/>

### REST(Representational State Transfer)
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 2000년 로이 필딩의 박사학위 논문에서 처음으로 소개된 후 네트워킹 문화에 널리 퍼짐
- 소프트웨어 아키텍쳐 디자인 제약 모음
- REST원리를 따르는 시스템을 RESTful 하다고 부름
- REST에서 자원을 정의하고 주소를 지정하는 방법
  - 자원의 식별
    - URL
  - 자원의 행위
    - HTTP Methods
  - 자원의 표현
    - 궁극적으로 표현되는 결과물
    - JSON으로 표현된 데이터를 제공
- REST API
  - REST라는 API디자인 아키텍처를 지켜 구현한 API

<br/>

## Response JSON
- 서버가 응답하는 것
  - 지금까지 Django로 작성한 서버는 사용자에게 페이지(html)만 응답하고 있었음
  - 하지만 사실 서버가 응답할 수 있는 것은 페이지뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
    - 페이지(html)를 응답하는 서버
    - 이제는 JSON데이터를 응답하는 서버로의 변환
    - Django는 더이상 Template부분에 대한 역할을 담당하지 않게 되며 Front-end와 Back-end가 분리되어 구성되게 됨
- 사전 준비
  - http://127.0.0.1:8000/api/v1/articles/ 요청 테스트
- Django REST framework(DRF)
  - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
    - https://www.django-rest-framework.org/
- python에서 json 응답 받기
  - ```python
      # sample.py

      import requests
      from pprint import pprint

      response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

      # json을 python 타입으로 변환
      result = response.json()

      print(type(result))
      # list

      pprint(result)
      # 딕셔너리들을 담은 리스트형태의 데이터들

      pprint(result[0])
      # 첫 번째 글의 딕셔너리형태

      pprint(result[0].get('title'))
      # 첫 번째 글의 title / 'Land probably you.'
    ```

<br/>

## Serialization (직렬화)
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 즉, 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정

<br/>

## DRF - Single Model
- 사전 준비
  - Postman 설치
    - https://www.postman.com/downloads/
  - Postman
    - API를 구축하고 사용하기 위한 플랫폼
    - API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공

<br/>

### ModelSerializer
- ModelSerializer 작성
  - articles/serializers.py 생성
    - ```python
        # articles/serializers.py

        from rest_framework import serializers
        from .models import Article

        class ArticleListSerializer(serializers.ModelSerializer):
            class Meta:
                model = Article
                fields = ('id', 'title', 'content',)
      ```
- ModelSerializer
  - 모델 필드에 해당하는 필드가 있는 Serializer클래스를 자동으로 만듦
    - Models정보에 맞춰 자동으로 필드를 생성
    - serializer에 대한 유효성 검사기를 자동으로 생성
    - .create()및 .update()의 기본 구현 메서드가 포함됨
- URL과 HTTP requests methods 설계
  - ||GET|POST|PUT|DELETE|
    |--|--|--|--|--|
    |articles/|전체 글 조회|글 작성|전체 글 수정|전체 글 삭제|
    |articles/1/|1번 글 조회|.|1번 글 수정|1번 글 삭제|

<br/>

### GET - List
- 게시글 데이터 목록 조회
    - ```python
        # articles/urls.py

        from django.urls import path
        from articles import views

        urlpatterns = [
            path('articles/', views.article_list),
        ]

        # articles/ views.py

        from rest_framework.response import Response
        from rest_framework.decorators import api_view

        from .models import Article
        from .serializers import ArticleListSerializer

        # 4. 해당 VIEW함수가 어떤 HTTP 요청 메서드를 허용하는지 결정하는 데코레이터 작성 (DRF의 VIEW함수에서 필수)
        @api_view(['GET'])
        def article_list(request):
            # 1. 제공할 게시글 목록 조회
            articles = Article.objects.all()

            # 2. 게시글 목록 데이터를 직렬화(serialization)
                # many => 단일객체가 아니라 쿼리셋이기 때문에 True로 설정
            serializer = ArticleListSerializer(articles, many=True)

            # 3. 직렬화된 데이터를 json데이터로 응답
            return Response(serializer.data)
      ```
    - http://127.0.0.1:8000/api/v1/articles/ 응답 확인
    - Postman에서 GET메서드로 url send확인
- api_view decorator
  - DRF view함수가 응답해야 하는 HTTP메서드 목록을 받음
  - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
  - DRF view함수에서는 필수로 작성

<br/>

### GET - Detail
- 단일 게시글 데이터 조회
- 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의
    - ```python
        # articles/serializers.py

        class ArticleSerializer(serializers.ModelSerializer):
          class Meta:
              model = Article
              fields = '__all__'
        
        # articles/urls.py

        from django.urls import path
        from articles import views

        urlpatterns = [
            ...,
            path('articles/<int:article_pk>/', views.article_detail),
        ]

        # articles/views.py

        from .serializers import ArticleListSerializer, ArticleSerializer

        @api_view(['GET'])
        def article_detail(request, article_pk):
            article = Article.objects.get(pk=article_pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
      ```
    - http://127.0.0.1:8000/api/v1/articles/1/ 응답 확인
    - Postman에서도 확인

<br/>

### POST
- 게시글 데이터 생성
- 요청에 대한 데이터 생성이 성공했을 경우 201 Created상태 코드를 응답하고 실패했을 경우 400 Bad request를 응답
    - ```python
        # articles/views.py

        from rest_framework import status

        @api_view(['GET','POST'])
        def article_list(request):
            if request.method == 'GET':
                # 1. 제공할 게시글 목록 조회
                articles = Article.objects.all()

                # 2. 게시글 목록 데이터를 직렬화(serialization)
                    # many => 단일객체가 아니라 쿼리셋이기 때문에 True로 설정
                serializer = ArticleListSerializer(articles, many=True)

                # 3. 직렬화된 데이터를 json데이터로 응답
                return Response(serializer.data)
            elif request.method == 'POST':
                # 사용자 데이터를 받아서 serializer로 직렬화
                serializer = ArticleSerializer(data=request.data)
                # 유효성 검사
                if serializer.is_valid():
                    serializer.save()
                    # 생성 성공 시 201 응답
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                # 생성 실패 시 400 응답
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      ```
    - POST http://127.0.0.1:8000/api/v1/articles/ 응답 확인
    - Postman에서도 확인 / Body 에서 확인
- raise_exception
  - is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception인자를 사용 가능
  - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환
  - ```python
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          # 생성 성공 시 201 응답
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      # 생성 실패 시 400 응답
      # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

<br/>

### DELETE
- 게시글 데이터 삭제
- 요청에 대한 데이터 삭제가 성공했을 경우 204 No Content상태 코드 응답
    - ```python
        articles/views.py

        @api_view(['GET','DELETE'])
        def article_detail(request, article_pk):
            article = Article.objects.get(pk=article_pk)

            if request.method == 'GET':
                serializer = ArticleSerializer(article)
                return Response(serializer.data)

            elif request.method == 'DELETE':
                article.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
      ```
    - DELETE http://127.0.0.1:8000/api/v1/articles/21/ 응답 확인
    - Postman에서도 확인 / Body 에서 확인

<br/>

### PUT
- 게시글 데이터 수정
- 요청에 대한 데이터 수정이 성공했을 경우 200 OK 상태 코드 응답
    - ```python
        # articles/views.py

        @api_view(['GET','DELETE','PUT'])
        def article_detail(request, article_pk):
            ...

            elif request.method == 'PUT':
                # 사용자 데이터를 받아서 serializer로 직렬화 + 기존 데이터
                serializer = ArticleSerializer(article, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      ```
    - PUT http://127.0.0.1:8000/api/v1/articles/1/ 응답 확인
    - Postman에서도 확인 / Body 에서 확인
