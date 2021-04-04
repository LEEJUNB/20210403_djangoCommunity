from django.contrib import admin
from django.urls import path
from commuapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),

    path('freehome/', views.freehome, name='freehome'), # 자유게시판 목록
    path('freepostcreate', views.freepostcreate, name='freepostcreate'), # 자유게시판 글작성
    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'), # 자유게시판 상세페이지 
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'), 
]
