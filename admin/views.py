from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from blog.models import Blog
from blog.models import Category
from django.contrib import messages 
from django.contrib.auth.models import  User
from django.core.files.storage import FileSystemStorage



# Create your views here.

@login_required(login_url='login')
def adminHome(request):
    return render(request,'admin/index.html')

def adminForm(request):
    
    return render(request,'admin/forms-elements.html')

def adminTable(request):

    return render(request,'admin/table.html')

def addBlog(request):
    if request.method == "POST":
        user_id   = request.POST.get('user_id')
        cat_id   = request.POST.get('categori_id')
        user = User.objects.get(id=user_id)
        category = Category.objects.get(id=cat_id)
    
        blog=Blog()

        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        
        file_url = fss.url(file)

        blog.blog_title             = request.POST.get('title')
        blog.blog_description       = request.POST.get('description')
        blog.user_id                = user
        blog.category_id            = category
        blog.blog_featured_image    = file_url
        result = blog.save()
        messages.success(request, "Blog Added Successfully.")
        return redirect('/admin/view-blogs')
    categories = Category.objects.all()
    return render(request,'admin/add-new-blog.html',{'categories':categories})

def viewBlogs(request):

    blogs = Blog.objects.all()
    print(blogs)
    context = {'blogs':blogs}
    return render(request,'admin/view-blogs.html',context)   

def editBlog(request,id):
   
    blog = Blog.objects.get(id=id)
    return render(request,'admin/update-blog.html',{'blog':blog})


def updateBlog(request):
     if request.method == "POST":
        blog = Blog.objects.get(id=request.POST.get('id'))
        if len(request.FILES) != 0:
            upload = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
        else:
            blog = Blog.objects.get(id=request.POST.get('id'))
            file_url = blog.blog_featured_image
            

        blog.blog_title  = request.POST.get('title')
        blog.blog_description = request.POST.get('description')
        blog.blog_featured_image = file_url
        result = blog.save()
        messages.success(request, "Blog updated Successfully.")
        return redirect('/admin/view-blogs')

def ChangeBlogStatus(request,id):
    blog = Blog.objects.get(id=id)

    if(blog.status == 1):
        blog.status = 0
    else:
        blog.status = 1
    blog.save()

    messages.success(request, "Blog status updated Successfully.")
    return redirect('/admin/view-blogs')


def deleteBlog(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, "Blog Deleted Successfully.")
    return redirect('/admin/view-blogs')


def addCategory(request):

    if request.method == "POST":
        user_id   = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        category=Category()
        category.category_name  = request.POST.get('title')
        result = category.save()
        messages.success(request, "Category Added Successfully.")
        return redirect('/admin/view-all-categories')

    categories = Category.objects.all()
    return render(request,'admin/add-new-category.html',{'categories':categories})

def viewCategories(request):

    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'admin/view-categories.html',context)   

def editCategory(request,id):
   
    category = Category.objects.get(id=id)
    return render(request,'admin/update-category.html',{'category':category})


def updateCategory(request):
     if request.method == "POST":
        category = Category.objects.get(id=request.POST.get('id'))
       
        category.category_name  = request.POST.get('name')
    
        result = category.save()
        messages.success(request, "Category updated Successfully.")
        return redirect('/admin/view-all-categories')

def deleteCategory(request,id):
    blog = Category.objects.get(id=id)
    blog.delete()
    messages.success(request, "Category Deleted Successfully.")
    return redirect('/admin/view-all-categories')

def ChangeCategoryStatus(request,id):
    category = Category.objects.get(id=id)

    if(category.category_status == 1):
        category.category_status = 0
    else:
        category.category_status = 1
    category.save()

    messages.success(request, "Category status updated Successfully.")
    return redirect('/admin/view-all-categories')

def viewInActiveCategories(request):
    category = Category.objects.raw('select * from categories where category_status = 0')
    print(123)
    return render(request,'admin/view-inactive-categories.html',{'categories':category})


  
def Logout(request):
    logout(request)
    return redirect('login')


def Logout(request):
    
    logout(request)
    return redirect('login')