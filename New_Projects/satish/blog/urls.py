from django.urls import path
from . import views

urlpatterns = [
    #APIs to post a comment
    path("postcomment", views.postcomment,name="postcomment"),

    path("", views.blog,name="BlogHome"),  
    path("blogpost/<str:slug>", views.blogpost,name="blogpost"),

]