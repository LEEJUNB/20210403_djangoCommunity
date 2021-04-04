from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

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

# 자유게시판
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    # 작성자칼럼. 이는 유저객체를 참조함. User객체 참조하는 외래키
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 자유게시판 댓글
class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # FreePost를 참조
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment