from django.shortcuts import render
from django.http import HttpResponse
from ajaxdbapp.models import Emp

# Create your views here.

def home(request):
    print('request received for home.html')
    all_emps = Emp.objects.all()
    print(len(all_emps))
    emp_list = []
    for e in all_emps:
        emp_list.append(e.empno)
    context = {'emp_list': emp_list}
    return render(request, 'ajaxdbapp/home.html', context)

def getempdetails(request): 
    print('request received for:', request.GET['eno'])
    text = ''
    eno = request.GET['eno']
    try :
        empobj = Emp.objects.get(empno  = eno)
        context = {'e': empobj}
        return render(request,'ajaxdbapp/showempdetails.html',context)
    except (Emp.DoesNotExist):
        text = f'No record of employee {eno} found'
        return HttpResponse(text)
