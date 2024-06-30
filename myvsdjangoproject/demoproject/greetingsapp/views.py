from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcomePage(request):
    return HttpResponse('<h1><i><u>Welcome to Sharma Computer Academy</u></i></h1>')

def contactPage(request): # request object belongs to class HttpRequest
    return HttpResponse('<h1>You can contact us at scalive4u@gmail.com')