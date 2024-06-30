from django.http import HttpResponse
from django.shortcuts import render
trackme = True

def visitcounter(request):
    if trackme:
        visits = request.COOKIES.get('lastvisit')
        if visits is None:
            visits = 1
        else:
            visits = int(visits) + 1
        response = render(request, 'hitcounterapp/showcounter.html',
                            {'visits':visits})
        response.set_cookie('lastvisit',str(visits),max_age=60)
    else:
        response = render(request, 'hitcounterapp/showcounter.html',
                            {'visits':0})
    return response

# def visitcounter(request):
    # visits = request.COOKIES.get('lastvisit')
    # if visits is None:
    #     visits = 1
    # else :
    #     visits = int(visits) + 1
    # response = render(request,'hitcounterapp/showcounter.html',{'visits':visits})
    # response.set_cookie('lastvisit',str(visits))
    # return response

def stoptracking(request):
    if request.COOKIES.get('lastvisit'):
        response = render(request,'hitcounterapp/stoptracking.html')
        response.delete_cookie('lastvisit')
        global trackme
        trackme =  False
        return response
    else:
        return HttpResponse('No cookies present<br><a href="/ck/">Go back</a')
