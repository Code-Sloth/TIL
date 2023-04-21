import os
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_posts')
    select1_content = models.CharField(max_length=100)

    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_posts')
    select2_content = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

    def product_image_path(instance, filename):
        return f'posts/{instance.title}/{filename}'
    
    image1 = ProcessedImageField(
        upload_to=product_image_path,
        spec_id='albums:image',
        processors=[ResizeToFill(230,230)],
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True,
    )    
    image2 = ProcessedImageField(
        upload_to=product_image_path,
        spec_id='albums:image',
        processors=[ResizeToFill(230,230)],
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


