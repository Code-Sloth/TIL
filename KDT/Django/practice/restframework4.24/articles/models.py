from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
import os

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()

    def articles_image_path(instance, filename):
      return f'images/{instance.title}/{filename}'

    image = ProcessedImageField(
        upload_to = articles_image_path,
        processors=[ResizeToFill(150,150)],
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True
    )

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(Article, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_post = Article.objects.get(id=self.id)
            if self.image != old_post.image:
                if old_post.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_post.image.path))
        super(Article, self).save(*args, **kwargs)
