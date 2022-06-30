from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')  # to do my_app to connect with PROJECT urls.py
]