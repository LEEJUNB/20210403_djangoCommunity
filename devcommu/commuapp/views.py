from django.shortcuts import render
from .forms import PostForm # forms.py의 PostForm객체 불러오기

# Create your views here.
def home(request) :
    return render(request, 'index.html')

def postcreate(request) : 
    # request method가 POST
    if request.method == 'POST' :
        pass
        # 입력값 저장

    # request method가 GET
    # form 입력 html 띄우기
    else : 
        form = PostForm() # forms.py의 PostForm객체클래스
    return render(request, 'post_form.html', {'form':form})

    