from django.shortcuts import render, redirect
from django.contrib import auth # login,out을 위해 필수

def login(request) : 
    # request == POST
    # Login
    if request.method == "POST" : 
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
    
        # 실제 DB에 있는 회원이라면 로그인 진행
        if user is not None : 
            auth.login(request, user)
            return redirect('home')
        # 회원이 아니라면
        else :
            return render(request, 'bad_login.html')

    # request == GET
    else : 
        return render(request, 'login.html')
    # login html 띄우기