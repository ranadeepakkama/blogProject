from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default= datetime.now)
    deleted_at = models.DateTimeField(default= datetime.now)

    def __str__(self):
        return self.title

