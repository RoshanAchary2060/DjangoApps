from django.shortcuts import render

# Create your views here.

def showCourses(request):
    return render(request, 'appleveltemplates/frontendcourses.html')
