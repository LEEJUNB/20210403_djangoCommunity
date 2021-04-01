from django.shortcuts import render

def login(request) : 
    # request == POST
    if request.method == "POST" : 
        pass
    # Login

    # request == GET
    else : 
        return render(request, 'login.html')
    # login html 띄우기