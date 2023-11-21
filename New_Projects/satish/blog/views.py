from django.shortcuts import render, redirect
from .models import Post, Blogcomment
from blog.templatetags import extras
from django.core.paginator import Paginator
# Create your views here.


def blog(request):
    myposts = Post.objects.all()
    paginator = Paginator(myposts,3)
    page = request.GET.get('page')
    myposts = paginator.get_page(page)
    context = {'myposts':myposts}
    return render(request, 'blog/blog.html',context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Blogcomment.objects.filter(post=post,parent=None)
    replies = Blogcomment.objects.filter(post=post).exclude(parent=None)
    
    #replying the corresponding replies
    replyDict = {}
    for reply in replies:
    	if reply.parent.sno not in replyDict.keys():
    		replyDict[reply.parent.sno] = [reply]
    	else:
    		replyDict[reply.parent.sno].append(reply)

    context = {'post':post,'comments':comments,'user':request.user,'replyDict':replyDict}
    return render(request, 'blog/blogpost.html',context)

def postcomment(request):
	if request.method == 'POST':
		comment = request.POST.get("comment")
		user = request.user
		postSno = request.POST.get("postSno") 
		post = Post.objects.get(sno=postSno)
		parentSno = request.POST.get("parentSno")

		if parentSno == "":
			comment = Blogcomment(comment=comment,user=user,post=post)
			comment.save()

		else:
			parent = Blogcomment.objects.get(sno=parentSno)
			comment = Blogcomment(comment=comment,user=user,post=post,parent=parent)
			comment.save()
		
	return redirect(f"/blog/{post.slug}")
	#return redirect()