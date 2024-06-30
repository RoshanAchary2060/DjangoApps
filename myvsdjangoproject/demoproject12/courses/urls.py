from django.urls import path
from . import views

urlpatterns = [
    path('showc/', views.showCourses, name='courselist'),
]
