from django.urls import path
from . import views
urlpatterns = [
    path('showfe/', views.showFrontEnd),
    path('showbe/', views.showBackEnd ),
]
