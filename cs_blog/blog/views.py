from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Comment
from django.contrib import messages

# Create your views here.
def home(request):
    post= Post.objects.all()
    context={'posts':post}
    return render(request,'blog/home.html',context)

def blog(request,slug):
        post=Post.objects.filter().first()
        context={'post':post}
        return render(request,'blog/blog.html',context)
        # return HttpResponse(f"<h1> This is blog section page : {slug}</h1>")

def HandleComment(request,slug):
    if request.method=='POST':
        name=request.POST['user']
        print(name)
        comment=request.POST['comment']
        print(comment)

        slug=request.POST['slug']
        print(slug)

        cm=Comment.objects.Create(name=name,comment=comment,slug=slug)
        cm.save()
        messages.success(request,"Data saved")
        return redirect('/blog/slug')
    else:
        return HttpResponse("404 not found")

        

