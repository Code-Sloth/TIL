from django.db import models
from django.conf import settings
import os

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie = models.CharField(max_length=50)
    
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    count_hit = models.IntegerField(default=0)
    count_like = models.IntegerField(default=0)

    def delete(self, *args, **kargs):
      if self.image:
          os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
      super(Review, self).delete(*args, **kargs)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    content = models.CharField(max_length=100)
    
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
