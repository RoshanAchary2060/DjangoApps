from . import views
from django.urls import path

urlpatterns = [
    path('ck/', views.visitcounter),
    path('stop/',views.stoptracking),
]
