from django.urls import path
from . import views
urlpatterns = [
    path('show/', views.showForm),
    path('display/', views.showResponse),
]
