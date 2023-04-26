# 멀티 이미지

<br/>

## 멀티 이미지 첨부
- `$ pip install pillow`
- `$ pip install django-imagekit`

<br/>

### settings.py
- ```python
    INSTALLED_APPS = [
        ...,
        'imagekit',
    ]

    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = '/media/'
  ```

<br/>

### urls.py
- ```python
    from django.conf.urls.static import static
    from django.conf import settings

    urlpatterns = [
        ...,
    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

<br/>

### models.py
- ```python
    from django.db import models
    from imagekit.models import ProcessedImageField # 모델에서 사용할 때는 models에서 import
    from imagekit.processors import ResizeToFill
    import os
    from django.conf import settings

    class Post(models.Model):
        title = models.CharField(max_length=128)
        body = models.CharField(max_length=400)

        def delete(self, *args, **kwargs): # 게시글이 삭제될 때
            images = self.images_set.all() # 연결된 모든 이미지를
            for image in images: # 하나씩 꺼내서
                image.delete() # 삭제 // 2번으로 이동
            super(Post, self).delete(*args, **kwargs)

    class Images(models.Model): # 이미지 필드 생성
        post = models.ForeignKey(Post, on_delete=models.CASCADE) # 1:N

        def get_image_filename(instance, filename): # 저장될 때 글의 pk폴더 안에 저장
            return f'products/{instance.post.pk}/{filename}'
        
        image = ProcessedImageField(            # 이미지 필드 생성
            upload_to=get_image_filename,
            processors=[ResizeToFill(230,230)],
            format='JPEG',
            options={'quality' : 100},
            blank=True,
            null=True,
        )

        def delete(self, *args, **kargs): # 2번 //
            if self.image: # 연결된 이미지가 있으면
                os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name)) # 경로에서 이미지 삭제
                dir_path = os.path.dirname(os.path.join(settings.MEDIA_ROOT, self.image.name))
                if not os.listdir(dir_path): # 해당 경로 폴더 안에 아무것도 없을 때
                    os.rmdir(dir_path) # 폴더도 삭제
            super(Images, self).delete(*args, **kargs) # 다 완료 후 정상적으로 요청 객체 삭제
  ```

<br/>

### forms.py
- ```python
    class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['multiple'] = True # 여러 장의 이미지를 첨부할 수 있도록 설정
  ```

<br/>

### views.py
- ```python
    # index

    def index(request):
    posts = Post.objects.all()[::-1]
    context = {'posts':posts}
    return render(request, 'index.html',context)

    # create

    def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        files = request.FILES.getlist("image") # 리스트로 이미지들을 받음
        if form.is_valid():
            f = form.save()
            for i in files: # 리스트로 저장한 이미지들을 하나씩 꺼내서
                Images.objects.create(image=i, post=f) # Images모델에 추가
            return redirect('posts:index')
        else:
            print(form.errors)
    else:
        postform = PostForm()
        imageform = ImageForm()
    return render(request, 'create.html', {'postform': postform, 'imageform':imageform,})

    # update

    def update(request, product_pk):
    post = Post.objects.get(pk=product_pk)
    images = Images.objects.filter(post=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        files = request.FILES.getlist("image")
        if form.is_valid():
            f = form.save()

            if request.FILES.get('image'): # 요청받은 이미지가 있을 때
                if request.POST.get('sub') == '수정': # 수정을 클릭했으면
                    for i in images: # 기존에 존재하던 이미지들 삭제
                        i.delete()

            for i in files:
                Images.objects.create(image=i, post=f) # 새 이미지들 추가
            return redirect('posts:index')
        else:
            print(form.errors)
    else:
        postform = PostForm(instance=post)
        imageform = ImageForm() # instance로 여러 객체 입력이 불가능

    context = {
        'postform': postform, 
        'imageform':imageform, 
        'images':images # 대신 기존에 있던 이미지들을 전달
    }

    return render(request, 'update.html', context)
  ```
