from . import views
from django.urls import path

urlpatterns = [
    path('showct/', views.showContactForm),
    path('thankyou/', views.showThankyouPage),
]
