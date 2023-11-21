from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/',views.blog_home,name='blog_home'),
    path("blog/blogpost/<str:slug>/",views.blogpost,name='blogpost'),
    path('blog/postComment',views.postcomment,name='postcomment'),
]