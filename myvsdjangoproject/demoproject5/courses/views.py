from django.shortcuts import render

# Create your views here.

def showFrontEnd(request):
    return render(request,'frontendcourses.html')

def showBackEnd(request):
    return render(request,'backendcourses.html')
