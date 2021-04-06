from django.shortcuts import render, redirect
from django.contrib import auth # login,out을 위해 필수
from django.contrib.auth.models import User # 유저객체에 새로 생성된 유저 아이디 데이터 추가

def login(request) : 
    # request == POST
    # Login
    if request.method == "POST" : 
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
    
        # 실제 DB에 있는 회원이라면 로그인 진행
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # 회원이 아니라면
        else: 
            return render(request, 'bad_login.html')

    # request == GET
    else:
        return render(request, 'login.html')
        
def logout(request) : 
    auth.logout(request)
    return redirect('home')

# 가입
def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입 새로운 유저 객체 만들기
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')