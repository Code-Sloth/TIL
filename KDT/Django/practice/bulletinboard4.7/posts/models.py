from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    category = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)