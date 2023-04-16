from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(null=True)

    def profile_image_path(instance, filename):
        return f'profiles/{instance.username}/{filename}'
    
    profile_image = models.ImageField(upload_to=profile_image_path, blank=True)

    def delete(self, *args, **kargs):
        if self.profile_image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.profile_image.path))
        super(User, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_user = User.objects.get(id=self.id)
            if self.profile_image != old_user.profile_image:
                if old_user.profile_image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_user.profile_image.path))
        super(User, self).save(*args, **kwargs)
