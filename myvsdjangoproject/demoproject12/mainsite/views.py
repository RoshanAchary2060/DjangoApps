from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return render(request, 'mainsite/home.html', {'course2':'Data Science'})

def aboutPageView(request):
    return render(request, 'mainsite/about.html')
