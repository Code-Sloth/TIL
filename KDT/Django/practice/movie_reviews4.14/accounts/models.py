from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os

# Create your models here.

class User(AbstractUser):

    def profile_image_path(instance, filename):
        return f'profiles/{instance.username}/{filename}'

    profile_image = models.ImageField(upload_to=profile_image_path, blank=True, null=True)
