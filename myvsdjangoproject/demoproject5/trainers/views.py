from django.shortcuts import render

# Create your views here.

def showFrontEnd(request):
    return render(request,'frontendtrainers.html')

def showBackEnd(request):
    return render(request,'backendtrainers.html')
