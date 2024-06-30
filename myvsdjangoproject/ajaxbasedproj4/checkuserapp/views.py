from django.http import HttpResponse
from django.shortcuts import render
from checkuserapp.models import Users
# Create your views here.

def checkuser(request):
    text = ''
    name = request.GET['username']
    try :
        empobj = Users.objects.get(username=name)
        text = 'fail'
    except(Users.DoesNotExist):
        text = 'pass'
    except:
        print('Error in server side')
    finally:
        return HttpResponse(text)


def home(request):
    return render(request,'checkuserapp/home.html')
