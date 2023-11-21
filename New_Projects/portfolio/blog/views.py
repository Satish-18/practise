from django.shortcuts import render,redirect
from .models import Post,Blogcomment
from django.core.paginator import Paginator
from blog.templatetags import extra

# Create your views here.



def blog_home(request):
    myposts = Post.objects.all() 
    paginator = Paginator(myposts,3)
    page = request.GET.get('page')
    myposts = paginator.get_page(page)
    context = {'myposts':myposts}

    return render(request,'blog/base.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Blogcomment.objects.filter(post=post,parent=None)
    replies = Blogcomment.objects.filter(post=post).exclude(parent=None)


    #Replying to the corresponding posts
    replayDict = {}
    for replay in replies:
        if replay.parent.sno not in replayDict.key():
            replayDict[replay.parent.sno]= [replay]
        else:
            replayDict[replay.parent.sno].append(replay)
    context = {'post':post,'comments':comments,'user':request.user, 'replayDict':replayDict}
    
    return render(request,'blog/blogpage.html',context)

def postcomment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.POST.get('user')
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')

        
        if parentSno == '':
            comment = Blogcomment(comment=comment,user=user,post=post)
            comment.save()
        else:
            parent = Blogcomment.objects.get(sno=parentSno)
            comment = Blogcomment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
    
    print(post.slug)

    redirect (f'/blog/blogpost/{post.slug}')



