from django.shortcuts import render

# Create your views here.

def showFrontEnd(request):
    return render(request, 'courses/frontendcourses.html')

def showBackEnd(request):
    return render(request, 'courses/backendcourses.html')
