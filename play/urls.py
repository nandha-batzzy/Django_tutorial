from django.urls import path
from . import views

#urlconf
urlpatterns = [
    path('hello/',views.hello)
]