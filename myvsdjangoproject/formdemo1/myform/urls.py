from django.urls import path
from . import views
urlpatterns = [
    # path('search/',views.searchFormView),
    # path('show/',views.showBooks),
    path('search/',views.singleView),
    path('show/',views.singleView),
]
