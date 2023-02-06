from django.shortcuts import render

# Create your views here.

def adminHome(request):
    return render(request,'admin/index.html')

def home(request):
    return render(request,'web/index.html')

def category(request):
    return render(request,'web/category.html')

def contactPage(request):
    return render(request,'web/contact.html')