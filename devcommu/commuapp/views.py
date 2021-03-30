from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm # forms.py의 PostForm객체 불러오기
from .models import Post # models.py로 부터 쿼리셋형태로 Post목록가져옴

def home(request) :
    # 글목록 출력
    # posts는 쿼리셋 객체
    # posts = Post.objects.filter().order_by('date') # models.py의 date 오름차순
    posts = Post.objects.filter().order_by('-date') # models.py의 date 내림차순
    # posts = Post.objects.all() 
    return render(request, 'index.html', {'posts':posts})

def postcreate(request) : 
    # request method가 POST
    if request.method == 'POST' :
        # 입력값 저장
        form = PostForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('home') # 저장후 home으로 url이동

    # request method가 GET
    # form 입력 html 띄우기
    else : 
        form = PostForm() # forms.py의 PostForm객체클래스
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id) : 
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post_detail':post_detail})