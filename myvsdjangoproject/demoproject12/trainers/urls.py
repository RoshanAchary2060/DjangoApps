from django.urls import path
from . import views

urlpatterns = [
    path('showt/', views.showTrainers, name='trainerslist'),
]
