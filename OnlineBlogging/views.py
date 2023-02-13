from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from blog.models import Blog
from blog.models import Category

# Create your views here.

def adminHome(request):
    return render(request,'admin/index.html')

def home(request):

    blogs = Blog.objects.all()
    categories = Category.objects.all()

    return render(request,'web/index.html',{'blogs':blogs,'categories':categories})

def category(request):
    return render(request,'web/category.html')

def contactPage(request):
    return render(request,'web/contact.html')

def Login(request):

    if request.method == "POST":
        username     =request.POST.get('username')
        pass1  =request.POST.get('password')
        user = authenticate(request,username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('admin/home')
        else:
            messages.success(request, "Invalid credentials" )
            return redirect('login')
       
    else:
        return render(request,'web/login.html')