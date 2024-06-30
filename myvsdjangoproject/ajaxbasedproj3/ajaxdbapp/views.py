from django.http import HttpResponse
from django.shortcuts import render
from ajaxdbapp.models import Emp

def home(request):
    return render(request, 'ajaxdbapp/home.html')

def getsal(request):
    name = request.GET['name']
    try:
        empobj = Emp.objects.get(ename=name)
        sal = empobj.sal
        text = f'Salary is {sal}'
    except(Emp.DoesNotExist):
        text=f'No record of employee {name} found!'
    except:
        text = "Sorry! Server is experiencing some issues. Try again later"
    finally:
        return HttpResponse(text)