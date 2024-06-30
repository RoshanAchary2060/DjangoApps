from django.shortcuts import render
import cx_Oracle

def bookPageView(request):
    conn = None
    cur = None
    bookrecords = []
    errormsg = ""
    context = {}
    try :
        
        conn = cx_Oracle.connect('oraclebatchjmc/jmc123@ROSHANPRO/xe')
        print('Connected successfully to the DB...')
        cur = conn.cursor()
        cur.execute("Select bookname, bookprice from allbooks")
        for name, price in cur:
            bookrecords.append({'bookname':name,'bookprice':price})
    except cx_Oracle.DatabaseError as ex:
        errormsg = "Problem in connecting to DB!"
    finally :
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
        if errormsg != "" :
            context = {'error':errormsg}
        else:
            context = {'records':bookrecords}
        return render(request, 'dbapp1/showbooks.html', context)
