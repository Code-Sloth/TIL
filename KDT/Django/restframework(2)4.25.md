# Django - Django rest framework 2

<br/>

## N:1 Relation
- 사전 준비
  - Comment 모델 작성 및 데이터베이스 초기화
    - ```python
        # articles/models.py

        class Comment(models.Model):
          article = models.ForeignKey(Article, on_delete=models.CASCADE)
          content = models.TextField()
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
      ```
    - `$ python manage.py makemigrations`
    - `$ python manage.py migrate`
    - `$ python manage.py loaddata articles.json comments.json`

<br/>

### GET - List
- 댓글 데이터 목록 조회
    - ```python
        # articles/serializers.py

        from .models import Article, Comment

        class CommentSerializer(serializers.ModelSerializer):
          class Meta:
              model = Comment
              fields = '__all__'

        # articles/urls.py

        urlpatterns = [
            ...,
            path('comments/', views.comment_list),
        ]

        # articles/views.py

        from .models import Article,Comment
        from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

        @api_view(['GET'])
        def comment_list(request):
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
      ```
    - GET http://127.0.0.1:8000/api/v1/comments/ 응답 확인
    - Postman에서도 확인

<br/>

### GET - Detail
- 단일 댓글 데이터 조회
    - ```python
        # articles/urls.py

        urlpatterns = [
            ...,
            path('comments/<int:comment_pk>/', views.comment_detail),
        ]

        # articles/views.py

        @api_view(['GET'])
        def comment_detail(request, comment_pk):
            comment = Comment.objects.get(pk=comment_pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
      ```
    - GET http://127.0.0.1:8000/api/v1/comments/1/ 응답 확인
    - Postman에서도 확인

<br/>

## POST
- 단일 댓글 생성
    - ```python
        # articles/urls.py

        urlpatterns = [
            ...,
            path('articles/<int:article_pk>/comments/', views.comment_create),
        ]

        # articles/views.py

        @api_view(['POST'])
        def comment_create(request, article_pk):
            article = Article.objects.get(pk=article_pk)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
      ```
    - save()메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
    - CommentSerializer를 통해 Serialize되는 과정에서 Parameter로 넘어온 article_pk에 해당하는 article객체를 추가적인 데이터를 넘겨 저장
    - ```python
        # articles/views.py

        if serializer.is_valid(raise_exception=True):
          serializer.save(article=article)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      ```
    - POST http://127.0.0.1:8000/api/v1/articles/1/comments/ 응답 확인
    - Postman에서도 확인
- 읽기 전용 필드 설정
  - read_only_fields를 사용해 외래 키 필드를 `읽기 전용 필드`로 설정
  - 읽기 전용 필드는 데이터를 전송하는 시점에 해당 필드를 유효성 검사에서 제외시키고, 데이터 조회 시에는 출력하도록 함
    - ```python
        # articles/serializers.py

        class CommentSerializer(serializers.ModelSerializer):
          class Meta:
              model = Comment
              fields = '__all__'
              read_only_fields = ('article',)
      ```
    - POST http://127.0.0.1:8000/api/v1/articles/1/comments/ 응답 재확인

<br/>

### DELETE & PUT
- ```python
    # articles/views.py

    @api_view(['GET'])
    def comment_detail(request, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)

        if request.method == 'GET':
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        
        elif request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
  ```
  - DELETE http://127.0.0.1:8000/api/v1/comments/21/ 응답 확인
  - PUT http://127.0.0.1:8000/api/v1/comments/1/ 응답 확인

<br/>

## N:1 역참조 데이터 조회
- 2가지 역참조 상황
  - 특정 게시글에 작성된 댓글 목록 출력
    - 기존 필드 `override`
      - PrimaryKeyRelatedField()
      - Nested relationships
  - 특정 게시글에 작성된 댓글의 개수 출력
    - 새로운 필드 추가

<br/>

### 특정 게시글에 작성된 댓글 목록 출력
- PrimaryKeyRelatedField()
  - 게시글조회 시 해당 게시글의 댓글 목록까지 함께 출력
  - Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음
    - ```python
        # articles/serializers.py

        class ArticleSerializer(serializers.ModelSerializer):
          comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
          class Meta:
              model = Article
              fields = '__all__'
      ```
  - models.py에서 related_name을 통해 역참조 매니저명 변경 가능
    - ```python
        # articles/models.py

        class Comment(models.Model):
          article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
        
        # articles/serializers.py

        class ArticleSerializer(serializers.ModelSerializer):
          comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
          # 위의 related_name과 동일한 이름 작성
          class Meta:
              model = Article
              fields = '__all__'
              # read_only_fields = ('comment_set',)
              # comment_set은 Article모델의 물리적 필드가 아니기 때문에 위처럼 작성 불가능
      ```
- Nested relationships
    - ```python
        # articles/serializers.py

        class CommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = '__all__'
                read_only_fields = ('article',)

        class ArticleSerializer(serializers.ModelSerializer):
            comment_set = CommentSerializer(many=True, read_only=True)
            class Meta:
                model = Article
                fields = '__all__'
      ```
    - 일부의 필드만 출력하고 싶을 때
      - ```python
          # articles/serializers.py

          class MyCommentSerializer(serializers.ModelSerializer):
              class Meta:
                  model = Comment
                  fields = ('id','content',)

          class ArticleSerializer(serializers.ModelSerializer):
              comment_set = MyCommentSerializer(many=True, read_only=True)
              class Meta:
                  model = Article
                  fields = '__all__'

          class CommentSerializer(serializers.ModelSerializer):
              class Meta:
                  model = Comment
                  fields = '__all__'
                  read_only_fields = ('article',)

          # 순서를 고려해야 하는 문제가 발생하기 때문에 수정
          # 여러 곳에서 사용하는 serializer면 밖에, 한 곳의 전용 serilizer면 안에 배치

          class ArticleSerializer(serializers.ModelSerializer):
            class MyCommentSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Comment
                    fields = ('id','content',)
            comment_set = MyCommentSerializer(many=True, read_only=True)
            class Meta:
                model = Article
                fields = '__all__'
        ```
  - 모델 관계 상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음
  - 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현 가능

<br/>

### 특정 게시글에 작성된 댓글 목록 출력
- Nested relationships
  - 새로운 필드 추가
    - ```python
        # articles/serializers.py

        class ArticleListSerializer(serializers.ModelSerializer):
            class Meta:
                model = Article
                fields = ('id', 'title', 'content',)

        class ArticleSerializer(serializers.ModelSerializer):
            class MyCommentSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Comment
                    fields = ('id','content',)

            comment_set = MyCommentSerializer(many=True, read_only=True)
            comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
            # source : 필드를 채우는 데 사용할 속성의 이름, 점 표기법을 사용하여 속성을 탐색할 수 있음

            class Meta:
                model = Article
                fields = '__all__'
      ```
- 주의 / 읽기 전용 필드 지정 이슈
  - 특정 필드를 override 혹은 추가한 경우 read_only_fields가 동작하지 않음
    - ```python
        # articles/serializers.py

        class ArticleSerializer(serializers.ModelSerializer):
            class MyCommentSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Comment
                    fields = ('id','content',)

            comment_set = MyCommentSerializer(many=True, read_only=True)
            comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

            class Meta:
                model = Article
                fields = '__all__'
                read_only_fields = ('comment_set','comment_count',)
                # 새로 추가한 필드들은 read_only_fields x
      ```

<br/>

## API 문서화
- Swagger
  - REST웹 서비스를 설계, 빌드, 문서화 등을 도와주는 오픈 소스 소프트웨어 프레임워크
  - `$ pip install drf-yasg`
  - INSTALLED_APPS에 `drf_yasg` 추가
  - https://drf-yasg.readthedocs.io/en/stable/readme.html 참고
    - ```python
        # 프로젝트 단위 urls.py

        from django.contrib import admin
        from django.urls import path, include

        from rest_framework import permissions
        from drf_yasg.views import get_schema_view
        from drf_yasg import openapi


        schema_view = get_schema_view(
          openapi.Info(
              title="Snippets API",
              default_version='v1',
              description="Test description",
              terms_of_service="https://www.google.com/policies/terms/",
              contact=openapi.Contact(email="contact@snippets.local"),
              license=openapi.License(name="BSD License"),
          ),
          public=True,
          permission_classes=[permissions.AllowAny],
        )


        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/v1/', include('articles.urls')),
            path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        ]
      ```
    - http://127.0.0.1:8000/swagger/ 확인

<br/>

## 참고
- Django shortcuts functions
  - render()
  - redirect()
  - get_object_or_404()
    - 모델 manager objects에서 get()을 호출하지만 해당 객체가 없을 땐 DoesNotExist 예외 대신 Http404를 raise함
      - ```python
          # articles/views.py

          from django.shortcuts import get_object_or_404

          article = Article.objects.get(pk=article_pk)
          comment = Comment.objects.get(pk=comment_pk)
          # 위 코드를 아래 코드로 변경
          article = get_object_or_404(Article, pk=article_pk)
          comment = get_object_or_404(Comment, pk=comment_pk)
        ```
  - get_list_or_404()
    - 모델 manager.objects에서 filter()의 결과를 반환하고 해당 객체 목록이 없을 땐 Http404를 raise함
      - ```python
          # articles/views.py

          from django.shortcuts import get_object_or_404,get_list_or_404

          article = Article.objects.all()
          comment = Comment.objects.all()
          # 위 코드를 아래 코드로 변경
          article = get_list_or_404(Article)
          comment = get_list_or_404(Comment)
        ```
  - 그 전에 존재하지 않는 게시글 조회 시 500상태코드였지만 현재는 404상태코드로 응답
  - 사용하는 이유
    - 클라이언트 입장에서 "서버에 오류가 발생하여 요청을 수행할 수 없다`(500)`"라는 원인이 정확하지 않은 에러를 마주하기 보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소이기 때문

<br/>

## 최종 코드
- ```python
    # 프로젝트 urls.py

    from django.contrib import admin
    from django.urls import path, include

    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi


    schema_view = get_schema_view(
      openapi.Info(
          title="Snippets API",
          default_version='v1',
          description="Test description",
          terms_of_service="https://www.google.com/policies/terms/",
          contact=openapi.Contact(email="contact@snippets.local"),
          license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=[permissions.AllowAny],
    )


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/v1/', include('articles.urls')),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

    # articles/models.py

    from django.db import models

    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

    # articles/serializers.py

    from rest_framework import serializers
    from .models import Article, Comment


    class ArticleListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title', 'content',)

    class ArticleSerializer(serializers.ModelSerializer):
        class MyCommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = ('id','content',)

        comment_set = MyCommentSerializer(many=True, read_only=True)
        comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

        class Meta:
            model = Article
            fields = '__all__'

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('article',)
    
    # articles/urls.py

    from django.urls import path
    from articles import views


    urlpatterns = [
        path('articles/', views.article_list),
        path('articles/<int:article_pk>/', views.article_detail),
        path('comments/', views.comment_list),
        path('comments/<int:comment_pk>/', views.comment_detail),
        path('articles/<int:article_pk>/comments/', views.comment_create),
    ]

    # views.py

    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    from rest_framework import status
    from .models import Article,Comment
    from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
    from django.shortcuts import get_object_or_404,get_list_or_404

    @api_view(['GET', 'POST'])
    def article_list(request):
        if request.method == 'GET':
            articles = get_list_or_404(Article)
            serializer = ArticleListSerializer(articles, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    @api_view(['GET', 'DELETE', 'PUT'])
    def article_detail(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        if request.method == 'GET':
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

        elif request.method == 'DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    @api_view(['GET'])
    def comment_list(request):
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def comment_detail(request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)

        if request.method == 'GET':
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        
        elif request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    @api_view(['POST'])
    def comment_create(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```