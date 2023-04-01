# 장고 이미지 첨부

<br/>

### 모델 관리
- `$ pip install pillow`
  - Python Imaging Library
  - 사진을 처리할 수 있는 라이브러리 설치
- ```python
    # models.py

    image = models.ImageField(upload_to='image/', null=True, blank=True)

    # 이미지필드로 모델을 만들고 기본 경로를 image폴더 안으로 지정

    # null : 데이터베이스의 레코드가 해당 필드에 대해 null값을 가질 수 있음(비어있을 수 있음)

    # blank : 양식을 채울 때 필드를 비워 둘 수 있으며 Django가 유효성 검사 오류를 발생시키지 않음
  ```

<br/>

### 이미지가 저장될 공간 설정
- ```python
    # settings.py

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

    # Django는 MEDIA_ROOT에서 지정한 디렉토리에 이미지 파일을 저장하고, 이미지를 웹 페이지에 표시하려면 MEDIA_URL에 지정된 URL을 사용하여 이미지 파일에 연결
  ```
  ```python
    # urls.py (앱이 아닌 프로젝트의 url에 설정해야 함)

    from django.conf.urls.static import static
    from django.conf import settings

    urlpatterns = [
      ...
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    # static 함수는 지정된 디렉토리에서 파일을 제공하는 URL패턴을 생성

    # document_root는 Django에 미디어 파일을 찾을 위치를 알려줌

    # static 함수를 호출하면 settings.MEDIA_URL로 시작하는 모든 URL과 일치하는 패턴을 추가, 일치하는 URL이 요청되면 Django는 settings.MEDIA_ROOT에 지정된 디렉토리에서 해당 파일을 제공
  ```

<br/>

### 이미지 첨부
- ```html
    <!-- new.html -->

    <form action="{% url 'todos:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
      <input type="file" name="image">
    </form>

    <!-- 파일을 첨부할 때, enctype="multipart/form-data"로 인코딩을 해줘야 함 -->
  ```
  ```python
    # views.py

    def create(request):
    if request.method == 'POST':
        todo.image = request.FILES.get('image')
        todo.save()
        return redirect('todos:detail', todo.pk)
    return redirect('todos:index')
    
    # request.FILES['image']로 저장하면 첨부한 이미지가 없으면 오류가 발생하므로 get을 통해 저장
  ```
  ```html
    <!-- detail.html -->

    {% if todo.image %}
      <img src="{{ todo.image.url }}" alt="{{ todo.title }}">
    {% endif %}

    <!-- 데이터에 저장된 이미지가 없을 때 url을 가져오려고 하면 오류가 발생하기 때문에 조건문으로 미리 판별 후 출력 -->
  ```