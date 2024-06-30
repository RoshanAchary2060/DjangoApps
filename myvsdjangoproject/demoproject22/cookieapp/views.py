from http.client import responses
from django.http import HttpResponse

# def createCookie(request):
#     response = HttpResponse('Cookie Set In Browser')
#     response.set_cookie('favcolor', 'yellow',max_age=60)
#     return response

def createCookie(request):
    response = HttpResponse("Cookie Set in Browser");
    response.set_cookie('favcolor','yellow',max_age=60) # in seconds
    return response

# def getCookie(request):
#     color = request.COOKIES.get('favcolor')
#     response = HttpResponse(f'Your favourite color is {color}')
#     return response

def getCookie(request):
    # color = request.COOKIES['favcolor'] # COOKIES is a dictionary
    color = request.COOKIES.get('favcolor')
    response = HttpResponse(f'Your favcolor is {color}')
    return response

# def removecookie(request):
#     response = HttpResponse('Cookie deleted')
#     response.delete_cookie("favcolor")
#     return response

def removecookie(request):
    response = HttpResponse('Cookie deleted')
    response.delete_cookie('favcolor')
    return response