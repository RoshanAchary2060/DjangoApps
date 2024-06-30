from django.http import HttpResponse

def showInfo(request):
    browser = request.META['HTTP_USER_AGENT']
    if 'Chrome' in browser:
        str = 'Chrome'
    elif 'Firefox' in browser:
        str = 'Firefox'
    else :
        str = 'unknown browser'
    ipaddr = request.META['REMOTE_ADDR']
    return HttpResponse(f"Your browser:{str}<br>Your ip:{ipaddr}")

# def showInfo(request):
#     browser = request.META['HTTP_USER_AGENT']
#     str = '<table border="2"'
#     str += "<tr><th>Key</th><th>Value</th></tr>"
#     for k, v in request.META.items():
#         str += f"<tr><td>{k}</td><td>{v}</td></tr>"
#     str += "</table>"
#     return HttpResponse(f"{str}")
