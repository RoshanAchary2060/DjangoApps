from django.urls import path
from . import views

urlpatterns = [
    path('showdate/', views.showDate),
    path('showtime/', views.showTime),
]