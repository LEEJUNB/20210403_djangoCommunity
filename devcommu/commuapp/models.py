from django.db import models
from django.conf import settings

# 게시물 모음
class Post(models.Model) : 
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # 게시글 작성시 DB에 title이 나오도록함
    def __str__(self) :
        return self.title