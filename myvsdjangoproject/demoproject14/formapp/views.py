from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from formapp.models import Books

# Create your views here.

def showSearchPage(request):
    return render(request, 'formapp/show_search_page.html')

def showResultPage(request):
    subj = request.GET['subject']
    if subj != '':
        booklist = Books.objects.filter(subject=subj)
        return render(request, 'formapp/show_search_result.html', {'booklist':booklist})
    # else:
    #     return HttpResponse('<h2>Please input subject</h2>')
    else:
        return render(request, 'formapp/show_search_page.html', {'error':True})
