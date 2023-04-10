from django.db import models
from django.conf import settings
import os

# Create your models here.

class Album(models.Model):
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

    def delete(self, *args, **kargs):
      if self.image:
          os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
      super(Album, self).delete(*args, **kargs)
