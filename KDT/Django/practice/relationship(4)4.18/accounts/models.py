from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def profile_image_path(instance, filename):
        return f'profile/{instance.username}/{filename}'

    image = ProcessedImageField(
        upload_to=profile_image_path,
        spec_id='User:image',
        processors=[ResizeToFill(200,200)],
        format='JPEG',
        options={'quality' : 90},
        blank=True,
        null=True,
    )
