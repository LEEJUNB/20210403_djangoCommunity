from django import forms
from .models import Post, Comment, FreePost, FreeComment # models.py의 클래스가져옴

# 게시글작성
# forms의 ModelForm을 상속받아 만듦
class PostForm(forms.ModelForm):
    class Meta : 
        model = Post # models.py의 Post객체
        fields = '__all__'
    
    # HTML에 속성을 넣고 싶다면 init으로 가능하다
    # Bootstrap클래스를 wiget으로 지정
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }

# 댓글작성
class CommentForm(forms.ModelForm):
    class Meta : 
        # 모델은 Comment 기반으로 제작
        model = Comment # models.py의 Comment 객체
        fields = ['comment']
        
    # HTML에 속성을 넣고 싶다면 init으로 가능하다
    # Bootstrap클래스를 wiget으로 지정
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }

# Model폼 기반
class FreePostForm(forms.ModelForm):
    class Meta:
        
        # 모델은 FreePost 기반으로 제작
        model = FreePost
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(FreePostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class FreeCommentForm(forms.ModelForm):
    class Meta:
        # 모델은 FreeComment 기반으로 제작
        model = FreeComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }