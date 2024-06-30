from django.shortcuts import render
from django.http import HttpResponse
from getuserdataapp.models import Emp

# Create your views here.
def home(request):
    return render(request, 'getuserdataapp/home.html')

def getdata(request):
    text = ''
    name = request.GET['name']
    try:
        empobj = Emp.objects.get(ename = name)
        context = {'e':empobj}
        return render(request,'getuserdataapp/show.html',context)
    except:
        text = f'No record of employee {name} found'
        return HttpResponse(text)
