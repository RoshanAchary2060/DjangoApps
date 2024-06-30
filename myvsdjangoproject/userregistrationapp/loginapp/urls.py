from django.urls import path
from . import views
urlpatterns = [
   
    path('login/', views.showLoginForm),
    path('logout/',views.logout),
]