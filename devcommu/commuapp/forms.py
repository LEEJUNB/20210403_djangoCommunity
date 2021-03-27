from django import forms
from .models import Post # 모델기반이므로

# forms의 ModelForm을 상속받아 만듦
class PostForm(forms.ModelForm):
    class Meta : 
        model = Post
        fields = '__all__'