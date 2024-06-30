from django.shortcuts import render

# Create your views here.
def showTrainers(request):
    return render(request, 'trainers/showtrainers.html')
