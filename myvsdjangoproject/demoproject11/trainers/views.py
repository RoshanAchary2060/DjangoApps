from django.shortcuts import render

# Create your views here.

def showFrontEnd(request):
    return render(request, 'trainers/frontendtrainers.html')

def showBackEnd(request):
    return render(request, 'trainers/backendtrainers.html')
