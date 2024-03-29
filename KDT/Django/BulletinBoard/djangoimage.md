# 장고 이미지 첨부

<br/>

### 모델 관리
- `$ pip install pillow`
  - Python Imaging Library
  - 사진을 처리할 수 있는 라이브러리 설치
- ```python
    # models.py

    from django.db import models
    from django.conf import settings
    import os

    class Todo(models.Model):
      author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE) # accounts쪽에서 만든 user정보와 연결

      def todos_image_path(instance, filename): # 이미지 저장 경로 설정 함수
        return f'images/{instance.author.username}/{filename}' # images/유저의 아이디/경로로 저장 *여기서 적은 author은 바로 위에서 만든 author

      image = models.ImageField(upload_to=todos_image_path,blank=True,null=True)

        def delete(self, *args, **kargs): # 글을 삭제하면 저장된 이미지도 삭제
          if self.image:
              os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
          super(Todo, self).delete(*args, **kargs)

        def save(self, *args, **kwargs): # 이미지를 수정하면 기존의 이미지를 삭제
          if self.id:
              old_post = Todo.objects.get(id=self.id)
              if self.img_file != old_post.img_file:
                  if old_post.img_file:
                      os.remove(os.path.join(settings.MEDIA_ROOT, old_post.img_file.path))
          super(Todo, self).save(*args, **kwargs)

    # null : 데이터베이스의 레코드가 해당 필드에 대해 null값을 가질 수 있음(비어있을 수 있음)

    # blank : 양식을 채울 때 필드를 비워 둘 수 있으며 Django가 유효성 검사 오류를 발생시키지 않음

    # delete : 글을 삭제했을 때 경로를 설정한 폴더에서도 image를 삭제
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
    # urls.py (!!!앱이 아닌 프로젝트의 url에 설정해야 함)

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

### 이미지 폼 설정
- `pip install django-imagekit` 이미지킷 설치
- settings.py의 INSTALLED_APPS에 'imagekit' 추가
- ```python
    # forms.py

    from imagekit.forms import ProcessedImageField
    from imagekit.processors import ResizeToFill

    class TodoForm(forms.ModelForm):
      image = ProcessedImageField(
          spec_id='albums:image',
          processors=[ResizeToFill(100,150)], # 100x150 픽셀로 설정
          format='JPEG', # JPEG파일로 저장
          options={'quality' : 90}, # 화질을 90%로 바꿈
          required=False, # 이미지 첨부를 하지 않아도 오류가 나지 않도록 설정
      )

      class Meta:
          model = Todo
          fields = ('image',)
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

