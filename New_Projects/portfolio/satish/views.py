from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Contact

def home(request):
    return render(request,'satish/basic.html')
def satish_home(request):
    return render(request,'satish/base.html')

def contact(request):
    thank = False
    if request.method =='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,desc=desc)
        thank = True
        contact.save()
    return render(request,'satish/contact.html',{'thank':thank,'msg':"Thanks for reaching to us we'll get to you soon" })

def projects(request):
    return render(request,'satish/project.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #checking for errorneous input
        if len(username) > 10:
            return render(request,'satish/sign-up.html',{'error':'username must be under 10 characters'})
        if not username.isalnum():
            return render(request,'satish/sign-up.html',{'error':'username can only have letters and numbers'})
        if pass1 != pass2:
            return render(request,'satish/sign-up.html',{'error':"password didn't matched"})    

        #create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
    return render(request,'satish/sign-up.html',{})

def Login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            return redirect('satish_home')
        else:
            return render(request,"satish/login.html",{'error':'Invalid username or password'})
          

    return render(request,'satish/login.html')

def Logout(request):
    logout(request)
    return redirect('satish_home')


