from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createCookie),
    path('show/', views.getCookie),
    path('remove/', views.removecookie),
]
