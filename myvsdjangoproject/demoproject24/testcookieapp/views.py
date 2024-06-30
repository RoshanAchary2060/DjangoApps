from django.http import HttpResponse

# def test_session(request):
#     request.session.set_test_cookie()
#     request.session['myname'] = 'Roshan'
#     return HttpResponse('Testing session cookie')

def test_session(request):
    request.session.set_test_cookie()
    request.session['myname'] = 'Roshan'
    return HttpResponse('Testing session cookie')

# def test_delete(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         response = HttpResponse('Cookie test passed')
#     else:
#         response = HttpResponse('Cookie test failed')
#     return response

def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookie test passed")
    else:
        response = HttpResponse('Cookie test failed')
    return response