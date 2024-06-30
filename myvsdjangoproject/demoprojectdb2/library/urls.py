from django.urls import path
from . import views

urlpatterns = [
    path('ab/',views.addBookView),
    path('sb/',views.showBookView),
]
