from django.shortcuts import render
from library.models import Book

def addBookView(request):
    b1 = Book(book_id=101, book_name='Let Us C',book_price=250,subject='C',pub_date='2001-01-15')
    b2 = Book(book_id=102, book_name='Mastering Python',book_price=450,subject='Python',pub_date='2014-10-21')
    b3 = Book(book_id=103, book_name='Python Projects',book_price=350,subject='Python',pub_date='2016-04-09')
    b1.save()
    b2.save()
    b3.save()
    total = Book.objects.count()
    return render(request, 'library/showresult.html', {'bookcount':total})

def showBookView(request):
    booklist = Book.objects.all()
    return render(request, 'library/showbooks.html', {'booklist':booklist})
