from django.db import models

# Create your models here.
class AccountBook(models.Model):
    note = models.CharField(max_length=80) 
    description = models.TextField(null=True)
    category = models.CharField(max_length=20)   	
    amount = models.IntegerField(default=0)	
    date = models.DateField()		
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)