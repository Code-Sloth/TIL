# CK Editor

<br/>

### 터미널
- `$ pip install django-ckeditor`

<br/>

### settings.py
- ```python
    INSTALLED_APPS = [
        ...
        'ckeditor',
        'ckeditor_uploader',
    ]

    CKEDITOR_UPLOAD_PATH = 'uploads/'
    CKEDITOR_IMAGE_BACKEND = "pillow" 
  ```

<br/>

### 프로젝트 단위 urls.py
- ```python
    urlpatterns = [
        ...
        path('ckeditor/', include('ckeditor_uploader.urls')),
        path(r'^upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
        path(r'^browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

<br/>

### models.py
- ```python
    from ckeditor_uploader.fields import RichTextUploadingField
 
    class Post(models.Model):
        ...,
        content = RichTextUploadingField(blank=True,null=True)
  ```

<br/>

### html
- ```html
    <!-- create -->

    <form method ="POST">
      {% csrf_token %}
      {{form.media}}    
      {{form.as_p}}
      <input type="submit">
    </form>

    <!-- detail -->
    {{ post.content|safe }}

    <script src="https://cdn.ckeditor.com/ckeditor5/34.0.0/classic/ckeditor.js"></script>
    <script src="https://cdn.ckeditor.com/ckeditor5/34.0.0/classic/translations/ko.js"></script>
    <script>
      ClassicEditor.create( document.querySelector( '#editor' ), {
        language: "ko"
      } );
    </script>
  ```

<br/>

### venv/Lib/site-packages/ckeditor_uploader/urls.py
- ```python
    # 프로젝트 단위 urls에 r'^upload/' 부분들 없으면 아래에 추가
    urlpatterns = [
        re_path(r'^upload/', views.upload, name='ckeditor_upload'),
        re_path(r'^browse/', never_cache(views.browse), name='ckeditor_browse'),
    ]
  ```
