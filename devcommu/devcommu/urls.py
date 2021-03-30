from django.contrib import admin
from django.urls import path
from commuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('/postcreate', views.postcreate, name='postcreate'),
    path('/detail/<int:post_id>', views.detail, name='detail'),
]

