from django.db import models
from django.conf import settings
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils import timezone
from datetime import timedelta,datetime

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_products')
    title = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
    delivery_date = models.DateField()
    star = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False)
    count = models.IntegerField(default=1)
    
    def product_image_path(instance, filename):
        return f'products/{instance.title}/{filename}'
    
    urls = models.TextField(default='')
    image = models.ImageField(blank=True, upload_to=product_image_path, null=True)

    category_Choices = (('패션의류/잡화', '패션의류/잡화'), ('뷰티', '뷰티'), ('식품', '식품'), ('주방용품', '주방용품'), ('생활용품', '생활용품'))
    category = models.CharField(max_length=20, choices=category_Choices)

    def count_likes_user(self):
        return self.like_users.count()
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def product_image_path(instance, filename):
        return f'products/{instance.product.title}/{filename}'

    product_img = ProcessedImageField(
        upload_to=product_image_path,
        spec_id='albums:image',
        processors=[ResizeToFill(230,230)],
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True,
    )


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # def comment_image_path(instance, filename):
    #     return f'comments/{instance.title}/{filename}'
    
    # comment_img = models.ImageField(blank=True,null=True, upload_to=comment_image_path)

    star = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return self.strftime('%Y-%m-%d')

class CommentImage(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_img')

    def comment_image_path(instance, filename):
        return f'comments/{instance.comment.title}/{filename}'
    
    comment_img = ProcessedImageField(
        upload_to=comment_image_path,
        spec_id='albums:image',
        processors=[ResizeToFill(230,230)],
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True,
    )

    
