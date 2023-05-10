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
  ```

<br/>

### venv/Lib/site-packages/ckeditor_uploader/urls.py
- ```python
    urlpatterns = [
        url(r'^upload/', views.upload, name='ckeditor_upload'),
        url(r'^browse/', never_cache(views.browse), name='ckeditor_browse'),
    ]
  ```
