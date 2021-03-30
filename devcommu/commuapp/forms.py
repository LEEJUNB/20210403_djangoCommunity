from django import forms
from .models import Post, Comment # models.py의 클래스가져옴

# 게시글작성
# forms의 ModelForm을 상속받아 만듦
class PostForm(forms.ModelForm):
    class Meta : 
        model = Post # models.py의 Post객체
        fields = '__all__'

# 댓글작성
class CommentForm(forms.ModelForm):
    class Meta : 
        model = Comment # models.py의 Comment 객체
        fields = ['comment']