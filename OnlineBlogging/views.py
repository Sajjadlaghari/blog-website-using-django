from django.shortcuts import render

# Create your views here.

def adminHome(request):
    return render(request,'admin/index.html')