from django.db import models
from django.conf import settings

# 게시물 모음
class Post(models.Model) : 
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)