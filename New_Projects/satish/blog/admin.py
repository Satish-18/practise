from django.contrib import admin

# Register your models here.
from . models import Post, Blogcomment

admin.site.register(Post)

admin.site.register(Blogcomment)
