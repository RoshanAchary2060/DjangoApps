from django.http import HttpResponse
from django.shortcuts import render
from myform.models import Book

# Create your views here.
def searchFormView(request):
    return render(request, 'myform/searchform.html')

def showBooks(request):
    # if request.GET['subject'] != '':
    if request.GET.get('subject')!= '':
        subj = request.GET['subject']
        books = Book.objects.filter(subject=subj)
        return render(request, 'myform/showbooks.html',{'books':books, 'query':subj})
    else:
        return render(request, 'myform/searchform.html', {'error':True})
    
def singleView(request):
    error = False
    size = 0
    if 'subject' in request.GET:
        subj = request.GET['subject']
        if subj == '':
            error = True
        elif len(subj)>= 10 :
            error = True
            size = 1
        else:
            books = Book.objects.filter(subject=subj)
            return render(request, 'myform/showbooks.html', {'books':books, 'query':subj})
    return render(request,'myform/searchform.html',{'error':error, 'size':size})