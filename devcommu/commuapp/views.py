from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm ,FreeCommentForm, FreePostForm# forms.py의 PostForm객체 불러오기
from .models import Post, FreePost # models.py로 부터 쿼리셋형태로 Post목록가져옴

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
    comment_form = CommentForm() # forms.py의 CommentForm클래스
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글 저장
def new_comment(request, post_id) : 
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid() : 
        # 바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # models.py > class Comment > post 정보 확인하여 연결된 게시글 확인
        # 모델객체안에 필요한 정보를 채우고
        finished_form.post = get_object_or_404(Post, pk=post_id)
        # 저장한다.
        finished_form.save()
    return redirect('detail', post_id) # 댓글작성한 상세페이지로 이동

## 자유게시판 관련
# 자유게시판 보여주는 함수
def freehome(request):
    # posts = Post.objects.all()
    # FreePost객체를 모조리 띄워라
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})

# 자유게시판에서 글작성
def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        # 입력값이 정당하다면
        if form.is_valid():
            # 아직은 저장하지말고
            unfinished = form.save(commit=False)
            # user객체를 author에 담음. models.py FreePost클래스 참조
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})

# 자유게시판 상세페이지
def freedetail(request, post_id):
    # FreePost로 부터 가져옴
    post_detail = get_object_or_404(FreePost, pk=post_id)
    # 자유게시판 댓글 분류하기 위해 FreeCommentForm 활용
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})

# 
def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)