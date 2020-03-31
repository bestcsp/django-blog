from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Image
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')
    
def contact(request):

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<3:
            messages.error(request,'Fill the form correctly')
        else:
            contact= Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Contact Saved')

    
    
    return render(request,'home/contact.html')

def Search(request):
    # posts=Post.objects.all()
    query=request.GET['search']
    if len(query)>80:
        posts=Post.objects.none()
    else:
        postsTitle=Post.objects.filter(title__icontains=query)
        postsContent=Post.objects.filter(content__icontains=query)
        posts=postsTitle.union(postsContent)
        context={'posts':posts,'query':query}
    if posts.count()==0:
        messages.warning(request,"Search wisely")
    return render(request,'home/search.html',context)
    # return HttpResponse("this is search",context)

def HandleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass']
        cpassword=request.POST['pass1']
        

        #check validity
        if User.objects.filter(username=username).exists():
            messages.error(request,"This username already exists")
            return redirect('/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"This email already exists")
            return redirect('/')

        if password != cpassword:
            messages.error(request,"both password are not same")
            return redirect('/')
        if len(password)<8:
            messages.error(request,"Password is less than 8 character ,try again")
            return redirect('/')
        
        if not(password.isalnum()):
            messages.error(request,"Password is not alphanumeric")
            return redirect('/')  
        

        #save user
        user=User.objects.create_user(username,email,password,first_name=fname,last_name=lname)
        image=request.POST['image']
        age=request.POST['age']

        v=Image(image=image,age=age,user=user)
        v.save()
        messages.success(request,"Your account is successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 page not found")

#login handle
def HandleLogin(request):
    if request.method=='POST':

        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "User is not authorised")
            return redirect('/')
    else:
        return HttpResponse("login with username and password")


def HandleLogout(request):
    logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('/')

def profile(request):

    return render(request,'blog/profile.html')
    





