from django.shortcuts import render

# Create your views here.

def adminHome(request):
    return render(request,'admin/index.html')

def adminForm(request):
    
    return render(request,'admin/forms-elements.html')

def adminTable(request):

    return render(request,'admin/table.html')