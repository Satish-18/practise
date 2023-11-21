from django.shortcuts import render,redirect
from .models import Contact, Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
#from xhtml2pdf import pisa
from django.views import View
from django.template.loader import get_template
from io import BytesIO






# Create your views here.
def index(request):

	return render(request, 'sas/index.html')

def about(request):
    #profiles = Profile.objects.all()
    return render(request,'sas/about.html')

def contact(request):
    thank = False
    if request.method =='POST':
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,desc=desc)
        thank = True
        contact.save()
    return render(request,'sas/contact.html',{'thank':thank})
'''

'''
def resume(request):
    
    user_profile = Profile.objects.get()
    
    template = get_template('sas/resume.html')
    html = template.render({'user_profile':user_profile})

    options ={
        'page-size':"Letter",
        'encoding':"utf-8",

    }

    pdf = result = BytesIO()
    pdf = pisa.pisaDocument(result)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response

def register(request):
    if request.method =='POST':
        '''
       
            # now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'sas/register.html',{'error':"User already exists"})
'''

        #get the post parameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs
        if len(username) > 10:
            return render(request,"sas/register.html",{'error':'username must be under 10 characters'})
           
        if not username.isalnum():
            return render(request,"sas/register.html",{'error':'username can only have letters and numbers'})

        if pass1 != pass2:
            return render(request,"sas/register.html",{'error':"password didn't matched with conform password"})
           

        #create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()  

    return render(request,'sas/register.html')

def Login(request):
    if request.method =='POST':
        #get the post parameter
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,"sas/login.html",{'error':'Invalid username or password'})
            

    return render(request,'sas/login.html')

def Logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request,'sas/profile.html')
