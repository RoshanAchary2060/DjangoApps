from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.showSearchPage),
    path('findbooks/', views.showResultPage),
]
