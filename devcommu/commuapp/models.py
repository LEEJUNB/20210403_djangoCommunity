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

# 댓글
class Comment(models.Model) : 
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    # Post를 참조(foreign)함
    # 댓글달린 게시글이 삭제되면 참조객체도 삭제
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    # 게시글 작성시 DB에 title이 나오도록함
    def __str__(self) :
        return self.comment