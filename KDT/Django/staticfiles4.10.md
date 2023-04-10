# Django - Static Files

<br/>

## 개요
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
- 이미지, JS, CSS파일 등
- 웹서버의 기본 동작
  - 특정 위치(URL)에 있는 자원을 요청(HTTP ruquest)받아서
  - 응답(HTTP response)을 처리하고 제공(serving)하는 것
  - 이는 자원에 접근 가능한 주소가 있다라는 의미
  - 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공함
  - 결국, 정적 파일을 제공하기 위한 경로(URL)가 있어야 함

<br/>

## Static Files 제공
- 경로에 따른 Static file 제공하기
  - 기본 경로 app/static/
  - 추가 경로 STATICFILES_DIRS
- 기본 경로 static file 제공하기
  - articles/static/articles/ 경로에 이미지 파일 배치
  - static tag를 사용해 이미지 파일에 대한 url 제공
      - ```html
          <!-- articles/index.html -->

          {% load static %}

          <img src="{% 'articles/sample-1.png' %}" alt="img">
        ```
- STATIC_URL
    - 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
    - 실제 파일이나 디렉토리가 아니며, URL로만 존재
    - 비어 있지 않은 값으로 설정한다면 반드시 /로 끝나야 함
    - ```python
        # settings.py

        STATIC_URL = '/static/'
        # 경로 : articles/static/
      ```
    - URL + STATIC_URL + 정적파일 경로
      - http://127.0.0.1:8000/static/articles/sample-1.png
- 추가 경로 static file 제공하기
    - 추가 경로에 이미지 파일 배치
    - ```python
        # settings.py

        # STATICFILES_DIRS : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
        STATICFILES_DIRS = [
          BASE_DIR / 'static',
        ]
        # 경로 : static/
      ```
    - ```html
        <!-- articles/index.html -->

        <img src="{% static 'sample-2.png' %}" alt="img">
      ```
    - css파일 등 static으로 가져올 수 있음
      - ```html
          <!-- articles/index.html -->

          <link rel='stylesheet' href="{% static 'style.css' %}">
        ```

<br/>

## Media Files
- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
- ImageField()
  - 이미지 업로드에 사용하는 모델 필드
  - 이미지 객체가 직접 저장되는 것이 아닌 이미지 파일의 경로 문자열이 DB에 저장
- ```python
    # settings.py

    # 미디어 파일들이 위치하는 디렉토리의 절대 경로
    MEDIA_ROOT = BASE_DIR / 'media'

    # MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성
    MEDIA_URL = '/media/'
  ```
- ```python
    # crud/urls.py

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
      ...,
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # 업로드 된 파일의 URL == settings.MEDIA_URL
    # 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
  ```

<br/>

## 이미지 업로드 및 제공하기
- 이미지 업로드
    - blank=True 속성을 작성해 빈 문자열이 저장될 수 있도록 설정
    - ```python
        # articles/models.py

        class Article(models.Model):
          image = models.ImageField(blank=True)
          def delete(self, *args, **kargs):
            if self.image:
                os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
            super(Articles, self).delete(*args, **kargs)
      ```
    - `$ pip install pillow`
    - `$ python manage.py makemigrations`
    - `$ python manage.py migrate`
    - ```html
        <!-- articles/create.html -->

        <form action="{% url 'articles:create %}" method="POST" enctype="multipart/form-data">
        </form>
      ```
    - ```python
        # articles/view.py

        def create(request):
          if request.method = "POST":
            form = ArticlesForm(request.POST, request.FILES)
      ```
    - ```html
        <!-- articles/detail.html -->

        {% load static %}

        {% if article.image %} <!-- 업로드 파일의 파일 이름 -->
          <img src="{{ article.image.url }}" alt="img"> <!-- 업로드 파일의 경로 -->
        {% else %}
          <img src="{% static 'articles/no-image.png' %}" alt="no-img"> <!-- 이미지가 없을 시, 대체 이미지 설정 -->
        {% endif %}
        <!-- 파일을 업로드 하지 않아도 오류가 나지 않게 처리 -->
      ```

<br/>

## 참고
- upload_to argument
  - ```python
      # 1 media/images/파일 저장
      image = models.ImageField(blank=True, upload_to='images/')

      # 2 media/2023/04/10/파일 저장
      image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

      # 3 media/images/username/파일 저장
      def articles_image_path(instance, filename):
        return f'images/{instance.user.username}/{filename}'
      
      image = models.ImageField(blank=True, upload_to=articles_image_path)
    ```
- Image Kit
  - ```python
      from imagekit.forms import ProcessedImageField
      from imagekit.processors import ResizeToFill

      class AlbumForm(forms.ModelForm):
          image = ProcessedImageField(
              spec_id='albums:image',
              processors=[ResizeToFill(100,100)], # 이미지를 100x100으로
              format='JPEG', # JPEG로 저장
              options={'quality' : 80}, # 화질을 낮춤
              required=False, # 이미지를 첨부하지 않아도 유효성 검사 통과
          )
    ```
